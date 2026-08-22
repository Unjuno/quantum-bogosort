# Selection-Equivalence and Identifiability Boundary

This note records an **unnumbered exact boundary result** for the QBS weighted measure. It does not add `T6`, `S2.14`, or `E6`.

The purpose is adversarial: before assigning any specifically Everettian meaning to observer accessibility, ask how much of the first-person law can already be represented by ordinary classical ascertainment, record multiplicity, or selection conditioning.

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
P_{FP}(X\in C)
=
\frac{E_\mu[\mathbf 1_{\{X\in C\}}S]}{E_\mu[S]}.
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

## Relation to weighted-distribution prior art

This boundary is classical rather than uniquely quantum. Fisher's 1934 ascertainment analysis, Rao's 1965 work on distributions arising from methods of ascertainment, and Patil--Rao's 1978 weighted-distribution framework all study how unequal observation / recording propensities alter the distribution of encountered data. Patil and Rao explicitly allow general weight functions not necessarily bounded by one.

The QBS-specific research question is therefore **not** whether normalized weighting can alter an encountered distribution. The remaining distinctive question is whether recognition-dependent policy, trajectory generation, and observer accessibility can be coupled in a useful model, and whether any proposed accessibility map has an independently defensible Everettian physical origin.

## ERROR CHECK

1. **Normalization:** `m>0` is required. If `E[S]=0`, the first-person law is undefined.
2. **Support:** because `mu^FP << mu`, weighting cannot create base-null events. The selection representations preserve this.
3. **Bounded binary selection:** `S/M` is a valid probability only when `0<=S<=M` almost surely.
4. **General exact representation:** the Poisson record construction requires only `E[S]<infinity`; it does not require bounded `S`.
5. **TV approximation:** the truncation proof uses `S_n<=S` and monotone convergence; it does not assume a finite second moment.
6. **Units:** an acceptance probability must be dimensionless. Rescaling `S` by a positive constant leaves the weighted law unchanged.
7. **Mechanism versus law:** equality of probability laws does not imply equality of physical mechanisms or causal graphs.
8. **Identifiability:** matching only the marginal law of `X` or only the marginal law of `S` is insufficient; the corollary requires the same relevant joint law, or directly the same weighted observable law.
9. **Everett boundary:** none of these classical representations derives or refutes an Everett accessibility mechanism. They establish a stringent null that any specifically Everettian interpretation must exceed.

## Status

**EXACT UNNUMBERED BOUNDARY RESULT. THE ABSTRACT NORMALIZED ACCESSIBILITY LAW HAS CLASSICAL ASCERTAINMENT / SIZE-BIAS REPRESENTATIONS. THE WEIGHTED OBSERVABLE LAW ALONE DOES NOT IDENTIFY A PHYSICAL EVERETT BRIDGE.**
