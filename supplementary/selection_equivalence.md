# Selection-Equivalence and Identifiability Boundary

This note records **unnumbered exact boundary results** for the QBS weighted measure. It does not add `T6`, `S2.14`, or `E6`.

The purpose is adversarial: before assigning any specifically Everettian meaning to observer accessibility, ask how much of the first-person law can already be represented by ordinary classical ascertainment, record multiplicity, or selection conditioning, and what additional restrictions are actually needed for mechanism identification.

## Setup

Let

```math
(\Omega,\mathcal F,\mu)
```

be a probability space and let

```math
S:\Omega\to[0,\infty)
```

be measurable with

```math
0<m:=E_\mu[S]<\infty.
```

Define the normalized weighted law

```math
\mu^{FP}(B)
=
\frac{E_\mu[\mathbf 1_B S]}{E_\mu[S]}
=
\frac{E_\mu[\mathbf 1_B S]}{m},
\qquad B\in\mathcal F.
```

The weight can be taken dimensionless because multiplying `S` by any positive constant leaves `mu^FP` unchanged. If a concrete model assigns units to an unnormalized score, every acceptance ratio below uses a bound with the same units so the probability remains dimensionless.

| Symbol | Meaning | Units | Domain / assumption | Type |
|---|---|---|---|---|
| `mu` | base law | none | probability measure | measure |
| `S` | accessibility / selection weight | dimensionless by convention | nonnegative, finite positive mean | random variable |
| `m` | `E_mu[S]` | same as `S` | `0<m<infinity` | scalar |
| `M` | finite upper bound for `S` | same as `S` | `S<=M` a.s., `M>0` | scalar |
| `U` | auxiliary uniform randomizer | none | independent `Uniform(0,1)` | random variable |
| `A` | ascertainment event | none | defined below | event |
| `N` | number of recorded copies | count | conditional Poisson mean proportional to `S` | integer random variable |
| `c` | context / intervention / policy index | none | arbitrary index set | index |
| `r_c` | `dQ_c/dmu_c` | none | nonnegative, mean one under `mu_c` | density ratio |

## Exact bounded selection representation

### Proposition: bounded accessibility is ordinary ascertainment conditioning

Assume in addition that for some finite `M>0`,

```math
0\le S\le M
\qquad \mu\text{-a.s.}
```

Extend the probability space by an independent

```math
U\sim\mathrm{Uniform}(0,1)
```

and define the recording / ascertainment event

```math
A
=
\left\{
U\le\frac{S}{M}
\right\}.
```

Then

```math
P(A)=\frac{m}{M}>0,
```

and for every `B in F`,

```math
P(\omega\in B\mid A)
=
\mu^{FP}(B).
```

### Proof

Conditioning on `omega`, independence and uniformity give

```math
P(A\mid\omega)
=
\frac{S(\omega)}{M}.
```

Therefore

```math
P(A)
=
E_\mu\left[\frac{S}{M}\right]
=
\frac{m}{M}
>0.
```

For any measurable `B`,

```math
P(\omega\in B,A)
=
E_\mu\left[
\mathbf 1_B\frac{S}{M}
\right].
```

Dividing by `P(A)=m/M` yields

```math
P(\omega\in B\mid A)
=
\frac{E_\mu[\mathbf 1_B S/M]}{m/M}
=
\frac{E_\mu[\mathbf 1_B S]}{m}
=
\mu^{FP}(B).
```

This is exact. `QED`

### Interpretation

At a fixed base law and fixed bounded weight, the abstract first-person law is therefore distributionally identical to a classical data-generating process in which trajectories are recorded with state-dependent probability `S/M` and analysis conditions on being recorded.

The equality is a probability-law equivalence. It is **not** a claim that the physical mechanism generating accessibility is classical, causal selection, or an actual laboratory recording process.

## Exact general record-multiplicity representation

The boundedness assumption is not needed if ordinary selection is allowed to act through the number of records rather than a single binary acceptance event.

### Proposition: every integrable nonnegative weight is a classical size-biased record law

On an augmented classical model, let the conditional number of records satisfy

```math
N\mid\omega
\sim
\mathrm{Poisson}(cS(\omega)),
```

where `c>0` is any constant that makes the Poisson mean dimensionless. With dimensionless `S`, take `c=1`.

Define the record-size-biased law of `omega` by

