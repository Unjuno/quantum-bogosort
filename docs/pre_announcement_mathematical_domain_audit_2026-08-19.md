# Pre-announcement mathematical-domain audit — 2026-08-19

## Purpose

This pass audits whether the expressions used by the core T1–T5 framework, the principal S2 statistical certificates, and the main supplementary toy models are actually finite, real-valued, measurable, and normalized under their stated assumptions.

The frozen `v0.3-public-review` tag/Release at commit `58038763127258bd3e2f0d41708c4dfa01f81fd6` is not modified. Corrections described here apply to current `main`.

An identity can be algebraically correct while its public theorem statement is too weak to make one side finite. Likewise, a confidence guarantee can be correct on its validity event while the reported random statistic is undefined elsewhere. This audit targets those domain failures rather than trying to re-prove every theorem from scratch.

## Finding 1 — T1 requires the complete generic accessibility/outcome domain

The frozen compact T1 wording did not state all assumptions required by both sides of

```math
E_{FP}[X]-E[X]
=
\frac{\mathrm{Cov}(X,S)}{E[S]}.
```

Current `main` states the complete generic domain:

```math
S\ge0,
\qquad
0<E[S]<\infty,
\qquad
E[|X|]<\infty,
\qquad
E[|X|S]<\infty.
```

Both integrability clauses are genuinely needed. On `(0,1)`, `X(x)=1/x` and `S(x)=x^2` give finite `E[S]` and `E[|X|S]` but infinite `E[|X|]`. Conversely, `X(x)=S(x)=x^{-1/2}` gives finite `E[|X|]` and `E[S]` but infinite `E[|X|S]`.

A later literal-source check also found that the compact TeX setup quantified `S_pi` while T1 introduced a generic `S`. Current T1 now binds the nonnegativity/normalization assumptions locally instead of relying on a differently indexed setup variable.

T2 needs no additional outcome assumption because its indicator is bounded and `E[S]<infinity` supplies weighted integrability.

## Finding 2 — T4 requires base integrability for each policy outcome

T4 contains both base expectations and accessibility-weighted expectations. Current `main` therefore requires, for each recognition state `R`:

```math
0<E[S_R]<\infty,
\qquad
E[|U_R|]<\infty,
\qquad
E[|U_R|S_R]<\infty.
```

The recognition decomposition itself is unchanged.

## Finding 3 — general T5 requires cross-integrability

The selector-changing proof adds and subtracts:

```math
Q(U_1,S_0).
```

State-specific T4 assumptions do not imply this cross-weighted term is finite. Current `main` therefore additionally requires:

```math
E[|U_1|S_0]<\infty.
```

For a fixed selector this requirement is already supplied by the state-1 weighted-integrability condition.

## Finding 4 — discrete pointwise present-self-location requires a positive-probability atom

The event formula

```math
P_{FP}(Z\in A)
=
\frac{E[\mathbf1_{\{Z\in A\}}S_T]}{E[S_T]}
```

is well-defined under the normalized accessibility assumptions. The pointwise discrete rewrite

```math
P_{FP}(Z=z)
=
\frac{E[S_T\mid Z=z]P(Z=z)}{E[S_T]}
```

is stated only for atoms satisfying `P(Z=z)>0`. At a null atom a pointwise conditional expectation is not canonically determined; absolute continuity already gives zero FP probability there.

## Finding 5 — S2.8 needed a total real-valued random certificate

The original generic envelope used

```math
D_{\mathrm{env}}
=
C_L-\sqrt{U_MV_U}.
```

On the simultaneous confidence event this is valid because the MSE inequality forces `U_M>=0`. Outside that event, however, the generic statistical procedure was not required to return a nonnegative numerical `U_M`, so the random certificate itself could cease to be real-valued.

Current `main` defines

```math
U_M^+=\max\{0,U_M\},
```

and

```math
D_{\mathrm{env}}
=
C_L-\sqrt{U_M^+V_U}.
```

