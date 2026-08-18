"""Render every repository Markdown file through GitHub's own GFM API.

This complements local syntax checks. It catches page-level parser regressions where
valid-looking source swallows headings, tables, or images when GitHub renders it.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import json
import os
import re
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "Unjuno/quantum-bogosort")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API_URL = "https://api.github.com/markdown"
API_VERSION = "2026-03-10"

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+\S")
TABLE_SEPARATOR_RE = re.compile(
    r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$"
)
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")


class RenderedStructure(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.headings = 0
        self.tables = 0
        self.images = 0

    def handle_starttag(self, tag: str, attrs) -> None:  # type: ignore[override]
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings += 1
        elif tag == "table":
            self.tables += 1
        elif tag == "img":
            self.images += 1


def source_structure(text: str) -> tuple[int, int, int]:
    """Count render-critical structures outside fenced blocks."""
    headings = 0
    tables = 0
    images = 0
    fence_char: str | None = None
    fence_len = 0

    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            trailer = match.group(2).strip()
            char = marker[0]
            if fence_char is None:
                fence_char = char
                fence_len = len(marker)
                continue
            if char == fence_char and len(marker) >= fence_len and not trailer:
                fence_char = None
                fence_len = 0
                continue

        if fence_char is not None:
            continue

        if HEADING_RE.match(line):
            headings += 1
        if TABLE_SEPARATOR_RE.match(line):
            tables += 1
        images += len(IMAGE_RE.findall(line))

    return headings, tables, images


def render_with_github(text: str) -> str:
    payload = json.dumps(
        {"text": text, "mode": "gfm", "context": REPOSITORY}
    ).encode("utf-8")
    headers = {
        "Accept": "text/html",
        "Content-Type": "application/json",
        "User-Agent": "qbs-markdown-render-validator",
        "X-GitHub-Api-Version": API_VERSION,
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    last_error: Exception | None = None
    for attempt in range(3):
        request = Request(API_URL, data=payload, headers=headers, method="POST")
        try:
            with urlopen(request, timeout=30) as response:
                if response.status != 200:
                    raise RuntimeError(f"GitHub Markdown API returned HTTP {response.status}")
                return response.read().decode("utf-8")
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(1 + attempt)
                continue
            raise RuntimeError(f"GitHub Markdown API request failed: {exc}") from exc
    raise RuntimeError(f"GitHub Markdown API request failed: {last_error}")


def main() -> None:
    errors: list[str] = []
    files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        expected_headings, expected_tables, expected_images = source_structure(text)

        try:
            rendered = render_with_github(text)
        except RuntimeError as exc:
            errors.append(f"{relative}: {exc}")
            continue

        if text.strip() and not rendered.strip():
            errors.append(f"{relative}: GitHub renderer returned empty HTML")
            continue

        parser = RenderedStructure()
        parser.feed(rendered)

        if parser.headings < expected_headings:
            errors.append(
                f"{relative}: rendered headings {parser.headings} < source headings {expected_headings}"
            )
        if parser.tables < expected_tables:
            errors.append(
                f"{relative}: rendered tables {parser.tables} < source tables {expected_tables}"
            )
        if parser.images < expected_images:
            errors.append(
                f"{relative}: rendered images {parser.images} < source images {expected_images}"
            )

    if errors:
        raise SystemExit("GitHub Markdown rendering validation failed:\n" + "\n".join(errors))

    print(
        f"GitHub Markdown rendering OK: {len(files)} files rendered through the "
        "GitHub GFM API with expected headings, tables, and images preserved."
    )


if __name__ == "__main__":
    main()
