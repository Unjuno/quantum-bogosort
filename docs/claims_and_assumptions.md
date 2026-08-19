# Claims, Assumptions, and Non-Claims

This document prevents theorem statements, simulation results, statistical validation results, and Everett interpretation claims from being conflated.

## Core exact claims

For covariance/mean identities, assume the relevant outcome is integrable under both the base measure and the accessibility weighting:

```math
E[|X|]<\infty,
\qquad
0<E[S]<\infty,
\qquad
E[|X|S]<\infty.
```

Then:

```math
E_{FP}[X]-E[X]
=
\frac{\mathrm{Cov}(X,S)}{E[S]}.
```

```math
P_{FP}(X\ge c)-P(X\ge c)
=
\frac{\mathrm{Cov}(\mathbf 1_{\{X\ge c\}},S)}{E[S]}.
```

If:

```math
g(x)=E[S\mid X=x]
```

is nondecreasing, then:

```math
F_{FP}(c)\le F(c).
```

For recognition states, assume for each `R`:

```math
0<E[S_R]<\infty,
\qquad
E[|U_R|]<\infty,
\qquad
E[|U_R|S_R]<\infty.
```

Recognition decomposes as:

```math
V_1-V_0
=
E[U_1-U_0]
+
Q(U_1,S_1)-Q(U_0,S_0).
```

The general selector-changing interaction identity additionally requires:

```math
E[|U_1|S_0]<\infty,
```

because it introduces the cross term `Q(U_1,S_0)`. Under that condition:

```math
I
=
\frac{\mathrm{Cov}(D,S_0)}{E[S_0]}
+
\left[Q(U_1,S_1)-Q(U_1,S_0)\right].
```

These are domain conditions ensuring the displayed expectations and covariance terms are finite; they do not change the algebraic identities themselves.

## Present self-location under future accessibility

Let `Z` denote a present state or present trajectory descriptor and let `S_T` denote accessibility determined over its future continuation. Restricting the same normalized weighted measure to the present state gives:

```math
P_{FP}(Z\in A)
=
\frac{E[\mathbf 1_{\{Z\in A\}}S_T]}{E[S_T]}.
```

For a discrete atom with positive base probability:

```math
P(Z=z)>0,
```

we may write:

```math
P_{FP}(Z=z)
=
\frac{E[S_T\mid Z=z]P(Z=z)}{E[S_T]}.
```

If `P(Z=z)=0`, absolute continuity of the weighted measure gives `P_FP(Z=z)=0`; no pointwise value of `E[S_T\mid Z=z]` at that null atom is required.

This is an exact change-of-measure consequence once the weighted first-person measure is adopted. It means that differential expected future accessibility can reweight present self-location. It does **not** imply backward causation or a causal change in the base law of `Z`.

A favorable or upward self-location shift requires an additional alignment between the relevant favorability/utility statistic and expected future accessibility. Future accessibility that varies across present states is sufficient for reweighting, but not by itself for a favorable direction.

## S2 predictive-alignment family

For:

```math
m(Y)=E[U\mid Y],
\qquad
S=s(Y),
```

S2 gives:

```math
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),s(Y)).
```

If:

```math
Y=E[U\mid B],
```

S2.2 gives:

```math
E[U\mid Y]=Y.
```

S2.3–S2.4 give calibration-error and prediction-MSE population lower bounds. S2.5–S2.10 provide bounded, selection-safe, generic-envelope, light-tail, and robust finite-moment finite-sample certification layers under their stated assumptions.

## S2.11–S2.12: general accessibility and residual dependence

For the current S2.11 statement assume:

```math
U,S\in L^2,
\qquad
S\ge0,
\qquad
0<E[S]<\infty.
```

Let:

```math
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
```

Then:

```math
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),a(Y))
+
E[\mathrm{Cov}(U,S\mid Y)].
```

With:

```math
v_U(Y)=\mathrm{Var}(U\mid Y),
\qquad
v_S(Y)=\mathrm{Var}(S\mid Y),
```

S2.12 gives:

```math
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
E[\sqrt{v_U(Y)v_S(Y)}],
```

and:

```math
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
\sqrt{E[v_U(Y)]E[v_S(Y)]}.
```

The basic residual-variance penalty is sharp under perfect conditional anti-correlation. The proof-review sharpness construction uses bounded Rademacher residuals and strictly positive accessibility, so no hidden unbounded-shift assumption remains.

## S2.13: explained-variance alignment

Assume additionally:

```math
\mathrm{Var}(U)>0,
\qquad
\mathrm{Var}(S)>0.
```

Define:

```math
A_U
=
\frac{\mathrm{Var}(m(Y))}{\mathrm{Var}(U)},
\qquad
A_S
=
\frac{\mathrm{Var}(a(Y))}{\mathrm{Var}(S)}.
```

Then:

```math
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
\sqrt{
\mathrm{Var}(U)
\mathrm{Var}(S)
(1-A_U)(1-A_S)
}.
```

