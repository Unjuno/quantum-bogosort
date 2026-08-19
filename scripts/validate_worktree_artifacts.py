"""Reject ignored/untracked artifacts outside the validation job's explicit allowlist.

The repository-validation job intentionally creates Python bytecode caches through
``py_compile`` and six ignored manuscript-figure PDFs. Other ignored files (for
example an unexpected ``*.log`` or ``*.out`` written by a validator/experiment)
should not be able to hide behind ``.gitignore`` and still produce a clean CI pass.
"""
from __future__ import annotations

from pathlib import Path
import subprocess

from validate_figure_set import EXPECTED_PDFS

ROOT = Path(__file__).resolve().parents[1]
BYTECODE_PREFIXES = (
    "experiments/__pycache__/",
    "figures/__pycache__/",
    "scripts/__pycache__/",
)
EXPECTED_PDF_PATHS = {f"figures/generated_pdf/{name}" for name in EXPECTED_PDFS}


def ignored_untracked_files() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "--others", "--ignored", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    return {
        raw.decode("utf-8")
        for raw in result.stdout.split(b"\0")
        if raw
    }


def allowed(path: str) -> bool:
    if path in EXPECTED_PDF_PATHS:
        return True
    return path.endswith(".pyc") and path.startswith(BYTECODE_PREFIXES)


def main() -> None:
    ignored = ignored_untracked_files()
    unexpected = sorted(path for path in ignored if not allowed(path))

    missing_pdfs = sorted(EXPECTED_PDF_PATHS - ignored)
    if missing_pdfs:
        raise SystemExit(
            "Ignored-artifact validation failed: expected generated manuscript PDF(s) "
            "are not present as ignored/untracked outputs:\n" + "\n".join(missing_pdfs)
        )

    if unexpected:
        raise SystemExit(
            "Ignored-artifact validation failed: unexpected ignored/untracked file(s):\n"
            + "\n".join(unexpected)
        )

    bytecode_count = sum(
        1 for path in ignored if path.endswith(".pyc") and path.startswith(BYTECODE_PREFIXES)
    )
    print(
        "Ignored-artifact validation passed: only expected Python bytecode caches and the "
        f"{len(EXPECTED_PDF_PATHS)} manuscript figure PDFs are ignored/untracked "
        f"({bytecode_count} bytecode files)."
    )


if __name__ == "__main__":
    main()
