# Minimal Binary Soft-QBS Model

## Motivation

The binary model is the smallest example that separates favorable-event prior probability from first-person accessibility weighting.

## Definitions

Let favorable outcomes have prior probability `p`. Give favorable outcomes accessibility weight 1 and unfavorable outcomes accessibility weight `lambda`.

Then:

$$
0\le\lambda\le1.
$$

## Result

The favorable first-person probability is:

$$
p_{FP}
=
\frac{p}{p+(1-p)\lambda}.
$$

If:

$$
0\le\lambda<1
$$

and:

$$
0<p<1,
$$

then:

$$
p_{FP}>p.
$$

## Execution / leakage parameterization

A provisional toy parameterization used in exploratory experiments is:

$$
\lambda
=
1-q(1-\alpha),
$$

where `q` is an execution-strength parameter and `alpha` is residual leakage/accessibility in the downweighted class.

At:

$$
q=0,
$$

we obtain:

$$
\lambda=1,
$$

so there is no weighting effect.

## Interpretation

This model is useful for algebra and intuition, but `alpha` is not treated as a universal physical constant. Its meaning depends on the accessibility mechanism being modeled.

## Limitations

The model has only two outcome classes and does not represent trajectory changes caused by recognition-dependent policy. Those require the general recognition framework.

## Status

**EXACT within the binary weighting model. Physical interpretation OPEN.**
