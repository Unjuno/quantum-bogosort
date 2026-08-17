# QBS Research Status

**Snapshot date:** 2026-08-18

This is the canonical status ledger for the Quantum Bogosort repository. It separates proved mathematics, statistical validation results, simulation evidence, and the physically open Everett bridge.

## Release baseline

The public-review baseline remains:

`v0.2 — Public Review`

at merge commit:

`7405f7408f74fa32b16d1cc9f624070cc14624ab`

Post-v0.2 theorem work is intentionally kept in stacked review PRs rather than merged directly into `main`.

## Mathematical results

| ID | Result | Status | Primary source |
|---|---|---|---|
| T1 | QBS Covariance Identity | PROVED | `theory/theorem_1_3.md` |
| T2 | Tail Probability Identity | PROVED | `theory/theorem_1_3.md` |
| T3 | Monotone Accessibility implies FOSD | PROVED | `theory/theorem_1_3.md` |
| T4 | Recognition Decomposition | PROVED | `theory/theorem_4_5.md` |
| T5 | Policy–QBS Interaction Decomposition | PROVED | `theory/theorem_4_5.md` |
| C5.1 | Adaptive rescue gives nonpositive interaction under opposite monotonicity | PROVED | `theory/theorem_4_5.md` |
| S1 | Shared-latent branch-policy coherence | PROVED (SUPPLEMENTARY) | `supplementary/branch_recognition.md` |
| S2 | Predictive-calibration alignment for score-measurable accessibility | PROVED (POST-v0.2 CANDIDATE) | `supplementary/adaptive_agent.md` |
| S2.2 | Posterior-mean self-calibration | PROVED | `supplementary/adaptive_agent.md` |
| S2.3 | Approximate-calibration covariance robustness | PROVED | `supplementary/adaptive_agent.md` |
| S2.4 | Prediction-MSE population certificate | PROVED | `supplementary/adaptive_agent.md` |
| S2.5 | Bounded finite-sample held-out covariance certificate | PROVED | `supplementary/finite_sample_certificate.md` |
| S2.6 | Validity after arbitrary independent training | PROVED | `supplementary/selection_validity.md` |
| S2.7 | Multiplicity-corrected finite candidate selection | PROVED | `supplementary/selection_validity.md` |
| S2.8 | Generic simultaneous-confidence-envelope composition | PROVED | `supplementary/confidence_envelope_certificate.md` |
| S2.9 | Light-tail sub-Gaussian/Bernstein instantiation | PROVED | `supplementary/light_tail_certificate.md` |
| S2.10 | Robust median-of-means instantiation | PROVED | `supplementary/robust_mom_certificate.md` |
| S2.11 | Residual conditional-covariance extension beyond `S=s(Y)` | PROVED | `supplementary/residual_covariance_extension.md` |
| P1 | Costless recognition has nonnegative option value | PROVED | `theory/propositions_boundaries.md` |
| P2 | Pure reweighting cannot create support | PROVED | `theory/propositions_boundaries.md` |

The locked core theorem set remains T1–T5. S1 and S2.* are supplementary developments.

## S2 alignment chain

For score-measurable accessibility:

$$
S=s(Y),
$$

S2 gives:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(E[U\mid Y],s(Y)).
$$

For a posterior-mean score:

$$
Y=E[U\mid B],
$$

S2.2 gives:

$$
E[U\mid Y]=Y.
$$

Approximate calibration gives S2.3:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)},
$$

where:

$$
e(Y)=E[U\mid Y]-Y.
$$

S2.4 replaces the latent calibration variance with ordinary prediction MSE:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{E[(U-Y)^2]\operatorname{Var}(S)}.
$$

## Statistical certification layers

S2.5 provides a bounded independent-held-out certificate:

$$
P\left(
\operatorname{Cov}(U,S)\ge D_L
\right)
\ge1-\delta.
$$

S2.6 shows that arbitrary upstream training may be conditioned on when the final certification sample is independent. S2.7 extends validity to same-holdout selection among a finite predeclared candidate family after multiplicity correction.

S2.8 makes the QBS composition concentration-method agnostic. It consumes simultaneous confidence bounds for:

$$
E[Y],
\quad
E[S],
\quad
E[YS],
\quad
E[S^2],
\quad
E[(U-Y)^2]
$$

and composes them into:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_{\mathrm{env}}
\right)
\ge1-\delta.
$$

S2.9 instantiates this interface for unbounded light tails using explicit sub-Gaussian/Bernstein mean controls. S2.10 instantiates it using median-of-means with finite variance bounds on the five S2.8 target variables.

The S2.10 assumption is stronger than raw-variable finite variance. In particular:

