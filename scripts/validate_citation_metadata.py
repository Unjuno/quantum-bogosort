"""Validate the narrow CITATION.cff contract used by this research repository.

The repository intentionally keeps citation metadata on the current frozen public-review
snapshot while `main` continues review/development. This validator therefore checks the
CFF fields against STATUS.md rather than assuming CITATION.cff must describe HEAD.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CITATION = ROOT / "CITATION.cff"
STATUS = ROOT / "STATUS.md"
REPOSITORY_URL = "https://github.com/Unjuno/quantum-bogosort"
REQUIRED_KEYWORDS = {
    "quantum foundations",
    "Everett interpretation",
    "decision theory",
    "self-locating uncertainty",
    "observer selection",
    "reproducible research",
}
TOP_LEVEL_KEYS = {
    "cff-version",
    "message",
    "title",
    "type",
    "authors",
    "repository-code",
    "url",
    "version",
    "date-released",
    "abstract",
    "keywords",
}
SCALAR_RE = re.compile(r"^([A-Za-z0-9-]+):\s*(.*)$")
STATUS_DATE_RE = re.compile(r"^\*\*Snapshot date:\*\*\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
STATUS_TAG_RE = re.compile(r"^- tag/Release:\s*`(v[^`]+)`\s*$", re.MULTILINE)
STATUS_COMMIT_RE = re.compile(r"^- commit:\s*`([0-9a-f]{40})`\s*$", re.MULTILINE)


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_cff(text: str) -> tuple[dict[str, str], list[str], list[str], list[str]]:
    scalars: dict[str, str] = {}
    authors: list[str] = []
    keywords: list[str] = []
    errors: list[str] = []
    section: str | None = None

    for line_no, raw in enumerate(text.splitlines(), start=1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        if raw.startswith(" "):
            stripped = raw.strip()
            if section == "authors":
                match = re.fullmatch(r"-\s+family-names:\s*(.+)", stripped)
                if match:
                    authors.append(unquote(match.group(1)))
                elif stripped.startswith("-") or stripped.startswith("family-names:"):
                    errors.append(
                        f"CITATION.cff:{line_no}: unsupported author form; expected '- family-names: ...'"
                    )
            elif section == "keywords":
                match = re.fullmatch(r"-\s+(.+)", stripped)
                if match:
                    keywords.append(unquote(match.group(1)))
                else:
                    errors.append(f"CITATION.cff:{line_no}: malformed keyword entry")
            continue

        match = SCALAR_RE.fullmatch(raw)
        if not match:
            errors.append(f"CITATION.cff:{line_no}: unsupported top-level syntax")
            section = None
            continue

        key, raw_value = match.groups()
        if key not in TOP_LEVEL_KEYS:
            errors.append(f"CITATION.cff:{line_no}: unexpected top-level key {key!r}")
        if key in scalars:
            errors.append(f"CITATION.cff:{line_no}: duplicate top-level key {key!r}")

        value = unquote(raw_value)
        if key in {"authors", "keywords"}:
            if value:
                errors.append(f"CITATION.cff:{line_no}: {key} must be a block list")
            section = key
        else:
            scalars[key] = value
            section = None

    return scalars, authors, keywords, errors


def main() -> None:
    errors: list[str] = []

    if not CITATION.is_file():
        raise SystemExit("Missing CITATION.cff")
    if not STATUS.is_file():
        raise SystemExit("Missing STATUS.md")

    scalars, authors, keywords, parse_errors = parse_cff(CITATION.read_text(encoding="utf-8"))
    errors.extend(parse_errors)

    required_scalars = {
        "cff-version",
        "message",
        "title",
        "type",
        "repository-code",
        "url",
        "version",
        "date-released",
        "abstract",
    }
    missing = sorted(required_scalars - set(scalars))
    if missing:
        errors.append("CITATION.cff missing required scalar field(s): " + ", ".join(missing))

    for key in sorted(required_scalars & set(scalars)):
        if not scalars[key].strip():
            errors.append(f"CITATION.cff field {key!r} must be nonempty")

    if scalars.get("cff-version") != "1.2.0":
        errors.append(f"cff-version must remain 1.2.0; got {scalars.get('cff-version')!r}")
    if scalars.get("type") != "software":
        errors.append(f"citation type must remain 'software'; got {scalars.get('type')!r}")
    if scalars.get("repository-code") != REPOSITORY_URL:
        errors.append("repository-code does not match canonical GitHub repository URL")
    if scalars.get("url") != REPOSITORY_URL:
        errors.append("url does not match canonical GitHub repository URL")

    if not authors or any(not author.strip() for author in authors):
        errors.append("CITATION.cff must contain at least one nonempty family-names author")
    if len(authors) != len(set(authors)):
        errors.append("CITATION.cff contains duplicate family-names author entries")

    keyword_set = set(keywords)
    if keyword_set != REQUIRED_KEYWORDS:
        errors.append(
            "CITATION.cff keyword set differs from the public-review contract; got "
            + repr(sorted(keyword_set))
        )
    if len(keywords) != len(keyword_set):
        errors.append("CITATION.cff contains duplicate keywords")

    released = scalars.get("date-released", "")
    try:
        date.fromisoformat(released)
    except ValueError:
        errors.append(f"date-released must be ISO YYYY-MM-DD; got {released!r}")

    status_text = STATUS.read_text(encoding="utf-8")
    status_date_match = STATUS_DATE_RE.search(status_text)
    status_tags = STATUS_TAG_RE.findall(status_text)
    status_commits = STATUS_COMMIT_RE.findall(status_text)
    if not status_date_match:
        errors.append("STATUS.md is missing the frozen snapshot date")
    if not status_tags:
        errors.append("STATUS.md is missing a frozen tag/Release entry")
    if not status_commits:
        errors.append("STATUS.md is missing a frozen commit entry")

    citation_version = scalars.get("version", "")
    expected_tag = f"v{citation_version}" if citation_version else ""
    if status_tags and status_tags[0] != expected_tag:
        errors.append(
            f"CITATION.cff version {citation_version!r} does not match current STATUS tag {status_tags[0]!r}"
        )
    if status_date_match and released != status_date_match.group(1):
        errors.append(
            f"CITATION.cff date-released {released!r} does not match STATUS snapshot date "
            f"{status_date_match.group(1)!r}"
        )

    if "eventual manuscript when available" not in scalars.get("message", ""):
        errors.append("citation message no longer preserves the pre-identifier manuscript boundary")
    if "Everett accessibility bridge remains" not in scalars.get("abstract", ""):
        errors.append("citation abstract must preserve the explicit Everett-bridge boundary")

    if errors:
        raise SystemExit("Citation metadata validation failed:\n" + "\n".join(errors))

    print(
        "Citation metadata validation passed: CFF 1.2.0, canonical repository URLs, "
        f"{len(authors)} author entry, {len(keywords)} keywords, and frozen snapshot "
        f"{expected_tag} / {released} aligned with STATUS.md."
    )


if __name__ == "__main__":
    main()
