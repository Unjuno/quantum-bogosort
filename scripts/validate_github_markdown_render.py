"""Render every repository Markdown file through GitHub's own GFM API.

This complements local syntax checks. It catches page-level parser regressions where
valid-looking source swallows headings, tables, inline images, or ordinary fenced code
blocks during GitHub's server-side GFM conversion. Fenced ``math`` and ``mermaid``
blocks are counted for audit reporting but are not required to map to ``<pre>``: GitHub
may route those special block types through rendering-specific HTML. Their actual
MathJax/Mermaid presentation remains a direct browser-UI release gate.
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
INLINE_CODE_RE = re.compile(r"(`+)(.*?)\1")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
CLOSING_FENCE_RE = re.compile(r"^ {0,3}([`~]{3,})[ \t]*$")
SPECIAL_FENCE_CANDIDATE_RE = re.compile(
    r"^(?P<indent>[ \t]*)(?P<marker>`{3,}|~{3,})(?P<info>.*)$"
)
SPECIAL_RENDER_INFO = {"math", "mermaid"}


class RenderedStructure(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.headings = 0
        self.tables = 0
        self.images = 0
        self.pre_blocks = 0
        self.math_renderers = 0

    def handle_starttag(self, tag: str, attrs) -> None:  # type: ignore[override]
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings += 1
        elif tag == "table":
            self.tables += 1
        elif tag == "img":
            self.images += 1
        elif tag == "pre":
            self.pre_blocks += 1
        elif tag == "math-renderer":
            # Informational only. GitHub's HTML carrier for math is not part of the
            # repository's stable validation contract.
            self.math_renderers += 1


def closes_fence(line: str, marker: str) -> bool:
    match = CLOSING_FENCE_RE.match(line)
    if not match:
        return False
    candidate = match.group(1)
    return candidate[0] == marker[0] and len(candidate) >= len(marker)


def valid_fence_opener(marker: str, info: str) -> bool:
    return marker[0] != "`" or "`" not in info


def fence_info_name(info: str) -> str:
    stripped = info.strip()
    return stripped.split(None, 1)[0].lower() if stripped else ""


def strip_inline_code_spans(line: str) -> str:
    """Remove one-line inline-code spans before counting rendered image syntax.

    A literal example such as ``[![...](image.svg)](page.md)`` is rendered as code, not as
    an image. Counting its inner ``![...]`` token as a source image creates a false
    mismatch against GitHub's rendered HTML. Fenced code is already excluded separately.
    """
    return INLINE_CODE_RE.sub("", line)


def special_render_fence_errors(relative: str, text: str) -> list[str]:
    """Reject special-render fence forms outside the repository's GitHub contract."""
    errors: list[str] = []
    fence_marker: str | None = None

    for line_no, line in enumerate(text.splitlines(), start=1):
        if fence_marker is not None:
            if closes_fence(line, fence_marker):
                fence_marker = None
            continue

        candidate = SPECIAL_FENCE_CANDIDATE_RE.match(line)
        if candidate:
            indent = candidate.group("indent")
            marker = candidate.group("marker")
            raw_info = candidate.group("info")
            info = raw_info.strip()
            info_name = fence_info_name(raw_info)

            if info_name in SPECIAL_RENDER_INFO:
                if "\t" in indent or len(indent) > 3:
                    errors.append(
                        f"{relative}:{line_no}: {info_name} fence is indented beyond the "
                        "CommonMark 0-3-space fence boundary and would render as code"
                    )
                if marker[0] != "`":
                    errors.append(
                        f"{relative}:{line_no}: repository {info_name} render blocks must "
                        "use backtick fences, not tilde fences"
                    )
                if info != info_name:
                    errors.append(
                        f"{relative}:{line_no}: repository {info_name} fence info string "
                        f"must be exactly {info_name!r}, got {info!r}"
                    )

            # Track only syntactically valid CommonMark fences so literal special-fence
            # examples inside an ordinary outer fence are ignored by this contract check.
            if (
                "\t" not in indent
                and len(indent) <= 3
                and valid_fence_opener(marker, raw_info)
            ):
                fence_marker = marker

    return errors


def source_structure(text: str) -> tuple[int, int, int, int, int, int]:
    """Count render-critical structures and classify valid CommonMark fences."""
    headings = 0
    tables = 0
    images = 0
    ordinary_fences = 0
    math_fences = 0
    mermaid_fences = 0
    fence_marker: str | None = None

    for line in text.splitlines():
        if fence_marker is not None:
            if closes_fence(line, fence_marker):
                fence_marker = None
            continue

        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            info = match.group(2)
            if valid_fence_opener(marker, info):
                fence_marker = marker
                stripped_info = info.strip()
                if marker[0] == "`" and stripped_info == "math":
                    math_fences += 1
                elif marker[0] == "`" and stripped_info == "mermaid":
                    mermaid_fences += 1
                else:
                    ordinary_fences += 1
                continue

        if HEADING_RE.match(line):
            headings += 1
        if TABLE_SEPARATOR_RE.match(line):
            tables += 1
        images += len(IMAGE_RE.findall(strip_inline_code_spans(line)))

    return headings, tables, images, ordinary_fences, math_fences, mermaid_fences


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
    total_ordinary = 0
    total_math = 0
    total_mermaid = 0
    observed_math_renderers = 0

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        errors.extend(special_render_fence_errors(relative, text))
        (
            expected_headings,
            expected_tables,
            expected_images,
            ordinary_fences,
            math_fences,
            mermaid_fences,
        ) = source_structure(text)
        total_ordinary += ordinary_fences
        total_math += math_fences
        total_mermaid += mermaid_fences

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
        observed_math_renderers += parser.math_renderers

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
        if parser.pre_blocks < ordinary_fences:
            errors.append(
                f"{relative}: rendered <pre> blocks {parser.pre_blocks} < ordinary source fences {ordinary_fences}"
            )

    if errors:
        raise SystemExit("GitHub Markdown rendering validation failed:\n" + "\n".join(errors))

    print(
        f"GitHub Markdown rendering OK: {len(files)} files rendered through the GitHub "
        "GFM API; expected headings, tables, inline images, and ordinary fenced code "
        f"blocks preserved. Source audit counted {total_ordinary} ordinary, {total_math} "
        f"math, and {total_mermaid} Mermaid fences under the exact special-render fence "
        f"contract; GitHub returned {observed_math_renderers} <math-renderer> elements. "
        "MathJax/Mermaid visual presentation remains a browser-UI gate."
    )


if __name__ == "__main__":
    main()
