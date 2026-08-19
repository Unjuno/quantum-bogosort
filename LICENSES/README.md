# Licensing map

This repository uses path-explicit split licensing. The rule is based on repository role/path, not merely on filename extension.

## MIT — executable/software-support layer

The root [`LICENSE`](../LICENSE) applies to:

- all Python source files (`**/*.py`);
- GitHub Actions workflow files under `.github/workflows/`;
- `requirements.txt`;
- `.python-version`;
- `.gitignore`.

These are the executable/configuration files used to run, validate, or reproduce the repository.

## CC BY 4.0 — research/documentation layer

[`CC-BY-4.0.txt`](CC-BY-4.0.txt) applies to:

- all Markdown research/documentation files (`**/*.md`), including issue templates and this licensing map;
- all LaTeX manuscript/theory source files (`**/*.tex`);
- `paper/references.bib`;
- all committed SVG figures under `figures/generated/`;
- `CITATION.cff`;
- `experiments/manifest.csv`.

`experiments/manifest.csv` is curated research/provenance metadata, not a generated research dataset, so it is intentionally **not** placed under CC0 merely because it is a CSV file.

## CC0 1.0 Universal — generated research data

[`CC0-1.0.txt`](CC0-1.0.txt) applies to:

- every committed generated/locked research CSV under `data/processed/`.

No CSV outside `data/processed/` is assigned to CC0 by this rule.

## License/notice files

The root `LICENSE` contains the scoped MIT grant itself. `LICENSES/CC-BY-4.0.txt` and `LICENSES/CC0-1.0.txt` are concise licensing notices that identify the applicable Creative Commons instrument and link to its canonical legal code; they are not research content being relicensed by this map.

The categories above are intended to cover every other tracked repository file exactly once. `scripts/validate_license_map.py` checks the tracked Git inventory against these path rules so a new file class cannot silently fall outside the declared split-license scheme.
