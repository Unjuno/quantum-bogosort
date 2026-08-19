"""Validate GitHub Markdown math syntax and display-block structure."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ROOT_README = ROOT / "README.md"
REPOSITORY_DISALLOWED_MATH_MACROS = {
    r"\operatorname": r"use the repository convention \mathrm{Cov}, \mathrm{Var}, etc.",
}
LEGACY_MATH_DELIMITERS = (r"\(", r"\)", r"\[", r"\]")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
CLOSING_FENCE_RE = re.compile(r"^ {0,3}([`~]{3,})[ \t]*$")
SPECIAL_FENCE_CANDIDATE_RE = re.compile(
    r"^(?P<indent>[ \t]*)(?P<marker>`{3,}|~{3,})(?P<info>.*)$"
)
BEGIN_END_RE = re.compile(r"\\(begin|end)\{([^{}]+)\}")
errors = []


def check_disallowed_math_macros(path: Path, line_no: int, line: str) -> None:
    """Enforce repository math-macro conventions in rendered Markdown."""
    for macro, replacement_hint in REPOSITORY_DISALLOWED_MATH_MACROS.items():
        if macro in line:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_no}: repository-disallowed math macro "
                f"{macro}; {replacement_hint}"
            )


def strip_inline_code_spans(line: str) -> str:
    """Remove inline code before checking prose for math delimiters."""
    return re.sub(r"(`+)(.*?)\1", "", line)


def closes_fence(line: str, marker: str) -> bool:
    """Return whether a line closes the currently open CommonMark fence."""
    match = CLOSING_FENCE_RE.match(line)
    if not match:
        return False
    candidate = match.group(1)
    return candidate[0] == marker[0] and len(candidate) >= len(marker)


def valid_fence_opener(marker: str, info: str) -> bool:
    # CommonMark forbids backticks inside a backtick-fence info string.
    return marker[0] != "`" or "`" not in info


def check_special_render_fence_contract(path: Path, line_no: int, line: str) -> None:
    """Reject fence lookalikes that GitHub would not treat as repository special blocks."""
    match = SPECIAL_FENCE_CANDIDATE_RE.match(line)
    if not match:
        return

    indent = match.group("indent")
    marker = match.group("marker")
    info = match.group("info").strip()
    if not info:
        return
    info_name = info.split(None, 1)[0].lower()
    if info_name not in {"math", "mermaid"}:
        return

    relative = path.relative_to(ROOT)
    if "\t" in indent or len(indent) > 3:
        errors.append(
            f"{relative}:{line_no}: {info_name} fence is indented beyond the "
            "CommonMark 0-3-space fence boundary and would render as code"
        )
    if marker[0] != "`":
        errors.append(
            f"{relative}:{line_no}: repository {info_name} render blocks must use "
            "backtick fences, not tilde fences"
        )
    if info != info_name:
        errors.append(
            f"{relative}:{line_no}: repository {info_name} fence info string must be "
            f"exactly {info_name!r}, got {info!r}"
        )


def check_math_structure(path: Path, start_line: int, lines: list[str]) -> None:
    """Catch structural TeX errors that commonly stop MathJax block rendering."""
    text = "\n".join(lines)

    # Count only grouping braces, not escaped literal set braces such as \{ and \}.
    brace_depth = 0
    escaped = False
    for char in text:
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "{":
            brace_depth += 1
        elif char == "}":
            brace_depth -= 1
            if brace_depth < 0:
                errors.append(
                    f"{path.relative_to(ROOT)}:{start_line}: unmatched closing brace in math block"
                )
                break
    if brace_depth > 0:
        errors.append(
            f"{path.relative_to(ROOT)}:{start_line}: {brace_depth} unclosed grouping brace(s) in math block"
        )

    env_stack: list[str] = []
    for match in BEGIN_END_RE.finditer(text):
        kind, env = match.groups()
        if kind == "begin":
            env_stack.append(env)
        elif not env_stack or env_stack[-1] != env:
            expected = env_stack[-1] if env_stack else "<none>"
            errors.append(
                f"{path.relative_to(ROOT)}:{start_line}: mismatched \\end{{{env}}}; "
                f"expected {expected}"
            )
            break
        else:
            env_stack.pop()
    if env_stack:
        errors.append(
            f"{path.relative_to(ROOT)}:{start_line}: unclosed TeX environment(s): "
            + ", ".join(env_stack)
        )

    # Count common MathJax delimiters, including raw vertical bars such as \left|x\right|.
    left_count = len(re.findall(r"\\left(?=\\|\.|\s|\(|\[|\{|\|)", text))
    right_count = len(re.findall(r"\\right(?=\\|\.|\s|\)|\]|\}|\|)", text))
    if left_count != right_count:
        errors.append(
            f"{path.relative_to(ROOT)}:{start_line}: \\left/\\right count mismatch "
            f"({left_count} != {right_count})"
        )

    for token in LEGACY_MATH_DELIMITERS:
        if token in text:
            errors.append(
                f"{path.relative_to(ROOT)}:{start_line}: nested legacy delimiter {token} "
                "inside fenced math"
            )


for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue

    text = path.read_text(encoding="utf-8")

    fence_marker: str | None = None
    fence_kind: str | None = None
    fence_start: int | None = None
    math_fence_has_content = False
    math_fence_count = 0
    math_lines: list[str] = []

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()

        if fence_marker is not None:
            if closes_fence(line, fence_marker):
                if fence_kind == "math":
                    if not math_fence_has_content:
                        errors.append(
                            f"{path.relative_to(ROOT)}:{fence_start}: empty fenced math block"
                        )
                    else:
                        check_math_structure(path, fence_start or line_no, math_lines)
                fence_marker = None
                fence_kind = None
                fence_start = None
                math_fence_has_content = False
                math_lines = []
                continue

            if fence_kind == "math":
                math_lines.append(line)
                if stripped:
                    math_fence_has_content = True
                check_disallowed_math_macros(path, line_no, line)
            continue

        check_special_render_fence_contract(path, line_no, line)

        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            raw_info = fence_match.group(2)
            if valid_fence_opener(marker, raw_info):
                info = raw_info.strip()
                fence_marker = marker
                fence_kind = "math" if marker[0] == "`" and info == "math" else "code"
                fence_start = line_no
                math_fence_has_content = False
                math_lines = []
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
    "Markdown math validation passed: repository display math uses backtick-fenced "
    "GitHub math blocks; special math/Mermaid fence indentation and info strings satisfy "
    "the repository rendering contract; CommonMark fences and TeX grouping/environments "
    "are balanced; repository math-macro conventions are satisfied."
)
