# QBS Research Roadmap

This roadmap turns the public repository into the source of truth for the theory, experiments, and manuscript.

## Phase 1 — Research map and claim discipline

- [x] Publish core theorem set.
- [x] Publish E1–E5 reproduction code and outputs.
- [x] Add CI for math delimiters, Python compilation, experiments, manifest validation, figure generation, and manuscript PDF build.
- [x] Maintain `STATUS.md` as the canonical claim ledger.
- [x] Add notation and assumptions documents.
- [x] Add a research map linking claims to proof, code, and data.

## Phase 2 — Supplementary decomposition

- [x] Multi-observer normalization.
- [x] Binary soft-QBS.
- [x] Repeated filtering.
- [x] Gaussian closed form.
- [x] Adaptive-agent mechanism.
- [x] Evidence-driven recognition.
- [x] Recognition-time stopping-time formalization.
- [x] Selectivity frontier.
- [x] Branch-wide recognition and policy coherence.

The recognition-time note explicitly defers a universal early-versus-late ordering theorem beyond v0.2 unless stronger causal/information assumptions are introduced.

## Phase 3 — Experiment cards and archive

- [x] Create H/T/D/C/U + ERROR CHECK cards for E1–E5.
- [x] Add historical experiment archive policy.
- [x] Add an archive index classifying prior work as CORE, APPENDIX CANDIDATE, SUPERSEDED, or HISTORICAL LOCAL ARTIFACT.
- [x] Decide v0.2 archive scope: no archived experiment is promoted as new active evidence, so reconstruction is not a release requirement.

## Phase 4 — Literature and novelty

- [x] Build initial Everett / self-location / observer-selection / anthropic prior-art ledger.
- [x] Add criticism-side Everett probability literature.
- [x] Add alternative many-world probability constructions and weighted-measure context.
- [x] Narrow novelty claims so normalized weighting and the covariance identity are not treated as the central novelty.
- [x] Perform targeted direct-overlap search; integrate Armstrong, Conitzer, and Cooper--Oesterheld--Conitzer into the novelty boundary.
- [ ] Continue literature search after v0.2 only if review identifies a more specific overlap question.

## Phase 5 — Figures

- [x] Framework diagram.
- [x] FOSD illustration.
- [x] Recognition decomposition.
- [x] Interaction-sign figure.
- [x] Adaptation quality / total-effect figure.
- [x] Branch-coherence versus marginal FP figure.
- [x] Commit deterministic SVG figure generator and provenance documentation.
- [x] Add PDF figure generation for LaTeX.
- [x] Place figures in the manuscript with audited captions and cross-references.

## Phase 6 — Manuscript

- [x] Create manuscript scaffold.
- [x] Add Related Work and bibliography.
- [x] Integrate complete proofs of T1–T5 into the appendix.
- [x] Add strict/equality conditions and supplementary derivations.
- [x] Add GitHub Actions LaTeX/PDF build and artifact upload.
- [x] Perform a claim-by-claim consistency audit against `STATUS.md` and `docs/claims_and_assumptions.md`.
- [x] Integrate figures, captions, and cross-references.
- [x] Re-run the claim audit after final figure/caption placement.
- [x] Complete final repository-level v0.2 release audit.
- [ ] Apply wording corrections that arise during public review.

## Phase 7 — Everett bridge review

- [x] Keep the Everett accessibility map as a separate bridge assumption rather than a theorem consequence.
- [x] Review the bridge against both supportive and critical Everett probability literature.
- [x] Specify structural support, constraint, and rejection criteria in `docs/everett_bridge_tests.md`.
- [x] Add layer-specific falsifiability wording to the manuscript Everett and Limitations sections.
- [x] Defer a concrete physical derivation or empirical model to post-v0.2 research unless review produces a credible candidate.

## Phase 8 — Public review and later preprint

- [x] Keep GitHub Issues open for proof corrections, counterexamples, prior art, and implementation bugs.
- [x] Integrate major repository corrections through PRs with CI gates.
- [x] Complete v0.2 manuscript-readiness and release audit.
- [x] Synchronize repository metadata to `v0.2-public-review` in the release-audit PR.
- [ ] Create a formal GitHub Release/tag for `v0.2-public-review` when a release-write interface is available.
- [ ] Collect public review and revise the repository/manuscript.
- [ ] Prepare `v1.0-preprint` only after the review interval and subsequent revisions stabilize the manuscript for arXiv submission.

## Post-v0.2 theorem development

- [x] Prove Supplementary Theorem S2: score-measurable predictive-calibration alignment.
- [x] Prove the exact projection identity:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(E[U\mid Y],s(Y)).
$$

- [x] Give monotone/comonotone sufficient conditions for nonnegative and strict covariance.
- [x] Prove posterior-mean self-calibration:

$$
Y=E[U\mid B]
\Longrightarrow
E[U\mid Y]=Y.
$$

- [x] Derive the approximate-calibration robustness bound:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)}.
$$

- [x] Record the counterexample showing that positive mutual information alone is insufficient.
- [x] Integrate S2 and its corollaries into a separate manuscript appendix while keeping the core five fixed.
- [ ] Derive learning-theoretic upper bounds on `Var(e(Y))` for finite adapted agents.
- [ ] Add a calibration diagnostic experiment only if review requires direct estimation of the S2.3 margin.
- [ ] Extend S2 beyond score-measurable accessibility by bounding or signing the residual conditional-covariance term.

## Current focus

The v0.2 public-review baseline remains fixed at merge commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`. Post-v0.2 work should remain separately reviewable.

Current theoretical priority:

1. review S2, posterior-mean self-calibration, and the approximate-error bound;
2. derive finite-model learning bounds for calibration error;
3. only then consider a new experiment if the bound requires a missing falsification test;
4. preserve the Everett bridge as a separate physical question.
