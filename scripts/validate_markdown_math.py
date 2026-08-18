"""Validate GitHub Markdown math delimiters and display-block structure."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

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
    in_math = False

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()

        # Ignore literal examples inside fenced code blocks.
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            continue

        if in_fence:
            continue

        # Single-dollar math is not used in GitHub Markdown in this repository.
        for match in re.finditer(r"(?<!\$)\$(?!\$)", line):
            errors.append(
                f"{path.relative_to(ROOT)}:{line_no}: single-dollar math delimiter"
            )

        if "$$" in line:
            # GitHub rendering is most reliable when each display delimiter is on
            # a line by itself. Reject forms such as '$$ x = 1' or 'x $$'.
            if stripped != "$$":
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_no}: display delimiter must be on its own line"
                )
                continue
            in_math = not in_math

    if in_fence:
        errors.append(f"{path.relative_to(ROOT)}: unclosed fenced code block")
    if in_math:
        errors.append(f"{path.relative_to(ROOT)}: unclosed double-dollar display block")

if errors:
    print("Markdown math validation failed:")
    print("\n".join(errors))
    sys.exit(1)

print(
    "Markdown math validation passed: display delimiters are balanced, "
    "double-dollar only, and delimiter-only lines."
)
