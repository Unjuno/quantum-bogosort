"""Validate Markdown issue-template front matter used by GitHub's template chooser.

The repository deliberately uses a small YAML subset: one scalar per supported chooser
key, with no sequences, mappings, block scalars, anchors, or multiline continuations.
Keeping that subset explicit avoids a false PASS where the ad-hoc validator accepts a
nonempty string that GitHub's YAML parser rejects (for example an unterminated quote).
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / ".github" / "ISSUE_TEMPLATE"
REQUIRED_KEYS = {"name", "about"}
ALLOWED_KEYS = {"name", "about", "title", "labels", "assignees", "type"}
KEY_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$")
PLAIN_FORBIDDEN_START = set("-?:,[]{}#&*!|>'\"%@`")


def parse_scalar(value: str) -> tuple[str | None, str | None]:
    """Parse the repository's intentionally narrow YAML scalar subset."""
    value = value.strip()
    if not value:
        return "", None

    if value[0] == '"':
        if len(value) < 2 or value[-1] != '"':
            return None, "unterminated double-quoted scalar"
        body = value[1:-1]
        escaped = False
        for char in body:
            if escaped:
                escaped = False
                continue
            if char == "\\":
                escaped = True
            elif char == '"':
                return None, "unescaped double quote inside double-quoted scalar"
        if escaped:
            return None, "trailing escape in double-quoted scalar"
        return body, None

    if value[0] == "'":
        if len(value) < 2 or value[-1] != "'":
            return None, "unterminated single-quoted scalar"
        body = value[1:-1]
        # YAML represents a literal single quote inside a single-quoted scalar as ''.
        if "'" in body.replace("''", ""):
            return None, "undoubled single quote inside single-quoted scalar"
        return body.replace("''", "'"), None

    if value[-1] in {'"', "'"}:
        return None, "stray closing quote in plain scalar"
    if value[0] in PLAIN_FORBIDDEN_START:
        return None, f"plain scalar starts with YAML indicator {value[0]!r}; quote it"
    if ": " in value or " #" in value:
        return None, "plain scalar contains YAML mapping/comment delimiter; quote it"
    return value, None


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

            value, scalar_error = parse_scalar(raw_value or "")
            if scalar_error is not None:
                errors.append(f"{relative}:{line_no}: {scalar_error}")
                continue
            values[key] = value or ""

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
        "restricted-scalar GitHub chooser front matter and nonempty bodies."
    )


if __name__ == "__main__":
    main()
