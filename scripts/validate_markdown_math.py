"""Validate GitHub Markdown math syntax and display-block structure."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ROOT_README = ROOT / "README.md"
UNSUPPORTED_MATH_MACROS = {
    r"\operatorname": r"use a GitHub-safe roman form such as \mathrm{Cov}",
}
LEGACY_MATH_DELIMITERS = (r"\(", r"\)", r"\[", r"\]")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
errors = []


def check_unsupported_math_macros(path: Path, line_no: int, line: str) -> None:
    """Reject macros known to fail in GitHub's rendered math context."""
    for macro, replacement_hint in UNSUPPORTED_MATH_MACROS.items():
        if macro in line:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_no}: GitHub-disallowed math macro "
                f"{macro}; {replacement_hint}"
            )


def strip_inline_code_spans(line: str) -> str:
    """Remove inline code before checking prose for math delimiters."""
    return re.sub(r"(`+)(.*?)\1", "", line)


def closes_fence(stripped: str, marker: str) -> bool:
    """Return whether a line closes the currently open CommonMark fence."""
    if not stripped or stripped[0] != marker[0]:
        return False
    if set(stripped) != {marker[0]}:
        return False
    return len(stripped) >= len(marker)


for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue

    text = path.read_text(encoding="utf-8")

    fence_marker: str | None = None
    fence_kind: str | None = None
    fence_start: int | None = None
    math_fence_has_content = False
    math_fence_count = 0

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()

        if fence_marker is not None:
            if closes_fence(stripped, fence_marker):
                if fence_kind == "math" and not math_fence_has_content:
                    errors.append(
                        f"{path.relative_to(ROOT)}:{fence_start}: empty fenced math block"
                    )
                fence_marker = None
                fence_kind = None
                fence_start = None
                math_fence_has_content = False
                continue

            if fence_kind == "math":
                if stripped:
                    math_fence_has_content = True
                check_unsupported_math_macros(path, line_no, line)
            continue

        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            info = fence_match.group(2).strip()
            fence_marker = marker
            fence_kind = "math" if info == "math" else "code"
            fence_start = line_no
            math_fence_has_content = False
            if fence_kind == "math":
                math_fence_count += 1
            continue

        rendered_line = strip_inline_code_spans(line)

        # Legacy LaTeX delimiters are intentionally disallowed in rendered prose.
        for token in LEGACY_MATH_DELIMITERS:
            if token in rendered_line:
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_no}: forbidden legacy math delimiter"
                )

        # Single-dollar inline/display math is not used in repository Markdown.
        for _match in re.finditer(r"(?<!\$)\$(?!\$)", rendered_line):
            errors.append(
                f"{path.relative_to(ROOT)}:{line_no}: single-dollar math delimiter"
            )

        # Although GitHub documents $$ display math, this repository standardizes on
        # fenced math because direct rendered-UI review exposed inconsistent $$
        # rendering on repository pages. Keep the syntax uniform and regression-safe.
        if "$$" in rendered_line:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_no}: use fenced ```math blocks "
                "instead of $$ display delimiters"
            )

    if fence_marker is not None:
        kind = "math" if fence_kind == "math" else "code"
        errors.append(
            f"{path.relative_to(ROOT)}:{fence_start}: unclosed fenced {kind} block"
        )
    if path == ROOT_README and math_fence_count == 0:
        errors.append("README.md: expected at least one fenced ```math display block")

if errors:
    print("Markdown math validation failed:")
    print("\n".join(errors))
    sys.exit(1)

print(
    "Markdown math validation passed: repository display math uses fenced GitHub "
    "math blocks; fences are balanced; unsupported GitHub math macros are absent."
)
