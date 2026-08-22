# Contributing and Public Review

QBS is currently in public technical review. The highest-value contributions are corrections, counterexamples, reproducibility failures, prior-art overlap, recursive-model stress tests, and precise criticism of the Everett bridge.

## Before opening an issue

Identify which layer the concern applies to:

1. exact mathematics or proof;
2. statistical certificate or assumption;
3. classical simulation or reproducibility;
4. prior art or novelty positioning;
5. observer/accessibility model;
6. recursive observer-information / model-comparison extension;
7. Everett physical bridge;
8. documentation or repository structure.

Do not collapse these layers. For example, failure of the Everett bridge is not by itself a counterexample to the abstract covariance identity, and failure of a particular recursive bridge-belief model is not by itself a counterexample to T1–T5.

## Current review targets

- Current frozen public-review snapshot: tag/Release `v0.3-public-review`
- Canonical current review/development surface: `main`
- Snapshot ledger: `STATUS.md`
- Current review/development status: `DEVELOPMENT_STATUS.md`
- Previous archived snapshot: tag/Release `v0.2-public-review`
- Historical derivation provenance: PRs #11–#21

The frozen v0.3 tag does not include the later unnumbered recursive observer-information extension. Review the v0.3 theorem/certificate line against the frozen snapshot; review current post-snapshot material against `main` and the canonical `docs/research_map.md` / `docs/claims_and_assumptions.md` ledgers.

## Proof or counterexample reports

Please include:

- exact theorem/corollary/proposition identifier or unnumbered supplementary section;
- file and section;
- assumptions being used;
- the exact implication, equality, inequality, assumption, or boundary condition you dispute;
- a derivation, counterexample, or smallest failing case when possible;
- whether the issue affects the locked core, a supplementary result, or only a boundary/modeling condition.

The compact standalone canonical T1–T5 body is `theory/core_theorems.tex`. Its theorem/proof/boundary content is locked to the frozen v0.3 snapshot except for the deliberate audited domain/title corrections on current `main`. A substantive change requires explicit scientific review, not a repository-QA edit.

## Recursive observer-information reports

For criticism of the unnumbered recursive extension in `supplementary/evidence_activation.md`, please distinguish:

- an error in the sequential change-of-measure algebra;
- an error in the predictable/innovation decomposition;
- dependence on an inappropriate information filtration;
- misspecification of the candidate bridge/null observer models;
- survivorship-only or ordinary Bayesian explanations that reproduce the same apparent evidence;
- an implementation error in `supplementary/recursive_qbs_simulation.py`;
- a physical objection to the accessibility bridge itself.

`Innovation selection` is intentionally filtration-relative. Showing that a different information state changes the predictable/innovation split is therefore important model criticism, but not by itself a contradiction of the decomposition identity.

## Reproducibility reports

Please include:

- operating system and Python version;
- command run;
- relevant traceback or output;
- experiment/script ID;
- whether the failure reproduces on a clean environment.

Core experiments E1–E5 are expected to run under GitHub Actions. The repository pins the primary Python package versions to reduce execution-environment drift; install `requirements.txt` rather than substituting newer dependency versions when checking committed reproduction outputs. Current numeric CSV cells are compared to committed `HEAD` with a tight `rtol=1e-12`, `atol=1e-14` contract, while schema, row order, and non-numeric cells must match exactly and the experiment scripts retain independent scientific regression assertions.

The recursive QBS toy is supplementary exploratory code rather than part of the locked E1–E5 manifest. Run it separately with:

```bash
python supplementary/recursive_qbs_simulation.py
```

## Prior-art reports

Please provide a primary source where possible and explain the structural overlap. The useful question is not merely whether another work mentions Everett, anthropics, observer selection, Bayesian updating, martingales, or decision theory, but whether it duplicates a specific QBS construction or the combined recognition-dependent architecture.

Standard change-of-measure, conditional-expectation, martingale/predictable decomposition, likelihood-ratio, and KL identities are not claimed as standalone novelty.

## Everett bridge criticism

Please distinguish:

