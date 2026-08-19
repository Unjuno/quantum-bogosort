"""Verify frozen public-review tag targets and matching GitHub Releases.

This is a remote provenance check. Source files record the intended snapshot commits,
but tags are hosting-layer refs and can move unless separately protected. CI therefore
verifies the live GitHub tag targets rather than treating the names alone as proof of
immutability. A Release may be marked as a prerelease; that presentation flag does not
change the frozen commit identity.
"""
from __future__ import annotations

import json
import os
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "Unjuno/quantum-bogosort")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API_VERSION = "2026-03-10"
EXPECTED = {
    "v0.3-public-review": "58038763127258bd3e2f0d41708c4dfa01f81fd6",
    "v0.2-public-review": "7405f7408f74fa32b16d1cc9f624070cc14624ab",
}


def api_json(path: str) -> dict:
    url = f"https://api.github.com/repos/{REPOSITORY}{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "qbs-snapshot-ref-validator",
        "X-GitHub-Api-Version": API_VERSION,
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    request = Request(url, headers=headers)
    try:
        with urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise RuntimeError(f"GitHub API returned HTTP {response.status} for {path}")
            payload = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"GitHub API request failed for {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise RuntimeError(f"GitHub API returned non-object JSON for {path}")
    return payload


def resolve_tag_target(tag: str) -> str:
    encoded = quote(tag, safe="")
    ref = api_json(f"/git/ref/tags/{encoded}")
    obj = ref.get("object")
    if not isinstance(obj, dict):
        raise RuntimeError(f"tag ref {tag} has no object")

    object_type = obj.get("type")
    sha = obj.get("sha")
    if not isinstance(sha, str):
        raise RuntimeError(f"tag ref {tag} has no object SHA")

    # Lightweight tags point directly to commits. Annotated tags point to tag objects;
    # resolve nested annotated tag objects defensively until a commit is reached.
    for _ in range(4):
        if object_type == "commit":
            return sha
        if object_type != "tag":
            raise RuntimeError(f"tag {tag} points to unsupported object type {object_type!r}")
        tag_object = api_json(f"/git/tags/{sha}")
        nested = tag_object.get("object")
        if not isinstance(nested, dict):
            raise RuntimeError(f"annotated tag object for {tag} has no nested object")
        object_type = nested.get("type")
        sha = nested.get("sha")
        if not isinstance(sha, str):
            raise RuntimeError(f"annotated tag object for {tag} has no nested SHA")

    raise RuntimeError(f"tag {tag} exceeded annotated-tag resolution depth")


def main() -> None:
    errors: list[str] = []

    for tag, expected_commit in EXPECTED.items():
        try:
            actual_commit = resolve_tag_target(tag)
        except RuntimeError as exc:
            errors.append(str(exc))
            continue

        if actual_commit != expected_commit:
            errors.append(
                f"{tag}: live tag target {actual_commit} != frozen snapshot {expected_commit}"
            )

        try:
            release = api_json(f"/releases/tags/{quote(tag, safe='')}")
        except RuntimeError as exc:
            errors.append(str(exc))
            continue

        if release.get("tag_name") != tag:
            errors.append(f"{tag}: release tag_name mismatch: {release.get('tag_name')!r}")
        if release.get("draft") is True:
            errors.append(f"{tag}: frozen public-review Release is unexpectedly a draft")

    if errors:
        raise SystemExit("Snapshot-ref validation failed:\n" + "\n".join(errors))

    print(
        "Snapshot-ref validation passed: live v0.3/v0.2 tag targets match the recorded "
        "frozen commits and both public GitHub Releases exist."
    )


if __name__ == "__main__":
    main()
