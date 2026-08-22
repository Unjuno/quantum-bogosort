"""Validate current reproduction outputs and the post-experiment repository state.

The experiment suite is deterministic at the model/RNG level, but floating-point
reductions can differ in the last few bits across GitHub-hosted runner hardware even under
the same pinned Python/NumPy/pandas versions. Requiring byte identity for raw decimal
serialization therefore creates false failures without detecting a scientific change.

This validator instead requires exact CSV shape/order/non-numeric cells and a very tight
numeric equivalence contract. The experiment scripts' own mechanism assertions remain the
primary scientific regression guards. After a successful comparison, generated current
CSV files are restored to the committed canonical bytes so later clean-worktree checks
still prove that validation leaves no tracked artifacts behind.
"""
from __future__ import annotations

from pathlib import Path
import csv
import io
import math
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "experiments" / "manifest.csv"
DATA_RELATIVE = Path("data") / "processed"
DATA = ROOT / DATA_RELATIVE
CURRENT_NAME_RE = re.compile(r"^e[1-5]_.+\.csv$")

# These tolerances are deliberately far below the experiment-scale effects and below the
# regression thresholds enforced inside E1-E5. They absorb only last-bit floating-point
# serialization drift observed across otherwise identical GitHub-hosted runners.
NUMERIC_REL_TOL = 1e-12
NUMERIC_ABS_TOL = 1e-14
MAX_REPORTED_CELL_ERRORS = 20


