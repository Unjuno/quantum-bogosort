# QBS Research Roadmap

This file tracks future work. Completed theorem details belong in [`docs/research_map.md`](docs/research_map.md), the frozen snapshot belongs in [`STATUS.md`](STATUS.md), and current review state belongs in [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md).

## Current phase

The project is in **v0.3 public review / preprint preparation**.

The locked core remains T1–T5 and E1–E5. The supplementary line is complete through S2.13. The default next step is review quality, not theorem expansion.

Source-level presentation QA now includes repository-wide GitHub rendering hardening, a second-pass audit of the validators themselves for false-PASS conditions, and an external bibliography/prior-art metadata truth pass. Broad announcement remains gated on the final `main` Actions result, direct human inspection of rendered GitHub pages, and final repository-governance cleanup.

## Immediate review gates

- [ ] Obtain external/public proof review of S2, S2.11, S2.12, and S2.13.
- [ ] Collect concrete counterexamples, assumption objections, or boundary-condition corrections if reviewers identify them.
- [ ] Obtain focused prior-art review of the combined recognition-dependent architecture.
- [x] Cross-check current manuscript bibliography chronology/provenance against publisher, journal, author, or archival records where available; prefer verified publication records when a later preprint upload would obscure established prior-art chronology, while retaining genuinely earlier public preprints and current working papers deliberately.
- [x] Align the three working `literature/` ledgers with the authoritative recognition boundary so they do not describe recognition as having privileged physical causal power.
- [ ] Review whether S2.13 should remain in the manuscript main text.
- [ ] Decide whether all S2.5–S2.10 material belongs in the paper Appendix or partly in repository-only supplementary material.
- [ ] Review the Everett accessibility bridge independently from the abstract covariance mathematics.

## Repository and reproducibility gates

- [ ] Keep `main` CI-green after review-driven editorial or scientific corrections.
- [ ] Keep README, research map, claim ledger, notation, status, and roadmap free of conflicting source-of-truth roles.
- [x] Validate repository-relative Markdown links in CI.
- [x] Reject repository-relative Markdown targets that escape the repository root; validate linked-image outer destinations and reference-style definitions in addition to ordinary inline links/images.
- [x] Inspect the complete repository Markdown surface for rendering-critical structure rather than sampling representative pages only.
- [x] Standardize repository Markdown display mathematics on balanced fenced `math` blocks; reject legacy display/inline delimiters outside literal code examples and enforce repository math-macro conventions.
- [x] Align math, link, and GFM source scanners on CommonMark's zero-to-three-space fenced-code boundary.
- [x] Validate brace balance, TeX environment balance, and common `\left`/`\right` pairing inside fenced Markdown math blocks.
- [x] Add CI GFM conversion of every Markdown file through GitHub's Markdown REST renderer with source/render structure checks for headings, tables, and images.
- [x] Validate all committed SVGs as static/self-contained XML/browser assets, including viewBox/size, full-viewBox explicit background, forbidden active/event/animation content, external/active references, malformed numeric attributes, and non-finite attributes.
- [x] Validate manuscript LaTeX input, bibliography/citation, environment, generated-graphic dependencies, and resolve compiled references only within the graph reachable from `paper/main.tex`.
- [x] Lock `paper/sections/robust_mom_summary.tex` as the sole intentionally uncompiled paper TeX source so accidental omission of any other section from `main.tex` fails preflight.
- [x] Validate bibliography provenance classes structurally: journal records require journal/volume/pages/DOI, book chapters require booktitle/editor/publisher/pages/DOI, and arXiv-only records use a separate eprint/archive contract.
- [x] Pin the primary byte-reproduction contract: Ubuntu 24.04, Python 3.11.15, NumPy 2.4.6, pandas 3.0.5, and Matplotlib 3.11.1.
- [x] Cross-check `.python-version`, primary package pins/installed versions, runner choice, required jobs/commands, manual dispatch, full-SHA action pins, and checkout credential isolation with `scripts/validate_runtime_contract.py` in both jobs.
- [x] Pin reusable GitHub Actions to full commit SHAs rather than mutable major-version tags.
- [x] Set `persist-credentials: false` for checkout in both jobs and keep workflow permissions at `contents: read`.
- [x] Add `workflow_dispatch` so maintainers can run the complete `validate` workflow manually on `main` without a dummy commit.
- [x] Expose the `main` validation workflow badge on the root README.
- [x] Validate GitHub issue-template chooser front matter and nonempty bodies in CI.
- [x] Synchronize the open S2 review Issue #14 with the repository fenced-math/operator rendering convention.
- [x] Add executable scientific regression guards to E1–E5 for the declared identities, nulls, controls, signs, and coherence/predictive-alignment behavior.
- [x] Route the E3 inert recognition-label null through the general first-person weighted-value calculation while preserving its committed exact-zero result.
- [x] Validate manifest ID/order, `LOCK` state, file existence, and separation of locked historical versus current reproduction provenance classes.
- [x] Derive current reproduction byte validation from the manifest rather than maintaining a duplicate hard-coded CSV list in CI.
- [x] Require E1–E5 execution to leave the complete `data/processed/` tree otherwise unchanged, including no locked-file mutation and no undeclared ignored files.
- [x] Explicitly require core theory sources, split-license/configuration files, archived experiment provenance, all three pre-announcement audits, and principal validator scripts in repository-structure validation.
- [x] Expose the committed SVG theorem/simulation figures through the README, experiment index, and figure-provenance page.
- [x] Provide a dedicated visual route for every locked experiment family E1–E5, including E2 predictive alignment.
- [x] Require committed SVGs and the deterministic Figure 2 theorem-illustration CSV to match generator output byte-for-byte under the pinned primary runtime contract.
- [x] Keep deterministic theorem illustrations, current reproduction outputs, and locked historical summaries explicitly separated at figure level.
- [x] Provide a static SVG fallback for the root Mermaid dependency diagram.
- [x] Keep `main` as the only active branch; preserve frozen v0.2/v0.3 snapshots as named, commit-pinned tags/GitHub Releases and record their exact commits.
- [ ] Confirm the final `main` `validate` workflow is green after the validator/Actions/bibliography changes.
- [ ] Confirm rendered GitHub pages display correctly in the web UI, including the root README plus representative theory, experiment, canonical-doc, supplementary, literature, and audit pages.
- [ ] After final CI stabilizes, configure a `main` branch ruleset/protection policy appropriate for the public source-of-truth branch; the current branch API reports classic protection disabled.
- [ ] Consider a tag ruleset restricting updates/deletions for frozen release tags if platform-level immutability is desired; current documentation relies on explicit commit pinning rather than assuming such protection.
- [ ] Normalize repository-header metadata before broad promotion: replace the stale `recognition-activated` description with recognition-dependent wording and add relevant topics; the current audit connector cannot write repository metadata/settings.
- [ ] Keep E1–E5 as the locked reproducibility suite unless a review identifies a concrete missing core test.
- [ ] Preserve deterministic figure regeneration and manuscript PDF verification.

