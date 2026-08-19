"""Validate the repository's file-type split licensing declarations."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROOT_LICENSE = ROOT / "LICENSE"
MAP = ROOT / "LICENSES/README.md"
CC_BY = ROOT / "LICENSES/CC-BY-4.0.txt"
CC0 = ROOT / "LICENSES/CC0-1.0.txt"
README = ROOT / "README.md"
CITATION = ROOT / "CITATION.cff"

REQUIRED_FILES = [ROOT_LICENSE, MAP, CC_BY, CC0, README, CITATION]


def require(path: Path, text: str, needle: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"{path.relative_to(ROOT)}: missing licensing contract text {needle!r}")


def main() -> None:
    errors: list[str] = []
    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(f"missing licensing-related file: {path.relative_to(ROOT)}")
    if errors:
        raise SystemExit("License-map validation failed:\n" + "\n".join(errors))

    root_license = ROOT_LICENSE.read_text(encoding="utf-8")
    require(
        ROOT_LICENSE,
        root_license,
        "This MIT License applies to the repository's Python source code and software support files only.",
        errors,
    )
    require(ROOT_LICENSE, root_license, "LICENSES/README.md", errors)
    for standard_fragment in (
        "MIT License",
        "Permission is hereby granted, free of charge",
        'copies or substantial portions of the "Software"',
        'THE SOFTWARE IS PROVIDED "AS IS"',
    ):
        require(ROOT_LICENSE, root_license, standard_fragment, errors)

    license_map = MAP.read_text(encoding="utf-8")
    require(MAP, license_map, "This repository uses file-type split licensing.", errors)
    require(MAP, license_map, "Python source code and software support files: **MIT License**", errors)
    require(
        MAP,
        license_map,
        "Manuscript text, theoretical notes, Markdown/LaTeX documentation, and figures: **CC BY 4.0**",
        errors,
    )
    require(MAP, license_map, "Generated research CSV datasets: **CC0 1.0 Universal**", errors)

    cc_by = CC_BY.read_text(encoding="utf-8")
    require(CC_BY, cc_by, "SPDX identifier: CC-BY-4.0", errors)
    require(CC_BY, cc_by, "https://creativecommons.org/licenses/by/4.0/legalcode", errors)
    require(
        CC_BY,
        cc_by,
        "Manuscript text, theoretical notes, documentation, and figures in this repository are licensed under CC BY 4.0",
        errors,
    )

    cc0 = CC0.read_text(encoding="utf-8")
    require(CC0, cc0, "SPDX identifier: CC0-1.0", errors)
    require(CC0, cc0, "https://creativecommons.org/publicdomain/zero/1.0/legalcode", errors)
    require(
        CC0,
        cc0,
        "Generated research datasets in this repository are dedicated under CC0 1.0 Universal",
        errors,
    )

    readme = README.read_text(encoding="utf-8")
    for fragment in (
        "This repository uses file-type split licensing:",
        "source code: **MIT**",
        "theory, documentation, manuscript text, and figures: **CC BY 4.0**",
        "generated research datasets: **CC0 1.0**",
        "GitHub's repository-level license badge may show MIT because it detects the root `LICENSE`; that does not override the file-type licensing map.",
    ):
        require(README, readme, fragment, errors)

    citation = CITATION.read_text(encoding="utf-8")
    for fragment in (
        "Source code is MIT-licensed",
        "theory, documentation, manuscript text, and figures are CC BY 4.0",
        "generated research datasets are CC0 1.0",
    ):
        require(CITATION, citation, fragment, errors)

    if errors:
        raise SystemExit("License-map validation failed:\n" + "\n".join(errors))

    print(
        "License-map validation passed: root MIT scope, split-license map, Creative Commons "
        "notices, README disclosure, and CFF summary are mutually consistent."
    )


if __name__ == "__main__":
    main()
