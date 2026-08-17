# QBS Research Status

**Snapshot date:** 2026-08-17

This file is the canonical status ledger for the Quantum Bogosort research repository. It distinguishes proved mathematics, simulation-supported mechanisms, interpretation-level assumptions, and open problems.

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
| Six publication-oriented SVG figures | COMMITTED / REGENERATED IN CI |
| Figure provenance and source-data mapping | DOCUMENTED |
| Manuscript theorem appendix | FULL PROOFS INTEGRATED |
| LaTeX/PDF build | VALIDATED BY CI |
| Expanded bibliography and critique-side prior art | INTEGRATED |
| Historical experiment archive ledger | DOCUMENTED |
| Bridge support / constraint / rejection criteria | DOCUMENTED |

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

## Open problems

1. Derive, constrain, or reject a concrete physical Everett accessibility map from observer/branch physics; the current bridge-test framework now states what such a proposal must satisfy.
2. Strengthen the adaptive-agent information-theoretic mechanism into a theorem with explicit sufficient conditions linking predictive information to positive accessibility covariance.
3. Reconstruct any historical secondary experiment that is promoted from archive status back into active manuscript evidence.
4. Continue targeted literature search for direct prior art combining endogenous policy change with self-locating or observer-indexed weighting.
5. Integrate the committed SVG figures into the final manuscript layout and finish caption/cross-reference review.
6. Develop a recognition-time ordering theorem only if explicit pathwise/conditional advantage assumptions justify one; otherwise keep it as a post-v0.2 extension.

## Release state

Current public state: **v0.1 — Public Technical Review**.

The repository is close to **v0.2 — manuscript-ready review package**. Remaining release gates are final manuscript layout/caption review, claim-by-claim consistency audit, targeted novelty search, and a decision on whether any archived experiment must be reconstructed before the v0.2 tag.
