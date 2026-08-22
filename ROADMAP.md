# QBS Research Roadmap

This file tracks future work. Completed theorem details belong in [`docs/research_map.md`](docs/research_map.md), the frozen snapshot belongs in [`STATUS.md`](STATUS.md), and current review state belongs in [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md).

## Current phase

The project is in **v0.3 public review / preprint preparation**, with later unnumbered recursive observer-information and selection/context-identifiability work on current development.

The locked core remains T1–T5 and E1–E5. The numbered supplementary line is complete through S2.13. The recursive and selection/context-identifiability extensions are intentionally unnumbered and do not create T6, S2.14, or E6. The default next step remains review quality rather than automatic theorem expansion.

Broad announcement remains gated on final settled Actions results, direct inspection of rendered GitHub pages when available, and explicit handling or deferral of the remaining repository-governance/presentation items.

## Immediate review gates

- [ ] Obtain external/public proof review of S2, S2.11, S2.12, and S2.13.
- [ ] Collect concrete counterexamples, assumption objections, or boundary-condition corrections if reviewers identify them.
- [ ] Obtain focused prior-art review of the combined recognition-dependent architecture.
- [x] Formalize the classical selection-equivalence null for the normalized first-person law, including bounded ascertainment conditioning, general record-size bias, total-variation truncation, and the observable non-identifiability corollary.
- [x] Extend the selection-equivalence null across arbitrary policy/intervention contexts: any `Q_c << mu_c` is exactly reproducible by context-specific classical record-size bias.
- [x] Prove the context-invariant shared-selection restriction: cross-context Radon--Nikodym density ratios must be proportional on common support, with equality under one common base law.
- [x] Audit the operational limitation of that restriction: base/selected laws must be identifiable on a common observable state space, and latent violations can disappear under projection.
- [x] Add a dedicated H/T/D/C/U proof/stress audit with 20,000 random finite-state property tests and explicit projection counterexamples.
- [x] Add classical ascertainment / weighted-distribution prior art (Fisher 1934; Rao 1965; Patil--Rao 1978) and narrow novelty claims accordingly.
- [x] Add sample-selection/MNAR identifiability prior art to the research ledger/audit as a methodological comparison (Heckman; Miao--Ding--Geng; Miao--Tchetgen Tchetgen).
- [ ] Decide whether those additional selection-identifiability references should enter the manuscript bibliography fact lock in a separate bibliography-governance pass.
- [ ] Specify a concrete low-dimensional/predeclared cross-policy law for `S_pi` that is motivated independently of observed favorable outcomes.
- [ ] Specify which base and observer-conditioned quantities are operationally observable/identifiable under that candidate law.
- [ ] Design a held-out context/intervention test that compares the candidate Everett bridge against classical structural nulls with comparable degrees of freedom and no context-by-context retuning.
- [ ] Stress-test the recursive observer-information extension against model misspecification, survivorship-only controls, and alternative null observer models.
- [ ] Review whether innovation selection is a useful stable filtration-relative diagnostic rather than merely a model-dependent decomposition label.
- [x] Cross-check current manuscript bibliography chronology/provenance against publisher, journal, author, or archival records where available; prefer verified publication records when a later preprint upload would obscure established prior-art chronology, while retaining genuinely earlier public preprints and current working papers deliberately.
- [x] Align the working `literature/` ledgers with the authoritative recognition boundary so they do not describe recognition as having privileged physical causal power.
- [ ] Review whether S2.13 should remain in the manuscript main text.
- [ ] Decide whether all S2.5–S2.10 material belongs in the paper Appendix or partly in repository-only supplementary material.
- [ ] Review the Everett accessibility bridge independently from the abstract covariance mathematics and independently from the selection/context-identifiability nulls.

## Repository and reproducibility gates

