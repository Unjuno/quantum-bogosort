"""Validate manuscript/theory LaTeX source relationships before PDF compilation."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
MAIN = PAPER / "main.tex"
EXPECTED_BIB = (PAPER / "references.bib").resolve()
INTENTIONALLY_UNCOMPILED = {
    (PAPER / "sections/robust_mom_summary.tex").resolve(),
}

INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
UNSUPPORTED_INPUT_RE = re.compile(r"\\(?:include|subfile)\{([^}]+)\}")
GRAPHICS_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
BIB_RE = re.compile(r"\\bibliography\{([^}]+)\}")
BIBLATEX_RE = re.compile(r"\\addbibresource(?:\[[^\]]*\])?\{([^}]+)\}")
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


def within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def resolve_tex_target(target: str) -> Path:
    """Resolve TeX paths as used by CI, whose working directory is paper/."""
    candidate = PAPER / target
    if candidate.suffix != ".tex":
        candidate = candidate.with_suffix(".tex")
    resolved = candidate.resolve()
    if not within(resolved, PAPER.resolve()):
        raise ValueError(f"LaTeX input escapes paper/: {target}")
    return resolved


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
        unsupported = UNSUPPORTED_INPUT_RE.findall(text)
        if unsupported:
            raise ValueError(
                f"unsupported manuscript include command in {path.relative_to(ROOT)}: "
                + ", ".join(unsupported)
            )
        for target in INPUT_RE.findall(text):
            pending.append(resolve_tex_target(target))
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

    if not MAIN.is_file():
        raise SystemExit("Missing paper/main.tex")

    for path in sorted(INTENTIONALLY_UNCOMPILED):
        if not path.is_file():
            errors.append(
                f"missing intentionally uncompiled TeX source: {path.relative_to(ROOT)}"
            )

    # Resolve the manuscript input graph and fail before TeX if an input is absent,
    # escapes paper/, or uses an input primitive not covered by this preflight.
    try:
        reachable = collect_reachable_tex()
    except (FileNotFoundError, ValueError) as exc:
        raise SystemExit(f"Invalid LaTeX input graph: {exc}") from exc
    reachable_set = set(reachable)

    paper_tex = sorted(PAPER.rglob("*.tex"))
    theory_core = ROOT / "theory/core_theorems.tex"
    if not theory_core.is_file():
        errors.append("missing standalone theory/core_theorems.tex")
        extra_tex: list[Path] = []
    else:
        extra_tex = [theory_core]
    all_tex = paper_tex + extra_tex

    source_text: dict[Path, str] = {}
    for path in all_tex:
        text = strip_comments(path.read_text(encoding="utf-8"))
        source_text[path] = text
        check_environment_balance(path, text, errors)
        if path in paper_tex and BIBLATEX_RE.search(text):
            errors.append(
                f"{path.relative_to(ROOT)}: biblatex \\addbibresource is outside the current "
                "BibTeX preflight contract"
            )
        if path in paper_tex:
            unsupported = UNSUPPORTED_INPUT_RE.findall(text)
            if unsupported:
                errors.append(
                    f"{path.relative_to(ROOT)}: unsupported \\include/\\subfile input(s): "
                    + ", ".join(unsupported)
                )

    # Bibliography declarations resolve from paper/, matching latexmk's working dir.
    bib_files: list[Path] = []
    for path in reachable:
        text = source_text.get(path)
        if text is None:
            text = strip_comments(path.read_text(encoding="utf-8"))
            source_text[path] = text
        for group in BIB_RE.findall(text):
            for name in (part.strip() for part in group.split(",")):
                bib = (PAPER / name).with_suffix(".bib").resolve()
                if not within(bib, PAPER.resolve()):
                    errors.append(f"{path.relative_to(ROOT)}: bibliography escapes paper/: {name}")
                elif not bib.is_file():
                    errors.append(f"{path.relative_to(ROOT)}: missing bibliography {name}.bib")
                else:
                    bib_files.append(bib)

    resolved_bibs = set(bib_files)
    if resolved_bibs != {EXPECTED_BIB}:
        errors.append(
            "compiled manuscript bibliography set must be exactly paper/references.bib; got "
            + (", ".join(sorted(path.relative_to(ROOT).as_posix() for path in resolved_bibs))
               if resolved_bibs else "<none>")
        )

    bib_keys: set[str] = set()
    duplicate_bib: set[str] = set()
    for bib in sorted(resolved_bibs):
        text = strip_comments(bib.read_text(encoding="utf-8"))
        for key in BIB_KEY_RE.findall(text):
            if key in bib_keys:
                duplicate_bib.add(key)
            bib_keys.add(key)
    for key in sorted(duplicate_bib):
        errors.append(f"duplicate bibliography key: {key}")

    # Every citation in every manuscript source, including intentionally un-input
    # appendix/summary files, should resolve to the manuscript bibliography.
    for path in paper_tex:
        for group in CITE_RE.findall(source_text[path]):
            for key in (part.strip() for part in group.split(",")):
                if key and key not in bib_keys:
                    errors.append(f"{path.relative_to(ROOT)}: missing citation key {key}")

    # Globally duplicate labels are confusing even if one copy is currently outside the
    # compiled graph. Check the complete paper source set, but keep compiled-ref resolution
    # separate so an uncompiled label can never make a compiled reference pass.
    all_labels: dict[str, Path] = {}
    for path in paper_tex:
        for key in LABEL_RE.findall(source_text[path]):
            if key in all_labels:
                errors.append(
                    f"duplicate manuscript label {key}: "
                    f"{all_labels[key].relative_to(ROOT)} and {path.relative_to(ROOT)}"
                )
            else:
                all_labels[key] = path

    compiled_labels: dict[str, Path] = {}
    for path in reachable:
        text = source_text[path]
        for key in LABEL_RE.findall(text):
            if key in compiled_labels:
                # The global check above already records the detailed duplicate, but retain
                # a compiled-graph-specific error so the failure mode is explicit.
                errors.append(f"duplicate compiled label {key}")
            else:
                compiled_labels[key] = path

    for path in reachable:
        for key in REF_RE.findall(source_text[path]):
            if key not in compiled_labels:
                errors.append(f"{path.relative_to(ROOT)}: unresolved compiled reference {key}")

    # Retained uncompiled sources should also be internally referentially coherent with the
    # repository manuscript source set, even though they do not participate in PDF compile.
    for path in paper_tex:
        if path.resolve() in reachable_set:
            continue
        for key in REF_RE.findall(source_text[path]):
            if key not in all_labels:
                errors.append(f"{path.relative_to(ROOT)}: unresolved retained-source reference {key}")

    # The non-reachable manuscript-source set is part of the publication structure.
    # If a new section is accidentally omitted from main.tex, fail instead of merely
    # reporting a larger unreachable count. The sole current exception is the retained
    # standalone robust-MoM summary, superseded in the compiled sequence by its appendix.
    unreachable = {path.resolve() for path in paper_tex if path.resolve() not in reachable_set}
    if unreachable != INTENTIONALLY_UNCOMPILED:
        unexpected = sorted(unreachable - INTENTIONALLY_UNCOMPILED)
        accidentally_compiled = sorted(INTENTIONALLY_UNCOMPILED - unreachable)
        if unexpected:
            errors.append(
                "unexpected TeX source(s) outside compiled graph: "
                + ", ".join(path.relative_to(ROOT).as_posix() for path in unexpected)
            )
        if accidentally_compiled:
            errors.append(
                "intentionally uncompiled TeX source(s) are now reachable; update the "
                "publication decision/allowlist deliberately: "
                + ", ".join(path.relative_to(ROOT).as_posix() for path in accidentally_compiled)
            )

    # Graphics resolve from paper/, matching `working-directory: paper` in CI. The
    # script runs after figures/generate_pdf_figures.py, so generated PDFs must exist.
    for path in reachable:
        text = source_text[path]
        for target in GRAPHICS_RE.findall(text):
            graphic = (PAPER / target).resolve()
            if not within(graphic, ROOT.resolve()):
                errors.append(f"{path.relative_to(ROOT)}: graphic escapes repository root: {target}")
            elif not graphic.is_file():
                errors.append(f"{path.relative_to(ROOT)}: missing graphic {target}")

    if errors:
        raise SystemExit("LaTeX source validation failed:\n" + "\n".join(errors))

    print(
        "LaTeX source validation passed: "
        f"{len(all_tex)} TeX files structurally checked; "
        f"{len(reachable)} files reachable from paper/main.tex; "
        f"{len(INTENTIONALLY_UNCOMPILED)} explicitly retained source outside the compiled graph; "
        f"{len(bib_keys)} bibliography keys available; "
        f"{len(compiled_labels)} compiled labels resolved."
    )


if __name__ == "__main__":
    main()
