"""Byte-compare all manifest-declared current reproduction outputs with HEAD."""
from __future__ import annotations

from pathlib import Path
import csv
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "experiments" / "manifest.csv"
DATA_RELATIVE = Path("data") / "processed"


def split_files(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


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

    missing = [path for path in paths if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit("Missing reproduction outputs:\n" + "\n".join(missing))

    for path in paths:
        tracked = subprocess.run(
            ["git", "cat-file", "-e", f"HEAD:{path}"],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if tracked.returncode != 0:
            raise SystemExit(f"Manifest reproduction output is not tracked in HEAD: {path}")

    diff = subprocess.run(
        ["git", "diff", "--exit-code", "--", *paths],
        cwd=ROOT,
        check=False,
    )
    if diff.returncode != 0:
        raise SystemExit(
            "Current reproduction output differs from committed HEAD; see git diff above."
        )

    print(
        f"Reproduction output validation passed: {len(paths)} manifest-declared "
        "current CSVs are tracked and byte-identical to HEAD."
    )


if __name__ == "__main__":
    main()