- [ ] Keep `main` CI-green after review-driven editorial or scientific corrections.
- [x] Synchronize README, research map, claim ledger, supplementary index, and development status after the recursive extension.
- [x] Index the single-context selection-equivalence boundary in the supplementary index, research map, claim ledger, prior-art ledgers, manuscript, and development status.
- [x] Index the context-identifiability extension in the supplementary index, research map, claim ledger, Everett bridge tests, manuscript Discussion, development status, roadmap, and dedicated audit record.
- [x] Keep `main` as the canonical public source of truth and preserve frozen v0.2/v0.3 snapshots as named, commit-pinned tags/GitHub Releases.
- [ ] Remove redundant `fix/recursive-qbs-validation` and `research/recursive-qbs` branches; both contain no commits ahead of `main` and no file differences.
- [x] Validate repository-relative Markdown links in CI.
- [x] Reject repository-relative Markdown targets that escape the repository root; validate linked-image outer destinations and reference-style definitions in addition to ordinary inline links/images.
- [x] Inspect the complete repository Markdown surface for rendering-critical structure rather than sampling representative pages only.
- [x] Standardize repository Markdown display mathematics on balanced fenced `math` blocks; reject legacy display/inline delimiters outside literal code examples and enforce repository math-macro conventions.
- [x] Align the math, link, and GFM source scanners on CommonMark's zero-to-three-space fenced-code boundary.
- [x] Validate brace balance, TeX environment balance, and common `\left`/`\right` pairing inside fenced Markdown math blocks.
- [x] Add CI GFM conversion of every Markdown file through GitHub's Markdown REST renderer with source/render structure checks for headings, tables, and images.
- [x] Validate all committed SVGs as static/self-contained XML/browser assets, including viewBox/size, full-viewBox explicit background, forbidden active/event/animation content, external/active references, malformed numeric attributes, and non-finite attributes.
- [x] Validate manuscript LaTeX input, bibliography/citation, environment, generated-graphic dependencies, and resolve compiled references only within the graph reachable from `paper/main.tex`.
- [x] Lock `paper/sections/robust_mom_summary.tex` as the sole intentionally uncompiled paper TeX source so accidental omission of any other section from `main.tex` fails preflight.
- [x] Validate bibliography provenance classes structurally: journal records require journal/volume/pages/DOI, book chapters require booktitle/editor/publisher/pages/DOI, and arXiv-only records use a separate eprint/archive contract.
- [x] Extend the reviewed bibliography fact lock with DOI-verified Fisher and Patil--Rao ascertainment/weighted-distribution publications while retaining Rao 1965 in the repository prior-art ledger.
- [x] Pin the primary runtime/reproduction environment: Ubuntu 24.04, Python 3.11.15, NumPy 2.4.6, pandas 3.0.5, and Matplotlib 3.11.1; current floating-point reproduction CSVs use exact structure plus a tight numerical-equivalence contract rather than assuming last-bit decimal serialization is hardware invariant.
- [x] Cross-check `.python-version`, primary package pins/installed versions, runner choice, required jobs/commands, manual dispatch, full-SHA action pins, and checkout credential isolation with `scripts/validate_runtime_contract.py` in both jobs.
- [x] Pin reusable GitHub Actions to full commit SHAs rather than mutable major-version tags.
- [x] Set `persist-credentials: false` for checkout in both jobs and keep workflow permissions at `contents: read`.
- [x] Add `workflow_dispatch` so maintainers can run the complete `validate` workflow manually on `main` without a dummy commit.
- [x] Expose the `main` validation workflow badge on the root README.
- [x] Validate GitHub issue-template chooser front matter and nonempty bodies in CI.
- [x] Synchronize the open S2 review Issue #14 with current frozen-snapshot/current-main routing and keep the later recursive extension outside the frozen-v0.3 issue scope.
- [x] Add executable scientific regression guards to E1–E5 for the declared identities, nulls, controls, signs, and coherence/predictive-alignment behavior.
- [x] Route the E3 inert recognition-label null through the general first-person weighted-value calculation while preserving its committed exact-zero result.
- [x] Validate manifest ID/order, `LOCK` state, file existence, and separation of locked historical versus current reproduction provenance classes.
- [x] Derive current reproduction validation from the manifest rather than maintaining a duplicate hard-coded CSV list in CI; require exact schema/order/non-numeric cells, tight numeric equivalence, and restoration of committed canonical bytes after successful comparison.
- [x] Require E1–E5 execution to leave the complete `data/processed/` tree otherwise unchanged, including no locked-file mutation and no undeclared ignored files.
- [x] Require `supplementary/recursive_qbs_simulation.py` in the repository inventory and execute its aligned, anti-aligned, decomposition, and policy-only-null mechanism checks from CI independently of the script's own assertions.
- [x] Explicitly require core theory sources, split-license/configuration files, archived experiment provenance, pre-announcement/context-identifiability audits, principal validator scripts, and the selection-equivalence supplementary note in repository-structure validation.
- [x] Expose the committed SVG theorem/simulation figures through the README, experiment index, and figure-provenance page.
- [x] Provide a dedicated visual route for every locked experiment family E1–E5, including E2 predictive alignment.
- [x] Require committed SVGs to match generator output byte-for-byte; validate the deterministic Figure 2 theorem-illustration CSV by exact structure plus tight numerical equivalence and restore canonical bytes before the final worktree check.
- [x] Keep deterministic theorem illustrations, current reproduction outputs, and locked historical summaries explicitly separated at figure level.
- [x] Provide a static SVG fallback for the root Mermaid dependency diagram.
- [ ] Directly observe a final push-triggered `main` `validate` run when connector tooling exposes push runs; final green PR synthetic merge and actual merged trees should be compared as a fallback audit.
- [ ] Confirm rendered GitHub pages display correctly in the web UI, including desktop/mobile MathJax, Mermaid, SVG sizing, tables, and representative linked pages; current server-side GFM and SVG structural checks do not substitute for pixel-level UI inspection.
- [ ] After final CI stabilizes, configure a `main` branch ruleset/protection policy appropriate for the public source-of-truth branch; classic protection is currently disabled.
- [ ] Consider a tag ruleset restricting updates/deletions for frozen release tags if platform-level immutability is desired; current documentation relies on explicit commit pinning rather than assuming such protection.
- [ ] Normalize repository-header metadata before broad promotion: replace stale `recognition-activated` description wording with recognition-dependent wording and add relevant topics when repository-settings write access is available.
- [ ] Keep E1–E5 as the locked reproducibility suite unless a review identifies a concrete missing core test.
- [ ] Preserve deterministic figure regeneration and manuscript PDF verification.

