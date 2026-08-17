"""Check that every file named in experiments/manifest.csv exists."""
from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
MANIFEST = ROOT / "experiments" / "manifest.csv"
missing = []

with MANIFEST.open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        for column in ("locked_files", "reproduction_files"):
            for name in [x.strip() for x in row[column].split(";") if x.strip()]:
                if not (DATA / name).exists():
                    missing.append(f"{row['experiment_id']}:{column}:{name}")

if missing:
    print("Manifest references missing files:")
    print("\n".join(missing))
    sys.exit(1)
print("Manifest validation passed.")