On the validity event `U_M^+=U_M`, so the covariance bound and coverage are unchanged. The clipping only makes the statistic total on the whole sample space.

## Finding 6 — S2.9 concentration parameters require an explicit nonnegative domain

S2.9 defines its own concentration radii rather than importing one universal named parameterization. Current `main` therefore explicitly requires

```math
\sigma_X\ge0,
\qquad
v_W\ge0,
\qquad
b_W\ge0.
```

This makes every square-root/radius real and nonnegative. The five-event union-bound constant `t=log(10/delta)` is unchanged.

For the residual-square moment,

```math
U_M
=
\overline{(U-Y)^2}+r_{R^2}\ge0
```

on every sample, so the generic S2.8 clipping satisfies `U_M^+=U_M` identically for S2.9.

## Finding 7 — S2.10 needs a separate zero-variance proof branch

S2.10 permits

```math
0\le\mathrm{Var}(Z_j)\le v_j<\infty.
```

For `v_j>0`, Chebyshev at radius `2 sqrt(v_j/m)` gives bad-block probability at most `1/4`, after which the median/Hoeffding argument gives `exp(-b/8)`.

For `v_j=0`, the original proof could not literally reuse a Chebyshev division at zero threshold. Instead:

```math
v_j=0
\Longrightarrow
\mathrm{Var}(Z_j)=0,
```

so `Z_j` is almost surely constant, every block mean is exact, the MoM radius is zero, and the deviation probability is exactly zero. Current `main` explicitly splits those two cases.

## Finding 8 — recognition time needed measurability and FP-admissibility boundaries

The recognition-confidence process was previously written in event-like notation. Current `main` correctly treats

```math
C_t:\Omega\to\mathbb R
```

as an adapted, `F_t`-measurable random variable.

In discrete time, adaptedness gives the stopping-time property directly through the finite/countable union of threshold events. In continuous time, adaptedness alone is not used as a blanket hitting-time theorem; adapted continuous sample paths together with the usual filtration conditions are stated as one sufficient setup.

For a stopping rule `tau`, the FP value/T1 decomposition is now restricted to FP-admissible rules satisfying

```math
S_\tau\ge0,
\qquad
0<E[S_\tau]<\infty,
```

```math
E[|U_\tau|]<\infty,
\qquad
E[|U_\tau|S_\tau]<\infty.
```

The repository still makes no universal theorem that earlier recognition is better.

## Finding 9 — repeated-filter sensitivity needed explicit differentiation regularity

For

```math
S=\lambda^{N_B},
\qquad
V(\lambda)
=
\frac{E[U\lambda^{N_B}]}{E[\lambda^{N_B}]},
```

the identity

```math
\frac{dV}{d\log\lambda}
=
\mathrm{Cov}_\lambda(U,N_B)
```

is not justified by a purely formal derivative when the adverse-trigger count or utility is unbounded.

Current `main` states the downweighting domain `0<lambda<=1`, takes `N_B` finite and nonnegative integer-valued, and requires a positive neighborhood in which differentiation may be exchanged with the numerator and denominator expectations. In particular, the relevant weighted derivative moments

```math
E[|U|N_B\lambda^{N_B}],
\qquad
E[N_B\lambda^{N_B}]
```

must be finite at the evaluation point together with an appropriate domination condition. At the endpoint `lambda=1` of a family restricted to `lambda<=1`, the corresponding statement is a left derivative under the same one-sided regularity.

The sensitivity identity itself is unchanged.

## Finding 10 — the binary soft-QBS toy needs parameter and normalization boundaries

The binary toy now explicitly requires

```math
0\le p\le1,
\qquad
0\le\lambda\le1.
```

Total expected accessibility is

```math
E[S]=p+(1-p)\lambda,
```

so the normalized FP probability is defined only when

```math
p+(1-p)\lambda>0.
```

Within the unit square the sole excluded zero-normalization corner is `(p,lambda)=(0,0)`.

