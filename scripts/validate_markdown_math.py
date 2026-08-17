"""Reject Markdown math delimiters that are not double-dollar display blocks."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    for token in (r"\(", r"\)", r"\[", r"\]"):
        if token in text:
            errors.append(f"{path.relative_to(ROOT)}: forbidden legacy math delimiter")
    for match in re.finditer(r"(?<!\$)\$(?!\$)", text):
        line = text.count("\n", 0, match.start()) + 1
        errors.append(f"{path.relative_to(ROOT)}:{line}: single-dollar math delimiter")

if errors:
    print("Markdown math validation failed:")
    print("\n".join(errors))
    sys.exit(1)
print("Markdown math validation passed: only double-dollar display delimiters are used.")