Detailed audit records:

- [`docs/pre_announcement_execution_audit_2026-08-19.md`](docs/pre_announcement_execution_audit_2026-08-19.md) — commit-fixed source/execution/reproduction pass;
- [`docs/pre_announcement_validator_audit_2026-08-19.md`](docs/pre_announcement_validator_audit_2026-08-19.md) — false-PASS, validator, Actions-supply-chain, and public-routing pass;
- [`docs/pre_announcement_bibliography_audit_2026-08-19.md`](docs/pre_announcement_bibliography_audit_2026-08-19.md) — external bibliography/publication chronology and prior-art semantic-boundary pass;
- [`docs/pre_announcement_mathematical_domain_audit_2026-08-19.md`](docs/pre_announcement_mathematical_domain_audit_2026-08-19.md) — mathematical-domain and boundary audit;
- [`docs/context_identifiability_audit_2026-08-23.md`](docs/context_identifiability_audit_2026-08-23.md) — context-specific representability, shared-selection restriction, finite-state property test, projection counterexamples, and operational-identifiability audit.

## Broad-announcement gate

Before directing broad external traffic to the repository:

- [ ] complete a visual pass of the root README and representative linked research pages in GitHub desktop and mobile layouts when a browser-capable environment is available;
- [ ] verify in the rendered UI that the main conceptual diagram, mathematical definitions, theorem pages, experiment figures, recursive supplementary page, selection/context-identifiability page, and literature/audit pages are visible without opening raw source files;
- [x] verify in repository source that every locked visual result links to its H/T/D/C/U experiment card and figure/data provenance;
- [x] verify that the interpretation boundary and Everett bridge status are visible from the landing-page source;
- [x] verify that the recursive and selection/context-identifiability extensions are explicitly separated from frozen v0.3 and from the locked T1–T5/E1–E5 sets;
- [ ] confirm both `repository-validation` and `manuscript-build` are successful on the final settled review branch and merge result;
- [ ] either finish repository-header / redundant-branch / ruleset governance items above or explicitly defer them with rationale before broad promotion.

