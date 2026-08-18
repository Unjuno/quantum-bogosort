# Repeated Filtering and Accessible-Measure Decay

## Motivation

Repeated QBS-style downweighting raises two separate questions:

1. how the normalized first-person value changes with selectivity;
2. how much total accessible measure remains.

These must not be conflated.

## Definitions

Let `N_B` count adverse triggers along a history. Define repeated accessibility by:

```math
S
=
\lambda^{N_B},
```

with:

```math
0<\lambda\le1.
```

The weighted value is:

```math
V(\lambda)
=
\frac{E[U\lambda^{N_B}]}{E[\lambda^{N_B}]}.
```

## Result

Differentiating with respect to log selectivity gives:

```math
\frac{dV}{d\log\lambda}
=
\mathrm{Cov}_{\lambda}(U,N_B),
```

where the covariance is evaluated under the normalized measure induced by the current value of `lambda`.

## Accessible-measure boundary

Normalization requires:

```math
E[S]>0.
```

If repeated filtering drives:

```math
E[S]\rightarrow0,
```

then the normalized FP mean may remain finite while effective support and Monte Carlo effective sample size collapse.

At:

```math
E[S]=0,
```

the normalized FP measure is undefined.

## Interpretation

Small accessible measure is a numerical and interpretive boundary, not automatically a negative utility term. The model should report normalized FP effects and surviving accessible measure separately.

## Experiment

Historical recursive and long-horizon simulations numerically verified the sensitivity identity and exponential-like accessible-measure decay under repeated downweighting.

## Limitations

The physical meaning of total accessible measure depends on the Everett bridge and is not established by the mathematical identity.

## Status

**Sensitivity identity EXACT under regularity conditions. Measure-decay behavior SIMULATION-SUPPORTED in toy models.**
