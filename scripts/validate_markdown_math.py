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
    in_dollar_math = False

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

        # GitHub supports ```math fenced display blocks. Treat them as first-class
        # math syntax rather than ordinary code fences.
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

        # Single-dollar math is not used in repository Markdown.
        for _match in re.finditer(r"(?<!\$)\$(?!\$)", line):
            errors.append(
                f"{path.relative_to(ROOT)}:{line_no}: single-dollar math delimiter"
            )

        if "$$" in line:
            # The public landing page uses fenced math blocks. Do not regress it to
            # double-dollar blocks even though GitHub also documents that syntax.
            if path == ROOT_README:
                errors.append(
                    f"README.md:{line_no}: root README display math must use ```math fences"
                )
                continue

            if stripped != "$$":
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_no}: display delimiter must be on its own line"
                )
                continue
            in_dollar_math = not in_dollar_math
            continue

        if in_dollar_math:
            check_unsupported_math_macros(path, line_no, line)

    if in_fence:
        kind = "math" if fence_kind == "math" else "code"
        errors.append(
            f"{path.relative_to(ROOT)}:{fence_start}: unclosed fenced {kind} block"
        )
    if in_dollar_math:
        errors.append(f"{path.relative_to(ROOT)}: unclosed double-dollar display block")
    if path == ROOT_README and math_fence_count == 0:
        errors.append("README.md: expected at least one fenced ```math display block")

if errors:
    print("Markdown math validation failed:")
    print("\n".join(errors))
    sys.exit(1)

print(
    "Markdown math validation passed: root README uses fenced GitHub math blocks; "
    "display blocks are balanced; unsupported GitHub math macros are absent."
)