- mathematical inconsistency of a proposed accessibility map;
- observer-model inadequacy;
- conflict with an Everettian probability account;
- lack of physical derivation;
- empirical rejection of a concrete physical prediction.

The repository does not treat the abstract weighted measure, recursive belief updating, or classical toy simulations as a derivation of Everettian physics.

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

Repository-relative Markdown links currently must not use local `#fragment` or `?query` suffixes. The validator deliberately rejects them until a GitHub-compatible heading-slug/query validator is implemented, rather than silently validating only the file part of a potentially broken anchor.

Before committing documentation, metadata, theory, or repository-structure changes, run:

```bash
python scripts/validate_runtime_contract.py
python scripts/validate_markdown_math.py
python scripts/validate_markdown_links.py
python scripts/validate_repository_structure.py
python scripts/validate_core_theorem_lock.py
python scripts/validate_citation_metadata.py
python scripts/validate_bibliography_metadata.py
python scripts/validate_license_map.py
python scripts/validate_issue_templates.py
python scripts/validate_manifest.py
python scripts/validate_svg_sources.py
```

The GitHub-GFM renderer and live frozen-tag/Release checks require network access and are run by Actions with the scoped workflow token:

```bash
python scripts/validate_github_markdown_render.py
python scripts/validate_snapshot_refs.py
```

For manuscript-source changes, generate the PDF figures before the LaTeX dependency preflight:

```bash
python figures/generate_pdf_figures.py
python scripts/validate_latex_sources.py
```

For experiment changes, run the locked suite and then verify declared output equivalence plus repository cleanliness:

```bash
python experiments/exp1_fosd_and_stress.py
python experiments/exp2_minimal_agent.py
python experiments/exp3_recognition_decomposition.py
python experiments/exp4_interaction.py
python experiments/exp5_branch_map.py
python scripts/validate_reproduction_outputs.py
```

The manifest validator fixes the canonical E1–E5 locked/current file mappings, experiment-card theory routing, and all 16 frozen historical CSV Git blob identities. The reproduction validator is manifest-driven: it requires the tracked E1–E5 current CSV set to match the manifest; requires exact schema, row order, and non-numeric cells; requires numeric cells to match committed `HEAD` within `rtol=1e-12`, `atol=1e-14`; rejects changes to tracked repository content outside the declared current outputs during experiment execution; and rejects undeclared generated files under `data/processed/`, including ignored files. After a successful comparison, it restores the committed canonical current-output bytes before later clean-worktree checks.

For figure changes, regenerate both the public SVGs and the gitignored manuscript PDF figures before validating the exact output sets:

```bash
python figures/generate_figures.py
python figures/generate_pdf_figures.py
python scripts/validate_figure_set.py
python scripts/validate_svg_sources.py
git diff --exit-code -- figures/generated/ data/processed/fig2_fosd_theorem_illustration.csv
git diff --exit-code
test -z "$(git ls-files --others --exclude-standard)"
```

GitHub Actions additionally sends every repository Markdown file through GitHub's GFM rendering API and checks that expected source headings, tables, inline images, and fenced blocks survive server-side GFM conversion. This structural check complements, but does not replace, direct browser inspection of GitHub's MathJax, Mermaid, SVG sizing, and page layout.

The repository-validation job also runs `scripts/validate_worktree_artifacts.py` at the end. That check uses an **exact CI-only ignored-artifact allowlist** derived from the Python files compiled by the workflow plus the six generated manuscript PDFs. Do not treat it as a normal local-development check in a checkout containing an ignored `.venv/` or other deliberate local tooling; its purpose is to prove that the clean Actions checkout produced only the ignored artifacts expected from validation itself.

The `validate` workflow is configured with `workflow_dispatch`, so repository maintainers can use **Actions → validate → Run workflow** on `main` to repeat the complete CI audit without creating a dummy commit. The workflow's reusable Actions are pinned to audited full commit SHAs, checkout credentials are not persisted into later steps, and the workflow token is read-only; update these constraints deliberately rather than weakening them incidentally.