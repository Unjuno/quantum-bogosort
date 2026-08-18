# QBS Research Roadmap

This file tracks future work. Completed theorem details belong in [`docs/research_map.md`](docs/research_map.md), the frozen snapshot belongs in [`STATUS.md`](STATUS.md), and current review state belongs in [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md).

## Current phase

The project is in **v0.3 public review / preprint preparation**.

The locked core remains T1–T5 and E1–E5. The supplementary line is complete through S2.13. The default next step is review quality, not theorem expansion.

Source-level presentation QA now includes repository-wide GitHub rendering hardening: public Markdown display mathematics is standardized on fenced `math` blocks, repository math-macro conventions use roman forms such as `\mathrm{Cov}`, and CI rejects legacy delimiter regressions and structurally malformed math blocks. Broad announcement remains gated on direct human inspection of rendered GitHub pages and the final `main` validation state.

## Immediate review gates

- [ ] Obtain external/public proof review of S2, S2.11, S2.12, and S2.13.
- [ ] Collect concrete counterexamples, assumption objections, or boundary-condition corrections if reviewers identify them.
- [ ] Obtain focused prior-art review of the combined recognition-dependent architecture.
- [ ] Review whether S2.13 should remain in the manuscript main text.
- [ ] Decide whether all S2.5–S2.10 material belongs in the paper Appendix or partly in repository-only supplementary material.
- [ ] Review the Everett accessibility bridge independently from the abstract covariance mathematics.

## Repository and reproducibility gates

- [ ] Keep `main` CI-green after review-driven editorial or scientific corrections.
- [ ] Keep README, research map, claim ledger, notation, status, and roadmap free of conflicting source-of-truth roles.
- [x] Validate repository-relative Markdown links in CI.
- [x] Inspect all 66 repository Markdown sources for rendering-critical structure rather than sampling representative pages only.
- [x] Standardize repository Markdown display mathematics on balanced fenced `math` blocks; reject legacy display/inline delimiters outside literal code examples and enforce repository math-macro conventions.
- [x] Validate brace balance, TeX environment balance, and common `\left`/`\right` pairing inside fenced Markdown math blocks.
- [x] Add CI rendering of every Markdown file through GitHub's own GFM REST renderer with source/render structure checks for headings, tables, and images.
- [x] Validate all committed SVGs as XML/browser assets, including viewBox/size, explicit background, forbidden active elements/external hrefs, and non-finite attributes.
- [x] Validate manuscript LaTeX input, bibliography/citation, label/reference, environment, and generated-graphic dependencies before PDF compilation.
- [x] Expose the committed SVG theorem/simulation figures through the README, experiment index, and figure-provenance page.
- [x] Provide a dedicated visual route for every locked experiment family E1–E5, including E2 predictive alignment.
- [x] Require committed SVGs to match deterministic generator output byte-for-byte.
- [x] Keep deterministic theorem illustrations, current reproduction outputs, and locked historical summaries explicitly separated at figure level.
- [x] Provide a static SVG fallback for the root Mermaid dependency diagram.
- [x] Keep `main` as the only branch; preserve frozen v0.2/v0.3 snapshots as tags/GitHub Releases.
- [ ] Confirm rendered GitHub pages display correctly in the web UI, including the root README plus representative theory, experiment, canonical-doc, supplementary, and audit pages.
- [ ] Keep E1–E5 as the locked reproducibility suite unless a review identifies a concrete missing core test.
- [ ] Preserve deterministic figure regeneration and manuscript PDF verification.

## Broad-announcement gate

Before directing broad external traffic to the repository:

- [ ] complete a visual pass of the root README and representative linked research pages in GitHub desktop and mobile layouts;
- [ ] verify in the rendered UI that the main conceptual diagram, mathematical definitions, theorem pages, and experiment figures are visible without opening raw source files;
- [x] verify in repository source that every visual result links to its H/T/D/C/U experiment card and figure/data provenance;
- [x] verify that the interpretation boundary and Everett bridge status are visible from the landing-page source;
- [ ] confirm the final `main` validation state after the last presentation/status changes.

The unchecked items in this section are presentation/release checks, not missing mathematical results.

## Publication gates

- [ ] Resolve review-driven mathematical or citation corrections.
- [ ] Freeze the manuscript candidate after substantive review stabilizes.
- [ ] Finalize author/citation metadata for the preprint version.
- [ ] Prepare `v1.0-preprint` only after review-driven revisions stabilize.
- [ ] Add DOI/arXiv metadata only when an identifier actually exists.
- [x] Preserve formal GitHub tags/Releases for frozen v0.2 and v0.3 public-review snapshots.

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

The novelty hypothesis remains provisional and concerns the combined recognition-dependent architecture and its decompositions. A limited prior-art search is not evidence that no structural duplicate exists.

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

The next high-value work is direct rendered-UI QA, external review, correction, compression, and publication readiness.
