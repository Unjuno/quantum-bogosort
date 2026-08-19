"""Reject ignored/untracked artifacts outside the validation job's exact allowlist.

The repository-validation job intentionally creates Python bytecode through the explicit
``py_compile experiments/*.py figures/*.py scripts/*.py`` step and six ignored manuscript
figure PDFs. Derive the exact bytecode paths from those top-level source files rather than
allowing arbitrary ``*.pyc`` names anywhere under a cache directory. Other ignored files
must not be able to hide behind ``.gitignore`` and still produce a clean CI pass. Every
allowed artifact must also be a nonsymlink regular file; matching an allowed pathname is
not sufficient.
"""
from __future__ import annotations

from importlib.util import cache_from_source
from pathlib import Path
import subprocess

from validate_figure_set import EXPECTED_PDFS

ROOT = Path(__file__).resolve().parents[1]
PYTHON_SOURCE_DIRS = (
    ROOT / "experiments",
    ROOT / "figures",
    ROOT / "scripts",
)
EXPECTED_PDF_PATHS = {f"figures/generated_pdf/{name}" for name in EXPECTED_PDFS}


def expected_bytecode_paths() -> set[str]:
    """Mirror the workflow's top-level ``py_compile`` source globs exactly."""
    paths: set[str] = set()
    for directory in PYTHON_SOURCE_DIRS:
        for source in sorted(directory.glob("*.py")):
            cached = Path(cache_from_source(str(source))).resolve()
            try:
                paths.add(cached.relative_to(ROOT).as_posix())
            except ValueError as exc:
                raise SystemExit(
                    "Ignored-artifact validation failed: derived bytecode path escapes repository: "
                    f"{cached}"
                ) from exc
    return paths


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


def validate_artifact_types(expected: set[str]) -> list[str]:
    errors: list[str] = []
    for relative in sorted(expected):
        path = ROOT / relative
        if path.is_symlink():
            errors.append(f"{relative} (symlink; nonsymlink regular file required)")
        elif not path.is_file():
            errors.append(f"{relative} (missing or not a regular file)")
    return errors


def main() -> None:
    ignored = ignored_untracked_files()
    expected_pycs = expected_bytecode_paths()
    expected = EXPECTED_PDF_PATHS | expected_pycs

    missing_pdfs = sorted(EXPECTED_PDF_PATHS - ignored)
    if missing_pdfs:
        raise SystemExit(
            "Ignored-artifact validation failed: expected generated manuscript PDF(s) "
            "are not present as ignored/untracked outputs:\n" + "\n".join(missing_pdfs)
        )

    missing_pycs = sorted(expected_pycs - ignored)
    if missing_pycs:
        raise SystemExit(
            "Ignored-artifact validation failed: expected py_compile bytecode output(s) "
            "are missing:\n" + "\n".join(missing_pycs)
        )

    unexpected = sorted(ignored - expected)
    if unexpected:
        raise SystemExit(
            "Ignored-artifact validation failed: unexpected ignored/untracked file(s):\n"
            + "\n".join(unexpected)
        )

    invalid_types = validate_artifact_types(expected)
    if invalid_types:
        raise SystemExit(
            "Ignored-artifact validation failed: allowed artifact path is not a nonsymlink "
            "regular file:\n" + "\n".join(invalid_types)
        )

    print(
        "Ignored-artifact validation passed: ignored/untracked files equal the exact "
        f"workflow-derived allowlist ({len(expected_pycs)} bytecode files and "
        f"{len(EXPECTED_PDF_PATHS)} manuscript figure PDFs), all as nonsymlink regular files."
    )


if __name__ == "__main__":
    main()
