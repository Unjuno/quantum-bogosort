# Gaussian Minimal Model

## Motivation

The Gaussian toy model provides a closed-form bridge between score/outcome correlation, downweighting strength, and first-person mean shift.

## Definitions

Let outcome `L` and score `Y` be jointly standard normal with correlation:

```math
-1\le\rho\le1.
```

Accessibility is:

```math
S
=
1
```

for:

```math
Y\ge0,
```

and:

```math
S
=
\lambda
```

for:

```math
Y<0,
```

with:

```math
0\le\lambda\le1.
```

Thus `S` is nonnegative and:

```math
E[S]
=
\frac{1+\lambda}{2}
>0.
```

## Result

The first-person mean outcome is:

```math
E_{FP}[L]
=
\frac{2(1-\lambda)\rho}
{(1+\lambda)\sqrt{2\pi}}.
```

Under the provisional binary execution/leakage parameterization:

```math
\lambda
=
1-q(1-\alpha),
```

with:

```math
0\le q\le1,
\qquad
0\le\alpha\le1,
```

this becomes:

```math
E_{FP}[L]
=
\frac{2q(1-\alpha)\rho}
{[2-q(1-\alpha)]\sqrt{2\pi}}.
```

The parameter bounds imply `0<=lambda<=1` and keep the denominator strictly positive.

## Interpretation

The expression makes three model-level facts explicit:

- zero score/outcome correlation gives zero mean shift;
- no downweighting gives zero mean shift;
- for positive `rho`, stronger positive alignment and stronger selectivity increase the mean shift within this toy model.

For negative `rho`, the same selector shifts the mean in the negative direction, as the exact formula shows.

## Experiment

Monte Carlo checks matched the analytic expression in exploratory simulations.

## Limitations

The closed form depends on joint Gaussianity and a two-level accessibility rule. It is not a universal QBS formula and is not an Everett prediction.

## Status

**EXACT for the stated Gaussian toy model and parameter domain.**