```math
\mu^{record}(B)
=
\frac{E[N\mathbf 1_B]}{E[N]}.
```

Then

```math
\mu^{record}(B)
=
\mu^{FP}(B)
```

for every measurable `B`.

### Proof

By iterated expectation,

```math
E[N\mid\omega]
=
cS(\omega).
```

Hence

```math
E[N]
=
cE_\mu[S]
=
cm,
```

and

```math
E[N\mathbf 1_B]
=
E_\mu\left[
\mathbf 1_B E[N\mid\omega]
\right]
=
cE_\mu[\mathbf 1_B S].
```

Therefore

```math
\mu^{record}(B)
=
\frac{cE_\mu[\mathbf 1_B S]}{cm}
=
\mu^{FP}(B).
```

`QED`

This is the standard size-bias intuition in explicit measure form: if states produce different expected numbers of records and one samples a random record from the pooled record population, states are represented in proportion to their expected record multiplicity.

## Unbounded weights are limits of binary ascertainment laws

A single Bernoulli acceptance probability proportional to `S` requires a finite bound. For a general integrable nonnegative `S`, define

```math
S_n=\min(S,n),
\qquad
m_n=E_\mu[S_n],
```

and

```math
\mu_n(B)
=
\frac{E_\mu[\mathbf 1_B S_n]}{m_n}.
```

Each `mu_n` has the exact bounded binary-selection representation above. Moreover,

```math
\|\mu_n-\mu^{FP}\|_{TV}
\le
\frac{m-m_n}{m}
\longrightarrow 0.
```

### Proof

For the convention

```math
\|P-Q\|_{TV}
=
\frac12\int\left|\frac{dP}{d\mu}-\frac{dQ}{d\mu}\right|d\mu,
```

we have

```math
2\|\mu_n-\mu^{FP}\|_{TV}
=
E_\mu\left|
\frac{S_n}{m_n}-\frac{S}{m}
\right|.
```

Using `S_n<=S`,

```math
E_\mu\left|
\frac{S_n}{m_n}-\frac{S}{m}
\right|
\le
E_\mu\left[
S_n\left|\frac1{m_n}-\frac1m\right|
\right]
+
\frac{E_\mu[S-S_n]}{m}.
```

Because `m_n<=m`, the first term equals

```math
m_n\left(\frac1{m_n}-\frac1m\right)
=
\frac{m-m_n}{m},
```

and the second term is also

```math
\frac{m-m_n}{m}.
```

Thus

```math
\|\mu_n-\mu^{FP}\|_{TV}
\le
\frac{m-m_n}{m}.
```

By monotone convergence, `m_n` increases to `m`, so the right-hand side tends to zero. `QED`

## Observable non-identifiability corollary

Let `X` be any measurable observable. Under the weighted model,

```math
P_{FP}(X\in D)
=
\frac{E_\mu[\mathbf 1_{\{X\in D\}}S]}{E_\mu[S]}.
```

Therefore the first-person observable law depends only on the base joint law of `(X,S)`.

If two candidate mechanisms---for example, an Everett accessibility interpretation and a classical ascertainment model---induce the same base joint law of `(X,S)`, then they induce the same first-person law of `X`. No statistic computed only from that observer-conditioned `X` distribution can distinguish the mechanisms.

This is an **observational equivalence statement**, not a universal causal-equivalence theorem. Candidate models may still be distinguished by:

- independent physical constraints on what `S` is allowed to be;
- interventions that change policy or accessibility in ways the competing models predict differently;
- sequential records whose transition laws differ under the candidate mechanisms;
- observables not included in the matched joint law;
- a physical derivation tying `S` to independently measured quantum quantities.

## Behavior-matched classical null

For every fixed policy with bounded `S_pi`, the first proposition supplies an exact behavior-matched classical null:

```math
P(A_\pi\mid\omega)
=
\frac{S_\pi(\omega)}{M_\pi}.
```

Conditioned on `A_pi`, this null reproduces exactly the same weighted trajectory law as `mu_pi^{FP}`.

For general integrable `S_pi`, the record-multiplicity construction gives an exact classical size-biased null, and bounded truncations give binary-selection nulls converging in total variation.

Consequently, observing a first-person uplift, positive innovation selection, or a recursively favorable observer history does not by itself identify an Everettian bridge. A bridge model must either derive `S_pi` from independent physics or make additional observable / interventional predictions that survive comparison with these behavior-matched classical selection nulls.

