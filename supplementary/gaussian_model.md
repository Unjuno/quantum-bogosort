# Gaussian Minimal Model

## Motivation

The Gaussian toy model provides a closed-form bridge between score/outcome correlation, downweighting strength, and first-person mean shift.

## Definitions

Let outcome `L` and score `Y` be jointly standard normal with correlation `rho`.

Accessibility is:

$$
S
=
1
$$

for:

$$
Y\ge0,
$$

and:

$$
S
=
\lambda
$$

for:

$$
Y<0.
$$

## Result

The first-person mean outcome is:

$$
E_{FP}[L]
=
\frac{2(1-\lambda)\rho}
{(1+\lambda)\sqrt{2\pi}}.
$$

Under the provisional binary execution/leakage parameterization:

$$
\lambda
=
1-q(1-\alpha),
$$

this becomes:

$$
E_{FP}[L]
=
\frac{2q(1-\alpha)\rho}
{[2-q(1-\alpha)]\sqrt{2\pi}}.
$$

## Interpretation

The expression makes three model-level facts explicit:

- zero score/outcome correlation gives zero mean shift;
- no downweighting gives zero mean shift;
- stronger positive alignment and stronger selectivity increase the mean shift within this toy model.

## Experiment

Monte Carlo checks matched the analytic expression in exploratory simulations.

## Limitations

The closed form depends on joint Gaussianity and a two-level accessibility rule. It is not a universal QBS formula and is not an Everett prediction.

## Status

**EXACT for the stated Gaussian toy model.**
