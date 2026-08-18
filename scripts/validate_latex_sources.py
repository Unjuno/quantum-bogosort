"""Validate manuscript/theory LaTeX source relationships before PDF compilation."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
MAIN = PAPER / "main.tex"

INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
GRAPHICS_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
BIB_RE = re.compile(r"\\bibliography\{([^}]+)\}")
BIB_KEY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE)
CITE_RE = re.compile(r"\\cite[a-zA-Z*]*\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}")
ENV_RE = re.compile(r"\\(begin|end)\{([^{}]+)\}")


def strip_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        out: list[str] = []
        escaped = False
        for char in line:
            if char == "%" and not escaped:
                break
            out.append(char)
            if char == "\\":
                escaped = not escaped
            else:
                escaped = False
        lines.append("".join(out))
    return "\n".join(lines)


def resolve_input(source: Path, target: str) -> Path:
    candidate = source.parent / target
    if candidate.suffix != ".tex":
        candidate = candidate.with_suffix(".tex")
    return candidate.resolve()


def collect_reachable_tex() -> list[Path]:
    pending = [MAIN.resolve()]
    seen: set[Path] = set()
    ordered: list[Path] = []
    while pending:
        path = pending.pop(0)
        if path in seen:
            continue
        seen.add(path)
        ordered.append(path)
        text = strip_comments(path.read_text(encoding="utf-8"))
        for target in INPUT_RE.findall(text):
            pending.append(resolve_input(path, target))
    return ordered


def check_environment_balance(path: Path, text: str, errors: list[str]) -> None:
    stack: list[str] = []
    for match in ENV_RE.finditer(text):
        kind, env = match.groups()
        if kind == "begin":
            stack.append(env)
        elif not stack or stack[-1] != env:
            expected = stack[-1] if stack else "<none>"
            errors.append(
                f"{path.relative_to(ROOT)}: mismatched \\end{{{env}}}; expected {expected}"
            )
            return
        else:
            stack.pop()
    if stack:
        errors.append(
            f"{path.relative_to(ROOT)}: unclosed environment(s): " + ", ".join(stack)
        )


def main() -> None:
    errors: list[str] = []

    if not MAIN.exists():
        raise SystemExit("Missing paper/main.tex")

    # Resolve the manuscript input graph and fail before TeX if an input is absent.
    try:
        reachable = collect_reachable_tex()
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing LaTeX input: {exc.filename}") from exc

    paper_tex = sorted(PAPER.rglob("*.tex"))
    extra_tex = [ROOT / "theory/core_theorems.tex"]
    all_tex = paper_tex + [p for p in extra_tex if p.exists()]

    source_text: dict[Path, str] = {}
    for path in all_tex:
        text = strip_comments(path.read_text(encoding="utf-8"))
        source_text[path] = text
        check_environment_balance(path, text, errors)

    # Bibliography declarations in the reachable manuscript must resolve.
    bib_files: list[Path] = []
    for path in reachable:
        text = strip_comments(path.read_text(encoding="utf-8"))
        for group in BIB_RE.findall(text):
            for name in (part.strip() for part in group.split(",")):
                bib = (path.parent / name).with_suffix(".bib").resolve()
                if not bib.exists():
                    errors.append(f"{path.relative_to(ROOT)}: missing bibliography {name}.bib")
                else:
                    bib_files.append(bib)

    bib_keys: set[str] = set()
    duplicate_bib: set[str] = set()
    for bib in sorted(set(bib_files)):
        text = strip_comments(bib.read_text(encoding="utf-8"))
        for key in BIB_KEY_RE.findall(text):
            if key in bib_keys:
                duplicate_bib.add(key)
            bib_keys.add(key)
    for key in sorted(duplicate_bib):
        errors.append(f"duplicate bibliography key: {key}")

    # Every citation in every manuscript source, including intentionally un-input
    # appendix/summary files, should resolve to the declared bibliography.
    for path in paper_tex:
        for group in CITE_RE.findall(source_text[path]):
            for key in (part.strip() for part in group.split(",")):
                if key and key not in bib_keys:
                    errors.append(f"{path.relative_to(ROOT)}: missing citation key {key}")

    # Labels/references are checked across all paper sources to catch silent ?? output.
    labels: dict[str, Path] = {}
    for path in paper_tex:
        for key in LABEL_RE.findall(source_text[path]):
            if key in labels:
                errors.append(
                    f"duplicate label {key}: {labels[key].relative_to(ROOT)} and {path.relative_to(ROOT)}"
                )
            else:
                labels[key] = path
    for path in paper_tex:
        for key in REF_RE.findall(source_text[path]):
            if key not in labels:
                errors.append(f"{path.relative_to(ROOT)}: unresolved reference {key}")

    # Graphics in reachable manuscript sources must exist at validation time. This
    # script runs after figures/generate_pdf_figures.py in the manuscript job.
    for path in reachable:
        text = strip_comments(path.read_text(encoding="utf-8"))
        for target in GRAPHICS_RE.findall(text):
            graphic = (path.parent / target).resolve()
            if not graphic.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing graphic {target}")

    if errors:
        raise SystemExit("LaTeX source validation failed:\n" + "\n".join(errors))

    print(
        "LaTeX source validation passed: "
        f"{len(all_tex)} TeX files structurally checked; "
        f"{len(reachable)} files reachable from paper/main.tex; "
        f"{len(bib_keys)} bibliography keys available; "
        f"{len(labels)} labels resolved."
    )


if __name__ == "__main__":
    main()