def split_files(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def git_output(*args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in result.stdout.splitlines() if line]


def git_text(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def csv_rows(text: str) -> list[list[str]]:
    return list(csv.reader(io.StringIO(text)))


def numeric_equivalent(expected: str, actual: str) -> bool:
    """Return whether two CSV cells are exactly equal or tightly numerically equivalent."""
    if expected == actual:
        return True
    if expected == "" or actual == "":
        return False
    try:
        expected_value = float(expected)
        actual_value = float(actual)
    except ValueError:
        return False

    if math.isnan(expected_value) or math.isnan(actual_value):
        return math.isnan(expected_value) and math.isnan(actual_value)
    if not math.isfinite(expected_value) or not math.isfinite(actual_value):
        return expected_value == actual_value
    return math.isclose(
        expected_value,
        actual_value,
        rel_tol=NUMERIC_REL_TOL,
        abs_tol=NUMERIC_ABS_TOL,
    )


def compare_csv_to_head(relative: str) -> list[str]:
    """Compare one generated CSV to committed HEAD under the numeric contract."""
    expected_rows = csv_rows(git_text("show", f"HEAD:{relative}"))
    actual_rows = csv_rows((ROOT / relative).read_text(encoding="utf-8"))
    errors: list[str] = []

    if len(actual_rows) != len(expected_rows):
        return [
            f"{relative}: row-count drift: generated {len(actual_rows)} != committed {len(expected_rows)}"
        ]

    for row_index, (expected_row, actual_row) in enumerate(
        zip(expected_rows, actual_rows), start=1
    ):
        if len(actual_row) != len(expected_row):
            errors.append(
                f"{relative}: row {row_index} column-count drift: generated "
                f"{len(actual_row)} != committed {len(expected_row)}"
            )
            if len(errors) >= MAX_REPORTED_CELL_ERRORS:
                break
            continue

        for column_index, (expected_cell, actual_cell) in enumerate(
            zip(expected_row, actual_row), start=1
        ):
            if numeric_equivalent(expected_cell, actual_cell):
                continue
            errors.append(
                f"{relative}: row {row_index}, column {column_index}: generated "
                f"{actual_cell!r} != committed {expected_cell!r} beyond numeric tolerance"
            )
            if len(errors) >= MAX_REPORTED_CELL_ERRORS:
                break
        if len(errors) >= MAX_REPORTED_CELL_ERRORS:
            break

    return errors


def restore_canonical_outputs(paths: list[str]) -> None:
    subprocess.run(
        ["git", "checkout", "--", *paths],
        cwd=ROOT,
        check=True,
    )


def main() -> None:
    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    names: list[str] = []
    for row in rows:
        names.extend(split_files(row["reproduction_files"]))

    if not names:
        raise SystemExit("No reproduction outputs declared in manifest")
    if len(names) != len(set(names)):
        raise SystemExit("Duplicate reproduction output names in manifest")

    paths = [(DATA_RELATIVE / name).as_posix() for name in names]
    manifest_paths = set(paths)

    invalid_outputs: list[str] = []
    for relative in paths:
        path = ROOT / relative
        if path.is_symlink():
            invalid_outputs.append(f"{relative} (symlink; regular CSV required)")
        elif not path.is_file():
            invalid_outputs.append(f"{relative} (missing or not a regular file)")
    if invalid_outputs:
        raise SystemExit(
            "Missing/invalid reproduction outputs:\n" + "\n".join(invalid_outputs)
        )

    # Symlinks are outside the processed-data provenance contract. In particular, a
    # tracked CSV symlink could redirect an experiment write while leaving the Git blob
    # for the link itself unchanged, defeating a diff-based provenance check.
    symlinks = sorted(
        path.relative_to(ROOT).as_posix()
        for path in DATA.rglob("*")
        if path.is_symlink()
    )
    if symlinks:
        raise SystemExit(
            "Processed-data tree contains symlink(s); regular in-repository files are required:\n"
            + "\n".join(symlinks)
        )

    tracked_data = set(git_output("ls-files", "--", DATA_RELATIVE.as_posix()))
    tracked_current = {
        path
        for path in tracked_data
        if CURRENT_NAME_RE.match(Path(path).name)
    }
    if tracked_current != manifest_paths:
        undeclared = sorted(tracked_current - manifest_paths)
        untracked_by_manifest = sorted(manifest_paths - tracked_current)
        details: list[str] = []
        if undeclared:
            details.append(
                "tracked E1-E5 CSVs missing from manifest: " + ", ".join(undeclared)
            )
        if untracked_by_manifest:
            details.append(
                "manifest reproduction CSVs not tracked in HEAD: "
                + ", ".join(untracked_by_manifest)
            )
        raise SystemExit("Reproduction manifest/tracked-file mismatch:\n" + "\n".join(details))

    # Experiments may change only the manifest-declared current reproduction files.
    changed_repo = set(git_output("diff", "--name-only"))
    unexpected_tracked_changes = sorted(changed_repo - manifest_paths)
    if unexpected_tracked_changes:
        raise SystemExit(
            "Experiment execution changed tracked repository content outside the current "
            "reproduction outputs:\n" + "\n".join(unexpected_tracked_changes)
        )

    comparison_errors: list[str] = []
    for relative in paths:
        comparison_errors.extend(compare_csv_to_head(relative))
        if len(comparison_errors) >= MAX_REPORTED_CELL_ERRORS:
            break
    if comparison_errors:
        raise SystemExit(
            "Current reproduction output exceeds the tight committed numeric-equivalence "
            f"contract (rtol={NUMERIC_REL_TOL:g}, atol={NUMERIC_ABS_TOL:g}):\n"
            + "\n".join(comparison_errors[:MAX_REPORTED_CELL_ERRORS])
        )

    # Preserve committed CSV bytes as the repository's canonical serialization after the
    # generated values have been verified. This makes the later clean-worktree gate useful
    # without pretending that last-bit decimal serialization is hardware invariant.
    restore_canonical_outputs(paths)

    full_data_diff = subprocess.run(
        ["git", "diff", "--exit-code", "--", DATA_RELATIVE.as_posix()],
        cwd=ROOT,
        check=False,
    )
    if full_data_diff.returncode != 0:
        raise SystemExit(
            "Processed-data tree remained dirty after restoring verified canonical current outputs."
        )

    full_repo_diff = subprocess.run(
        ["git", "diff", "--exit-code"],
        cwd=ROOT,
        check=False,
    )
    if full_repo_diff.returncode != 0:
        raise SystemExit(
            "Repository remained dirty after restoring verified canonical reproduction outputs."
        )

    # Compare the actual filesystem with Git's tracked set rather than asking Git only
    # for non-ignored files; an ignored debug/log artifact in data/processed is still
    # an undeclared side effect of an experiment run. Symlinks were rejected above.
    present_data = {
        path.relative_to(ROOT).as_posix()
        for path in DATA.rglob("*")
        if path.is_file() and not path.is_symlink()
    }
    extra_files = sorted(present_data - tracked_data)
    if extra_files:
        raise SystemExit(
            "Experiment execution produced undeclared processed-data files "
            "(including ignored files):\n" + "\n".join(extra_files)
        )

    print(
        f"Reproduction output validation passed: {len(paths)} manifest-declared current "
        "CSVs exactly cover the tracked E1-E5 output set; schema/order/non-numeric cells "
        f"match exactly; numeric cells match committed HEAD within rtol={NUMERIC_REL_TOL:g}, "
        f"atol={NUMERIC_ABS_TOL:g}; no other tracked content changed; canonical committed "
        "CSV bytes were restored; and data/processed has no symlinks or undeclared files."
    )


if __name__ == "__main__":
    main()
