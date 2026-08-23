# Randomization-regime and proxy-refinement diagnostic

This unnumbered supplementary note extends the randomized-context diagnostic. It is not T6, S2.14, E6, or evidence for an Everett/QBS physical bridge.

## H — hypotheses

Let `R` denote a predeclared randomization regime with known context probability

```math
P(C=1\mid R=r)=p_r,
\qquad
0<p_r<1.
```

Let `Omega` be the pre-treatment latent state and `Z=T(Omega)` an observed pre-treatment proxy. The within-regime assignment assumption is

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
s_{0,r}(\omega)=s_{1,r}(\omega)=s_r(\omega)
```

for every regime;
2. **regime-invariant context selector**:

```math
s_{c,r}(\omega)=s_c(\omega).
```

The first null may still allow the common selector to vary across regimes. The second forbids context-selector retuning when the randomization probability changes.

For the stronger claim that a **nonzero selected log-odds offset is common across regimes**, the experiment additionally requires the pre-treatment latent distribution to be regime-invariant. A sufficient design condition is

```math
R\perp\!\!\!\perp \Omega.
```

More generally, it is enough that the conditional selector-mean ratio defined below is invariant in `r`.

## T — exact structural consequences

### Shared-selector preservation requires only within-regime randomization

Under the shared-selector null and `C` randomized independently of `Omega` within each regime,

```math
P(C=1\mid A=1,Z=z,R=r)=p_r.
```

The regime may have a different latent-state distribution or a different common selector; those factors cancel because inclusion does not distinguish `C=0` from `C=1` within the regime.

### Common nonzero offset needs a regime-stable latent distribution

Under the regime-invariant context-selector null, define the regime-specific proxy-level selector means

```math
m_{c,r}(z)
=
E[s_c(\Omega)\mid Z=z,R=r].
```

Then always

```math
P(C=1\mid A=1,Z=z,R=r)
=
\frac{p_r m_{1,r}(z)}{p_r m_{1,r}(z)+(1-p_r)m_{0,r}(z)},
```

and hence

```math
\mathrm{logit}\,P(C=1\mid A=1,Z=z,R=r)
-
\mathrm{logit}\,p_r
=
\log\frac{m_{1,r}(z)}{m_{0,r}(z)}.
```

Thus a regime-invariant selector alone does **not** guarantee a common nonzero offset if the pre-treatment population differs across regimes.

If, in addition, `R` is independent of `Omega` and `Z=T(Omega)`, then

```math
m_{c,r}(z)=m_c(z)
=
E[s_c(\Omega)\mid Z=z],
```

so

```math
\mathrm{logit}\,P(C=1\mid A=1,Z=z,R=r)
-
\mathrm{logit}\,p_r
=
\log\frac{m_1(z)}{m_0(z)},
```

which is independent of `r`.

Therefore varying known assignment odds gives two distinct checks:

- zero offset tests the shared-selector null using only within-regime randomization;
- common nonzero offset tests the stronger combination of regime-invariant context selection **and** regime-stable pre-treatment composition.

### Projection limit

Multiple randomization regimes do **not** eliminate the projection problem. If

```math
E[s_1(\Omega)\mid Z=z,R=r]
=
E[s_0(\Omega)\mid Z=z,R=r]
```

for every observed `(z,r)`, then the selected context probability equals the randomized probability in every regime even when `s_1` and `s_0` differ strongly on latent states.

An informative proxy can refine the sigma-field and break that equality. This motivates the proxy-accuracy stress test below.

For the projection-blind toy model used in the script, `L` is Bernoulli one-half, `P(Z=L)=q`, and the selectors are

```math
s_0(0)=0.8,
\quad
s_0(1)=0.2,
\quad
s_1(0)=0.2,
\quad
s_1(1)=0.8.
```

For `Z=1`, the exact selector-mean ratio is

```math
\frac{m_1(1)}{m_0(1)}
=
\frac{0.2+0.6q}{0.8-0.6q}.
```

It equals one at `q=1/2` and moves monotonically away from one as the proxy becomes informative, explaining the observed power recovery.

## D — diagnostics

The deterministic script [`randomization_regime_proxy_stress.py`](randomization_regime_proxy_stress.py) uses three assignment regimes:

```text
p_r in {0.2, 0.5, 0.8}
```

with the same latent-state law in every regime except for the explicit `composition_shift` countercontrol. The main stable-context simulations therefore satisfy the stronger `R`-independence condition above. A binary latent state `L` has a noisy observed proxy `Z` satisfying

```math
P(Z=L)=q.
```

The script compares five mechanisms:

- `shared_null`: nontrivial latent-state selection shared across contexts and regimes;
- `stable_context`: context-dependent selection with one regime-invariant odds offset and stable composition;
- `regime_retuned`: context selection explicitly changes with the randomization regime;
- `projection_blind`: strong context-dependent latent selection whose marginal effect vanishes when `q=1/2`;
- `composition_shift`: selector functions are fixed across regimes but the latent-state prevalence changes from `0.2` to `0.5` to `0.8`, demonstrating that the common-offset diagnostic also reacts to composition drift.

### Shared-selector test

Within each predeclared `(r,z)` cell, the shared-selector null implies

```math
K_{r,z}\mid n_{r,z}
\sim
\mathrm{Binomial}(n_{r,z},p_r).
```

The script uses exact two-sided binomial p-values and Bonferroni correction over the six predeclared cells. Under the stated iid randomized binary-inclusion design, this gives finite-sample family-wise type-I control.

### Regime-invariance diagnostic

For each `z`, under the **combined** null of regime-invariant context selection and regime-stable pre-treatment composition, the selected data have one common log-odds offset. The script fits that scalar offset and compares it with the saturated three-regime model by a likelihood-ratio deviance. With three regimes, the per-stratum reference distribution is asymptotic chi-square with two degrees of freedom; two proxy strata are Bonferroni corrected.

This second test is an asymptotic stress diagnostic, not an exact finite-sample certificate. Rejection can be caused either by selector retuning or by an unmodeled regime shift in the pre-treatment latent distribution.

## C — deterministic stress results

Seed `20260823`, 5,000 Monte Carlo repetitions per cell:

| mechanism | gamma | proxy accuracy | selected n / regime | shared-null reject | common-offset reject |
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
| composition shift, fixed selector | 0.40 | 0.80 | 500 | 1.0000 | 0.9854 |

Interpretation:

1. the exact shared-selector test remains near nominal size under a nontrivial shared selector;
2. a stable context effect is detected by the zero-offset test while the common-offset diagnostic remains near nominal size;
3. explicit regime retuning is detected by both diagnostics and especially by the common-offset test;
4. changing assignment probabilities alone does not reveal a projection-blind latent violation;
5. adding an informative pre-treatment proxy restores power continuously as the proxy becomes more informative;
6. for a fixed imperfect proxy, increasing selected sample size increases power, but cannot solve a truly uninformative projection (`q=1/2`);
7. the composition-shift countercontrol strongly rejects the common-offset restriction even though the selector functions themselves are fixed across regimes, confirming that composition stability is an essential identifying assumption rather than a cosmetic one.

A separate calibration pass at selected `n` per regime `100, 200, 500, 1000` gave common-offset diagnostic rejection rates approximately `4.7%–6.0%` under the tested stable-composition nulls. This is only a Monte Carlo calibration check; the diagnostic remains classified as asymptotic.

## U — unresolved / non-claims

- Rejection of either null does not identify Everett, observer selection, or a QBS physical bridge.
- Failure to reject does not establish shared selection because latent context dependence can remain projection-blind.
- The homogeneity diagnostic uses an asymptotic chi-square reference; its Monte Carlo calibration here is a stress check, not a universal finite-sample theorem.
- The common-offset interpretation requires either `R` independent of the latent pre-treatment state or another justified condition making the proxy-level selector-mean ratio stable across regimes.
- The exact binomial guarantee assumes independent experimental units, known randomization probabilities, pre-treatment proxy strata, and binary inclusion. It does not automatically transfer to dependent duplicate-record or Poisson multiplicity sampling.
- Proxy refinement improves identifiability only to the extent that the proxy exposes latent heterogeneity relevant to the selector ratio.

## Error check

The result is deliberately one-sided. Multiple assignment regimes identify a **joint restriction on selector stability and pre-treatment composition**, not an arbitrary latent selector. An informative proxy can shrink the observational equivalence class, but no finite proxy family is assumed to recover the full latent state.
