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
| S2 | Predictive-calibration alignment for score-measurable accessibility | PROVED (SUPPLEMENTARY; POST-v0.2 CANDIDATE) | `supplementary/adaptive_agent.md` |
| S2.2 | Posterior-mean self-calibration: `Y=E[U|B]` implies `E[U|Y]=Y` | PROVED | `supplementary/adaptive_agent.md` |
| S2.3 | Approximate-calibration covariance robustness bound | PROVED | `supplementary/adaptive_agent.md` |
| P1 | Costless recognition has nonnegative option value | PROVED | `theory/propositions_boundaries.md` |
| P2 | Pure reweighting cannot create support | PROVED | `theory/propositions_boundaries.md` |

The core five theorem set remains unchanged. The post-v0.2 development branch adds an isolated proof appendix for S2 and its corollaries so they can be reviewed separately from the v0.2 baseline.

## S2 adaptive-alignment result

Let:

$$
m(Y)=E[U\mid Y],
\qquad
S=s(Y).
$$

S2 proves:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),s(Y)).
$$

If `m` and `s` are comonotone, including the scalar case where both are nondecreasing in `Y`, then:

$$
\operatorname{Cov}(U,S)\ge0.
$$

Strict pairwise comonotonicity with positive probability gives strict positivity. Combined with T1, this yields nonnegative or strict first-person mean uplift under the weighted-measure model.

### Posterior-mean self-calibration

If an internal information state `B` generates:

$$
Y=E[U\mid B],
$$

then:

$$
E[U\mid Y]=Y.
$$

Thus a true posterior-mean score satisfies S2's conditional-mean calibration premise exactly.

### Approximate calibration

Let:

$$
e(Y)=E[U\mid Y]-Y.
$$

Under square integrability:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)}.
$$

Therefore:

$$
\operatorname{Cov}(Y,S)
>
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)}
$$

is sufficient for positive covariance. This converts the finite-agent question into a calibration-margin comparison that can be measured in future review-driven experiments.

The theorem also records an exact boundary: positive mutual information `I(U;Y)>0` alone is insufficient. General dependence can change conditional variance while leaving `E[U|Y]` constant, in which case every score-measurable accessibility map has zero covariance with `U`.

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

All five experiments are rerun by GitHub Actions. S2 does not add a sixth core experiment: E2 and E3 remain mechanism demonstrations, while a future calibration diagnostic should be added only if review requires direct estimation of the S2.3 bound.

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
| Ordered conditional-mean prediction plus ordered score-measurable accessibility implies nonnegative covariance | PROVED (S2) |
| A true posterior-mean score is conditionally mean-calibrated | PROVED (S2.2) |
| Finite learned models necessarily have small calibration error | NOT CLAIMED |
| Shared recognition/shared latent structure can increase cross-branch decision correlation | THEOREM UNDER EXPLICIT HIERARCHICAL ASSUMPTIONS + SIMULATION |
| External random generators become objectively lucky | NOT CLAIMED |

## Open problems after S2

1. Derive, constrain, or reject a concrete physical Everett accessibility map from observer/branch physics.
2. Derive learning-theoretic bounds on `Var(e(Y))` for finite adapted agents and compare them with the S2.3 alignment margin.
3. Extend S2 beyond score-measurable accessibility by controlling the residual conditional-covariance term in the law of total covariance.
4. Reconstruct a historical secondary experiment only if future review promotes it back into active evidence.
5. Continue literature search if review identifies a more specific novelty conflict.
6. Develop a recognition-time ordering theorem only if explicit pathwise/conditional advantage assumptions justify one.

## Release state

Repository baseline: **v0.2 — Public Review** at merge commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

The S2 work is post-v0.2 development and should be reviewed separately from the locked public-review baseline before any later preprint release.
