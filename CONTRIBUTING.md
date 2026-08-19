# Contributing and Public Review

QBS is currently in public technical review. The highest-value contributions are corrections, counterexamples, reproducibility failures, prior-art overlap, and precise criticism of the Everett bridge.

## Before opening an issue

Identify which layer the concern applies to:

1. exact mathematics or proof;
2. statistical certificate or assumption;
3. classical simulation or reproducibility;
4. prior art or novelty positioning;
5. observer/accessibility model;
6. Everett physical bridge;
7. documentation or repository structure.

Do not collapse these layers. For example, failure of the Everett bridge is not by itself a counterexample to the abstract covariance identity.

## Current review targets

- Current frozen public-review snapshot: tag/Release `v0.3-public-review`
- Current review/development surface: `main`
- Snapshot ledger: `STATUS.md`
- Current review/development status: `DEVELOPMENT_STATUS.md`
- Previous archived snapshot: tag/Release `v0.2-public-review`
- Historical derivation provenance: PRs #11–#21

Review current mathematics against the v0.3 snapshot or `main`. Use historical PRs only when tracing derivation provenance or earlier formulations.

## Proof or counterexample reports

Please include:

- exact theorem/corollary/proposition identifier;
- file and section;
- assumptions being used;
- the exact implication, equality, inequality, assumption, or boundary condition you dispute;
- a derivation, counterexample, or smallest failing case when possible;
- whether the issue affects the central result or only a boundary condition.

## Reproducibility reports

Please include:

- operating system and Python version;
- command run;
- relevant traceback or output;
- experiment ID;
- whether the failure reproduces on a clean environment.

Core experiments E1–E5 are expected to run under GitHub Actions. The repository pins the primary Python package versions used for byte-level reproduction; install `requirements.txt` rather than substituting newer dependency versions when checking committed-output identity.

## Prior-art reports

Please provide a primary source where possible and explain the structural overlap. The useful question is not merely whether another work mentions Everett, anthropics, observer selection, or decision theory, but whether it duplicates a specific QBS construction or decomposition.

## Everett bridge criticism

Please distinguish:

- mathematical inconsistency of a proposed accessibility map;
- observer-model inadequacy;
- conflict with an Everettian probability account;
- lack of physical derivation;
- empirical rejection of a concrete physical prediction.

The repository does not treat the abstract weighted measure as a derivation of Everettian physics.

## Markdown mathematics and rendering

Display mathematics in repository Markdown must use GitHub fenced `math` blocks:

````text
```math
E_{FP}[U]-E[U]
=
\frac{\mathrm{Cov}(U,S)}{E[S]}.
```
````

Do not introduce single-dollar math, `$$` display delimiters, `\(...\)`, or `\[...\]` in rendered repository prose. Literal examples of these syntaxes belong inside code spans or code fences.

Before committing documentation, metadata, or repository-structure changes, run:

```bash
python scripts/validate_runtime_contract.py
python scripts/validate_markdown_math.py
python scripts/validate_markdown_links.py
python scripts/validate_repository_structure.py
python scripts/validate_citation_metadata.py
python scripts/validate_bibliography_metadata.py
python scripts/validate_issue_templates.py
python scripts/validate_manifest.py
python scripts/validate_figure_set.py
python scripts/validate_svg_sources.py
```

The GitHub-GFM API validator requires network access and is run by Actions with the scoped workflow token:

```bash
python scripts/validate_github_markdown_render.py
```

For manuscript-source changes, generate the PDF figures before the LaTeX dependency preflight:

```bash
python figures/generate_pdf_figures.py
python scripts/validate_latex_sources.py
```

For experiment changes, run the locked suite and then verify declared output identity plus tracked-repository cleanliness:

```bash
python experiments/exp1_fosd_and_stress.py
python experiments/exp2_minimal_agent.py
python experiments/exp3_recognition_decomposition.py
python experiments/exp4_interaction.py
python experiments/exp5_branch_map.py
python scripts/validate_reproduction_outputs.py
```

The reproduction validator is manifest-driven. It requires the tracked E1–E5 current CSV set to match the manifest, requires current outputs to remain byte-identical to `HEAD`, rejects changes to any tracked repository content during experiment execution, and rejects undeclared generated files under `data/processed/`, including ignored files.

For figure changes, regenerate and validate the exact committed SVG set separately:

```bash
python figures/generate_figures.py
python scripts/validate_figure_set.py
python scripts/validate_svg_sources.py
git diff --exit-code -- figures/generated/ data/processed/fig2_fosd_theorem_illustration.csv
git diff --exit-code
```

GitHub Actions additionally sends every repository Markdown file through GitHub's GFM rendering API and checks that source headings, tables, images, and fenced blocks survive the server-side GFM conversion. This structural check complements, but does not replace, direct browser inspection of GitHub's MathJax, Mermaid, SVG sizing, and page layout.

The `validate` workflow is also configured with `workflow_dispatch`, so repository maintainers can use **Actions → validate → Run workflow** on `main` to repeat the complete CI audit without creating a dummy commit. The workflow's reusable Actions are pinned to full commit SHAs, checkout credentials are not persisted into later steps, and the workflow token is read-only; update these constraints deliberately rather than weakening them incidentally.
