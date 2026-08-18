# QBS Development Status

**Updated:** 2026-08-18

This file is the canonical ledger for active post-v0.2 research development.

The stable v0.2 public-review snapshot remains recorded in `STATUS.md` and frozen at:

- branch: `release/v0.2-public-review`
- commit: `7405f7408f74fa32b16d1cc9f624070cc14624ab`

The single active cumulative post-v0.2 review candidate is PR #21.

PRs #11–#20 are historical development records and are superseded for active review by PR #21.

## Locked core results

The core theorem set remains T1–T5.

The core experiment set remains E1–E5.

Neither set is renumbered or replaced by the post-v0.2 supplementary work.

## Post-v0.2 mathematical results

| ID | Result | Status | Primary source |
|---|---|---|---|
| S2 | Predictive-calibration alignment for score-measurable accessibility | PROVED / REVIEW CANDIDATE | `supplementary/adaptive_agent.md` |
| S2.2 | Posterior-mean self-calibration | PROVED | `supplementary/adaptive_agent.md` |
| S2.3 | Approximate-calibration covariance robustness | PROVED | `supplementary/adaptive_agent.md` |
| S2.4 | Prediction-MSE population certificate | PROVED | `supplementary/adaptive_agent.md` |
| S2.5 | Bounded finite-sample held-out covariance certificate | PROVED | `supplementary/finite_sample_certificate.md` |
| S2.6 | Validity after arbitrary independent training | PROVED | `supplementary/selection_validity.md` |
| S2.7 | Multiplicity-corrected finite candidate selection | PROVED | `supplementary/selection_validity.md` |
| S2.8 | Generic simultaneous-confidence-envelope composition | PROVED | `supplementary/confidence_envelope_certificate.md` |
| S2.9 | Light-tail sub-Gaussian/Bernstein instantiation | PROVED | `supplementary/light_tail_certificate.md` |
| S2.10 | Robust median-of-means instantiation | PROVED | `supplementary/robust_mom_certificate.md` |
| S2.11 | Residual conditional-covariance extension beyond score-measurability | PROVED / PROOF-REVIEWED | `supplementary/residual_covariance_extension.md` |
| S2.12 | Residual-variance lower certificate | PROVED / PROOF-REVIEWED | `supplementary/residual_variance_certificate.md` |
| S2.13 | Explained-variance alignment certificate | PROVED / PROOF-REVIEWED | `supplementary/explained_variance_certificate.md` |

## Predictive-alignment chain

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

S2.2 gives posterior-mean self-calibration.

S2.3–S2.4 give population robustness bounds.

S2.5–S2.10 provide bounded, selection-safe, generic-envelope, light-tail, and robust finite-moment statistical certification layers.

## General accessibility

The current S2.11 statement uses:

$$
U,S\in L^2,
\qquad
S\ge0,
\qquad
0<E[S]<\infty.
$$

Define:

$$
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
$$

S2.11 gives the exact decomposition:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),a(Y))
+
E[\operatorname{Cov}(U,S\mid Y)].
$$

This explicitly separates score-level alignment from residual branch-level dependence.

Let:

$$
v_U(Y)=\operatorname{Var}(U\mid Y),
\qquad
v_S(Y)=\operatorname{Var}(S\mid Y).
$$

S2.12 gives:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
E[\sqrt{v_U(Y)v_S(Y)}],
$$

and the coarser bound:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
\sqrt{E[v_U(Y)]E[v_S(Y)]}.
$$

The conditional Cauchy--Schwarz residual penalty is sharp without additional residual structure.

## Explained-variance certificate

Assume:

$$
\operatorname{Var}(U)>0,
\qquad
\operatorname{Var}(S)>0.
$$

Define:

$$
A_U
=
\frac{\operatorname{Var}(m(Y))}{\operatorname{Var}(U)},
\qquad
A_S
=
\frac{\operatorname{Var}(a(Y))}{\operatorname{Var}(S)}.
$$

When:

$$
A_UA_S>0,
$$

let:

$$
\rho_{ma}
=
\operatorname{Corr}(m(Y),a(Y)).
$$

S2.13 gives:

