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
- Supplementary Theorem S2.12 lower-bounding the S2.11 residual term using conditional variances;
- Supplementary Theorem S2.13 rewriting the S2.12 residual penalty in explained-variance / correlation-ratio form;
- S2.13 sufficient condition
  $$
  \rho_{ma}\sqrt{A_UA_S}
  >
  \sqrt{(1-A_U)(1-A_S)};
  $$
- the perfect conditional-mean alignment simplification
  $$
  A_U+A_S>1;
  $$
- the symmetric explained-variance threshold in its valid positive-alignment regime
  $$
  A>
  \frac{1}{1+\rho_{ma}};
  $$
- `docs/s2_stack_review_map.md` for dependency, manuscript-placement, and theorem-expansion stop rules;
- `docs/s2_stack_semantic_audit.md` for preservation of theorem and interpretation boundaries;
- `docs/post_v02_manuscript_compression_audit.md` for H/T/D/C/U review of the compressed manuscript structure;
- `docs/post_v02_core_s2_proof_review.md` for a dedicated proof-review pass over S2, S2.11, S2.12, and S2.13;
- `literature/post_v02_targeted_prior_art.md` for a narrow direct-overlap search after the general-accessibility development;
- Garisto, Lewis, and Khawaja in the Related Work / Everett-bridge boundary literature;
- bounded, generic-envelope, light-tail, median-of-means, residual, and explained-variance covariance lower certificates.

### Changed

- the main manuscript is compressed around the conceptual S2 → S2.11 → S2.13 spine rather than presenting all S2 statistical layers with equal prominence;
- detailed S2.3–S2.10 validation machinery is Appendix-first; the standalone robust-MoM summary is no longer part of the main-text sequence;
- Abstract, Introduction, Limitations, Discussion, Related Work, and the manuscript README are synchronized to the general-accessibility / residual-dependence framing;
- S2 is explicitly identified as the zero-residual special case of S2.11 when `S` is `Y`-measurable;
- S2.11 now uses explicit square-integrability assumptions so every covariance and residual term is unambiguously finite;
- the S2.11 negative-residual counterexample now uses bounded Rademacher residuals and strictly positive accessibility;
- the S2.12 sharpness construction now uses bounded Rademacher residuals, proving equality in the worst-case conditional Cauchy--Schwarz bound while preserving positive accessibility;
- the S2.13 symmetric divided threshold now states that division requires `rho_ma>-1` and that a feasible strict certificate under `0<A<=1` requires `rho_ma>0`;
- S2.12 replaces an abstract residual `epsilon` by a conservative variance-based penalty;
- S2.13 expresses that penalty through explained fractions `A_U`, `A_S` and conditional-mean correlation `rho_ma`;
- S2.13 explicitly remains a sufficient worst-case certificate rather than a necessary condition;
- observer-selection and Everett self-location prior art is expanded to make the physical bridge and novelty boundary more conservative;
- future S2 theorem/statistical expansion is deferred by default unless review identifies a specific need;
- uncorrected model search, post-hoc candidate invention, invalid tail/variance inputs, and ignored residual dependence remain outside the stated guarantees;
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

## v0.1 — Public Technical Review

- core theorem set published;
- E1–E5 reproduction scripts and result summaries published;
- null and counterexample stress tests published;
- split licensing and citation metadata added;
- GitHub Actions validation added;
- Markdown math rendering corrected;
- E4/E5 reproducibility audit completed.