$$
\operatorname{Var}(S^2)<\infty
$$

requires a finite fourth moment of `S`, while:

$$
\operatorname{Var}((U-Y)^2)<\infty
$$

requires a finite fourth moment of the prediction residual.

## S2.11 residual conditional-covariance extension

S2.11 removes the deterministic score-measurability assumption. Define:

$$
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
$$

The exact law of total covariance gives:

$$
\boxed{
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),a(Y))
+
E[\operatorname{Cov}(U,S\mid Y)]
}.
$$

If the conditional means are comonotone and:

$$
E[\operatorname{Cov}(U,S\mid Y)]
\ge-\varepsilon,
$$

then:

$$
\boxed{
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))-\varepsilon
}.
$$

Hence:

$$
\operatorname{Cov}(m(Y),a(Y))>\varepsilon
$$

is sufficient for positive total covariance.

S2 is recovered as the special case in which:

$$
S=s(Y),
$$

so the residual conditional covariance is zero almost surely.

## Core computational results

| ID | Experiment | Status |
|---|---|---|
| E1 | FOSD, independence null, nonmonotone counterexample | REPRODUCIBLE |
| E2 | Minimal learned agent / endogenous predictive correlation | REPRODUCIBLE |
| E3 | Paired recognition decomposition | REPRODUCIBLE |
| E4 | Fixed and changing-selector interaction decomposition | REPRODUCIBLE |
| E5 | Paired branch-map sweeps and shared-recognition comparison | REPRODUCIBLE |

All five core experiments are rerun by GitHub Actions. The S2 theorem stack does not create a sixth core experiment.

## Manuscript and CI state

| Item | Status |
|---|---|
| Six GitHub-readable SVG figures | COMMITTED / REGENERATED IN CI |
| Six manuscript PDF figures | GENERATED IN CI |
| T1–T5 proof appendix | INTEGRATED |
| S2.* supplementary appendices | STACKED REVIEW BRANCHES |
| Markdown `$$ ... $$` delimiter validation | CI ENFORCED |
| E1–E5 reproduction | CI ENFORCED |
| Repository structure validation | CI ENFORCED |
| Illustrated LaTeX/PDF manuscript build | CI ENFORCED |
| v0.2 repository audit | PASS |

## Interpretation status

| Claim | Status |
|---|---|
| Nonnegative accessibility can define an abstract weighted FP measure | MODEL ASSUMPTION / EXACT AFTER DEFINITION |
| Everett branches obey the proposed QBS accessibility bridge | PHYSICALLY OPEN BRIDGE ASSUMPTION |
| Ordered conditional-mean prediction can imply positive covariance | PROVED UNDER S2/S2.11 CONDITIONS |
| Bounded, light-tail, or MoM data can statistically certify the covariance premise | PROVED UNDER THEIR RESPECTIVE ASSUMPTIONS |
| A passed statistical certificate establishes Everettian observer selection | NOT CLAIMED |
| External random generators become objectively lucky | NOT CLAIMED |

## Sequential extension

| Item | Status | Source |
|---|---|---|
| Recognition time as a stopping time | FORMALIZED | `supplementary/recognition_time.md` |
| FP value functional for a stopping rule | EXACT BY DEFINITION | `supplementary/recognition_time.md` |
| Universal early-vs-late recognition ordering | NOT CLAIMED / DEFERRED | `supplementary/recognition_time.md` |

## Open problems after S2.11

1. Derive, constrain, or reject a concrete physical Everett accessibility map from observer/branch physics.
2. Develop empirical or structural bounds for the S2.11 residual term in specific agent models.
3. Derive explicit Orlicz/mgf sufficient conditions for the S2.9 product/square Bernstein parameters with convention-specific constants.
4. Explore robust estimators that weaken S2.10's fourth-moment-type requirements for squared targets.
5. Extend selection validity to infinite or certification-data-dependent candidate classes.
6. Add a held-out certificate experiment only if public review requires it.
7. Continue novelty/prior-art search when review identifies a specific overlap question.
8. Develop a recognition-time ordering theorem only under explicit pathwise or conditional-advantage assumptions.

## Current stacked review sequence

1. PR #11 — S2 through S2.3.
2. PR #12 — S2.4 prediction-MSE certificate.
3. PR #13 — S2.5 bounded finite-sample certificate.
4. PR #15 — S2.6–S2.7 selection validity.
5. PR #16 — S2.8 generic confidence-envelope composition.
6. PR #17 — S2.9 light-tail instantiation.
7. PR #18 — S2.10 robust median-of-means instantiation.
8. Current branch — S2.11 residual conditional-covariance extension.
