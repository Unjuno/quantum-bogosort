# Claims, Assumptions, and Non-Claims

This document prevents theorem statements, simulation results, statistical validation results, and Everett interpretation claims from being conflated.

## Core exact claims

$$
E_{FP}[X]-E[X]
=
\frac{\operatorname{Cov}(X,S)}{E[S]}.
$$

$$
P_{FP}(X\ge c)-P(X\ge c)
=
\frac{\operatorname{Cov}(\mathbf 1_{\{X\ge c\}},S)}{E[S]}.
$$

If:

$$
g(x)=E[S\mid X=x]
$$

is nondecreasing, then:

$$
F_{FP}(c)\le F(c).
$$

Recognition and interaction decompose as:

$$
V_1-V_0
=
E[U_1-U_0]
+
Q(U_1,S_1)-Q(U_0,S_0),
$$

and:

$$
I
=
\frac{\operatorname{Cov}(D,S_0)}{E[S_0]}
+
\left[Q(U_1,S_1)-Q(U_1,S_0)\right].
$$

## S2 predictive-alignment family

For:

$$
m(Y)=E[U\mid Y],
\qquad
S=s(Y),
$$

S2 gives:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),s(Y)).
$$

If:

$$
Y=E[U\mid B],
$$

S2.2 gives:

$$
E[U\mid Y]=Y.
$$

S2.3–S2.4 give calibration-error and prediction-MSE population lower bounds. S2.5–S2.10 provide bounded, selection-safe, generic-envelope, light-tail, and robust finite-moment finite-sample certification layers under their stated assumptions.

## S2.11–S2.12: general accessibility and residual dependence

Let:

$$
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
$$

Then:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),a(Y))
+
E[\operatorname{Cov}(U,S\mid Y)].
$$

With:

$$
v_U(Y)=\operatorname{Var}(U\mid Y),
\qquad
v_S(Y)=\operatorname{Var}(S\mid Y),
$$

S2.12 gives:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
E[\sqrt{v_U(Y)v_S(Y)}],
$$

and:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
\sqrt{E[v_U(Y)]E[v_S(Y)]}.
$$

The basic residual-variance penalty is sharp under perfect conditional anti-correlation.

## S2.13: explained-variance alignment

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

Then:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
\sqrt{
\operatorname{Var}(U)
\operatorname{Var}(S)
(1-A_U)(1-A_S)
}.
$$

When:

$$
A_UA_S>0,
$$

define:

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

Therefore:

$$
\rho_{ma}\sqrt{A_UA_S}
>
\sqrt{(1-A_U)(1-A_S)}
$$

is sufficient for positive total covariance.

If:

$$
\rho_{ma}=1,
$$

this simplifies to:

$$
A_U+A_S>1.
$$

If:

$$
A_U=A_S=A>0,
$$

then a sufficient threshold is:

$$
A>
\frac{1}{1+\rho_{ma}}.
$$

These are worst-case residual sufficient conditions inherited from S2.12, not necessary conditions.

## Simulation-supported claims

E1–E5 classically demonstrate the formal mechanisms: weighting/FOSD, learned predictive ordering, paired recognition decomposition, policy–QBS interaction, and cross-copy coherence. They do not establish Everettian physics or automatically satisfy any finite-sample certificate.

## Model and statistical assumptions

The abstract weighted measure requires:

$$
S_\pi(\omega)\ge0,
\qquad
0<E[S_\pi]<\infty.
$$

S2 assumes score-measurable accessibility. S2.11 relaxes that assumption but retains residual dependence explicitly. S2.12 assumes square integrability. S2.13 additionally assumes nonzero total variances when normalized explained-variance quantities are used.

S2.5 assumes independent bounded held-out evaluation. S2.6 permits training-dependent rules only with independent certification data. S2.7 assumes a finite predeclared candidate family with multiplicity accounting. S2.8 assumes a valid simultaneous five-moment confidence envelope. S2.9 assumes valid light-tail parameters. S2.10 assumes valid target-variable variance bounds and an i.i.d. block construction.

## Everett bridge assumption

A separate physical interpretation assumes:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

This is not derived from unitary quantum mechanics, decoherence, observer dynamics, or the Born rule.

## Non-claims

The repository does **not** claim that:

- an external RNG becomes objectively biased toward favorable outcomes;
- the weighting identities establish quantum immortality;
- every recognition-dependent policy is beneficial;
- positive correlation alone implies FOSD;
- mutual information alone implies positive accessibility covariance;
- adaptation automatically learns the true posterior mean;
- score-level alignment remains sufficient after removing `S=s(Y)` while ignoring residual dependence;
- the S2.12 worst-case residual penalty describes the actual residual correlation in a concrete model;
- high explained variance alone is enough when conditional means are nonpositively aligned;
- S2.13 is a necessary condition for positive covariance;
- failure of a sufficient certificate implies negative covariance;
- uncorrected model search preserves nominal confidence;
- a statistical certificate establishes the Everett accessibility bridge.

## Failure conditions

- outcome/accessibility independence gives zero pure weighting uplift in expectation;
- nonmonotone conditional accessibility can break FOSD;
- dependence without conditional-mean prediction can defeat S2;
- a sufficiently negative S2.11 residual term can overturn score-level alignment;
- large unexplained variance can make S2.12/S2.13 inconclusive;
- invalid concentration, tail, variance, or model-selection assumptions invalidate their corresponding statistical certificates;
- zero expected accessibility makes the normalized FP measure undefined;
- rejecting the Everett bridge removes the physical interpretation while leaving the abstract mathematical/statistical results intact.
