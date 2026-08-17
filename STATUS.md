# QBS Research Status

**Snapshot date:** 2026-08-18

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
| S2.8 | Generic simultaneous-confidence-envelope covariance certificate | PROVED (STACKED POST-v0.2 CANDIDATE) | `supplementary/confidence_envelope_certificate.md` |
| S2.9 | Light-tail sub-Gaussian/Bernstein instantiation of S2.8 | PROVED (STACKED POST-v0.2 CANDIDATE) | `supplementary/light_tail_certificate.md` |
| S2.10 | Robust median-of-means instantiation of S2.8 | PROVED (STACKED POST-v0.2 CANDIDATE) | `supplementary/robust_mom_certificate.md` |
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

S2.5 converts this population inequality into a bounded finite-sample held-out lower certificate `D_L` satisfying:

$$
P\left(
\operatorname{Cov}(U,S)\ge D_L
\right)
\ge1-\delta.
$$

S2.6 shows that arbitrary upstream training can be conditioned on when the final certification sample is independent.

S2.7 shows that same-holdout selection among a finite predeclared candidate family remains valid when candidate certificates are made simultaneous with multiplicity correction.

### S2.8 generic confidence-envelope composition

S2.8 removes Hoeffding from the QBS-specific composition layer. Suppose a statistical procedure supplies a simultaneous event controlling:

$$
E[Y],
\quad
E[S],
\quad
E[YS],
\quad
E[S^2],
\quad
E[(U-Y)^2].
$$

Let the simultaneous bounds be:

$$
L_Y\le E[Y]\le U_Y,
\qquad
L_S\le E[S]\le U_S,
$$

$$
E[YS]\ge L_{YS},
\qquad
E[S^2]\le U_{S^2},
\qquad
E[(U-Y)^2]\le U_M.
$$

With:

$$
L_S^+=\max\{0,L_S\},
$$

$$
P_U
=
\max\{L_YL_S^+,L_YU_S,U_YL_S^+,U_YU_S\},
$$

$$
C_L=L_{YS}-P_U,
$$

and:

$$
V_U
=
\max\{0,U_{S^2}-(L_S^+)^2\},
$$

S2.8 defines:

$$
D_{\mathrm{env}}
=
C_L-\sqrt{U_MV_U}
$$

and proves:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_{\mathrm{env}}
\right)
\ge1-\delta.
$$

### S2.9 light-tail instantiation

S2.9 instantiates S2.8 without deterministic boundedness. It assumes two-sided sub-Gaussian sample-mean control for `Y` and `S`, and explicit Bernstein/sub-exponential sample-mean control for:

$$
YS,
\qquad
S^2,
\qquad
(U-Y)^2.
$$

With:

$$
t_\delta=\log\frac{10}{\delta},
$$

the five concentration radii form an S2.8 simultaneous envelope with coverage at least:

$$
1-\delta.
$$

The resulting certificate:

$$
D_{\mathrm{LT}}
$$

satisfies:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_{\mathrm{LT}}
\right)
\ge1-\delta.
$$

The theorem deliberately treats the product/square Bernstein parameters as explicit inputs. It does not silently infer universal constants from marginal sub-Gaussianity.

### S2.10 robust median-of-means instantiation

Define the five S2.8 target variables:

$$
Z_1=Y,
\qquad
Z_2=S,
\qquad
Z_3=YS,
\qquad
Z_4=S^2,
\qquad
Z_5=(U-Y)^2.
$$

S2.10 assumes:

$$
\operatorname{Var}(Z_j)\le v_j<\infty,
\qquad
j=1,\ldots,5.
$$

Choose an odd number of blocks `b` with:

$$
b\ge8\log\frac{5}{\delta}
$$

and block size:

$$
m=\left\lfloor\frac{n}{b}\right\rfloor.
$$

For each target, the median-of-means estimator has radius:

$$
r_j
=
2\sqrt{\frac{v_j}{m}}
$$

with failure probability at most:

$$
\frac{\delta}{5}.
$$

A union bound supplies an S2.8 simultaneous envelope, producing a robust certificate:

$$
D_{\mathrm{MoM}}
$$

such that:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_{\mathrm{MoM}}
\right)
\ge1-\delta.
$$

This robust route does not require exponential tails, but it does require finite variance of the five target variables themselves. In particular, estimating the means of `S^2` and `(U-Y)^2` this way requires fourth-moment-type conditions.

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

All five experiments are rerun by GitHub Actions. S2–S2.10 do not create a sixth core experiment.

## Figure and manuscript state

| Item | Status |
|---|---|
| Six GitHub-readable SVG figures | COMMITTED / REGENERATED IN CI |
| Six LaTeX PDF figure build products | GENERATED IN CI |
| Figure placement and captions | INTEGRATED / AUDITED |
| Manuscript theorem appendix | FULL PROOFS INTEGRATED |
| Post-v0.2 S2/S2.10 appendices | SEPARATE STACKED REVIEW BRANCHES |
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
| Arbitrary independent training preserves held-out validity conditional on the trained rule | PROVED (S2.6) |
| Same-holdout selection among a finite predeclared family is valid with multiplicity correction | PROVED (S2.7) |
| Any valid simultaneous moment envelope can be composed into a covariance certificate | PROVED (S2.8) |
| Explicit light-tail concentration controls can instantiate the envelope without deterministic boundedness | PROVED (S2.9) |
| Median-of-means can instantiate the envelope under finite variances of the five target variables | PROVED (S2.10) |
| Raw-variable finite variance alone is enough for S2.10 | NOT CLAIMED |
| A passed statistical certificate establishes the Everett bridge | NOT CLAIMED |
| External random generators become objectively lucky | NOT CLAIMED |

## Open problems after S2.10

1. Derive, constrain, or reject a concrete physical Everett accessibility map from observer/branch physics.
2. Derive convenient sufficient conditions that imply the S2.9 product/square Bernstein parameters from a chosen Orlicz-norm or mgf convention, with constants stated explicitly.
3. Explore robust estimators that weaken the S2.10 fourth-moment-type requirements for `S^2` and `(U-Y)^2`.
4. Extend selection validity from finite predeclared candidate families to infinite or data-dependent classes using uniform-convergence, selective-inference, or fresh-sample methods.
5. Add a held-out diagnostic experiment only if review requires empirical evaluation of the S2.5–S2.10 stack.
6. Extend S2 beyond score-measurable accessibility by controlling the residual conditional-covariance term.
7. Continue literature search if review identifies a more specific novelty conflict.
8. Develop a recognition-time ordering theorem only under explicit pathwise/conditional advantage assumptions.

## Release state

Repository baseline: **v0.2 — Public Review** at merge commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

PR #11 is the base S2 review branch, PR #12 adds S2.4, PR #13 adds S2.5, PR #15 adds S2.6–S2.7, PR #16 adds S2.8, PR #17 adds S2.9, and S2.10 is developed as the next stacked robust finite-moment layer. All remain separately reviewable before any later preprint merge.