## Context-indexed representability no-go

A natural response to single-context non-identifiability is to vary policy, intervention, experimental setting, or observer context and compare several observer-conditioned distributions. This does **not** identify the physical mechanism if the classical null is allowed an unrestricted context-dependent selection channel.

Let `C` be any index set. For each `c in C`, let `mu_c` be a base probability measure on the same measurable space `(Omega,F)`, and let `Q_c` be any target observer-conditioned law satisfying

```math
Q_c\ll\mu_c.
```

Let

```math
r_c
=
\frac{dQ_c}{d\mu_c}.
```

Choose the usual finite nonnegative version of the Radon--Nikodym density; because `Q_c` is a probability measure,

```math
r_c\ge0,
\qquad
E_{\mu_c}[r_c]=1,
```

and `r_c<infinity` `mu_c`-almost surely.

### Proposition: arbitrary context-specific observer laws are classically selection-representable

For every context `c`, define a classical record count by

```math
N_c\mid(\omega,c)
\sim
\mathrm{Poisson}(r_c(\omega)).
```

Then the record-size-biased law in context `c` is exactly `Q_c`:

```math
\frac{E_{\mu_c}[N_c\mathbf 1_B]}{E_{\mu_c}[N_c]}
=
Q_c(B).
```

If `r_c` is essentially bounded by `M_c`, the same target law also has an exact Bernoulli ascertainment representation with

```math
P(A_c\mid\omega,c)
=
\frac{r_c(\omega)}{M_c}.
```

### Proof

For the Poisson construction,

```math
E[N_c\mid\omega,c]
=
r_c(\omega),
```

so

```math
E_{\mu_c}[N_c]
=
E_{\mu_c}[r_c]
=
1,
```

and

```math
E_{\mu_c}[N_c\mathbf 1_B]
=
E_{\mu_c}[r_c\mathbf 1_B]
=
Q_c(B).
```

The bounded Bernoulli representation follows from the earlier bounded-selection proposition with weight `r_c`. `QED`

### Consequence

A finite, countable, or otherwise indexed family of observer-conditioned laws is **not** mechanism-identifying merely because it is observed under multiple contexts. If the competing classical model may choose a separate selection function in each context, it can reproduce every absolutely continuous target law context by context.

Therefore "run more interventions" is not by itself an escape from the selection-equivalence null. Identification requires a **cross-context restriction** that is imposed before observing the selected laws.

## A restricted null: context-invariant selection

The no-go above is intentionally strong because it grants the classical null the same freedom to change its selection rule across contexts that an unconstrained accessibility model has. A useful comparison must restrict that freedom for an independent reason.

One simple restricted null assumes a single nonnegative selection function

```math
a:\Omega\to[0,\infty)
```

is used in every context, with

```math
0<E_{\mu_c}[a]<\infty
```

for each `c`. The selected law is then

```math
Q_c(B)
=
\frac{E_{\mu_c}[\mathbf 1_Ba]}{E_{\mu_c}[a]}.
```

Assume the base laws `mu_c` are all equivalent to a common reference probability measure `lambda`, so their Radon--Nikodym densities and the context-specific ratios below are comparable on a common support. Define

```math
r_c
=
\frac{dQ_c}{d\mu_c}.
```

### Proposition: shared selection implies proportional Radon--Nikodym densities

Under the context-invariant selection null,

```math
r_c(\omega)
=
\frac{a(\omega)}{Z_c},
\qquad
Z_c=E_{\mu_c}[a].
```

Hence for any two contexts `c,d`, wherever the densities are positive,

```math
\frac{r_c(\omega)}{r_d(\omega)}
=
\frac{Z_d}{Z_c},
```

which is constant in `omega` `lambda`-almost everywhere on the common positive-density support.

Conversely, if there is a nonnegative measurable function `a` and positive constants `Z_c` such that

```math
r_c=\frac{a}{Z_c}
```

`lambda`-almost everywhere for every context, then the family is generated by that context-invariant selection function; normalization of each `Q_c` forces `Z_c=E_{\mu_c}[a]`.

### Proof

By the definition of the selected law,

```math
dQ_c
=
\frac{a}{E_{\mu_c}[a]}
\,d\mu_c.
```

Therefore

```math
r_c
=
\frac{dQ_c}{d\mu_c}
=
\frac{a}{Z_c}.
```

