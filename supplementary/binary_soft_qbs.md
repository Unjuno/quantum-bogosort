# Minimal Binary Soft-QBS Model

## Motivation

The binary model is the smallest example that separates favorable-event prior probability from first-person accessibility weighting.

## Definitions

Let favorable outcomes have prior probability `p`. Give favorable outcomes accessibility weight 1 and unfavorable outcomes accessibility weight `lambda`.

Then:

```math
0\le\lambda\le1.
```

## Result

The favorable first-person probability is:

```math
p_{FP}
=
\frac{p}{p+(1-p)\lambda}.
```

If:

```math
0\le\lambda<1
```

and:

```math
0<p<1,
```

then:

```math
p_{FP}>p.
```

## Execution / leakage parameterization

A provisional toy parameterization used in exploratory experiments is:

```math
\lambda
=
1-q(1-\alpha),
```

with:

```math
0\le q\le1,
\qquad
0\le\alpha\le1.
```

Here `q` is an execution-strength parameter and `alpha` is residual leakage/accessibility in the downweighted class. These parameter bounds imply:

```math
0\le\lambda\le1,
```

so the resulting selector remains nonnegative and no larger than the favorable-class weight.

At:

```math
q=0,
```

we obtain:

```math
\lambda=1,
```

so there is no weighting effect. At `q=1`, the downweighted-class accessibility is `lambda=alpha`.

## Interpretation

This model is useful for algebra and intuition, but `alpha` is not treated as a universal physical constant. Its meaning depends on the accessibility mechanism being modeled.

## Limitations

The model has only two outcome classes and does not represent trajectory changes caused by recognition-dependent policy. Those require the general recognition framework.

## Status

**EXACT within the stated binary weighting and parameter domains. Physical interpretation OPEN.**
