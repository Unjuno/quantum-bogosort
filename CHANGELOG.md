# Changelog

## v0.3 — Public Review — 2026-08-18

### Added

- Supplementary Theorem S2 for score-measurable predictive-calibration alignment;
- Corollary S2.2 for posterior-mean self-calibration;
- Corollaries S2.3–S2.10 for calibration robustness, prediction-MSE bounds, finite-sample certification, selection validity, generic confidence envelopes, light-tail concentration, and robust median-of-means certification;
- Supplementary Theorem S2.11 extending predictive alignment beyond score-measurable accessibility via the exact law of total covariance;
- Supplementary Theorem S2.12 lower-bounding the residual term using conditional variances;
- Supplementary Theorem S2.13 rewriting the residual penalty in explained-variance / conditional-mean-correlation form;
- `docs/s2_stack_review_map.md` for dependency, manuscript-placement, and theorem-expansion stop rules;
- `docs/s2_stack_semantic_audit.md` for preservation of theorem and interpretation boundaries;
- `docs/post_v02_manuscript_compression_audit.md` for H/T/D/C/U review of the compressed manuscript structure;
- `docs/post_v02_core_s2_proof_review.md` for a dedicated proof-review pass over S2, S2.11, S2.12, and S2.13;
- `literature/post_v02_targeted_prior_art.md` for a narrow direct-overlap search after the general-accessibility development;
- repository-relative Markdown link validation in CI;
- current/stable/history routing for public review.

### Changed

- the main manuscript is compressed around the conceptual predictive-alignment → general-accessibility → residual-penalty → explained-variance spine rather than presenting all S2 statistical layers with equal prominence;
- detailed S2.3–S2.10 validation machinery is Appendix-first;
- S2 is explicitly identified as the zero-residual special case of S2.11 when accessibility is score-measurable;
- S2.11 now uses explicit square-integrability assumptions;
- S2.11 and S2.12 counterexample/sharpness constructions use bounded Rademacher residuals with strictly positive accessibility;
- S2.13 states the domain and feasibility of the symmetric threshold explicitly;
- observer-selection and Everett self-location prior art is expanded and novelty positioning remains conservative;
- future S2 theorem/statistical expansion is deferred by default unless review identifies a specific need;
- public repository navigation now treats `docs/research_map.md` as the canonical claim-to-source index;
- README, STATUS, DEVELOPMENT_STATUS, ROADMAP, CONTRIBUTING, manuscript routing, and citation metadata are synchronized to the v0.3 public-review snapshot;
- informal `effective/indexical luck` language is explicitly secondary to the formal first-person uplift / trajectory-reweighting terminology.

### Unchanged core

- T1–T5 remain the locked core theorem set;
- E1–E5 remain the locked core experiment suite;
- no sixth core experiment is introduced;
- no S2.14 is introduced;
- the Everett accessibility bridge remains physically open;
- external random generators becoming objectively lucky is not claimed.

## v0.2 — Public Review — 2026-08-17

### Added

- canonical `STATUS.md` research ledger;
- `ROADMAP.md` for repository and manuscript milestones;
- research map, notation reference, and claims/assumptions ledger;
- H/T/D/C/U experiment cards for E1–E5;
- topic-split supplementary notes;
- recognition-time stopping-time formalization with explicit v0.2 defer of a universal timing-order theorem;
- initial and extended prior-art ledgers;
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
- clarified that earlier recognition is not universally better without explicit causal and information assumptions;
- clarified that structural bridge coherence, interpretive adequacy, and empirical falsifiability are distinct levels of evaluation.

## v0.1 — Public Technical Review

- core theorem set published;
- E1–E5 reproduction scripts and result summaries published;
- null and counterexample stress tests published;
- split licensing and citation metadata added;
- GitHub Actions validation added;
- Markdown math rendering corrected;
- E4/E5 reproducibility audit completed.
