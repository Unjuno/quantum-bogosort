"""Validate the exact public SVG and manuscript PDF figure output sets."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / "figures" / "generated"
PDF_DIR = ROOT / "figures" / "generated_pdf"
EXPECTED_SVGS = {
    "fig1_framework.svg",
    "fig2_fosd.svg",
    "fig3_recognition_decomposition.svg",
    "fig4_interaction_sign.svg",
    "fig5_adaptation_quality.svg",
    "fig6_branch_coherence.svg",
    "fig7_predictive_alignment.svg",
}
EXPECTED_PDFS = {
    "fig1_framework.pdf",
    "fig2_fosd.pdf",
    "fig3_recognition_decomposition.pdf",
    "fig4_interaction_sign.pdf",
    "fig5_adaptation_quality.pdf",
    "fig6_branch_coherence.pdf",
}


def check_exact(directory: Path, expected: set[str], label: str, errors: list[str]) -> None:
    if not directory.is_dir():
        errors.append(f"missing {label} directory: {directory.relative_to(ROOT)}")
        return

    entries = {path.name for path in directory.iterdir()}
    missing = sorted(expected - entries)
    extra = sorted(entries - expected)
    if missing:
        errors.append(f"{label}: missing expected file(s): " + ", ".join(missing))
    if extra:
        errors.append(f"{label}: unexpected generated entry/entries: " + ", ".join(extra))

    non_files = sorted(name for name in expected if not (directory / name).is_file())
    if non_files:
        errors.append(f"{label}: expected path is not a regular file: " + ", ".join(non_files))


def main() -> None:
    errors: list[str] = []
    check_exact(SVG_DIR, EXPECTED_SVGS, "public SVG set", errors)
    check_exact(PDF_DIR, EXPECTED_PDFS, "manuscript PDF figure set", errors)

    if errors:
        raise SystemExit("Figure-set validation failed:\n" + "\n".join(errors))

    print(
        "Figure-set validation passed: exact "
        f"{len(EXPECTED_SVGS)}-SVG public set and {len(EXPECTED_PDFS)}-PDF manuscript set present."
    )


if __name__ == "__main__":
    main()
