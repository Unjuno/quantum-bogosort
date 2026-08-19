# Minimal Binary Soft-QBS Model

## Motivation

The binary model is the smallest example that separates favorable-event prior probability from first-person accessibility weighting.

## Definitions

Let favorable outcomes have prior probability:

```math
0\le p\le1.
```

Give favorable outcomes accessibility weight 1 and unfavorable outcomes accessibility weight `lambda`, with:

```math
0\le\lambda\le1.
```

The total expected accessibility is:

```math
E[S]
=
p+(1-p)\lambda.
```

The normalized first-person probability therefore requires:

```math
p+(1-p)\lambda>0.
```

Within the stated square `p,lambda in [0,1]`, the only excluded zero-normalization corner is:

```math
(p,\lambda)=(0,0).
```

## Result

On the positive-normalization domain, the favorable first-person probability is:

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

so the resulting selector remains nonnegative and no larger than the favorable-class weight. The separate positive-normalization condition must still be respected; for example, the extreme combination `p=0`, `q=1`, `alpha=0` gives `lambda=0` and therefore no accessible measure.

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

## ERROR CHECK

1. `p` and `lambda` are both probabilities/weights in `[0,1]`.
2. `p_FP` is defined only when `E[S]=p+(1-p)lambda>0`.
3. The corner `(p,lambda)=(0,0)` is excluded because the normalized FP measure is undefined there.
4. `q,alpha in [0,1]` implies `lambda in [0,1]` but does not by itself guarantee positive expected accessibility when `p=0`.
5. Physical interpretation remains separate from the exact binary algebra.

## Status

**EXACT within the stated binary weighting, execution/leakage, and positive-normalization domains. Physical interpretation OPEN.**
