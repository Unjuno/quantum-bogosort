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
| P1 | Costless recognition has nonnegative option value | PROVED | `theory/propositions_boundaries.md` |
| P2 | Pure reweighting cannot create support | PROVED | `theory/propositions_boundaries.md` |

## Core computational results

| ID | Experiment | Status |
|---|---|---|
| E1 | FOSD, independence null, nonmonotone counterexample | REPRODUCIBLE |
| E2 | Minimal learned agent / endogenous predictive correlation | REPRODUCIBLE |
| E3 | Paired recognition decomposition | REPRODUCIBLE |
| E4 | Fixed and changing-selector interaction decomposition | REPRODUCIBLE |
| E5 | Paired branch-map sweeps and shared-recognition comparison | REPRODUCIBLE |

All five experiments are run by GitHub Actions.

## Interpretation-level claims

| Claim | Status |
|---|---|
| Observer-indexed accessibility can be represented by a nonnegative weight function | MODEL ASSUMPTION |
| Everett branches admit the QBS accessibility bridge used here | BRIDGE ASSUMPTION / OPEN |
| Adapted agents can generate outcome-aligned accessibility signals endogenously | SIMULATION-SUPPORTED MECHANISM |
| Shared recognition can increase cross-branch decision correlation | SIMULATION-SUPPORTED MECHANISM |
| External random generators become objectively lucky | NOT CLAIMED |

## Open problems

1. Give a physically motivated Everett derivation or rejection criterion for the accessibility bridge.
2. Formalize recognition time as a stopping time and separate early-recognition causal effects from observer weighting.
3. Derive a recognition-induced policy-coherence theorem under explicit hierarchical branch assumptions.
4. Connect adaptive-agent predictive information to sufficient conditions for positive accessibility covariance.
5. Complete prior-art positioning and manuscript references.
6. Produce publication-quality figures from the locked experiments.
7. Convert the current theorem notes into a full manuscript with explicit assumptions and falsifiability sections.

## Release state

Current public state: **v0.1 — Public Technical Review**.

The next intended milestone is **v0.2 — manuscript-ready review package** after the research map, literature ledger, experiment cards, figures, and manuscript scaffold are complete.
