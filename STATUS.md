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
| S2 | Predictive-calibration alignment for score-measurable accessibility | PROVED (POST-v0.2 CANDIDATE) | `supplementary/adaptive_agent.md` |
| S2.2 | Posterior-mean self-calibration | PROVED | `supplementary/adaptive_agent.md` |
| S2.3 | Approximate-calibration covariance robustness | PROVED | `supplementary/adaptive_agent.md` |
| S2.4 | Prediction-MSE population certificate | PROVED (STACKED POST-v0.2 CANDIDATE) | `supplementary/adaptive_agent.md` |
| S2.5 | Bounded finite-sample held-out covariance certificate | PROVED (STACKED POST-v0.2 CANDIDATE) | `supplementary/finite_sample_certificate.md` |
| S2.6 | Conditional validity after arbitrary independent training | PROVED (STACKED POST-v0.2 CANDIDATE) | `supplementary/selection_validity.md` |
| S2.7 | Multiplicity-corrected finite candidate selection on one hold-out sample | PROVED (STACKED POST-v0.2 CANDIDATE) | `supplementary/selection_validity.md` |
| P1 | Costless recognition has nonnegative option value | PROVED | `theory/propositions_boundaries.md` |
| P2 | Pure reweighting cannot create support | PROVED | `theory/propositions_boundaries.md` |

The core five theorem set remains unchanged. The S2 theorem family is post-v0.2 development and is isolated in stacked review branches.

## S2 adaptive-alignment and certification chain

S2 proves:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(E[U\mid Y],s(Y))
$$

for score-measurable accessibility `S=s(Y)`. Comonotonic conditional-mean prediction and accessibility imply nonnegative covariance.

S2.2 proves exact posterior-mean self-calibration:

$$
Y=E[U\mid B]
\Longrightarrow
E[U\mid Y]=Y.
$$

S2.3 gives the calibration-error lower bound:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)}.
$$

S2.4 replaces the latent calibration variance with ordinary prediction MSE:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{E[(U-Y)^2]\operatorname{Var}(S)}.
$$

S2.5 turns the population inequality into a bounded finite-sample held-out certificate. Under known bounds and independent i.i.d. evaluation, it constructs `D_L` satisfying:

$$
P\left(
\operatorname{Cov}(U,S)\ge D_L
\right)
\ge1-\delta.
$$

Therefore:

$$
D_L>0
$$

certifies positive population covariance with confidence at least `1-delta`.

### S2.6 training-selection validity

Let `T` denote an arbitrary training random element. If the final certification sample is independent of `T`, then conditional on the realized trained rule S2.5 remains valid:

$$
P\!\left(
C(T)\ge D_L(T)
\mid T
\right)
\ge1-\delta.
$$

Hence arbitrary upstream training, hyperparameter search, or representation learning is compatible with the certificate provided the final certification sample remains independent and the post-training bounds are valid for fresh population draws.

### S2.7 finite candidate post-selection validity

If `K` candidate rules are fixed before the certification sample is inspected, apply S2.5 with per-candidate error budget:

$$
\delta_k=\frac{\delta}{K}.
$$

Then:

$$
P\!\left(
C_k\ge D_{L,k}
\text{ for every }k
\right)
\ge1-\delta.
$$

Consequently, any candidate index selected from the same held-out observations retains the corresponding valid lower bound. Equal allocation changes the Hoeffding radius to:

$$
\tau_{n,\delta,K}
=
\sqrt{\frac{\log(10K/\delta)}{2n}}.
$$

Uncorrected best-of-`K` reporting and post-hoc invention of new candidates are not covered.

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

All five experiments are rerun by GitHub Actions. S2–S2.7 do not create a sixth core experiment. A new held-out diagnostic should be added only if review requires empirical evaluation of the certificate stack.

## Figure and manuscript state

| Item | Status |
|---|---|
| Six GitHub-readable SVG figures | COMMITTED / REGENERATED IN CI |
| Six LaTeX PDF figure build products | GENERATED IN CI |
| Figure provenance and source-data mapping | DOCUMENTED |
| Figure placement, captions, and cross-references | INTEGRATED / AUDITED |
| Manuscript theorem appendix | FULL PROOFS INTEGRATED |
| Post-v0.2 S2/S2.7 appendices | SEPARATE STACKED REVIEW BRANCHES |
| LaTeX/PDF build | VALIDATED BY CI ON EACH REVIEW BRANCH WHEN GREEN |
| Expanded bibliography and critique-side prior art | INTEGRATED |
| Final v0.2 repository release audit | PASS |

## Interpretation-level claims

| Claim | Status |
|---|---|
| Observer-indexed accessibility can be represented by a nonnegative weight function | MODEL ASSUMPTION |
| Everett branches admit the QBS accessibility bridge used here | CONDITIONAL BRIDGE ASSUMPTION / PHYSICALLY OPEN |
| Ordered conditional-mean prediction plus ordered score-measurable accessibility implies nonnegative covariance | PROVED (S2) |
| A true posterior-mean score is conditionally mean-calibrated | PROVED (S2.2) |
| Population robustness via calibration error / MSE | PROVED SUFFICIENT CONDITIONS (S2.3/S2.4) |
| Bounded independent held-out data can certify positive covariance | PROVED SUFFICIENT HIGH-PROBABILITY CONDITION (S2.5) |
| Arbitrary independent training preserves S2.5 validity conditional on the trained rule | PROVED (S2.6) |
| Same-holdout selection among a finite predeclared candidate family is valid with multiplicity correction | PROVED (S2.7) |
| Finite learned models necessarily pass the certificate | NOT CLAIMED |
| A passed statistical certificate establishes the Everett bridge | NOT CLAIMED |
| External random generators become objectively lucky | NOT CLAIMED |

## Open problems after S2.7

1. Derive, constrain, or reject a concrete physical Everett accessibility map from observer/branch physics.
2. Extend S2.5 to unbounded/sub-Gaussian/sub-exponential or robust-mean settings.
3. Extend selection validity from finite predeclared candidate families to infinite or data-dependent classes using uniform-convergence, selective-inference, or fresh-sample methods.
4. Add a held-out diagnostic experiment only if review requires direct empirical evaluation of the S2.5–S2.7 certificate stack.
5. Extend S2 beyond score-measurable accessibility by controlling the residual conditional-covariance term.
6. Continue literature search if review identifies a more specific novelty conflict.
7. Develop a recognition-time ordering theorem only under explicit pathwise/conditional advantage assumptions.

## Release state

Repository baseline: **v0.2 — Public Review** at merge commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

PR #11 is the base S2 review branch. PR #12 adds S2.4. PR #13 adds S2.5. S2.6–S2.7 are developed as the next stacked selection-validity layer and remain separately reviewable before any later preprint merge.
