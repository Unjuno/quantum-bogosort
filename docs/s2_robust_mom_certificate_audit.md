# S2.10 Robust Median-of-Means Certificate — Theorem Audit

**Status:** post-v0.2 stacked theorem candidate

## H — claim under review

S2.10 should instantiate S2.8 without boundedness or exponential-tail assumptions by using median-of-means estimators for the five S2.8 target expectations.

Define:

```math
Z_1=Y,
\qquad
Z_2=S,
\qquad
Z_3=YS,
\qquad
Z_4=S^2,
\qquad
Z_5=(U-Y)^2.
```

The theorem assumes explicit finite variance bounds:

```math
\mathrm{Var}(Z_j)\le v_j.
```

## T — proof audit

### One-block control

For a block of size `m`:

```math
\mathrm{Var}(\bar Z_{j,r})
\le
\frac{v_j}{m}.
```

Chebyshev gives:

```math
P\!\left(
|\bar Z_{j,r}-E[Z_j]|>
2\sqrt{\frac{v_j}{m}}
\right)
\le
\frac14.
```

**Audit:** PASS.

### Median amplification

Let `b` be an odd number of independent blocks. If the MoM estimator is outside the radius:

```math
r_j=2\sqrt{\frac{v_j}{m}},
```

at least half of the blocks must be bad.

The bad-block indicators are independent across disjoint i.i.d. blocks and have expectations at most `1/4`. Hoeffding gives:

```math
P\!\left(
B_j\ge\frac{b}{2}
\right)
\le
\exp\left(-\frac{b}{8}\right).
```

Thus choosing:

```math
b\ge8\log\frac{5}{\delta}
```

makes the failure probability for one target at most:

```math
\frac{\delta}{5}.
```

**Audit:** PASS.

### Five-target simultaneous event

A union bound over the five MoM estimators gives simultaneous coverage at least:

```math
1-\delta.
```

No independence across the five target variables is required.

**Audit:** PASS.

### S2.8 composition

The five robust intervals provide exactly the S2.8 inputs. Therefore:

```math
\mathrm{Cov}(U,S)
\ge
D_{\mathrm{MoM}}
```

on the simultaneous event.

**Audit:** PASS.

### First-person lower bound

If:

```math
D_{\mathrm{MoM}}>0
```

and:

```math
E[S]\le U_S,
```

then T1 gives:

```math
E_{FP}[U]-E[U]
\ge
\frac{D_{\mathrm{MoM}}}{U_S}.
```

**Audit:** PASS.

## D — moment assumption audit

S2.10 does **not** require only raw-variable finite variance. It requires finite variance of all five target variables.

In particular:

```math
\mathrm{Var}(S^2)<\infty
```

requires:

```math
E[S^4]<\infty.
```

Also:

```math
\mathrm{Var}((U-Y)^2)<\infty
```

requires:

```math
E[(U-Y)^4]<\infty,
```

and:

```math
\mathrm{Var}(YS)<\infty
```

requires:

```math
E[Y^2S^2]<\infty.
```

This limitation is explicitly stated in the theorem.

**Audit:** PASS.

## C — failure boundaries

1. Invalid or data-tuned variance upper bounds invalidate the simple stated coverage unless additional accounting is supplied.
2. `n<b` prevents formation of the requested block structure.
3. MoM is robust but may be less efficient than a valid light-tail method.
4. `D_MoM<=0` is inconclusive.
5. Candidate search requires S2.7 multiplicity accounting.
6. The theorem does not establish the Everett bridge.

## U — scope conclusion

S2.10 establishes that the S2.8 QBS covariance-composition layer does not intrinsically require boundedness or exponential tails. It only requires a method that produces valid simultaneous confidence envelopes for the five target expectations.

Median-of-means supplies such envelopes under finite variance of the target variables themselves.

## ERROR CHECK

1. The Chebyshev radius gives per-block bad probability at most `1/4`.
2. The block-level Hoeffding exponent is `exp(-b/8)`.
3. `b >= 8 log(5/delta)` yields per-target failure at most `delta/5`.
4. The five-target union bound yields family failure at most `delta`.
5. Independence is only required across blocks.
6. Fourth-moment consequences are explicitly recorded.
7. The first-person denominator bound uses the correct upper-bound direction.
8. Everett interpretation remains separate.

## Audit conclusion

**S2.10 IS MATHEMATICALLY SOUND UNDER ITS STATED FINITE-VARIANCE BOUNDS FOR THE FIVE S2.8 TARGET VARIABLES AND THE I.I.D. BLOCK CONSTRUCTION.**
