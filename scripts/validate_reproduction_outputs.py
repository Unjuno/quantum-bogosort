"""Validate current reproduction outputs and the post-experiment data tree."""
from __future__ import annotations

from pathlib import Path
import csv
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "experiments" / "manifest.csv"
DATA_RELATIVE = Path("data") / "processed"
DATA = ROOT / DATA_RELATIVE
CURRENT_NAME_RE = re.compile(r"^e[1-5]_.+\.csv$")


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

    missing = [path for path in paths if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit("Missing reproduction outputs:\n" + "\n".join(missing))

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

    diff = subprocess.run(
        ["git", "diff", "--exit-code", "--", *paths],
        cwd=ROOT,
        check=False,
    )
    if diff.returncode != 0:
        raise SystemExit(
            "Current reproduction output differs from committed HEAD; see git diff above."
        )

    # Experiment scripts are not allowed to modify locked historical data or any
    # other tracked processed-data file. Figure-generation data is produced only
    # after this validator runs in CI.
    full_diff = subprocess.run(
        ["git", "diff", "--exit-code", "--", DATA_RELATIVE.as_posix()],
        cwd=ROOT,
        check=False,
    )
    if full_diff.returncode != 0:
        raise SystemExit(
            "Experiment execution changed a processed-data file outside the accepted "
            "byte-identical reproduction contract; see git diff above."
        )

    # Compare the actual filesystem with Git's tracked set rather than asking Git only
    # for non-ignored files; an ignored debug/log artifact in data/processed is still
    # an undeclared side effect of an experiment run.
    present_data = {
        path.relative_to(ROOT).as_posix()
        for path in DATA.rglob("*")
        if path.is_file()
    }
    extra_files = sorted(present_data - tracked_data)
    if extra_files:
        raise SystemExit(
            "Experiment execution produced undeclared processed-data files "
            "(including ignored files):\n" + "\n".join(extra_files)
        )

    print(
        f"Reproduction output validation passed: {len(paths)} manifest-declared "
        "current CSVs exactly cover the tracked E1-E5 output set, are byte-identical "
        "to HEAD, and experiment execution left data/processed otherwise clean."
    )


if __name__ == "__main__":
    main()
