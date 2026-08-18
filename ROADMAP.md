# QBS Research Roadmap

This roadmap turns the public repository into the source of truth for the theory, experiments, and manuscript.

## Completed repository foundations

- [x] Publish core theorem set T1–T5.
- [x] Publish E1–E5 reproduction code and outputs.
- [x] Add CI for Markdown math delimiters, Python, E1–E5, manifest validation, figures, repository structure, and manuscript PDF build.
- [x] Maintain canonical `STATUS.md`, notation, claims ledger, and research map.
- [x] Split supplementary topics and create H/T/D/C/U experiment cards.
- [x] Build historical experiment archive policy.
- [x] Build initial/extended prior-art ledgers and narrow novelty claims.
- [x] Produce six publication figures and integrate them into the manuscript.
- [x] Integrate complete T1–T5 proofs and validate the illustrated manuscript by CI.
- [x] Specify Everett bridge support / constraint / rejection criteria.
- [x] Complete v0.2 repository/manuscript audit.

## Public-review path

- [x] Keep GitHub Issues open for proof corrections, counterexamples, prior art, and implementation bugs.
- [x] Integrate major repository corrections through CI-gated PRs.
- [ ] Create a formal GitHub Release/tag for `v0.2-public-review` when release-write access is available.
- [ ] Collect public review and revise the repository/manuscript.
- [ ] Prepare `v1.0-preprint` only after review-driven revisions stabilize.

## Post-v0.2 theorem development

- [x] S2 predictive-calibration alignment.
- [x] S2.2 posterior-mean self-calibration.
- [x] S2.3 approximate-calibration robustness.
- [x] S2.4 prediction-MSE population certificate.
- [x] S2.5 bounded held-out finite-sample certification.
- [x] S2.6 validity after arbitrary independent training.
- [x] S2.7 finite predeclared candidate post-selection validity.
- [x] S2.8 generic five-moment confidence-envelope composition.
- [x] S2.9 light-tail sub-Gaussian/Bernstein instantiation.
- [x] S2.10 robust median-of-means instantiation.
- [x] S2.11 residual conditional-covariance extension beyond `S=s(Y)`.
- [x] S2.12 sharp residual-variance certificate using conditional Cauchy--Schwarz.
- [x] S2.13 explained-variance / correlation-ratio form of the residual certificate.
- [x] Derive the perfect conditional-mean alignment simplification:
  $$
  A_U+A_S>1.
  $$
- [x] Derive the symmetric explained-variance threshold:
  $$
  A>
  \frac{1}{1+\rho_{ma}}.
  $$

### Deferred unless review demands them

- [ ] Finite-sample confidence bounds for `A_U`, `A_S`, and `rho_ma`.
- [ ] Explicit Orlicz/mgf sufficient conditions for the S2.9 Bernstein parameters.
- [ ] Robust estimators that weaken S2.10's higher-moment requirements.
- [ ] Infinite or certification-data-dependent candidate classes.
- [ ] A held-out certificate experiment.

These are no longer automatic next steps. The theorem-expansion stop rule in `docs/s2_stack_review_map.md` applies.

## Post-v0.2 manuscript and novelty review

- [x] Build the S2 stack dependency / editorial review map.
- [x] Add a semantic-preservation audit for future stack consolidation.
- [x] Compress the main manuscript to the conceptual S2 → S2.11 → S2.13 spine.
- [x] Demote detailed S2.3–S2.10 statistical machinery to Appendix-first status.
- [x] Synchronize Abstract, Introduction, Limitations, Discussion, and manuscript README.
- [x] Add a H/T/D/C/U manuscript-compression audit.
- [x] Run a targeted post-v0.2 prior-art search around observer selection, self-location, policy choice, and Everettian credence.
- [x] Add Garisto, Lewis, and Khawaja to the manuscript's prior-art boundary.
- [ ] Obtain external or dedicated proof review of S2, S2.11, S2.12, and S2.13.
- [ ] Decide whether S2.13 remains in main text after review.
- [ ] Decide whether all S2.5–S2.10 results belong in the paper Appendix or partly in repository-only supplementary material.

## Current stacked review sequence

The v0.2 public-review baseline remains fixed at merge commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

1. PR #11 — S2 through S2.3.
2. PR #12 — S2.4 prediction-MSE certificate.
3. PR #13 — S2.5 bounded finite-sample certificate.
4. PR #15 — S2.6–S2.7 selection validity.
5. PR #16 — S2.8 generic confidence-envelope composition.
6. PR #17 — S2.9 light-tail instantiation.
7. PR #18 — S2.10 robust median-of-means instantiation.
8. PR #19 — S2.11 residual conditional-covariance extension.
9. PR #20 — S2.12 residual-variance certificate.
10. PR #21 — S2.13 explained-variance certificate plus manuscript compression / review architecture.

## Current focus

Do not add another abstract S2 theorem by default. The next gate is review quality:

1. keep PR #21 CI-green;
2. inspect proof and claim boundaries rather than expanding the theorem stack;
3. incorporate concrete public-review objections if they appear;
4. defer new statistical machinery unless a reviewer identifies a specific need;
5. preserve the Everett bridge as a separate physical question.
