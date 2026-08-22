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

## Classical selection-equivalence and identifiability boundary

The normalized accessibility law has a classical selection representation. Assume

```math
S\ge0,
\qquad
0<m:=E[S]<\infty.
```

If additionally

```math
S\le M<\infty
```

almost surely, augment the model by an independent `U~Uniform(0,1)` and define

```math
A=\left\{U\le\frac{S}{M}\right\}.
```

Then for every measurable `B`,

```math
P(\omega\in B\mid A)
=
\frac{E[\mathbf 1_BS]}{E[S]}
=
\mu^{FP}(B).
```

Thus bounded accessibility weighting is exactly representable as ordinary state-dependent ascertainment conditioning on an augmented classical probability space.

For a general integrable nonnegative `S`, let a classical record count satisfy

```math
N\mid\omega\sim\mathrm{Poisson}(cS(\omega)),
```

for any positive scaling constant `c` making the Poisson mean dimensionless. The record-size-biased law

```math
\mu^{record}(B)
=
\frac{E[N\mathbf 1_B]}{E[N]}
```

then satisfies exactly

```math
\mu^{record}(B)=\mu^{FP}(B).
```

Moreover, bounded truncations `S_n=min(S,n)` generate binary-ascertainment laws converging to `mu^FP` in total variation. The complete proofs are in [`../supplementary/selection_equivalence.md`](../supplementary/selection_equivalence.md).

This is a probability-law equivalence, not a universal physical or causal equivalence. It has an important identifiability consequence: if an Everett accessibility mechanism and a classical ascertainment/recording mechanism induce the same relevant base joint law of `(X,S)`, they induce the same first-person observable law of `X`. The weighted observable law alone cannot distinguish those mechanisms.

Therefore a specifically Everettian bridge requires more than reproduction of the normalized weighted distribution. It needs an independent physical derivation or additional observable/interventional/sequential predictions that differ from a behavior-matched classical selection null.

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

## Recursive observer-information extension

The recursive extension in [`../supplementary/evidence_activation.md`](../supplementary/evidence_activation.md) is **unnumbered supplementary theory**. It does not add a sixth core theorem or an `S2.14`.

Let `H_t` denote the information available when the decision for step `t+1` is chosen, and let `X_{t+1}` be the next outcome increment. Define the predictable component and filtration-relative innovation by:

```math
m_{t+1}=E_\mu[X_{t+1}\mid H_t],
\qquad
\varepsilon_{t+1}=X_{t+1}-m_{t+1}.
```

Then:

```math
E_\mu[\varepsilon_{t+1}\mid H_t]=0.
```

For:

```math
A_T=\sum_{t=0}^{T-1}m_{t+1},
\qquad
M_T=\sum_{t=0}^{T-1}\varepsilon_{t+1},
\qquad
U_T=A_T+M_T,
```

we have `E_mu[M_T]=0` under the stated integrability conditions. Applying the existing T1 identity to `A_T` and `M_T` gives:

```math
E_{FP}[U_T]-E_\mu[U_T]
=
\frac{\mathrm{Cov}_\mu(A_T,S_T)}{E_\mu[S_T]}
+
\frac{\mathrm{Cov}_\mu(M_T,S_T)}{E_\mu[S_T]}.
```

The repository calls these terms **predictable selection** and **innovation selection** respectively. This is an exact decomposition under the chosen filtration and weighted-measure assumptions. Innovation selection is not an objective physical luck variable: changing the information filtration can change the split between `A_T` and `M_T`.

For sequential accessibility factors `G_t` with cumulative accessibility `S_t=\prod_{j=1}^t G_j`, the one-step first-person update is a sequential use of T1:

```math
E_t^{FP}[Z]
=
\frac{E_{t-1}^{FP}[ZG_t]}{E_{t-1}^{FP}[G_t]}.
```

When a specified QBS observer model and a specified null observer model provide conditional next-record laws `P_{1,t}` and `P_{0,t}`, standard likelihood-ratio updating gives:

