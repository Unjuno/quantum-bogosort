"""Validate the locked E1-E5 experiment manifest and processed-data provenance classes."""
from pathlib import Path
import csv
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
MANIFEST = ROOT / "experiments" / "manifest.csv"
EXPECTED_IDS = ["E1", "E2", "E3", "E4", "E5"]
EXPECTED_COLUMNS = [
    "experiment_id",
    "title",
    "primary_claim",
    "locked_files",
    "reproduction_files",
    "linked_theorems",
    "status",
]
REPRODUCTION_NAME_RE = re.compile(r"^e([1-5])_.+\.csv$")
NON_EXPERIMENT_PROVENANCE = {
    "fig2_fosd_theorem_illustration.csv",
}


def split_files(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def tracked_processed_csvs() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "--", "data/processed"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    names: set[str] = set()
    for raw in result.stdout.splitlines():
        path = Path(raw)
        if path.suffix == ".csv":
            if path.parent.as_posix() != "data/processed":
                raise SystemExit(
                    "Manifest validation failed:\n"
                    f"nested processed-data CSV is outside the flat provenance contract: {raw}"
                )
            names.add(path.name)
    return names


def main() -> None:
    errors: list[str] = []

    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_COLUMNS:
            errors.append(
                "manifest columns differ from the canonical schema: "
                f"{reader.fieldnames!r} != {EXPECTED_COLUMNS!r}"
            )
        rows = list(reader)

    ids = [row.get("experiment_id", "") for row in rows]
    if ids != EXPECTED_IDS:
        errors.append(f"experiment IDs/order must be exactly {EXPECTED_IDS!r}; got {ids!r}")
    if len(set(ids)) != len(ids):
        errors.append("duplicate experiment IDs in manifest")

    all_locked: set[str] = set()
    all_reproduction: set[str] = set()

    for row in rows:
        experiment_id = row.get("experiment_id", "")
        for field in ("title", "primary_claim", "linked_theorems"):
            if not row.get(field, "").strip():
                errors.append(f"{experiment_id}: empty required field {field}")

        if row.get("status", "").strip() != "LOCK":
            errors.append(f"{experiment_id}: status must remain LOCK")

        locked = split_files(row.get("locked_files", ""))
        reproduction = split_files(row.get("reproduction_files", ""))
        if not locked:
            errors.append(f"{experiment_id}: no locked files declared")
        if not reproduction:
            errors.append(f"{experiment_id}: no current reproduction files declared")

        overlap = set(locked) & set(reproduction)
        if overlap:
            errors.append(
                f"{experiment_id}: locked/reproduction provenance classes overlap: "
                + ", ".join(sorted(overlap))
            )

        expected_number = experiment_id.removeprefix("E")
        for name in reproduction:
            match = REPRODUCTION_NAME_RE.match(name)
            if not match or match.group(1) != expected_number:
                errors.append(
                    f"{experiment_id}: reproduction file does not use its experiment prefix: {name}"
                )

        for column, names in (("locked_files", locked), ("reproduction_files", reproduction)):
            for name in names:
                if Path(name).name != name or "/" in name or "\\" in name:
                    errors.append(f"{experiment_id}:{column}: expected CSV basename, got {name}")
                    continue
                if not name.endswith(".csv"):
                    errors.append(f"{experiment_id}:{column}: expected .csv file, got {name}")
                if not (DATA / name).is_file():
                    errors.append(f"{experiment_id}:{column}: missing {name}")

        for name in locked:
            if name in all_locked:
                errors.append(f"locked file declared by multiple experiment rows: {name}")
            all_locked.add(name)
        for name in reproduction:
            if name in all_reproduction:
                errors.append(f"reproduction file declared by multiple experiment rows: {name}")
            all_reproduction.add(name)

    cross_class = all_locked & all_reproduction
    if cross_class:
        errors.append(
            "manifest mixes locked and reproduction provenance globally: "
            + ", ".join(sorted(cross_class))
        )

    tracked = tracked_processed_csvs()
    classified = all_locked | all_reproduction | NON_EXPERIMENT_PROVENANCE
    if tracked != classified:
        unclassified = sorted(tracked - classified)
        declared_missing = sorted(classified - tracked)
        if unclassified:
            errors.append(
                "tracked processed-data CSVs lack an explicit provenance class: "
                + ", ".join(unclassified)
            )
        if declared_missing:
            errors.append(
                "provenance contract names CSVs not tracked in HEAD: "
                + ", ".join(declared_missing)
            )

    for name in NON_EXPERIMENT_PROVENANCE:
        if not (DATA / name).is_file():
            errors.append(f"missing non-experiment theorem-illustration data: {name}")

    if errors:
        raise SystemExit("Manifest validation failed:\n" + "\n".join(errors))

    print(
        "Manifest validation passed: E1-E5 are uniquely LOCKed with disjoint "
        f"provenance classes ({len(all_locked)} locked CSVs, "
        f"{len(all_reproduction)} current reproduction CSVs), and all "
        f"{len(tracked)} tracked processed-data CSVs are explicitly classified."
    )


if __name__ == "__main__":
    main()
