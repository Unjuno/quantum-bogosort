# QBS Research Status — Stable v0.2 Snapshot

**Snapshot date:** 2026-08-17

This file records the frozen v0.2 public-review scientific state. It is not the current post-v0.2 development ledger.

For current work, see `DEVELOPMENT_STATUS.md` and the active cumulative review PR #21.

The exact v0.2 snapshot is preserved at:

- branch: `release/v0.2-public-review`
- commit: `7405f7408f74fa32b16d1cc9f624070cc14624ab`

## Core mathematical results

| ID | Result | Status | Primary source |
|---|---|---|---|
| T1 | QBS Covariance Identity | PROVED | `theory/theorem_1_3.md` |
| T2 | Tail Probability Identity | PROVED | `theory/theorem_1_3.md` |
| T3 | Monotone Accessibility implies FOSD | PROVED | `theory/theorem_1_3.md` |
| T4 | Recognition Decomposition | PROVED | `theory/theorem_4_5.md` |
| T5 | Policy–QBS Interaction Decomposition | PROVED | `theory/theorem_4_5.md` |
| C5.1 | Adaptive Rescue gives nonpositive interaction under opposite monotonicity | PROVED | `theory/theorem_4_5.md` |
| S1 | Shared-latent branch-policy coherence under conditional independence | PROVED (SUPPLEMENTARY) | `supplementary/branch_recognition.md` |
| P1 | Costless recognition has nonnegative option value | PROVED | `theory/propositions_boundaries.md` |
| P2 | Pure reweighting cannot create support | PROVED | `theory/propositions_boundaries.md` |

The manuscript appendix contains complete proofs of T1–T5, strict/equality conditions for FOSD, adaptive rescue, support preservation, the repeated-filter derivative identity, the Gaussian closed form, and multi-observer normalization.

## Sequential extension

| Item | Status | Source |
|---|---|---|
| Recognition time as a stopping time | FORMALIZED | `supplementary/recognition_time.md` |
| FP value functional for a stopping rule | EXACT BY DEFINITION | `supplementary/recognition_time.md` |
| Universal early-vs-late recognition ordering | NOT CLAIMED / DEFERRED | `supplementary/recognition_time.md` |

## Core computational results

| ID | Experiment | Status |
|---|---|---|
| E1 | FOSD, independence null, nonmonotone counterexample | REPRODUCIBLE |
| E2 | Minimal learned agent / endogenous predictive correlation | REPRODUCIBLE |
| E3 | Paired recognition decomposition | REPRODUCIBLE |
| E4 | Fixed and changing-selector interaction decomposition | REPRODUCIBLE |
| E5 | Paired branch-map sweeps and shared-recognition comparison | REPRODUCIBLE |

All five experiments are rerun by GitHub Actions.

## Figure and manuscript state

| Item | Status |
|---|---|
| Six GitHub-readable SVG figures | COMMITTED / REGENERATED IN CI |
| Six LaTeX PDF figure build products | GENERATED IN CI |
| Figure provenance and source-data mapping | DOCUMENTED |
| Figure placement, captions, and cross-references | INTEGRATED / AUDITED |
| Manuscript theorem appendix | FULL PROOFS INTEGRATED |
| LaTeX/PDF build | VALIDATED BY CI |
| Expanded bibliography and critique-side prior art | INTEGRATED |
| Direct anthropic-policy prior-art overlap | REVIEWED / INTEGRATED |
| Historical experiment archive ledger | DOCUMENTED |
| Archived experiment promotion before v0.2 | NOT REQUIRED; NONE USED AS NEW ACTIVE EVIDENCE |
| Bridge support / constraint / rejection criteria | DOCUMENTED |
| Post-layout claim consistency audit | PASS |
| Final v0.2 repository release audit | PASS |

## Interpretation-level claims

| Claim | Status |
|---|---|
| Observer-indexed accessibility can be represented by a nonnegative weight function | MODEL ASSUMPTION |
| Everett branches admit the QBS accessibility bridge used here | CONDITIONAL BRIDGE ASSUMPTION / PHYSICALLY OPEN |
| Structural tests for a candidate physical bridge | SPECIFIED |
| Independent empirical falsifiability without a concrete physical `S_pi` | NOT CLAIMED |
| Adapted agents can generate outcome-aligned accessibility signals endogenously | SIMULATION-SUPPORTED MECHANISM |
| Shared recognition/shared latent structure can increase cross-branch decision correlation | THEOREM UNDER EXPLICIT HIERARCHICAL ASSUMPTIONS + SIMULATION |
| External random generators become objectively lucky | NOT CLAIMED |

## Open problems as of the v0.2 snapshot

These items record the state of the project at the frozen v0.2 snapshot. Some have since been addressed in post-v0.2 development; see `DEVELOPMENT_STATUS.md` and PR #21.

1. Derive, constrain, or reject a concrete physical Everett accessibility map from observer/branch physics.
2. Strengthen the adaptive-agent information-theoretic mechanism into a theorem with explicit sufficient conditions linking predictive information to positive accessibility covariance.
3. Reconstruct a historical secondary experiment only if future review promotes it back into active evidence.
4. Continue literature search if review identifies a more specific novelty conflict.
5. Develop a recognition-time ordering theorem only if explicit pathwise/conditional advantage assumptions justify one.

## Release state

Scientific snapshot: **v0.2 — Public Review**.

The substantive v0.2 manuscript-readiness gates and final repository audit passed before the snapshot was fixed at commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

A formal GitHub Release/tag remains a hosting-layer action separate from the scientific snapshot. Until a tag can be created through the available tooling, branch `release/v0.2-public-review` is the stable repository reference.