Taking the ratio for two contexts gives the stated constant. Conversely, if `r_c=a/Z_c`, then

```math
1
=
E_{\mu_c}[r_c]
=
\frac{E_{\mu_c}[a]}{Z_c},
```

so `Z_c=E_{\mu_c}[a]`, and substitution recovers the selected-law formula. `QED`

### Mathematical falsification rule for the restricted null

If two contexts have a nonconstant cross-context ratio

```math
\frac{r_c(\omega)}{r_d(\omega)},
```

on a set of positive `lambda` measure where both densities are positive, then **no context-invariant classical selection function `a(omega)` can generate both selected laws** under the stated common-support assumptions.

This does not identify an Everett mechanism by itself. It only falsifies that particular restricted classical null. A more flexible context-dependent classical selection model can still fit the laws unless additional restrictions are independently justified.

### Operational requirements before calling this an empirical test

The density-ratio restriction is mathematically testable only on a state space that can actually be aligned across contexts. To turn it into an empirical test, additional identification work is required:

1. the relevant base law `mu_c` must be independently known or estimable in each context;
2. the observer-conditioned law `Q_c` must be estimable on a common observable state space, or a justified mapping from context-specific observations to that common space must be supplied;
3. the Radon--Nikodym ratios `r_c=dQ_c/dmu_c` must therefore be statistically identifiable from the available data;
4. the claim that the same `a(omega)` should hold across contexts must be independently motivated rather than chosen because it is easy to reject.

If `omega` is latent and only a projection `X_c=T_c(omega)` is observed, nonconstant latent density ratios need not remain detectable after projection. Conversely, a difference between projected observer-conditioned laws can arise solely because `T_c` or the base law changes, even when the latent selection rule is shared. Thus the proposition supplies a **structural restriction**, not an automatic experimental procedure.

In the special case where the same base law `mu` applies to every context and the same latent state space is observed, proportionality is even stronger: because every `r_c` integrates to one under the same `mu`, a constant ratio implies

```math
r_c=r_d
\qquad \mu\text{-a.s.}
```

for every pair of contexts under a shared selection rule. This statement concerns the selected law on the common latent/base state; policy-dependent outcome maps may still produce different observed outcome distributions from that same selected latent law.

## Numerical two-state example

Let

```math
\Omega=\{L,H\}
```

and use the same base law in two contexts:

```math
\mu_0(L)=\mu_0(H)=\frac12,
\qquad
\mu_1(L)=\mu_1(H)=\frac12.
```

Suppose the observer-conditioned laws are

```math
Q_0(L)=\frac23,
\qquad
Q_0(H)=\frac13,
```

and

```math
Q_1(L)=\frac13,
\qquad
Q_1(H)=\frac23.
```

Then

```math
r_0(L)=\frac43,
\qquad
r_0(H)=\frac23,
```

while

```math
r_1(L)=\frac23,
\qquad
r_1(H)=\frac43.
```

Thus

```math
\frac{r_0(L)}{r_1(L)}=2,
\qquad
\frac{r_0(H)}{r_1(H)}=\frac12.
```

The ratio is not constant, so a **single** context-invariant selection weight cannot produce both laws. Nevertheless, the unrestricted context-dependent classical null fits them exactly by using `a_0=r_0` and `a_1=r_1` or the corresponding record-multiplicity constructions.

This example isolates the identification problem: more contexts help only when the competing model is forced to share structure across those contexts.

## QBS implication across policies

In the QBS notation, policy or intervention can be treated as context `c=pi`. If accessibility is allowed to be an arbitrary policy-dependent function `S_pi`, then a classical null with an equally arbitrary policy-dependent selection function can reproduce the entire family of first-person laws exactly.

Therefore an empirically meaningful Everett-QBS bridge needs a **predeclared cross-policy law** for `S_pi`, not merely one fitted accessibility function per policy. Candidate identifying restrictions could come from:

- a physical functional dependence of `S_pi` on independently measured quantum/observer variables;
- invariance constraints that tie accessibility across equivalent policy implementations;
- a sequential state-transition law that restricts how `S_pi` can change over time;
- interventions that change policy while leaving the independently measured accessibility mechanism fixed;
- a low-dimensional parametric or structural model whose parameters are shared across contexts and estimated out of sample.

