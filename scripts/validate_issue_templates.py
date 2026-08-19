"""Validate Markdown issue-template front matter used by GitHub's template chooser."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / ".github" / "ISSUE_TEMPLATE"
REQUIRED_KEYS = {"name", "about"}
ALLOWED_KEYS = {"name", "about", "title", "labels", "assignees", "type"}
KEY_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$")


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def main() -> None:
    files = sorted(TEMPLATE_DIR.glob("*.md"))
    errors: list[str] = []
    names: dict[str, Path] = {}

    if not files:
        raise SystemExit("No Markdown issue templates found")

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0].strip() != "---":
            errors.append(f"{relative}: missing opening YAML front-matter delimiter")
            continue

        try:
            end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
        except StopIteration:
            errors.append(f"{relative}: missing closing YAML front-matter delimiter")
            continue

        values: dict[str, str] = {}
        for line_no, line in enumerate(lines[1:end], start=2):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            match = KEY_RE.match(line)
            if not match:
                errors.append(f"{relative}:{line_no}: unsupported front-matter syntax")
                continue
            key, raw_value = match.groups()
            if key in values:
                errors.append(f"{relative}:{line_no}: duplicate front-matter key {key}")
                continue
            if key not in ALLOWED_KEYS:
                errors.append(f"{relative}:{line_no}: unsupported front-matter key {key}")
            values[key] = scalar(raw_value or "")

        missing = sorted(REQUIRED_KEYS - values.keys())
        if missing:
            errors.append(f"{relative}: missing required front-matter keys: {', '.join(missing)}")

        name = values.get("name", "").strip()
        about = values.get("about", "").strip()
        if name and len(name) <= 3:
            errors.append(f"{relative}: template name must be longer than 3 characters")
        if not name:
            errors.append(f"{relative}: template name is empty")
        elif name in names:
            errors.append(
                f"{relative}: duplicate template name {name!r}; already used by "
                f"{names[name].relative_to(ROOT).as_posix()}"
            )
        else:
            names[name] = path
        if not about:
            errors.append(f"{relative}: template about text is empty")

        if not any(line.strip() for line in lines[end + 1 :]):
            errors.append(f"{relative}: template body is empty")

    if errors:
        raise SystemExit("Issue-template validation failed:\n" + "\n".join(errors))

    print(
        f"Issue-template validation passed: {len(files)} Markdown templates have valid "
        "GitHub chooser front matter and nonempty bodies."
    )


if __name__ == "__main__":
    main()
