# Changelog

## Post-v0.2 development — unreleased

### Added

- Supplementary Theorem S2 (Predictive-Calibration Alignment):
  $$
  \operatorname{Cov}(U,S)
  =
  \operatorname{Cov}(E[U\mid Y],s(Y))
  $$
  for score-measurable accessibility `S=s(Y)`;
- sufficient comonotonicity/monotonicity conditions for nonnegative and strict positive outcome-accessibility covariance;
- Corollary S2.2: posterior-mean self-calibration,
  $$
  Y=E[U\mid B]
  \Longrightarrow
  E[U\mid Y]=Y;
  $$
- Corollary S2.3: a Cauchy--Schwarz robustness bound for approximate conditional-mean calibration;
- a conditional-mean predictive-strength quantity based on `Var(E[U|Y])`;
- an explicit counterexample showing that positive mutual information alone does not imply positive accessibility covariance;
- a separate manuscript appendix file containing the S2 proofs and boundary conditions;
- `docs/s2_adaptive_alignment_audit.md` for theorem-level H/T/D/C/U + ERROR CHECK review.

### Changed

- the adaptive-agent mechanism is no longer described as a wholly simulation-supported covariance step: E2/E3 support the learning/prediction premise, while S2 proves the covariance consequence once calibration and score-measurable accessibility hold;
- a true posterior-mean score now supplies the S2 calibration premise exactly by the tower property;
- the remaining finite-agent problem is narrowed to bounding conditional-mean calibration error and comparing it with the S2.3 score/accessibility alignment margin;
- the core five theorem set remains unchanged.

## v0.2 — Public Review — 2026-08-17

### Added

- canonical `STATUS.md` research ledger;
- `ROADMAP.md` for repository and manuscript milestones;
- research map, notation reference, and claims/assumptions ledger;
- H/T/D/C/U experiment cards for E1–E5;
- topic-split supplementary notes;
- recognition-time stopping-time formalization with explicit v0.2 defer of a universal timing-order theorem;
- initial and extended prior-art ledgers;
- direct self-locating policy-optimization prior art in the novelty audit;
- manuscript scaffold with Related Work and bibliography;
- six committed publication-oriented SVG figures with deterministic regeneration script;
- PDF figure generator for LaTeX manuscript builds;
- complete manuscript appendix proofs for T1–T5 and supplementary derivations;
- Supplementary Theorem S1 for shared-latent branch-policy coherence;
- historical experiment archive index and supersession ledger;
- explicit Everett bridge support / constraint / rejection criteria;
- v0.2 manuscript claim consistency audit and post-layout re-audit;
- final `docs/v0.2_release_audit.md` repository audit;
- independent LaTeX/PDF manuscript build job in GitHub Actions.

### Changed

- narrowed novelty positioning so normalized weighting, anthropic decision-making, self-location-dependent action, and the elementary covariance identity are not treated as standalone novelty claims;
- expanded Related Work to include advocates and critics of Everettian probability, alternative many-world measure proposals, classical weighted-measure context, and direct self-locating policy-optimization work;
- integrated all six figures into the manuscript with captions that identify schematic, theorem-illustration, or classical-simulation status;
- updated CI so both SVG previews and manuscript PDF figures are regenerated from committed sources;
- clarified that earlier recognition is not universally better without explicit causal and information assumptions;
- clarified that structural bridge coherence, interpretive adequacy, and empirical falsifiability are distinct levels of evaluation;
- decided that no archived experiment is promoted as new active evidence for v0.2, so historical reconstruction is not a release blocker;
- synchronized README and citation metadata to the v0.2 public-review snapshot.

### Repository discipline

- GitHub is the source of truth for theorem status, experiment status, open assumptions, and manuscript progress.
- Markdown mathematics uses double-dollar display blocks only.
- Theorem, simulation, model assumption, Everett bridge assumption, and non-claim are tracked separately.
- CI reruns E1–E5, regenerates SVG/PDF figures, validates repository structure, and builds the illustrated manuscript PDF.

### Release interpretation

The repository snapshot is ready for public technical review. A formal GitHub Release/tag is a hosting-layer action separate from the scientific/reproducibility snapshot and is not required for the theorem, data, code, or manuscript state to be auditable.

## v0.1 — Public Technical Review

- core theorem set published;
- E1–E5 reproduction scripts and result summaries published;
- null and counterexample stress tests published;
- split licensing and citation metadata added;
- GitHub Actions validation added;
- Markdown math rendering corrected;
- E4/E5 reproducibility audit completed.