$$
\operatorname{Cov}(U,S)
\ge
\sqrt{\operatorname{Var}(U)\operatorname{Var}(S)}
\left[
\rho_{ma}\sqrt{A_UA_S}
-
\sqrt{(1-A_U)(1-A_S)}
\right].
$$

Therefore:

$$
\rho_{ma}\sqrt{A_UA_S}
>
\sqrt{(1-A_U)(1-A_S)}
$$

is sufficient for positive total covariance.

For perfectly aligned conditional means:

$$
\rho_{ma}=1,
$$

the sufficient condition simplifies to:

$$
A_U+A_S>1.
$$

For symmetric explained variance:

$$
A_U=A_S=A>0,
$$

the primitive sufficient condition is:

$$
\rho_{ma}A>1-A.
$$

When `rho_ma>-1`, this is algebraically equivalent to:

$$
A>
\frac{1}{1+\rho_{ma}}.
$$

Under `0<A<=1`, a strict symmetric worst-case certificate is feasible only for positive `rho_ma`.

S2.13 is sufficient, not necessary, because it inherits the worst-case residual penalty from S2.12.

## Dedicated proof review

`docs/post_v02_core_s2_proof_review.md` records a second-pass review of S2, S2.11, S2.12, and S2.13.

Result: **PASS WITH THREE CORRECTIONS**.

1. S2.11 moment assumptions were made explicit as square integrability.
2. S2.11/S2.12 counterexample and sharpness constructions were replaced by bounded Rademacher constructions compatible with strictly positive accessibility.
3. S2.13 symmetric-threshold denominator and feasibility conditions were made explicit.

The central covariance identities and inequalities were unchanged.

## Computational status

| ID | Experiment | Status |
|---|---|---|
| E1 | FOSD, independence null, nonmonotone counterexample | LOCKED / REPRODUCIBLE |
| E2 | Minimal learned agent / endogenous predictive correlation | LOCKED / REPRODUCIBLE |
| E3 | Paired recognition decomposition | LOCKED / REPRODUCIBLE |
| E4 | Fixed and changing-selector interaction decomposition | LOCKED / REPRODUCIBLE |
| E5 | Paired branch-map sweeps and shared-recognition comparison | LOCKED / REPRODUCIBLE |

No sixth core experiment is introduced by the S2 stack.

## Manuscript state

The post-v0.2 main-text conceptual spine is:

1. S2 predictive alignment;
2. S2.2 posterior-mean calibration;
3. S2.11 general accessibility;
4. compact S2.12 residual-variance penalty;
5. S2.13 explained-variance interpretation.

Detailed S2.3–S2.10 statistical machinery is Appendix-first.

The post-v0.2 manuscript compression audit passes.

The targeted prior-art audit is integrated.

The illustrated manuscript continues to build under CI.

## Interpretation status

| Claim | Status |
|---|---|
| Nonnegative accessibility can define an abstract weighted FP measure | MODEL ASSUMPTION / EXACT AFTER DEFINITION |
| Everett branches obey the proposed QBS accessibility bridge | PHYSICALLY OPEN BRIDGE ASSUMPTION |
| Ordered conditional-mean prediction can imply positive covariance | PROVED UNDER S2/S2.11–S2.13 CONDITIONS |
| Bounded, light-tail, or MoM data can statistically certify the covariance premise | PROVED UNDER THEIR RESPECTIVE ASSUMPTIONS |
| A passed statistical certificate establishes Everettian observer selection | NOT CLAIMED |
| External random generators become objectively lucky | NOT CLAIMED |

## Active review gates

1. Keep PR #21 CI-green after consolidation onto `main`.
2. Obtain external/public proof review of the compressed S2 spine.
3. Decide whether S2.13 remains in the main manuscript text after review.
4. Decide whether all S2.5–S2.10 results remain in the paper Appendix or partly move to repository-only supplementary material.
5. Add new theorem/statistical layers only in response to a concrete review-identified need.
6. Keep the Everett accessibility bridge as a separate physical problem.

## Historical development provenance

PRs #11–#20 are closed as historical and superseded for active review by PR #21.

They remain useful for provenance but are not authoritative current statements when later proof reviews corrected assumptions or boundary constructions.