Detailed audit records:

- [`docs/pre_announcement_execution_audit_2026-08-19.md`](docs/pre_announcement_execution_audit_2026-08-19.md) — commit-fixed source/execution/reproduction pass;
- [`docs/pre_announcement_validator_audit_2026-08-19.md`](docs/pre_announcement_validator_audit_2026-08-19.md) — false-PASS, validator, Actions-supply-chain, and public-routing pass;
- [`docs/pre_announcement_bibliography_audit_2026-08-19.md`](docs/pre_announcement_bibliography_audit_2026-08-19.md) — external bibliography/publication chronology and prior-art semantic-boundary pass.

## Broad-announcement gate

Before directing broad external traffic to the repository:

- [ ] complete a visual pass of the root README and representative linked research pages in GitHub desktop and mobile layouts;
- [ ] verify in the rendered UI that the main conceptual diagram, mathematical definitions, theorem pages, experiment figures, and literature/audit pages are visible without opening raw source files;
- [x] verify in repository source that every visual result links to its H/T/D/C/U experiment card and figure/data provenance;
- [x] verify that the interpretation boundary and Everett bridge status are visible from the landing-page source;
- [ ] confirm both `repository-validation` and `manuscript-build` are successful on the final `main` workflow run after the last audit/status/bibliography changes;
- [ ] finish the repository-header / branch-protection governance items above or explicitly defer them with rationale before broad promotion.

The unchecked items in this section are presentation, execution, governance, or external-review checks, not missing mathematical results.

## Publication gates

- [ ] Resolve review-driven mathematical or citation corrections.
- [x] Replace chronology-distorting later preprint-only bibliography records with verified publication metadata where source identity is clear, while preserving earlier public preprints and unresolved working papers deliberately.
- [ ] Freeze the manuscript candidate after substantive review stabilizes.
- [ ] Finalize author/citation metadata for the preprint version.
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
- a stronger recognition-time ordering theorem.

Pursue one of these only if it removes a material modeling assumption, answers a concrete review objection, introduces a genuinely useful operational quantity, or materially sharpens an existing result under motivated assumptions.

## Novelty gate

The project should continue to avoid novelty claims for standard components by themselves, including normalized weighting, covariance identities, total covariance, standard concentration inequalities, observer selection, or self-location.

The novelty hypothesis remains provisional and concerns the combined recognition-dependent architecture and its decompositions. The bibliography truth pass reduces chronology error; it does not establish novelty. A limited prior-art search is not evidence that no structural duplicate exists.

## Everett bridge gate

The physical bridge remains open. Future work on it should ask whether a concrete accessibility rule:

- has a defensible physical derivation;
- respects relabeling and coarse-graining requirements;
- is sequentially coherent;
- is compatible with established operational quantum statistics unless explicit new physics is proposed;
- yields empirical or structural consequences that distinguish it from competing accounts.

Do not treat statistical success inside the abstract model as validation of this physical bridge.

## Stop rule

Do not add S2.14 or a sixth core experiment by default.

The next high-value work is final Actions/UI confirmation, governance cleanup, external review, correction, compression, and publication readiness.
