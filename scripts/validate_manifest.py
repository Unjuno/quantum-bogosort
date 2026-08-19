"""Validate the locked E1-E5 manifest, data provenance, and experiment-card routing."""
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
CARD_DATA_RE = re.compile(r"data/processed/([A-Za-z0-9_.-]+\.csv)")
THEORY_TOKEN_RE = re.compile(r"\bT\d+\b|Corollary\s+\d+\.\d+")
CARD_MD_PATH_RE = re.compile(r"`([^`]+\.md)`")
NON_EXPERIMENT_PROVENANCE = {
    "fig2_fosd_theorem_illustration.csv",
}
EXPECTED_EXPERIMENTS = {
    "E1": {
        "card": "experiments/E1_FOSD.md",
        "locked": [
            "qbs_fosd_robustness_summary.csv",
            "qbs_fosd_monotonicity_summary.csv",
            "qbs_stress_independence_null.csv",
            "qbs_stress_nonmonotone_fosd.csv",
        ],
        "reproduction": [
            "e1_fosd_reproduction.csv",
            "e1_independence_null_reproduction.csv",
            "e1_nonmonotone_counterexample_reproduction.csv",
        ],
        "linked_theorems": "T1,T2,T3",
        "card_theory_tokens": {"T1", "T2", "T3"},
        "card_theory_paths": {"theory/theorem_1_3.md"},
    },
    "E2": {
        "card": "experiments/E2_LEARNED_AGENT.md",
        "locked": [
            "qbs_nonlinear_minimal_mock_summary.csv",
            "qbs_correlation_uplift_relation.csv",
        ],
        "reproduction": ["e2_minimal_agent_reproduction.csv"],
        "linked_theorems": "T1,T3 + adaptive-agent mechanism",
        "card_theory_tokens": {"T1", "T3"},
        "card_theory_paths": {"supplementary/adaptive_agent.md"},
    },
    "E3": {
        "card": "experiments/E3_RECOGNITION.md",
        "locked": [
            "qbs_paired_policy_selection_decomposition.csv",
            "qbs_paired_decomposition_replication_summary.csv",
            "qbs_stress_recognition_null_corrected.csv",
        ],
        "reproduction": [
            "e3_recognition_decomposition_reproduction.csv",
            "e3_recognition_null_reproduction.csv",
        ],
        "linked_theorems": "T4",
        "card_theory_tokens": {"T4"},
        "card_theory_paths": {"theory/theorem_4_5.md"},
    },
    "E4": {
        "card": "experiments/E4_INTERACTION.md",
        "locked": [
            "qbs_interaction_theorem_sign_test.csv",
            "qbs_general_interaction_summary.csv",
            "qbs_adaptation_total_effect_summary.csv",
        ],
        "reproduction": [
            "e4_fixed_selector_sign_reproduction.csv",
            "e4_general_interaction_reproduction.csv",
        ],
        "linked_theorems": "T5, Corollary 5.1",
        "card_theory_tokens": {"T5", "Corollary 5.1"},
        "card_theory_paths": {"theory/theorem_4_5.md"},
    },
    "E5": {
        "card": "experiments/E5_BRANCH_MAP.md",
        "locked": [
            "qbs_branch_policy_map_correlation_sweep.csv",
            "qbs_branch_policy_map_replication_summary.csv",
            "qbs_probabilistic_execution_corrected.csv",
            "qbs_shared_recognition_contrasts.csv",
        ],
        "reproduction": [
            "e5_q_paired_reproduction.csv",
            "e5_rho_paired_reproduction.csv",
            "e5_shared_vs_independent_recognition.csv",
            "e5_shared_recognition_contrasts.csv",
        ],
        "linked_theorems": "Recognition framework / branch-map extension",
        "card_theory_tokens": set(),
        "card_theory_paths": {
            "supplementary/branch_recognition.md",
            "docs/research_map.md",
        },
    },
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
        if path.parent.as_posix() != "data/processed":
            raise SystemExit(
                "Manifest validation failed:\n"
                f"nested tracked processed-data artifact is outside the flat provenance contract: {raw}"
            )
        if path.suffix != ".csv":
            raise SystemExit(
                "Manifest validation failed:\n"
                f"tracked processed-data artifact must be CSV under the current contract: {raw}"
            )
        names.add(path.name)
    return names


def markdown_h2_section(text: str, heading: str) -> str | None:
    """Return the body of an exact level-2 Markdown section."""
    lines = text.splitlines()
    target = f"## {heading}"
    start: int | None = None
    for index, line in enumerate(lines):
        if line.strip() == target:
            start = index + 1
            break
    if start is None:
        return None

    body: list[str] = []
    for line in lines[start:]:
        if re.match(r"^\s*##\s+", line):
            break
        body.append(line)
    return "\n".join(body).strip()


def main() -> None:
    errors: list[str] = []

    if set(EXPECTED_EXPERIMENTS) != set(EXPECTED_IDS):
        errors.append("validator self-contract: EXPECTED_EXPERIMENTS keys differ from EXPECTED_IDS")

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
        expected = EXPECTED_EXPERIMENTS.get(experiment_id)
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

        if expected is not None:
            if locked != expected["locked"]:
                errors.append(
                    f"{experiment_id}: locked provenance mapping drift: "
                    f"{locked!r} != {expected['locked']!r}"
                )
            if reproduction != expected["reproduction"]:
                errors.append(
                    f"{experiment_id}: reproduction provenance mapping drift: "
                    f"{reproduction!r} != {expected['reproduction']!r}"
                )
            if row.get("linked_theorems", "").strip() != expected["linked_theorems"]:
                errors.append(
                    f"{experiment_id}: linked_theorems drift: {row.get('linked_theorems')!r} "
                    f"!= {expected['linked_theorems']!r}"
                )

            card_path = ROOT / expected["card"]
            if not card_path.is_file():
                errors.append(f"{experiment_id}: missing experiment card {expected['card']}")
            else:
                card_text = card_path.read_text(encoding="utf-8")
                card_data = set(CARD_DATA_RE.findall(card_text))
                manifest_data = set(locked) | set(reproduction)
                if card_data != manifest_data:
                    missing_from_card = sorted(manifest_data - card_data)
                    extra_in_card = sorted(card_data - manifest_data)
                    if missing_from_card:
                        errors.append(
                            f"{experiment_id}: manifest CSV(s) absent from experiment card: "
                            + ", ".join(missing_from_card)
                        )
                    if extra_in_card:
                        errors.append(
                            f"{experiment_id}: experiment card references undeclared CSV(s): "
                            + ", ".join(extra_in_card)
                        )

                linked_section = markdown_h2_section(card_text, "Linked theory")
                if linked_section is None:
                    errors.append(f"{experiment_id}: experiment card is missing ## Linked theory")
                else:
                    card_tokens = set(THEORY_TOKEN_RE.findall(linked_section))
                    if card_tokens != expected["card_theory_tokens"]:
                        errors.append(
                            f"{experiment_id}: experiment-card theorem token drift: "
                            f"{sorted(card_tokens)!r} != {sorted(expected['card_theory_tokens'])!r}"
                        )
                    card_paths = set(CARD_MD_PATH_RE.findall(linked_section))
                    if card_paths != expected["card_theory_paths"]:
                        errors.append(
                            f"{experiment_id}: experiment-card theory-route drift: "
                            f"{sorted(card_paths)!r} != {sorted(expected['card_theory_paths'])!r}"
                        )
                    for relative_path in sorted(card_paths):
                        if not (ROOT / relative_path).is_file():
                            errors.append(
                                f"{experiment_id}: experiment-card theory route is missing: {relative_path}"
                            )

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
                errors.append(f"locked file declared more than once: {name}")
            all_locked.add(name)
        for name in reproduction:
            if name in all_reproduction:
                errors.append(f"reproduction file declared more than once: {name}")
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
        "Manifest validation passed: E1-E5 canonical locked/current mappings, manifest theorem "
        "links, experiment-card theorem tokens/routes, and card CSV references agree; provenance "
        f"classes are disjoint ({len(all_locked)} locked CSVs, {len(all_reproduction)} current "
        f"reproduction CSVs); all {len(tracked)} tracked flat processed-data CSVs are explicitly "
        "classified."
    )


if __name__ == "__main__":
    main()
