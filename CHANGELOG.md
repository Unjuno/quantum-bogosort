# Changelog

## Post-v0.2 development — unreleased

### Added

- Supplementary Theorem S2 for score-measurable predictive-calibration alignment;
- Corollary S2.2 for posterior-mean self-calibration;
- Corollary S2.3 for approximate-calibration covariance robustness;
- Corollary S2.4 for a conservative population certificate based on ordinary prediction MSE;
- Corollary S2.5 for a bounded independent-held-out high-probability covariance certificate;
- Corollary S2.6 proving that arbitrary upstream training preserves S2.5 validity when the final certification sample remains independent;
- Corollary S2.7 proving multiplicity-corrected same-holdout selection validity for a finite predeclared candidate family;
- Corollary S2.8 composing any valid simultaneous five-moment confidence envelope into a covariance lower certificate;
- Corollary S2.9 instantiating S2.8 for unbounded light-tail data using sub-Gaussian first-moment and Bernstein/sub-exponential product/square controls;
- Corollary S2.10 instantiating S2.8 with median-of-means under finite variance bounds for the five target variables;
- Supplementary Theorem S2.11 extending predictive alignment beyond `S=s(Y)` via the exact law of total covariance;
- S2.11 residual-tolerance bound
  $$
  \operatorname{Cov}(U,S)
  \ge
  \operatorname{Cov}(E[U\mid Y],E[S\mid Y])
  -\varepsilon
  $$
  whenever the average conditional residual covariance is at least `-epsilon`;
- an explicit S2.11 counterexample showing negative residual dependence can overturn score-level alignment;
- unequal confidence allocation for finite candidate families;
- bounded, generic-envelope, light-tail, and median-of-means covariance lower margins;
- quantitative first-person lower bounds using a simultaneous upper bound on `E[S]` when a certificate margin is positive;
- theorem audits for S2 through S2.11;
- explicit mutual-information, certificate-failure, multiple-selection, tail-parameter, target-moment, and residual-dependence boundaries.

### Changed

- the adaptive-agent mechanism now separates score-level predictive alignment from residual branch-level outcome/accessibility dependence;
- S2 is explicitly identified as the zero-residual special case of S2.11 when `S` is `Y`-measurable;
- the statistical certification layer is separated from the QBS covariance-composition layer through S2.8;
- S2.9 permits unbounded light-tail variables only when all required moment-concentration controls are valid;
- S2.10 permits robust median-of-means certification only when the five S2.8 target variables have valid finite variance bounds;
- S2.10 records the fourth-moment-type implications needed for squared targets;
- S2.11 explicitly prevents an overclaim that comonotone conditional means alone are enough once additional accessibility randomness is allowed;
- uncorrected model search, post-hoc candidate invention, invalid tail/variance inputs, and ignored negative residual dependence are outside the stated guarantees;
- no sixth core experiment is introduced by the S2 theorem stack;
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
