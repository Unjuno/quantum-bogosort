# S2.9 Light-Tail Certificate — Theorem Audit

**Status:** re-audited 2026-08-19; concentration-parameter domain made explicit on current `main`

## H — claim under review

S2.9 should convert valid light-tail concentration controls for the five S2.8 moments into a finite-sample lower confidence bound for:

```math
\mathrm{Cov}(U,S).
```

It must not rely on ambiguous universal `sub-exponential` constants or leave the radius parameter domain implicit.

## T — proof audit

### Five concentration events

S2.9 assumes two-sided mean concentration:

```math
P\!\left(
|\bar X-E[X]|>
\sigma_X\sqrt{\frac{2t}{n}}
\right)
\le2e^{-t}
```

for `X=Y,S`, with:

```math
\sigma_X\ge0,
```

and Bernstein mean concentration:

```math
P\!\left(
|\bar W-E[W]|>
\sqrt{\frac{2v_Wt}{n}}+
\frac{b_Wt}{n}
\right)
\le2e^{-t}
```

for:

```math
W\in\{YS,S^2,(U-Y)^2\},
```

with:

```math
v_W\ge0,
\qquad
b_W\ge0.
```

The original theorem text treated these signs as conventional properties of concentration parameters but did not state them explicitly. Because S2.9 defines its concentration form directly rather than importing a named parameterization, current `main` now makes the nonnegative domain explicit. This ensures that every reported radius is real and nonnegative on the full sample space.

With:

```math
t=\log\frac{10}{\delta},
```

each event fails with probability at most:

```math
\frac{\delta}{5}.
```

Union bound over five events gives simultaneous coverage at least:

```math
1-\delta.
```

**Audit:** PASS; parameter-domain omission FOUND AND CORRECTED on 2026-08-19 without changing the concentration inequalities or constants.

### S2.8 composition and full-sample totality

On the simultaneous event, the constructed intervals satisfy all five S2.8 envelope requirements. For S2.9 specifically:

```math
U_M
=
\overline{(U-Y)^2}+r_{R^2}.
```

The empirical squared-residual average and the radius are both nonnegative under the explicit parameter domain, so:

```math
U_M\ge0
```

on every sample. Therefore the generic S2.8 clipping:

```math
U_M^+=\max\{0,U_M\}
```

satisfies:

```math
U_M^+=U_M
```

identically for this light-tail instantiation. S2.8 therefore gives:

```math
\mathrm{Cov}(U,S)
\ge
D_{\mathrm{LT}}.
```

**Audit:** PASS.

### First-person lower bound

When:

```math
D_{\mathrm{LT}}>0
```

and:

```math
E[S]\le U_S,
```

T1 gives:

```math
E_{FP}[U]-E[U]
=
\frac{\mathrm{Cov}(U,S)}{E[S]}
\ge
\frac{D_{\mathrm{LT}}}{U_S}.
```

The denominator direction is correct because a positive numerator divided by a smaller positive denominator is at least the same numerator divided by the upper denominator bound.

**Audit:** PASS.

## D — assumption audit

The theorem requires more than marginal sub-Gaussianity of `Y` and `S`. It separately requires valid Bernstein controls for:

```math
YS,
\qquad
S^2,
\qquad
(U-Y)^2.
```

This is intentional. Product and square tails depend on the precise tail norm/mgf convention and constants.

S2.9 therefore treats these controls as explicit statistical inputs rather than deriving universal constants.

**Audit:** PASS.

## C — failure boundaries

1. Tail parameters estimated from certification data require additional coverage accounting.
2. Finite variance alone does not imply the assumed light-tail inequalities.
3. Same-holdout candidate selection requires S2.7 multiplicity correction.
4. `D_LT<=0` is inconclusive.
5. Negative concentration parameters are outside the theorem's domain rather than an alternative parameterization.
6. The theorem certifies an abstract covariance premise, not the Everett bridge.

## U — scope conclusion

S2.9 is not a new QBS composition theorem. It is one unbounded light-tail instantiation of S2.8:

```math
\text{light-tail moment envelopes}
\longrightarrow
\text{S2.8}
\longrightarrow
\text{covariance certificate}.
```

This modularization is mathematically preferable to repeatedly reproving the QBS covariance step for each concentration method.

## ERROR CHECK

1. `log(10/delta)` matches five two-sided events with failure `2 exp(-t)`.
2. `sigma_X`, `v_W`, and `b_W` are explicitly nonnegative, so the defined radii are real/nonnegative.
3. No independence among `Y`, `S`, and `U` within an observation is assumed.
4. Only i.i.d. sampling across observations is used for the stated concentration controls.
5. Product/square concentration is explicit rather than inferred without constants.
6. `U_M` is nonnegative on every sample in this construction, so S2.8's `U_M^+` clipping is inactive here.
7. Candidate selection is delegated to S2.7.
8. Heavy-tail finite-variance settings remain outside S2.9.
9. Everett interpretation remains separate.

## Audit conclusion

**S2.9 IS MATHEMATICALLY SOUND CONDITIONAL ON ITS EXPLICIT FIVE MEAN-CONCENTRATION ASSUMPTIONS AND NONNEGATIVE CONCENTRATION-PARAMETER DOMAIN.**