```math
\ell_{t+1}
=
\log\frac{dP_{1,t}}{dP_{0,t}}(O_{t+1}).
```

Under correctly specified conditional models, the expected one-step log likelihood ratio has the corresponding KL-divergence sign. These are standard Bayesian/information-theoretic identities used to formalize the feedback from experienced observer history to later belief/adoption. They do **not** establish that the QBS bridge is physically correct.

## Simulation-supported claims

E1–E5 classically demonstrate the locked formal mechanisms: weighting/FOSD, learned predictive ordering, paired recognition decomposition, policy–QBS interaction, and cross-copy coherence. They do not establish Everettian physics or automatically satisfy any finite-sample certificate.

The exploratory [`../supplementary/recursive_qbs_simulation.py`](../supplementary/recursive_qbs_simulation.py) is separate from E1–E5. It demonstrates that the recursive mechanism can be instantiated in a classical toy model, that predictable and innovation selection can be measured separately, and that an anti-aligned control can produce positive predictable selection with negative innovation selection and negative total first-person uplift. These simulation results are model-internal mechanism checks, not empirical evidence for a physical accessibility law.

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

The recursive innovation decomposition depends on the selected filtration/information state and requires the conditional expectations and weighted horizon quantities to exist. Sequential likelihood-ratio bridge updates require specified competing observer models and the needed absolute-continuity conditions. Claims about expected KL drift require correct model specification; misspecification can reverse or otherwise distort practical belief dynamics.

The bounded binary-selection representation additionally assumes an almost-sure finite upper bound on `S`. The general record-size-bias representation requires only nonnegative integrable `S`; the Poisson intensity must be dimensionless, which can always be arranged by positive rescaling because the normalized weighted law is scale invariant.

## Everett bridge assumption

A separate physical interpretation assumes:

```math
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
```

This is not derived from unitary quantum mechanics, decoherence, observer dynamics, or the Born rule.

The selection-equivalence result shows that this same probability law can have classical ascertainment / record-size-bias representations. Consequently, fitting or reproducing the weighted law is not by itself evidence for the Everett interpretation of `S_pi`.

## Non-claims

The repository does **not** claim that:

- an external RNG becomes objectively biased toward favorable outcomes;
- innovation selection is a causal increase in objective chance or a filtration-independent physical luck parameter;
- observing a favorable history by itself proves the QBS bridge rather than competing null, survivorship, or misspecified models;
- a weighted first-person distribution by itself identifies an Everettian rather than classical ascertainment/size-bias mechanism;
- classical probability-law equivalence proves that the underlying physical mechanism is classical or refutes an Everett mechanism;
- recursive bridge belief must increase monotonically on every realized path;
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
- a statistical certificate or recursive toy simulation establishes the Everett accessibility bridge.

## Failure conditions

- outcome/accessibility independence gives zero pure weighting uplift in expectation;
- constant expected future accessibility across present states gives no present self-location reweighting from future accessibility;
- any Everett bridge that predicts only a weighted law already matched by a classical selection null is observationally unidentified by that law alone;
- nonmonotone conditional accessibility can break FOSD;
- dependence without conditional-mean prediction can defeat S2;
- a sufficiently negative S2.11 residual term can overturn score-level alignment;
- positive predictable selection can coexist with negative innovation selection, and negative innovation selection can dominate total first-person uplift;
- the predictable/innovation split changes when the information filtration changes;
- a misspecified bridge model can produce misleading recursive belief dynamics;
- if the competing conditional observer laws are identical at a step, that step supplies zero likelihood-ratio evidence for distinguishing them;
- large unexplained variance can make S2.12/S2.13 inconclusive;
- invalid concentration, tail, variance, or model-selection assumptions invalidate their corresponding statistical certificates;
- zero expected accessibility makes the normalized FP measure undefined;
- missing base/weighted integrability makes the corresponding finite mean/covariance decomposition undefined even though the normalized accessibility measure itself may still exist;
- rejecting the Everett bridge removes the physical interpretation while leaving the abstract mathematical/statistical results intact.
