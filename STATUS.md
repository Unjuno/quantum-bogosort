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
| P1 | Costless recognition has nonnegative option value | PROVED | `theory/propositions_boundaries.md` |
| P2 | Pure reweighting cannot create support | PROVED | `theory/propositions_boundaries.md` |

The core five theorem set remains unchanged. The S2 theorem family is post-v0.2 development and is isolated in stacked review branches.

## S2 adaptive-alignment chain

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

The MSE decomposition:

$$
E[(U-Y)^2]
=
E[\operatorname{Var}(U\mid Y)]
+
E[e(Y)^2]
$$

shows why S2.4 is conservative.

### S2.5 finite-sample certificate

Assume a fixed predictor/accessibility rule is evaluated on independent i.i.d. held-out observations with known bounds:

$$
|Y|\le B_Y,
\qquad
0\le S\le B_S,
\qquad
|U-Y|\le B_R.
$$

S2.5 uses simultaneous Hoeffding bounds for empirical `Y`, `S`, `YS`, `S^2`, and squared residuals to construct:

$$
D_L=C_L-\sqrt{M_UV_U}
$$

such that:

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

certifies positive population covariance with confidence at least `1-delta`. Under T1:

$$
E_{FP}[U]-E[U]
\ge
\frac{D_L}{B_S}>0.
$$

The guarantee requires independent held-out evaluation or an equivalent conditional-on-training formulation. Training/tuning leakage or post-hoc choice of the population bounds invalidates the simple stated coverage.

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

All five experiments are rerun by GitHub Actions. S2–S2.5 do not create a sixth core experiment. A new held-out diagnostic should be added only if review requires empirical evaluation of the certificate.

## Figure and manuscript state

| Item | Status |
|---|---|
| Six GitHub-readable SVG figures | COMMITTED / REGENERATED IN CI |
| Six LaTeX PDF figure build products | GENERATED IN CI |
| Figure provenance and source-data mapping | DOCUMENTED |
| Figure placement, captions, and cross-references | INTEGRATED / AUDITED |
| Manuscript theorem appendix | FULL PROOFS INTEGRATED |
| Post-v0.2 S2/S2.5 appendices | SEPARATE REVIEW BRANCHES |
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
| Finite learned models necessarily pass the certificate | NOT CLAIMED |
| A passed statistical certificate establishes the Everett bridge | NOT CLAIMED |
| External random generators become objectively lucky | NOT CLAIMED |

## Open problems after S2.5

1. Derive, constrain, or reject a concrete physical Everett accessibility map from observer/branch physics.
2. Extend S2.5 to unbounded/sub-Gaussian/sub-exponential or robust-mean settings.
3. Handle adaptive model/accessibility selection without requiring a completely independent fixed-model hold-out.
4. Add a held-out diagnostic experiment only if review requires direct empirical evaluation of S2.5.
5. Extend S2 beyond score-measurable accessibility by controlling the residual conditional-covariance term.
6. Continue literature search if review identifies a more specific novelty conflict.
7. Develop a recognition-time ordering theorem only under explicit pathwise/conditional advantage assumptions.

## Release state

Repository baseline: **v0.2 — Public Review** at merge commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

PR #11 is the base S2 review branch. PR #12 adds S2.4 on top of PR #11. S2.5 is developed as the next stacked layer and should remain separately reviewable before any later preprint merge.
