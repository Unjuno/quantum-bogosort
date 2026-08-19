"""Validate the exact committed/public figure output set."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / "figures" / "generated"
EXPECTED = {
    "fig1_framework.svg",
    "fig2_fosd.svg",
    "fig3_recognition_decomposition.svg",
    "fig4_interaction_sign.svg",
    "fig5_adaptation_quality.svg",
    "fig6_branch_coherence.svg",
    "fig7_predictive_alignment.svg",
}


def main() -> None:
    if not SVG_DIR.is_dir():
        raise SystemExit("Missing figures/generated directory")

    entries = {path.name for path in SVG_DIR.iterdir()}
    missing = sorted(EXPECTED - entries)
    extra = sorted(entries - EXPECTED)
    errors: list[str] = []
    if missing:
        errors.append("missing expected figure(s): " + ", ".join(missing))
    if extra:
        errors.append("unexpected generated entry/entries: " + ", ".join(extra))

    non_files = sorted(name for name in EXPECTED if not (SVG_DIR / name).is_file())
    if non_files:
        errors.append("expected figure path is not a regular file: " + ", ".join(non_files))

    if errors:
        raise SystemExit("Figure-set validation failed:\n" + "\n".join(errors))

    print(f"Figure-set validation passed: exact {len(EXPECTED)}-SVG public figure set present.")


if __name__ == "__main__":
    main()