The scientific target is then not "does weighting occur?" but "does one predeclared cross-context accessibility law predict observer-conditioned data better than restricted classical alternatives without context-by-context retuning?"

## Relation to selection-model identifiability

This context-indexed boundary is consistent with the broader sample-selection and missing-data literature: nonrandom selection mechanisms are generally not identified from selected data without additional assumptions, exclusion restrictions, instruments, parametric structure, auxiliary variables, or other independently motivated information.

Heckman's sample-selection formulation is a canonical econometric example of how nonrandom observation changes behavioral inference. More directly on identification, modern missing-not-at-random work shows that even restrictive parametric missingness models can remain unidentified without additional outcome-model assumptions, while auxiliary or shadow variables can restore identification under stated conditions. These literatures support the methodological boundary here; they do not establish the QBS-specific propositions, whose proofs are given above.

The QBS-specific contribution here is to state that identification burden directly in the policy-dependent observer-accessibility notation used by the repository.

## Relation to weighted-distribution prior art

This boundary is classical rather than uniquely quantum. Fisher's 1934 ascertainment analysis, Rao's 1965 work on distributions arising from methods of ascertainment, and Patil--Rao's 1978 weighted-distribution framework all study how unequal observation / recording propensities alter the distribution of encountered data. Patil and Rao explicitly allow general weight functions not necessarily bounded by one.

The QBS-specific research question is therefore **not** whether normalized weighting can alter an encountered distribution. The remaining distinctive question is whether recognition-dependent policy, trajectory generation, and observer accessibility can be coupled in a useful model, whether a proposed accessibility map has an independently defensible Everettian physical origin, and whether that physical model imposes testable cross-context restrictions that survive classical selection alternatives.

## ERROR CHECK

1. **Normalization:** `m>0` is required. If `E[S]=0`, the first-person law is undefined.
2. **Support:** because `mu^FP << mu`, weighting cannot create base-null events. The selection representations preserve this.
3. **Bounded binary selection:** `S/M` is a valid probability only when `0<=S<=M` almost surely.
4. **General exact representation:** the Poisson record construction requires only `E[S]<infinity`; it does not require bounded `S`.
5. **TV approximation:** the truncation proof uses `S_n<=S` and monotone convergence; it does not assume a finite second moment.
6. **Units:** an acceptance probability must be dimensionless. Rescaling `S` by a positive constant leaves the weighted law unchanged.
7. **Mechanism versus law:** equality of probability laws does not imply equality of physical mechanisms or causal graphs.
8. **Single-context identifiability:** matching only the marginal law of `X` or only the marginal law of `S` is insufficient; the corollary requires the same relevant joint law, or directly the same weighted observable law.
9. **Multiple contexts:** observing several selected laws still does not identify a mechanism if the null may choose a separate selection channel in every context.
10. **Shared-null mathematics:** the constant density-ratio condition requires a common support/reference measure so `r_c/r_d` is meaningfully comparable. Failure falsifies only the context-invariant selection null, not every classical selection model.
11. **Shared-null empirics:** the density-ratio restriction is not operational unless the base and selected laws are identifiable on a common observable state space. Latent-state violations can disappear under projection.
12. **Policy dependence:** allowing arbitrary `S_pi` in the QBS model while forbidding policy dependence in the classical null would create an asymmetric comparison. Identifying restrictions must be independently motivated and applied fairly.
13. **Everett boundary:** none of these classical representations derives or refutes an Everett accessibility mechanism. They establish stringent nulls and show what extra cross-context structure a specifically Everettian interpretation must supply.

## Status

**EXACT UNNUMBERED BOUNDARY RESULTS. THE ABSTRACT NORMALIZED ACCESSIBILITY LAW HAS CLASSICAL ASCERTAINMENT / SIZE-BIAS REPRESENTATIONS. AN ARBITRARY FAMILY OF CONTEXT-SPECIFIC WEIGHTED LAWS IS ALSO CLASSICALLY REPRESENTABLE IF THE NULL MAY RETUNE SELECTION BY CONTEXT. IDENTIFICATION REQUIRES PREDECLARED CROSS-CONTEXT RESTRICTIONS OR INDEPENDENT PHYSICAL INFORMATION; TURNING SUCH RESTRICTIONS INTO EMPIRICAL TESTS FURTHER REQUIRES IDENTIFIABLE BASE/SELECTED LAWS ON A COMMON STATE SPACE.**