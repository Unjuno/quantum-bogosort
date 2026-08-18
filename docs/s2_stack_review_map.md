# S2 Stack Review Map

**Status:** post-v0.2 review architecture  
**Purpose:** prevent theorem proliferation from obscuring the paper's main argument.

The S2 family now contains several logically distinct layers. They should not all receive equal prominence in the manuscript.

## 1. Conceptual spine

The shortest conceptual chain is:

$$
\text{predictive signal}
\longrightarrow
\text{conditional-mean alignment}
\longrightarrow
\text{outcome/accessibility covariance}
\longrightarrow
\text{first-person mean shift}.
$$

For the general-accessibility model, the exact decomposition is:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(E[U\mid Y],E[S\mid Y])
+
E[\operatorname{Cov}(U,S\mid Y)].
$$

This decomposition should be the main conceptual endpoint of the S2 development.

## 2. Dependency graph

### Core predictive layer

**S2 — Predictive-calibration alignment**

For score-measurable accessibility:

$$
S=s(Y),
$$

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(E[U\mid Y],s(Y)).
$$

Role: establishes the basic conditional-mean mechanism.

**S2.2 — Posterior-mean self-calibration**

$$
Y=E[U\mid B]
\Longrightarrow
E[U\mid Y]=Y.
$$

Role: connects a standard posterior-mean predictor to the S2 premise.

### Population robustness layer

**S2.3 — Calibration-error robustness**

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)}.
$$

**S2.4 — Prediction-MSE certificate**

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{E[(U-Y)^2]\operatorname{Var}(S)}.
$$

Role: quantitative robustness; mainly appendix/statistical material.

### Finite-sample validation layer

**S2.5 — Bounded held-out certificate**  
**S2.6 — Independent-training validity**  
**S2.7 — Finite candidate post-selection validity**

Role: converts the population sufficient condition into a statistically valid testing procedure under explicit data-use rules.

### Statistical interface layer

**S2.8 — Generic confidence-envelope composition**

Role: isolates the QBS covariance composition from a particular concentration inequality.

**S2.9 — Light-tail instantiation**

Role: sub-Gaussian/Bernstein example of the S2.8 interface.

**S2.10 — Median-of-means instantiation**

Role: robust finite-moment example of the same interface.

These are validation technology, not part of the conceptual definition of QBS.

### General-accessibility layer

**S2.11 — Residual conditional-covariance extension**

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),a(Y))
+
E[\operatorname{Cov}(U,S\mid Y)],
$$

where:

$$
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
$$

Role: removes the restrictive assumption that accessibility is a deterministic function of the score.

**S2.12 — Residual-variance certificate**

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
\sqrt{E[v_U(Y)]E[v_S(Y)]}.
$$

Role: worst-case residual penalty when only unexplained conditional variation is controlled.

**S2.13 — Explained-variance form**

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

When both are positive:

$$
\rho_{ma}
=
\operatorname{Corr}(m(Y),a(Y)).
$$

Then:

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

Role: interpretable summary of the worst-case residual certificate.

## 3. Recommended manuscript placement

### Main text candidates

The main paper should emphasize only the results needed to understand the mechanism:

1. **S2** — conditional-mean predictive alignment;
2. **S2.2** — posterior-mean self-calibration, likely as a short corollary;
3. **S2.11** — exact general-accessibility decomposition;
4. **S2.13** — one interpretable sufficient-condition form, if space permits.

A compact main-text narrative can therefore move from the restrictive clean case to the general case without forcing readers through all finite-sample machinery.

### Appendix-first results

The following should remain primarily in the appendix unless review identifies them as central:

- S2.3 — calibration-error robustness;
- S2.4 — prediction-MSE certificate;
- S2.5 — bounded held-out certificate;
- S2.6 — conditional validity after training;
- S2.7 — finite candidate multiplicity control;
- S2.8 — generic confidence-envelope interface;
- S2.9 — light-tail instantiation;
- S2.10 — median-of-means instantiation;
- S2.12 — residual-variance worst-case bound.

These results strengthen falsifiability and statistical auditability but should not dominate the conceptual paper.

## 4. Main novelty boundary

The following are **not** strong standalone novelty claims:

- the law of total covariance;
- the law of total variance;
- Cauchy--Schwarz bounds;
- Hoeffding, Bernstein, or median-of-means concentration;
- normalized change-of-measure identities by themselves.

The potential contribution is the structured use of these tools inside the recognition-dependent QBS framework:

$$
R
\to
\pi_R
\to
(U_R,S_R),
$$

with explicit separation of:

- policy/trajectory change;
- observer-indexed accessibility change;
- predictive calibration;
- residual accessibility dependence;
- finite-sample certification;
- Everett bridge assumptions.

## 5. Results that must remain interpretation-neutral

S2 through S2.13 are probability/statistical results. They do not derive:

$$
d\mu^{FP}
\propto
S\,d\mu
$$

from quantum mechanics.

A theorem can establish a statement of the form:

$$
\text{if accessibility has property }P,
\text{ then FP value has property }Q.
$$

It cannot establish that Everettian observer self-location actually supplies that accessibility variable without a separate physical bridge.

## 6. Review gates before merge into a preprint branch

The stack should not be merged merely because CI is green. Before promotion, review should address:

1. proof correctness of S2, S2.11, S2.12, and S2.13;
2. whether S2.3–S2.10 are mathematically useful enough to retain in the paper appendix rather than only the repository;
3. whether the finite-sample constants are correct but unnecessarily conservative;
4. whether existing literature already contains the same combined conditional-mean/accessibility structure;
5. whether the general-accessibility residual term is modeled sharply enough;
6. whether an empirical certificate experiment adds information beyond the existing mathematical examples;
7. whether manuscript length remains appropriate for a foundations preprint.

## 7. Stop rule for theorem expansion

Do not add another S2-numbered theorem by default.

A new theorem should be added only if it does at least one of the following:

- removes a material modeling assumption;
- closes a specific review-identified gap;
- produces an operationally testable quantity not already captured by the current stack;
- supplies a substantially sharper result under clearly motivated assumptions.

Otherwise, further refinements should be recorded as remarks, propositions inside existing notes, or future-work items.

## ERROR CHECK

1. This document is an editorial/review map, not a new theorem.
2. It does not change theorem status in `STATUS.md`.
3. It keeps the core T1–T5 set unchanged.
4. It explicitly separates standard probability tools from the QBS-specific framework contribution.
5. It prevents CI success from being conflated with external mathematical review.
6. It preserves the Everett bridge as a separate physical assumption.
