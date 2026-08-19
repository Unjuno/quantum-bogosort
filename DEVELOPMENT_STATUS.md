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
- detailed pre-announcement execution audit: [`docs/pre_announcement_execution_audit_2026-08-19.md`](docs/pre_announcement_execution_audit_2026-08-19.md);
- second-pass validator/Actions audit: [`docs/pre_announcement_validator_audit_2026-08-19.md`](docs/pre_announcement_validator_audit_2026-08-19.md);
- archived v0.2 snapshot: tag/Release `v0.2-public-review` at commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

PRs #11–#20 preserve the staged derivation history. PR #21 preserves the cumulative integration history. PRs #27–#29 preserve the earlier pre-announcement rendering, visualization, reproducibility, and landing-page QA history. Current authoritative statements are the frozen v0.3 snapshot and the files on `main`.

## Branch and archive state

The repository has a single active branch:

- `main` — current review/development surface.

Frozen scientific snapshots are archived as tags and GitHub Releases rather than as branches:

- `v0.3-public-review` — frozen v0.3 snapshot at `58038763127258bd3e2f0d41708c4dfa01f81fd6`;
- `v0.2-public-review` — archived v0.2 snapshot at `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

Both tags were re-resolved during the second-pass validator audit and remain at those commits. Merged/superseded development branches remain removed.

## Post-snapshot `main` clarifications

The frozen `v0.3-public-review` snapshot is unchanged. Subsequent `main` changes are editorial, interpretive, visualization, repository-hygiene, reproducibility-hardening, validator-hardening, or CI-hardening changes rather than new theorem content.

Current `main` now makes the following points explicit:

- recognition may include recognition of a QBS-type rule itself, while recognition has no privileged causal power beyond the policy and trajectory/accessibility changes it induces;
- future accessibility can reweight present self-location under the same first-person change of measure;
- this present-self-location statement is conditioning/change of measure, not backward causation or objective-probability modification;
- a favorable present self-location shift additionally requires alignment between expected future accessibility and the relevant favorability/utility statistic;
- the root README states the self-referential motivating question, includes a Mermaid dependency diagram, exposes direct previews for every locked experiment family E1–E5, and exposes the `main` validation workflow badge;
- `experiments/README.md` exposes the E1–E5 H/T/D/C/U map and visual result previews;
- a dedicated E2 predictive-alignment figure closes the previous visualization gap;
- committed SVGs are deterministic generator outputs, checked byte-for-byte in CI and given explicit backgrounds for dark-mode readability;
- repository Markdown display mathematics is standardized on fenced `math` blocks, and local validation rejects repository-disallowed or legacy math syntax while checking structural TeX balance inside each math block;
- Markdown fence parsing in the math, link, and GitHub-GFM validators follows the zero-to-three-space CommonMark fenced-code boundary rather than treating arbitrarily indented fence-like text as a real fence;
- repository-relative links that escape the repository root through excessive `../` traversal are rejected rather than silently skipped;
- the complete repository Markdown surface has been inspected for rendering-critical structure, including issue templates, status/governance pages, canonical docs, experiment cards, audit pages, literature notes, paper README, supplementary notes, theory pages, and archived experiment provenance pages;
- CI includes a GitHub GFM structure check that submits every repository Markdown file to GitHub's Markdown REST renderer and verifies preservation of expected headings, tables, and images; this is not treated as proof of browser-level MathJax or Mermaid rendering;
- all seven committed SVG files are validated as static/self-contained browser assets for XML structure, viewBox/size, full-viewBox white background, active elements/event handlers, external or active references, malformed/non-finite numeric attributes, and DTD/entity declarations;
- manuscript LaTeX sources are preflighted using the graph reachable from `paper/main.tex`, so an uncompiled TeX file cannot falsely satisfy a compiled `\ref`; all paper TeX sources remain linted for environments and citation keys;
- the byte-reproduction environment is pinned to Ubuntu 24.04, Python 3.11.15, NumPy 2.4.6, pandas 3.0.5, and Matplotlib 3.11.1;
- E1–E5 execute scientific regression guards for the identities, nulls, control signs/counterexamples, predictive-alignment behavior, and branch-coherence contrasts described by their experiment cards;
- the E3 recognition-label null now runs identical trajectory/accessibility arrays through the general first-person weighted-value calculation rather than comparing the same mean expression twice; the committed numerical null remains unchanged;
- manifest validation enforces E1–E5 ID/order, `LOCK` state, CSV existence, and separation of locked historical versus current reproduction provenance classes;
- current reproduction byte verification is derived from the manifest rather than from a duplicate hard-coded file list;
- after E1–E5 execute, the complete `data/processed/` tree must remain clean: current outputs must be byte-identical, locked historical files cannot change, and undeclared files are rejected even if `.gitignore` would normally hide them;
- the E5 rho-sweep current reproduction field is correctly named `action_corr_increment`; the numerical series and Figure 6 are unchanged, while locked historical schemas are preserved;
- repository structure validation now explicitly requires the five core `theory/` sources, split-license/configuration files, archived experiment provenance, both pre-announcement audit records, the validation workflow, and all principal validators;
- the four Markdown issue templates are now validated for GitHub chooser front matter and nonempty bodies;
- reusable GitHub Actions are pinned to full commit SHAs rather than mutable major-version tags;
- the `validate` workflow supports `workflow_dispatch`, so maintainers can repeat the complete audit from the Actions UI without a dummy commit;
- contributor guidance matches the current validation/reproduction commands and manual workflow path;
- historical stacked-branch review pages are labeled or worded so they are not mistaken for current branch state;
- manuscript LaTeX installation is routed through explicit Ubuntu archive/security sources to reduce runner-mirror failures;
- current public headings and research-map language avoid stale development-version labels;
- historical snapshots are represented by tags/Releases rather than release branches;
- CI uses concurrency cancellation and runtime limits to prevent indefinitely stalled validation jobs.

No T1–T5 theorem, S2-family result, or Everett-bridge status is changed by these post-snapshot corrections. The E5 schema correction changes a current reproduction column name only; the E3 null hardening changes test plumbing only. Neither changes the corresponding numerical result or scientific conclusion.

## Pre-announcement QA status

Two complementary pre-announcement passes are now recorded.

The first source/execution pass inspected the complete repository Markdown surface and the rendering/publication pipeline: validation workflow, experiment/figure/validation Python scripts, all seven committed SVG sources, `paper/main.tex`, every file under `paper/sections/`, standalone `theory/core_theorems.tex`, bibliography metadata, manifest/configuration inputs, requirements, and figure-generation code. It covered display-math fences and TeX structure, code-fence balance, Mermaid blocks, Markdown tables, images and relative paths, issue-template front matter, public-state routing language, SVG XML/browser safety, manuscript input/figure/citation/reference relationships, deterministic figure generation, experiment-output identity, dependency-sensitive serialization, experiment-specific scientific invariants, and manifest provenance classes.

A commit-fixed local execution audit of E1–E5 reproduced all twelve current reproduction CSVs byte-for-byte against their committed Git blob identities, with the intentional E5 column-name correction reflected in the current rho-sweep output. The same audit regenerated all seven SVGs byte-for-byte. The SVG structural validator passed on the regenerated files.

That pass also exposed one environment-sensitive artifact: `fig2_fosd_theorem_illustration.csv` changed at the serialization-byte level under a different NumPy/pandas stack even though the generator and numerical construction were unchanged. The repository previously requested a byte-for-byte diff while allowing broad dependency ranges. The numerical environment was therefore pinned to the explicit environment demonstrated by the earlier successful reproduction run.

The second pass audited the **validators themselves for false PASS conditions**. It corrected:

- processed-data checks that could miss locked-file mutation or undeclared/ignored generated files;
- absence of a GitHub issue-template front-matter validator;
- structure validation that omitted core theory, split-license metadata, and archived experiment provenance;
- arbitrary-whitespace fence parsing in the math/link/GFM source scanners;
- relative-link traversal outside the repository root being silently skipped;
- LaTeX reference resolution across uncompiled source files;
- SVG checks that did not reject all active-reference/event/animation classes required by the repository's static-asset policy;
- mutable `actions/*@vN` workflow dependencies;
- absence of a manual complete-workflow dispatch path;
- a weak E3 recognition-label null calculation path.

The manifest/reproduction validators have negative-test evidence from the prior pass: a byte mutation in a current reproduction CSV is rejected, and changing a manifest experiment from `LOCK` is rejected. The current reproduction validator is stricter still: it also rejects changes to any other tracked processed-data file and any extra processed-data file, including ignored files.

The repository-validation workflow is now configured to:

- use the pinned Ubuntu/Python/numerical package environment and full-SHA-pinned reusable Actions;
- enforce repository-wide fenced display-math syntax and structural TeX balance;
- validate required repository structure, including core theory, archive, licensing/configuration, audit, executable, and validator files;
- validate GitHub issue-template chooser front matter;
- validate the E1–E5 manifest and provenance classes before executing the experiment suite;
- validate repository-relative Markdown links in rendered prose and reject root-escaping relative targets;
- submit every Markdown file to GitHub's GFM REST renderer and verify that source headings, tables, and images survive the structural conversion;
- reproduce E1–E5 while executing their scientific invariant guards;
- byte-compare every manifest-declared current reproduction CSV with committed `HEAD` and require the complete processed-data tree to remain otherwise unchanged;
- regenerate, statically validate, and byte-compare committed SVGs and the Figure 2 theorem-illustration CSV.

The manuscript workflow is now configured to:

- use the same pinned Ubuntu/Python/numerical package environment and pinned reusable Actions;
- generate the PDF figures;
- preflight the compiled LaTeX input graph, citation keys, labels/references, environments, and graphics;
- build the manuscript PDF with `latexmk`;
- verify and upload the resulting PDF.

The workflow runs on push and pull request and can be run manually with `workflow_dispatch` from `main`, which is the repository default branch.

These source/local checks do **not** mark the latest final `main` Actions run PASS. The connected GitHub interface available to this audit does not expose direct-push Actions check-run state through its commit-run lookup, and the commit-status endpoint returns no substitutable Actions status. The root README badge and/or a manually dispatched `validate` run should be used to establish the final Actions gate.

The repository is **not yet marked ready for broad announcement**. Remaining presentation gates are:

1. confirm the final `main` `validate` workflow completes successfully, including both `repository-validation` and `manuscript-build`;
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

E1–E5 remain the locked reproducibility suite. The earlier commit-fixed local audit reproduced the twelve current E1–E5 CSV outputs and all seven committed SVGs byte-for-byte under the then-current schemas, and all experiment-specific invariant guards passed. The second-pass audit strengthened the validators and workflow around that suite without changing numerical experiment conclusions.

The latest final `main` workflow result is intentionally not recorded as green until the corresponding Actions run is directly confirmed.

No sixth core experiment is planned by default.

## Manuscript state

The main text is compressed to the conceptual S2 line, with detailed S2.3–S2.10 machinery Appendix-first. The manuscript compression audit, proof review, and targeted prior-art audit are integrated.

## Physical interpretation status

The abstract weighted-measure mathematics and statistical certificates do not establish an Everettian accessibility law.

The Everett accessibility bridge remains a separate physical open problem. See [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md).

The repository does not claim that an external random-number generator becomes objectively biased. Favorable QBS effects are first-person measure shifts under the model, not causal changes in the base measure.

## Current review gates

Work should now prioritize:

1. confirmation of the final `main` Actions run including issue-template validation, manifest validation, scientific invariants, repository-wide GFM structure validation, complete processed-data cleanliness, SVG validation, and compiled-graph LaTeX preflight/build;
2. direct human GitHub-UI visual inspection of representative linked pages before broad announcement;
3. external/public proof review of S2, S2.11, S2.12, and S2.13;
4. prior-art and novelty review of the combined recognition-dependent architecture;
5. manuscript claim consistency and compression;
6. statistical-certificate assumption review, including leakage and selection boundaries;
7. independent scrutiny of the Everett accessibility bridge.

Do not add another S2-numbered theorem by default. Add new mathematical machinery only in response to a concrete modeling gap or review-identified need.
