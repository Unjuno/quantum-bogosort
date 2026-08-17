# Changelog

## Unreleased — toward v0.2 public review

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
- independent LaTeX/PDF manuscript build job in GitHub Actions.

### Changed

- narrowed novelty positioning so normalized weighting, anthropic decision-making, self-location-dependent action, and the elementary covariance identity are not treated as standalone novelty claims;
- expanded Related Work to include advocates and critics of Everettian probability, alternative many-world measure proposals, classical weighted-measure context, and direct self-locating policy-optimization work;
- integrated all six figures into the manuscript with captions that identify schematic, theorem-illustration, or classical-simulation status;
- updated CI so both SVG previews and manuscript PDF figures are regenerated from committed sources;
- refreshed `ROADMAP.md` to mark completed research-map, supplementary, experiment-card, figure, proof, archive, CI, bridge-review, novelty-search, and claim-audit milestones;
- clarified that earlier recognition is not universally better without explicit causal and information assumptions;
- clarified that structural bridge coherence, interpretive adequacy, and empirical falsifiability are distinct levels of evaluation;
- decided that no archived experiment is promoted as new active evidence for v0.2, so historical reconstruction is not a release blocker.

### Repository discipline

- GitHub remains the source of truth for theorem status, experiment status, open assumptions, and manuscript progress.
- Markdown mathematics continues to use double-dollar display blocks only.
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
