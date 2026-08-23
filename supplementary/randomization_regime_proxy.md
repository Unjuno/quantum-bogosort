# Randomization-regime and proxy-refinement diagnostic

This unnumbered supplementary note extends the randomized-context diagnostic. It is not T6, S2.14, E6, or evidence for an Everett/QBS physical bridge.

## H — hypotheses

Let `R` denote a predeclared randomization regime with known context probability

```math
P(C=1\mid R=r)=p_r,
\qquad
0<p_r<1.
```

Let `Omega` be the pre-treatment latent state, let `Z=T(Omega)` be an observed pre-treatment proxy, and assume

```math
C\perp\!\!\!\perp \Omega\mid R.
```

For independent experimental units, binary inclusion is

```math
A\mid(C=c,\Omega=\omega,R=r)
\sim
\mathrm{Bernoulli}(s_{c,r}(\omega)).
```

Two nested nulls are relevant.

1. **shared selector**:

```math
s_{0,r}(\omega)=s_{1,r}(\omega)=s(\omega)
```

for every regime;
2. **regime-invariant context selector**:

```math
s_{c,r}(\omega)=s_c(\omega),
```

which allows context-dependent selection but forbids retuning the selector when the randomization probability changes.

## T — exact structural consequences

Define, for an observed proxy value `z`,

```math
m_c(z)
=
E[s_c(\Omega)\mid Z=z].
```

Under the regime-invariant context-selector null,

```math
P(C=1\mid A=1,Z=z,R=r)
=
\frac{p_r m_1(z)}{p_r m_1(z)+(1-p_r)m_0(z)}.
```

Therefore

```math
\mathrm{logit}\,P(C=1\mid A=1,Z=z,R=r)
-
\mathrm{logit}\,p_r
=
\log\frac{m_1(z)}{m_0(z)},
```

which is independent of the regime `r`.

Under the stronger shared-selector null, `m_1(z)=m_0(z)`, so the offset is exactly zero:

```math
P(C=1\mid A=1,Z=z,R=r)=p_r.
```

Thus varying the known assignment odds gives two distinct checks:

- zero offset rejects the shared-selector null when violated;
- regime invariance rejects selector retuning when the selected log-odds offset changes with `r`.

### Projection limit

Multiple randomization regimes do **not** eliminate the projection problem. If

```math
E[s_1(\Omega)\mid Z=z]
=
E[s_0(\Omega)\mid Z=z]
```

for every observed `z`, then the selected context probability equals the randomized probability in every regime even when `s_1` and `s_0` differ strongly on latent states.

An informative proxy can refine the sigma-field and break that equality. This motivates the proxy-accuracy stress test below.

## D — diagnostics

The deterministic script [`randomization_regime_proxy_stress.py`](randomization_regime_proxy_stress.py) uses three assignment regimes:

```text
p_r in {0.2, 0.5, 0.8}
```

and a binary latent state `L` with a noisy observed proxy `Z` satisfying

```math
P(Z=L)=q.
```

It compares four mechanisms:

- `shared_null`: nontrivial latent-state selection shared across contexts and regimes;
- `stable_context`: context-dependent selection with one regime-invariant odds offset;
- `regime_retuned`: context selection explicitly changes with the randomization regime;
- `projection_blind`: strong context-dependent latent selection whose marginal effect vanishes when `q=1/2`.

### Shared-selector test

Within each predeclared `(r,z)` cell, the shared-selector null implies

```math
K_{r,z}\mid n_{r,z}
\sim
\mathrm{Binomial}(n_{r,z},p_r).
```

The script uses exact two-sided binomial p-values and Bonferroni correction over the six predeclared cells. Under the stated iid randomized binary-inclusion design, this gives finite-sample family-wise type-I control.

### Regime-invariance diagnostic

For each `z`, the regime-invariant null has one common log-odds offset. The script fits that scalar offset and compares it with the saturated three-regime model by a likelihood-ratio deviance. With three regimes, the per-stratum reference distribution is asymptotic chi-square with two degrees of freedom; two proxy strata are Bonferroni corrected.

This second test is an asymptotic stress diagnostic, not an exact finite-sample certificate.

## C — deterministic stress results

Seed `20260823`, 5,000 Monte Carlo repetitions per cell:

| mechanism | gamma | proxy accuracy | selected n / regime | shared-null reject | regime-retuning reject |
|---|---:|---:|---:|---:|---:|
| shared null | 0.00 | 0.80 | 500 | 0.0478 | 0.0518 |
| stable context effect | 0.40 | 0.80 | 500 | 0.9906 | 0.0560 |
| regime-retuned effect | 0.40 | 0.80 | 500 | 0.9998 | 1.0000 |
| projection blind | 0.40 | 0.50 | 500 | 0.0434 | 0.0514 |
| projection blind | 0.40 | 0.55 | 500 | 0.1760 | 0.0530 |
| projection blind | 0.40 | 0.60 | 200 | 0.2512 | 0.0508 |
| projection blind | 0.40 | 0.60 | 500 | 0.6210 | 0.0556 |
| projection blind | 0.40 | 0.60 | 1000 | 0.9434 | 0.0502 |
| projection blind | 0.40 | 0.65 | 500 | 0.9648 | 0.0486 |
| projection blind | 0.40 | 0.70 | 500 | 1.0000 | 0.0508 |

Interpretation:

1. the exact shared-selector test remains near nominal size under a nontrivial shared selector;
2. a stable context effect is detected by the zero-offset test while the regime-retuning diagnostic remains near nominal size;
3. explicit regime retuning is detected by both diagnostics and especially by the homogeneity test;
4. changing assignment probabilities alone does not reveal a projection-blind latent violation;
5. adding an informative pre-treatment proxy restores power continuously as the proxy becomes more informative;
6. for a fixed imperfect proxy, increasing selected sample size increases power, but cannot solve a truly uninformative projection (`q=1/2`).

## U — unresolved / non-claims

- Rejection of either null does not identify Everett, observer selection, or a QBS physical bridge.
- Failure to reject does not establish shared selection because latent context dependence can remain projection-blind.
- The homogeneity diagnostic uses an asymptotic chi-square reference; its Monte Carlo calibration here is a stress check, not a universal finite-sample theorem.
- The exact binomial guarantee assumes independent experimental units, known randomization probabilities, pre-treatment proxy strata, and binary inclusion. It does not automatically transfer to dependent duplicate-record or Poisson multiplicity sampling.
- Proxy refinement improves identifiability only to the extent that the proxy exposes latent heterogeneity relevant to the selector ratio.

## Error check

The result is deliberately one-sided. Multiple assignment regimes identify a **regime-invariance restriction**, not an arbitrary latent selector. An informative proxy can shrink the observational equivalence class, but no finite proxy family is assumed to recover the full latent state.
