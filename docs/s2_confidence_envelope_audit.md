# S2.8 Confidence-Envelope Certificate — Audit

**Date:** 2026-08-17; re-audited 2026-08-19  
**Status:** historical derivation audit with current-main total-definedness correction

## H — target

S2.5 uses a specific bounded Hoeffding construction. S2.8 should isolate the deterministic certificate-composition step so that any independently valid simultaneous moment confidence procedure can be substituted.

The required population objects are:

```math
E[Y],
\quad
E[S],
\quad
E[YS],
\quad
E[S^2],
\quad
E[(U-Y)^2].
```

## T — covariance product envelope

On a simultaneous event, suppose:

```math
E[Y]\in[L_Y,U_Y],
\qquad
E[S]\in[L_S^+,U_S],
```

where:

```math
L_S^+=\max\{0,L_S\}.
```

Because the product map is bilinear, its maximum over the rectangle occurs at a corner:

```math
P_U
=
\max\{L_YL_S^+,L_YU_S,U_YL_S^+,U_YU_S\}.
```

Therefore:

```math
E[Y]E[S]\le P_U.
```

If also:

```math
E[YS]\ge L_{YS},
```

then:

```math
\mathrm{Cov}(Y,S)
\ge
L_{YS}-P_U.
```

**Audit:** PASS.

## T — variance envelope

If:

```math
E[S^2]\le U_{S^2}
```

and:

```math
E[S]\ge L_S^+,
```

then:

```math
\mathrm{Var}(S)
=
E[S^2]-E[S]^2
\le
U_{S^2}-(L_S^+)^2.
```

Thus:

```math
V_U
=
\max\{0,U_{S^2}-(L_S^+)^2\}
```

is a valid reported upper envelope on the simultaneous event.

**Audit:** PASS.

## T — MSE envelope and total-definedness correction

The original audit wrote the certificate as:

```math
D_{\mathrm{env}}
=
C_L-\sqrt{U_MV_U}.
```

On the simultaneous confidence event this is valid because:

```math
E[(U-Y)^2]\le U_M
```

and the nonnegative left-hand side forces `U_M>=0` on that event.

However, S2.8 defines `D_env` as a random statistic on the full sample space. Outside the simultaneous-validity event, the theorem did not require the statistical procedure to return a nonnegative numerical `U_M`. A negative off-event `U_M` would make the displayed square root non-real even though the coverage proof never relies on that sample.

Current `main` therefore defines:

```math
U_M^+
=
\max\{0,U_M\},
```

and:

```math
D_{\mathrm{env}}
=
C_L-\sqrt{U_M^+V_U}.
```

On the simultaneous event `U_M^+=U_M`, so this correction changes neither the lower bound nor its coverage there. It only makes the reported certificate real-valued on all samples.

**Audit:** original on-event inequality PASS; full-sample total-definedness gap FOUND AND CORRECTED on 2026-08-19.

## T — S2.4 composition

On the simultaneous event:

```math
E[(U-Y)^2]\le U_M=U_M^+.
```

S2.4 therefore gives:

```math
\mathrm{Cov}(U,S)
\ge
C_L-\sqrt{U_M^+V_U}
=
D_{\mathrm{env}}.
```

If the input confidence event has probability at least:

```math
1-\delta,
```

then:

```math
P\!\left(
\mathrm{Cov}(U,S)\ge D_{\mathrm{env}}
\right)
\ge1-\delta.
```

**Audit:** PASS after the total-definedness correction.

## T — first-person lower bound

If the same event contains:

```math
E[S]\le U_S
```

and the realized certificate is positive, then:

```math
E_{FP}[U]-E[U]
=
\frac{\mathrm{Cov}(U,S)}{E[S]}
\ge
\frac{D_{\mathrm{env}}}{U_S}.
```

The positivity of the numerator is required for this denominator substitution direction.

**Audit:** PASS.

## D — why the four-corner product is necessary

A simplified expression such as:

```math
U_YU_S
```

is not always an upper bound on the product if the entire `Y` interval is negative. For example, when:

```math
U_Y<0,
```

the product is maximized by pairing the least-negative `Y` endpoint with the **smallest** nonnegative `S` endpoint.

Using all four corners removes this sign error.

**Audit:** PASS.

## C — simultaneous versus marginal confidence

S2.8 assumes one event containing all required moment bounds with probability at least `1-delta`.

Five marginal intervals each labeled `95%` do not imply a `95%` simultaneous event. The concentration or interval-construction layer must perform its own union bound, joint calibration, confidence-sequence construction, or other valid simultaneous accounting.

**Audit:** correctly explicit.

## C — modularity boundary

S2.8 does not establish the validity of any particular sub-Gaussian, empirical-Bernstein, bootstrap, median-of-means, or sequential interval. It only states:

```math
\text{valid simultaneous moment envelope}
\Longrightarrow
\text{valid covariance certificate}.
```

This prevents the QBS theorem from inheriting unspoken distributional assumptions from a particular estimator.

**Audit:** PASS.

## U — role in theorem architecture

The post-v0.2 stack separates:

```math
\text{QBS covariance algebra}
```

from:

```math
\text{statistical concentration method}.
```

S2.5 is a bounded Hoeffding instantiation. S2.8 is the generic composition layer. S2.9 and S2.10 supply light-tail and robust finite-moment instantiations.

## ERROR CHECK

1. The covariance product bound uses all four corners because the score mean can be negative.
2. Nonnegative accessibility justifies `L_S^+=max(0,L_S)`.
3. The variance bound subtracts a **lower** bound on the squared mean.
4. The five moment bounds must hold simultaneously.
5. The theorem assumes valid input intervals; it does not validate the interval-construction method itself.
6. `U_M^+=max(0,U_M)` is required to make the random certificate total on samples outside the confidence event; on the confidence event it equals `U_M`.
7. The FP denominator substitution uses `U_S` only when the certified covariance lower bound is positive.
8. `D_env<=0` remains inconclusive.
9. Selection among interval methods or candidate rules requires S2.6–S2.7-style accounting.
10. S2.8 is distribution-agnostic only at the composition layer; the upstream confidence method may impose strong distributional assumptions.
11. No Everettian physical conclusion follows from passing the certificate.

## Audit conclusion

**S2.8 IS MATHEMATICALLY SOUND AS A GENERIC COMPOSITION THEOREM AFTER THE 2026-08-19 OFF-EVENT TOTAL-DEFINEDNESS CORRECTION `U_M^+=MAX(0,U_M)`. THE CORRECTION DOES NOT ALTER THE CERTIFICATE ON ITS SIMULTANEOUS VALIDITY EVENT.**
