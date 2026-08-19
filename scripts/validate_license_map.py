"""Validate the repository's path-explicit split licensing contract."""
from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ROOT_LICENSE = ROOT / "LICENSE"
MAP = ROOT / "LICENSES/README.md"
CC_BY = ROOT / "LICENSES/CC-BY-4.0.txt"
CC0 = ROOT / "LICENSES/CC0-1.0.txt"
README = ROOT / "README.md"
CITATION = ROOT / "CITATION.cff"

REQUIRED_FILES = [ROOT_LICENSE, MAP, CC_BY, CC0, README, CITATION]
LICENSE_NOTICE_PATHS = {
    "LICENSE",
    "LICENSES/CC-BY-4.0.txt",
    "LICENSES/CC0-1.0.txt",
}
MIT_EXACT_PATHS = {
    "requirements.txt",
    ".python-version",
    ".gitignore",
}
CC_BY_EXACT_PATHS = {
    "CITATION.cff",
    "experiments/manifest.csv",
}


def require(path: Path, text: str, needle: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"{path.relative_to(ROOT)}: missing licensing contract text {needle!r}")


def tracked_files() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    return {raw.decode("utf-8") for raw in result.stdout.split(b"\0") if raw}


def categories(path: str) -> set[str]:
    if path in LICENSE_NOTICE_PATHS:
        return {"license-notice"}

    matched: set[str] = set()
    suffix = Path(path).suffix.lower()

    if suffix == ".py" or path in MIT_EXACT_PATHS or (
        path.startswith(".github/workflows/") and suffix in {".yml", ".yaml"}
    ):
        matched.add("MIT")

    if path.startswith("data/processed/") and suffix == ".csv":
        matched.add("CC0-1.0")

    if suffix in {".md", ".tex", ".bib", ".svg"} or path in CC_BY_EXACT_PATHS:
        matched.add("CC-BY-4.0")

    return matched


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
        "This MIT License applies only to the repository's executable/software-support layer",
        errors,
    )
    for fragment in (
        "all Python source files",
        "GitHub Actions workflow files under `.github/workflows/`",
        "`requirements.txt`, `.python-version`, and `.gitignore`",
        "LICENSES/README.md",
        "MIT License",
        "Permission is hereby granted, free of charge",
        'copies or substantial portions of the "Software"',
        'THE SOFTWARE IS PROVIDED "AS IS"',
    ):
        require(ROOT_LICENSE, root_license, fragment, errors)

    license_map = MAP.read_text(encoding="utf-8")
    for fragment in (
        "This repository uses path-explicit split licensing.",
        "all Python source files (`**/*.py`)",
        "GitHub Actions workflow files under `.github/workflows/`",
        "`CITATION.cff`",
        "`experiments/manifest.csv`",
        "every committed generated/locked research CSV under `data/processed/`",
        "No CSV outside `data/processed/` is assigned to CC0 by this rule.",
        "cover every other tracked repository file exactly once",
        "scripts/validate_license_map.py",
    ):
        require(MAP, license_map, fragment, errors)

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
        "See [`LICENSES/README.md`](LICENSES/README.md) for the authoritative licensing map.",
        "GitHub's repository-level single-license classifier is a hosting-layer summary and is not authoritative for this split-licensed repository",
    ):
        require(README, readme, fragment, errors)

    citation = CITATION.read_text(encoding="utf-8")
    for fragment in (
        "Source code is MIT-licensed",
        "theory, documentation, manuscript text, and figures are CC BY 4.0",
        "generated research datasets are CC0 1.0",
    ):
        require(CITATION, citation, fragment, errors)

    tracked = tracked_files()
    classified_counts = {"MIT": 0, "CC-BY-4.0": 0, "CC0-1.0": 0, "license-notice": 0}
    for path in sorted(tracked):
        matched = categories(path)
        if not matched:
            errors.append(f"unclassified tracked file: {path}")
            continue
        if len(matched) != 1:
            errors.append(f"tracked file matches multiple license classes {sorted(matched)!r}: {path}")
            continue
        classified_counts[next(iter(matched))] += 1

    if errors:
        raise SystemExit("License-map validation failed:\n" + "\n".join(errors))

    print(
        "License-map validation passed: every tracked file maps to exactly one path-explicit "
        f"class ({classified_counts['MIT']} MIT, {classified_counts['CC-BY-4.0']} CC BY 4.0, "
        f"{classified_counts['CC0-1.0']} CC0, {classified_counts['license-notice']} license/notice); "
        "root notices, README boundary, and CFF summary remain consistent."
    )


if __name__ == "__main__":
    main()