For the execution/leakage parameterization

```math
\lambda=1-q(1-\alpha),
```

current `main` explicitly takes

```math
0\le q\le1,
\qquad
0\le\alpha\le1,
```

which guarantees `lambda in [0,1]`. Those bounds alone do not rescue the `p=0, lambda=0` normalization boundary.

## Finding 11 — the Gaussian toy needs explicit correlation/accessibility parameter domains

The Gaussian toy now states

```math
-1\le\rho\le1,
\qquad
0\le\lambda\le1.
```

Hence

```math
E[S]=\frac{1+\lambda}{2}>0.
```

Under

```math
\lambda=1-q(1-\alpha),
\qquad
0\le q\le1,
\qquad
0\le\alpha\le1,
```

the selector remains in `[0,1]` and the closed-form denominator

```math
2-q(1-\alpha)
```

is strictly positive. The analytic FP-mean formula itself is unchanged.

## Cross-surface regression locks

### Core theorem lock

`scripts/validate_core_theorem_lock.py` compares current `theory/core_theorems.tex` with frozen v0.3 canonical blob

`82986d7197e79446d6574aab538d1edaeff47eb6`.

It normalizes exactly four approved current-main textual differences:

1. version-neutral title;
2. setup base-integrability;
3. complete generic T1 accessibility/outcome domain;
4. T5 cross-integrability.

After those replacements the complete Git blob must equal the frozen canonical blob. The validator also requires the approved T1/T4/T5 domains across nine theory, experiment-card, and manuscript surfaces.

### Supplementary consistency lock

`scripts/validate_supplementary_consistency.py` makes the later boundary corrections executable. It currently checks the relevant source/manuscript/audit representations for:

- S2.8 off-event real-valued totality;
- S2.9 nonnegative concentration-parameter domain;
- S2.10 zero-variance proof branch;
- recognition-time measurability, continuous-time qualification, and FP-admissibility;
- repeated-filter derivative regularity;
- binary positive-normalization and parameter domains;
- Gaussian correlation/accessibility/execution parameter domains.

The workflow runs this validator after the core theorem lock and before metadata/experiment execution.

## Results rechecked without further correction

The following were rechecked for the same class of domain/sign/coverage failure and no additional correction was identified in this pass:

- S1 shared-latent covariance/coherence theorem;
- S2 projection identity and strictness boundary;
- S2.3 residual decomposition;
- S2.4 MSE covariance lower bound;
- S2.5 bounded Hoeffding certificate and five-event constants;
- S2.6 independent held-out conditional validity;
- S2.7 finite predeclared-candidate multiplicity correction;
- S2.11 total-covariance residual decomposition;
- S2.12 conditional Cauchy--Schwarz residual lower bound and sharpness construction;
- S2.13 explained-variance normalization, including its explicit positive-variance boundary;
- S1's distinction between marginal first-person weighting and cross-copy coherence.

The evidence-activation note was also inspected. It is explicitly framed as an exploratory/statistical activation model rather than a universal exact theorem; no additional theorem-level correction was required in this pass.

## Scientific boundary

These corrections strengthen only domain, measurability, total-definedness, normalization, or boundary-case assumptions. They do not change:

- T1–T5 algebraic identities;
- T3 FOSD/sign conclusions;
- S2.8's on-validity-event covariance lower bound or confidence level;
- S2.9 concentration constants;
- S2.10 positive-variance MoM radius or Hoeffding amplification;
- repeated-filter sensitivity algebra on its valid differentiation domain;
- binary/Gaussian closed-form algebra on their valid normalization domains;
- any E1–E5 numerical result;
- the base probability law;
- the Everett accessibility bridge status.

## Remaining execution gate

The corrected sources and validators still require the final settled `main` GitHub Actions workflow to complete successfully. Source-level reasoning and connector-based inspection do not substitute for the unavailable direct-push Actions check-run state.