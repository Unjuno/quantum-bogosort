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

Then:

```math
0<S\le1
```

almost surely, so:

```math
0<E[\lambda^{N_B}]\le1.
```

Assume the weighted utility is absolutely integrable at the evaluation point:

```math
E[|U|\lambda^{N_B}]<\infty.
```

The weighted value is therefore finite and defined by:

```math
V(\lambda)
=
\frac{E[U\lambda^{N_B}]}{E[\lambda^{N_B}]}.
```

## Sensitivity identity and regularity domain

Fix a positive `lambda_0`. Assume `V(lambda)` is considered on an open positive neighborhood of `lambda_0` and that differentiation may be interchanged with both expectations there. A convenient sufficient formulation is that the numerator and denominator derivatives are dominated by integrable random variables on that neighborhood; in particular the quantities

```math
E[|U|N_B\lambda^{N_B}],
\qquad
E[N_B\lambda^{N_B}]
```

must be finite at the evaluation point, in addition to:

```math
E[|U|\lambda^{N_B}]<\infty.
```

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

The current downweighting domain `0<lambda<=1` and finite `N_B` imply positive total accessibility for every finite-stage model. More general repeated-filter limits may nevertheless have:

```math
E[S]\rightarrow0.
```

In such a limiting sequence, the normalized FP mean can remain finite while effective support and Monte Carlo effective sample size collapse.

If a generalized selector reaches:

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

## ERROR CHECK

1. For finite `N_B` and `0<lambda<=1`, `lambda^{N_B}` is strictly positive and at most one, so its expectation is automatically finite and positive.
2. The weighted value additionally requires `E[|U|lambda^{N_B}]<infinity`.
3. The derivative identity requires the two weighted derivative moments and a justified differentiation-under-expectation condition in a positive neighborhood.
4. The endpoint `lambda=1` is one-sided when the modeled family is restricted to `lambda<=1`.
5. A zero-accessible-measure statement concerns a generalized/limiting selector; it cannot occur at a finite stage under strictly positive `lambda` and finite `N_B`.
6. The Everett bridge remains separate.

## Status

**SENSITIVITY IDENTITY EXACT UNDER THE EXPLICIT WEIGHTED-VALUE AND DOMINATED-DIFFERENTIATION/FINITE-MOMENT CONDITIONS. MEASURE-DECAY BEHAVIOR SIMULATION-SUPPORTED IN TOY MODELS.**
