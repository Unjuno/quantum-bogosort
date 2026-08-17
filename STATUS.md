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

The manuscript appendix now contains complete proofs of T1--T5, strict/equality conditions for FOSD, the adaptive-rescue result, support preservation, the repeated-filter derivative identity, the Gaussian closed form, and multi-observer normalization.

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
| LaTeX/PDF build | VALIDATED BY CI WHEN THIS BRANCH MERGES |
| Expanded bibliography and critique-side prior art | INTEGRATED |

## Interpretation-level claims

| Claim | Status |
|---|---|
| Observer-indexed accessibility can be represented by a nonnegative weight function | MODEL ASSUMPTION |
| Everett branches admit the QBS accessibility bridge used here | BRIDGE ASSUMPTION / OPEN |
| Adapted agents can generate outcome-aligned accessibility signals endogenously | SIMULATION-SUPPORTED MECHANISM |
| Shared recognition/shared latent structure can increase cross-branch decision correlation | THEOREM UNDER EXPLICIT HIERARCHICAL ASSUMPTIONS + SIMULATION |
| External random generators become objectively lucky | NOT CLAIMED |

## Open problems

1. Give a physically motivated Everett derivation or rejection criterion for the accessibility bridge.
2. Formalize recognition time as a stopping time and separate early-recognition causal effects from observer weighting, or explicitly defer this extension from v0.2.
3. Strengthen the adaptive-agent information-theoretic mechanism into a theorem with explicit sufficient conditions linking predictive information to positive accessibility covariance.
4. Archive/document the remaining historical secondary experiments that are currently represented only by old CSVs or consolidated notes.
5. Continue literature search for direct prior art combining endogenous policy change with self-locating or observer-indexed weighting.
6. Integrate the committed SVG figures into the final manuscript layout or produce publication-format PDF equivalents after caption review.

## Release state

Current public state: **v0.1 — Public Technical Review**.

The next intended milestone is **v0.2 — manuscript-ready review package** after the remaining archive, stopping-time/defer decision, bridge review, and manuscript-layout tasks are complete.
