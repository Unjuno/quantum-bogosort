"""Validate GitHub Markdown math syntax and display-block structure."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ROOT_README = ROOT / "README.md"
UNSUPPORTED_MATH_MACROS = {
    r"\operatorname": r"use a GitHub-safe roman form such as \mathrm{Cov}",
}
errors = []


def check_unsupported_math_macros(path: Path, line_no: int, line: str) -> None:
    """Reject macros known to fail in GitHub's rendered math context."""
    for macro, replacement_hint in UNSUPPORTED_MATH_MACROS.items():
        if macro in line:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_no}: GitHub-disallowed math macro "
                f"{macro}; {replacement_hint}"
            )


for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue

    text = path.read_text(encoding="utf-8")

    # Legacy LaTeX delimiters are intentionally disallowed in repository Markdown.
    for token in (r"\(", r"\)", r"\[", r"\]"):
        if token in text:
            errors.append(f"{path.relative_to(ROOT)}: forbidden legacy math delimiter")

    in_fence = False
    fence_marker = None
    fence_kind = None
    fence_start = None
    math_fence_has_content = False
    math_fence_count = 0

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()

        if in_fence:
            if stripped == fence_marker:
                if fence_kind == "math" and not math_fence_has_content:
                    errors.append(
                        f"{path.relative_to(ROOT)}:{fence_start}: empty fenced math block"
                    )
                in_fence = False
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

        # Repository display mathematics uses GitHub fenced math blocks uniformly.
        if stripped == "```math":
            in_fence = True
            fence_marker = "```"
            fence_kind = "math"
            fence_start = line_no
            math_fence_has_content = False
            math_fence_count += 1
            continue

        # Ignore literal examples and program code inside non-math fences.
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = True
            fence_marker = stripped[:3]
            fence_kind = "code"
            fence_start = line_no
            continue

        # Single-dollar inline/display math is not used in repository Markdown.
        for _match in re.finditer(r"(?<!\$)\$(?!\$)", line):
            errors.append(
                f"{path.relative_to(ROOT)}:{line_no}: single-dollar math delimiter"
            )

        # Although GitHub documents $$ display math, this repository standardizes on
        # fenced math because direct rendered-UI review exposed inconsistent $$
        # rendering on repository pages. Keep the syntax uniform and regression-safe.
        if "$$" in line:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_no}: use fenced ```math blocks "
                "instead of $$ display delimiters"
            )

    if in_fence:
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
