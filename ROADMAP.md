# QBS Research Roadmap

This file tracks future work. Completed theorem details belong in [`docs/research_map.md`](docs/research_map.md), the frozen snapshot belongs in [`STATUS.md`](STATUS.md), and current review state belongs in [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md).

## Current phase

The project is in **v0.3 public review / preprint preparation**.

The locked core remains T1–T5 and E1–E5. The supplementary line is complete through S2.13. The default next step is review quality, not theorem expansion.

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
- [ ] Keep E1–E5 as the locked reproducibility suite unless a review identifies a concrete missing core test.
- [ ] Preserve deterministic figure regeneration and manuscript PDF verification.
- [ ] Remove merged/superseded `agent/*` branches when a branch-delete interface is available; retain `main` and release snapshot branches.

## Publication gates

- [ ] Resolve review-driven mathematical or citation corrections.
- [ ] Freeze the manuscript candidate after substantive review stabilizes.
- [ ] Finalize author/citation metadata for the preprint version.
- [ ] Prepare `v1.0-preprint` only after review-driven revisions stabilize.
- [ ] Add DOI/arXiv metadata only when an identifier actually exists.
- [ ] Create formal GitHub Release/tag objects for public-review snapshots if release-write access becomes available and archival value justifies them.

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

The next high-value work is external review, correction, compression, and publication readiness.