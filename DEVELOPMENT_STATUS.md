# QBS Current Research Status

**Updated:** 2026-08-19

This file records the current review and development state. It complements the frozen snapshot ledger in [`STATUS.md`](STATUS.md) and the future-work ledger in [`ROADMAP.md`](ROADMAP.md).

## Source of truth

- current frozen public-review snapshot: tag/Release `v0.3-public-review` at commit `58038763127258bd3e2f0d41708c4dfa01f81fd6`;
- current review/development surface: `main`;
- current snapshot ledger: [`STATUS.md`](STATUS.md);
- canonical claim/theorem/evidence index: [`docs/research_map.md`](docs/research_map.md);
- authoritative claim boundaries: [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md);
- future work: [`ROADMAP.md`](ROADMAP.md);
- archived v0.2 snapshot: tag/Release `v0.2-public-review` at commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

PRs #11–#20 preserve the staged derivation history. PR #21 preserves the cumulative integration history. PRs #27–#29 preserve the earlier pre-announcement rendering, visualization, reproducibility, and landing-page QA history. Current authoritative statements are the frozen v0.3 snapshot and the files on `main`.

## Branch and archive state

The repository has a single active branch:

- `main` — current review/development surface.

Frozen scientific snapshots are archived as tags and GitHub Releases rather than as branches:

- `v0.3-public-review` — frozen v0.3 snapshot;
- `v0.2-public-review` — archived v0.2 snapshot.

This keeps archival states immutable without making them look like pending or unmerged development work. Merged/superseded development branches have been removed.

## Post-snapshot `main` clarifications

The frozen `v0.3-public-review` snapshot is unchanged. Subsequent `main` changes are editorial, interpretive, visualization, repository-hygiene, reproducibility-hardening, or CI-hardening changes rather than new theorem or experiment content.

Current `main` now makes the following points explicit:

- recognition may include recognition of a QBS-type rule itself, while recognition has no privileged causal power beyond the policy and trajectory/accessibility changes it induces;
- future accessibility can reweight present self-location under the same first-person change of measure;
- this present-self-location statement is conditioning/change of measure, not backward causation or objective-probability modification;
- a favorable present self-location shift additionally requires alignment between expected future accessibility and the relevant favorability/utility statistic;
- the root README states the self-referential motivating question, includes a Mermaid dependency diagram, and exposes direct previews for every locked experiment family E1–E5;
- `experiments/README.md` exposes the E1–E5 H/T/D/C/U map and visual result previews;
- a dedicated E2 predictive-alignment figure closes the previous visualization gap;
- committed SVGs are deterministic generator outputs, checked byte-for-byte in CI and given explicit backgrounds for dark-mode readability;
- repository Markdown display mathematics is standardized on fenced `math` blocks, and local validation rejects repository-disallowed or legacy math syntax while checking structural TeX balance inside each math block;
- every repository Markdown source has been inspected in the current rendering audit, including issue templates, status/governance pages, canonical docs, experiment cards, audit pages, literature notes, paper README, supplementary notes, and theory pages;
- CI includes a GitHub GFM structure check that submits every repository Markdown file to GitHub's Markdown REST renderer and verifies preservation of expected headings, tables, and images; this is not treated as proof of browser-level MathJax or Mermaid rendering;
- all seven committed SVG files are validated as XML/browser assets for viewBox/size, explicit background, active/external content, and non-finite attributes;
- manuscript LaTeX sources are preflighted for input paths, environments, bibliography/citation keys, labels/references, and generated graphics before `latexmk` runs;
- the numerical environment used for byte-level reproduction is pinned to Python 3.11.15, NumPy 2.4.6, pandas 3.0.5, and Matplotlib 3.11.1;
- CI now verifies all twelve current E1–E5 reproduction CSVs byte-for-byte after executing the experiment scripts, rather than merely running the scripts;
- contributor guidance points to snapshot tags/Releases rather than removed release branches and matches the current rendering/reproducibility policy;
- historical stacked-branch review pages are labeled or worded so they are not mistaken for current branch state;
- manuscript LaTeX installation is routed through explicit Ubuntu archive/security sources to reduce runner-mirror failures;
- current public headings and research-map language avoid stale development-version labels;
- historical snapshots are represented by tags/Releases rather than release branches;
- CI uses concurrency cancellation and runtime limits to prevent indefinitely stalled validation jobs.

No T1–T5 theorem, E1–E5 experiment, S2-family result, or Everett-bridge status is changed by these post-snapshot clarifications.

## Pre-announcement QA status

The current source-level rendering/reproducibility audit inspected all 66 repository Markdown files rather than only representative entry pages. It also inspected the rendering pipeline and publication sources: the validation workflow, experiment/figure/validation Python scripts, all seven committed SVG sources, `paper/main.tex`, every file under `paper/sections/`, the standalone `theory/core_theorems.tex`, bibliography metadata, manifest/configuration inputs, requirements, and figure-generation code.

The audit covered display-math fences and TeX structure, code-fence balance, Mermaid blocks, Markdown tables, images and relative paths, issue-template front matter, public-state routing language, SVG XML/browser safety, manuscript input/figure/citation/reference relationships, deterministic figure generation, experiment-output identity, and dependency-sensitive serialization.