The unchecked items in this section are presentation, execution-observability, governance, or external-review checks, not known missing mathematical results.

## Publication gates

- [ ] Resolve review-driven mathematical or citation corrections.
- [x] Replace chronology-distorting later preprint-only bibliography records with verified publication metadata where source identity is clear, while preserving earlier public preprints and unresolved working papers deliberately.
- [x] Add the classical selection-equivalence limitation and its ascertainment prior art to manuscript Related Work and Discussion before freezing a preprint candidate.
- [x] Add the context-indexed no-go and operational-identifiability qualification to manuscript Discussion before freezing a preprint candidate.
- [ ] Decide whether the additional sample-selection/MNAR references belong in the locked manuscript bibliography or remain repository prior-art support.
- [ ] Freeze the manuscript candidate after substantive review stabilizes.
- [ ] Finalize author/citation metadata for the preprint version.
- [ ] Decide whether the recursive observer-information extension belongs in the manuscript, remains repository supplementary material, or is deferred to a later version after targeted review.
- [ ] Prepare `v1.0-preprint` only after review-driven revisions stabilize.
- [ ] Add DOI/arXiv metadata only when an identifier actually exists.
- [x] Preserve formal GitHub tags/Releases for frozen v0.2 and v0.3 public-review snapshots and record their exact target commits.

## Deferred mathematical work

The following are not automatic next steps:

- finite-sample confidence bounds for the S2.13 explained-variance quantities;
- more explicit Orlicz/mgf sufficient conditions for S2.9;
- robust estimators that weaken S2.10 higher-moment requirements;
- infinite or certification-data-dependent candidate classes;
- an additional held-out certificate experiment;
- a stronger recognition-time ordering theorem;
- a numbered theorem family for the recursive extension;
- adding still more selection representations without gaining a physically motivated identifying restriction;
- treating the current shared-selection density-ratio condition as a finished experiment before the observable-state identification problem is solved.

Pursue one of these only if it removes a material modeling assumption, answers a concrete review objection, introduces a genuinely useful operational quantity, or materially sharpens an existing result under motivated assumptions.

## Novelty gate

The project should continue to avoid novelty claims for standard components by themselves, including normalized weighting, ascertainment/weighted distributions, size-biased sampling, generic sample-selection/MNAR identifiability, covariance identities, total covariance, martingale/predictable decompositions, likelihood-ratio/KL identities, standard concentration inequalities, observer selection, or self-location.

The novelty hypothesis remains provisional and concerns the combined recognition-dependent architecture and its decompositions. The bibliography truth pass and selection/context-identifiability audits reduce novelty overclaim risk; they do not establish novelty. A limited prior-art search is not evidence that no structural duplicate exists.

## Everett bridge gate

The physical bridge remains open. Future work on it should ask whether a concrete accessibility rule:

- has a defensible physical derivation;
- respects relabeling and coarse-graining requirements;
- is sequentially coherent;
- is compatible with established operational quantum statistics unless explicit new physics is proposed;
- supplies a predeclared cross-policy/context law rather than one fitted selector per context;
- exposes base and observer-conditioned quantities that are identifiable on a common observable state space;
- yields held-out empirical, interventional, temporal, or structural consequences that distinguish it from comparably constrained classical ascertainment / record-size-bias models.

Do not treat statistical success, recursive toy-simulation success, reproduction of one weighted observer law, or reproduction of a family of separately fitted weighted laws as validation of this physical bridge.

## Stop rule

Do not add S2.14, T6, or a sixth core experiment by default.

The next high-value scientific work is to specify an **operationally identifiable, predeclared cross-context bridge consequence** that survives classical selection alternatives with comparable freedom, alongside external review, recursive-model stress testing, correction, compression, and publication readiness.