When:

```math
A_UA_S>0,
```

define:

```math
\rho_{ma}
=
\mathrm{Corr}(m(Y),a(Y)).
```

Then:

```math
\mathrm{Cov}(U,S)
\ge
\sqrt{\mathrm{Var}(U)\mathrm{Var}(S)}
\left[
\rho_{ma}\sqrt{A_UA_S}
-
\sqrt{(1-A_U)(1-A_S)}
\right].
```

Therefore:

```math
\rho_{ma}\sqrt{A_UA_S}
>
\sqrt{(1-A_U)(1-A_S)}
```

is sufficient for positive total covariance. Because the right-hand side is nonnegative, this worst-case sufficient certificate requires positive conditional-mean correlation.

If:

```math
\rho_{ma}=1,
```

this simplifies to:

```math
A_U+A_S>1.
```

If:

```math
A_U=A_S=A>0,
```

then the primitive condition is:

```math
\rho_{ma}A>1-A.
```

For:

```math
\rho_{ma}>-1,
```

this is algebraically equivalent to:

```math
A>
\frac{1}{1+\rho_{ma}}.
```

Since `0<A<=1`, the strict symmetric worst-case certificate is feasible only when:

```math
\rho_{ma}>0.
```

These are worst-case residual sufficient conditions inherited from S2.12, not necessary conditions.

## Simulation-supported claims

E1–E5 classically demonstrate the formal mechanisms: weighting/FOSD, learned predictive ordering, paired recognition decomposition, policy–QBS interaction, and cross-copy coherence. They do not establish Everettian physics or automatically satisfy any finite-sample certificate.

## Model and statistical assumptions

The abstract weighted **measure** requires:

```math
S_\pi(\omega)\ge0,
\qquad
0<E[S_\pi]<\infty.
```

Finite ordinary/first-person value and covariance decompositions additionally require the corresponding base and weighted outcome integrability:

```math
E[|U_\pi|]<\infty,
\qquad
E[|U_\pi|S_\pi]<\infty.
```

For the general T5 selector-changing decomposition, also require:

```math
E[|U_1|S_0]<\infty.
```

S2 assumes score-measurable accessibility. S2.11 relaxes that assumption but retains residual dependence explicitly and currently uses square integrability to make the covariance decomposition unambiguous. S2.12 uses the same square-integrability basis. S2.13 additionally assumes nonzero total variances when normalized explained-variance quantities are used.

S2.5 assumes independent bounded held-out evaluation. S2.6 permits training-dependent rules only with independent certification data. S2.7 assumes a finite predeclared candidate family with multiplicity accounting. S2.8 assumes a valid simultaneous five-moment confidence envelope. S2.9 assumes valid light-tail parameters. S2.10 assumes valid target-variable variance bounds and an i.i.d. block construction.

## Everett bridge assumption

A separate physical interpretation assumes:

```math
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
```

This is not derived from unitary quantum mechanics, decoherence, observer dynamics, or the Born rule.

## Non-claims

The repository does **not** claim that:

- an external RNG becomes objectively biased toward favorable outcomes;
- future accessibility by itself guarantees a favorable present self-location shift without an alignment between accessibility and the relevant favorability/utility statistic;
- the present-self-location identity implies backward causation;
- the weighting identities establish quantum immortality;
- every recognition-dependent policy is beneficial;
- positive correlation alone implies FOSD;
- mutual information alone implies positive accessibility covariance;
- adaptation automatically learns the true posterior mean;
- score-level alignment remains sufficient after removing `S=s(Y)` while ignoring residual dependence;
- the S2.12 worst-case residual penalty describes the actual residual correlation in a concrete model;
- high explained variance alone is enough when conditional means are nonpositively aligned;
- the symmetric S2.13 threshold can be satisfied with nonpositive `rho_ma` under `0<A<=1`;
- S2.13 is a necessary condition for positive covariance;
- failure of a sufficient certificate implies negative covariance;
- uncorrected model search preserves nominal confidence;
- a statistical certificate establishes the Everett accessibility bridge.

## Failure conditions

- outcome/accessibility independence gives zero pure weighting uplift in expectation;
- constant expected future accessibility across present states gives no present self-location reweighting from future accessibility;
- nonmonotone conditional accessibility can break FOSD;
- dependence without conditional-mean prediction can defeat S2;
- a sufficiently negative S2.11 residual term can overturn score-level alignment;
- large unexplained variance can make S2.12/S2.13 inconclusive;
- invalid concentration, tail, variance, or model-selection assumptions invalidate their corresponding statistical certificates;
- zero expected accessibility makes the normalized FP measure undefined;
- missing base/weighted integrability makes the corresponding finite mean/covariance decomposition undefined even though the normalized accessibility measure itself may still exist;
- rejecting the Everett bridge removes the physical interpretation while leaving the abstract mathematical/statistical results intact.