A commit-fixed local execution audit of E1–E5 reproduced all twelve current reproduction CSVs byte-for-byte against the committed Git blob identities. The same audit regenerated all seven SVGs byte-for-byte. It also exposed one environment-sensitive artifact: `fig2_fosd_theorem_illustration.csv` changed at the serialization-byte level under a different NumPy/pandas stack even though the generator and numerical construction were unchanged. The repository previously requested a byte-for-byte diff while allowing broad dependency ranges. The numerical environment is therefore now pinned to the exact versions demonstrated by the earlier successful GitHub Actions reproduction run, and the workflow explicitly checks all current reproduction CSVs as well as the figure/theorem-illustration outputs.

Source findings corrected during this pass include stale release-branch references, obsolete double-dollar contribution guidance, historical stacked-branch wording that could be read as current state, a fixed-three-backtick assumption in the Markdown validator, literal-code false positives in the link validator, insufficient structural checks inside Markdown math, the absence of a GitHub GFM structure test in CI, the absence of SVG XML/browser validation, the absence of a LaTeX dependency/reference preflight, unpinned numerical dependencies despite byte-level output verification, and lack of byte-diff enforcement for the twelve E1–E5 reproduction CSVs.

The repository-validation workflow is now configured to:

- use the pinned Python/numerical package environment;
- enforce repository-wide fenced display-math syntax and structural TeX balance;
- validate repository-relative Markdown links in rendered prose rather than literal code examples;
- validate required repository structure;
- submit every Markdown file to GitHub's GFM REST renderer and verify that source headings, tables, and images survive the structural conversion;
- reproduce E1–E5 and byte-compare all twelve committed current reproduction CSVs;
- regenerate, structurally validate, and byte-compare committed SVGs and the Figure 2 theorem-illustration CSV;
- validate manifest references.

The manuscript workflow is now configured to:

- use the same pinned Python/numerical package environment;
- generate the PDF figures;
- preflight all LaTeX source relationships, citation keys, labels/references, environments, and graphics;
- build the manuscript PDF with `latexmk`;
- verify and upload the resulting PDF.

These new/strengthened checks have been added to `main`, but the latest push-run result must still be confirmed before they are marked PASS. Source inspection and local deterministic-output checks are distinct from execution evidence on the final `main` commit, and both are distinct from browser-level visual inspection.

The repository is **not yet marked ready for broad announcement**. Remaining presentation gates are:

1. confirm the latest `main` validation run, including the GFM-structure, twelve-CSV byte-diff, SVG, and LaTeX preflight steps;
2. directly inspect rendered GitHub pages on desktop/mobile, not only the root README, with representative theory, experiment, canonical-doc, supplementary, and audit pages included;
3. confirm MathJax output, Mermaid rendering, SVG sizing/readability, tables, and overall navigation in the actual GitHub UI.

These are presentation/release checks, not new-theory requirements.

## Locked core

The core theorem set remains T1–T5.

The core experiment set remains E1–E5.

Neither set is renumbered or replaced by the supplementary work integrated in v0.3.

## Current supplementary result

The supplementary line is complete through S2.13 and is presented as one conceptual spine:

```math
\text{predictive alignment}
\longrightarrow
\text{general accessibility}
\longrightarrow
\text{residual penalty}
\longrightarrow
\text{explained-variance certificate}.
```

The principal review targets are S2, S2.11, S2.12, and S2.13. S2.3–S2.10 remain technical robustness and statistical-certification layers.

For theorem statements, assumptions, proof sources, and evidence classes, use [`docs/research_map.md`](docs/research_map.md) rather than this status file.

## Proof-review status

[`docs/post_v02_core_s2_proof_review.md`](docs/post_v02_core_s2_proof_review.md) records the dedicated second-pass review of S2, S2.11, S2.12, and S2.13.

Result: **PASS WITH THREE CORRECTIONS APPLIED**.

The corrections concern explicit square-integrability assumptions, bounded positive-accessibility counterexample/sharpness constructions, and the valid domain of the symmetric S2.13 threshold. The central covariance identities and inequalities are unchanged.

## Computational status

E1–E5 remain the locked reproducibility suite. A commit-fixed local audit reproduced the twelve current E1–E5 CSV outputs and all seven committed SVGs byte-for-byte. The validation workflow is configured to check Markdown syntax and GitHub GFM structure, repository-relative links, repository structure, E1–E5 output identity, deterministic and structurally valid committed SVG regeneration, manifest references, LaTeX source dependencies, manuscript build, and PDF output.

The latest post-audit `main` workflow result is intentionally not recorded as green until the corresponding Actions run is directly confirmed.

No sixth core experiment is planned by default.

## Manuscript state

The main text is compressed to the conceptual S2 line, with detailed S2.3–S2.10 machinery Appendix-first. The manuscript compression audit, proof review, and targeted prior-art audit are integrated.

## Physical interpretation status

The abstract weighted-measure mathematics and statistical certificates do not establish an Everettian accessibility law.

The Everett accessibility bridge remains a separate physical open problem. See [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md).

The repository does not claim that an external random-number generator becomes objectively biased. Favorable QBS effects are first-person measure shifts under the model, not causal changes in the base measure.

## Current review gates

Work should now prioritize:

1. confirmation of the latest `main` Actions run including repository-wide GFM structure validation, current-output byte checks, SVG validation, and LaTeX preflight;
2. direct human GitHub-UI visual inspection of representative linked pages before broad announcement;
3. external/public proof review of S2, S2.11, S2.12, and S2.13;
4. prior-art and novelty review of the combined recognition-dependent architecture;
5. manuscript claim consistency and compression;
6. statistical-certificate assumption review, including leakage and selection boundaries;
7. independent scrutiny of the Everett accessibility bridge.

Do not add another S2-numbered theorem by default. Add new mathematical machinery only in response to a concrete modeling gap or review-identified need.
