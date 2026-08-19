# Repeated Filtering and Accessible-Measure Decay

## Motivation

Repeated QBS-style downweighting raises two separate questions:

1. how the normalized first-person value changes with selectivity;
2. how much total accessible measure remains.

These must not be conflated.

## Definitions

Let `N_B` be a finite nonnegative integer-valued count of adverse triggers along a history. Define repeated accessibility by:

```math
S
=
\lambda^{N_B},
```

with the downweighting interpretation restricted to:

```math
0<\lambda\le1.
```

The weighted value is:

```math
V(\lambda)
=
\frac{E[U\lambda^{N_B}]}{E[\lambda^{N_B}]}.
```

Because `N_B<∞` almost surely and `lambda>0`, the denominator is strictly positive whenever the displayed expectations are finite.

## Sensitivity identity and regularity domain

Fix a positive `lambda_0`. Assume `V(lambda)` is considered on an open positive neighborhood of `lambda_0` and that differentiation may be interchanged with both expectations there. A convenient sufficient formulation is that the numerator and denominator derivatives are dominated by integrable random variables on that neighborhood; in particular the quantities

```math
E[|U|N_B\lambda^{N_B}],
\qquad
E[N_B\lambda^{N_B}]
```

must be finite at the evaluation point, in addition to the weighted-value numerator being finite.

Then differentiating with respect to log selectivity gives:

```math
\boxed{
\frac{dV}{d\log\lambda}
=
\mathrm{Cov}_{\lambda}(U,N_B)
}.
```

Here the covariance is evaluated under the normalized measure induced by the current value of `lambda`:

```math
E_\lambda[X]
=
\frac{E[X\lambda^{N_B}]}{E[\lambda^{N_B}]}.
```

Indeed:

```math
\lambda\frac{d}{d\lambda}E[U\lambda^{N_B}]
=
E[UN_B\lambda^{N_B}],
```

and similarly for the denominator, so the quotient rule gives the weighted covariance.

For the QBS downweighting family `0<lambda<=1`, the formula applies at interior points. At `lambda=1`, if the family is intentionally restricted to `lambda<=1`, the corresponding statement is the left derivative provided the same dominated-differentiation conditions hold from below.

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

The derivative identity requires the stated expectation/differentiation regularity; it is not justified merely by writing a formal derivative of an arbitrary unbounded history model. The physical meaning of total accessible measure depends on the Everett bridge and is not established by the mathematical identity.

## Status

**SENSITIVITY IDENTITY EXACT UNDER THE EXPLICIT DOMINATED-DIFFERENTIATION/FINITE-MOMENT CONDITIONS. MEASURE-DECAY BEHAVIOR SIMULATION-SUPPORTED IN TOY MODELS.**
