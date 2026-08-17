# S2.8 Confidence-Envelope Certificate — Audit

**Date:** 2026-08-17  
**Status:** post-v0.2 stacked theorem candidate

## H — target

S2.5 uses a specific bounded Hoeffding construction. S2.8 should isolate the deterministic certificate-composition step so that any independently valid simultaneous moment confidence procedure can be substituted.

The required population objects are:

$$
E[Y],
\quad
E[S],
\quad
E[YS],
\quad
E[S^2],
\quad
E[(U-Y)^2].
$$

## T — covariance product envelope

On a simultaneous event, suppose:

$$
E[Y]\in[L_Y,U_Y],
\qquad
E[S]\in[L_S^+,U_S],
$$

where:

$$
L_S^+=\max\{0,L_S\}.
$$

Because the product map is bilinear, its maximum over the rectangle occurs at a corner:

$$
P_U
=
\max\{L_YL_S^+,L_YU_S,U_YL_S^+,U_YU_S\}.
$$

Therefore:

$$
E[Y]E[S]\le P_U.
$$

If also:

$$
E[YS]\ge L_{YS},
$$

then:

$$
\operatorname{Cov}(Y,S)
\ge
L_{YS}-P_U.
$$

**Audit:** PASS.

## T — variance envelope

If:

$$
E[S^2]\le U_{S^2}
$$

and:

$$
E[S]\ge L_S^+,
$$

then:

$$
\operatorname{Var}(S)
=
E[S^2]-E[S]^2
\le
U_{S^2}-(L_S^+)^2.
$$

Thus:

$$
V_U
=
\max\{0,U_{S^2}-(L_S^+)^2\}
$$

is a valid reported upper envelope on the simultaneous event.

**Audit:** PASS.

## T — S2.4 composition

If:

$$
E[(U-Y)^2]\le U_M,
$$

then S2.4 gives:

$$
\operatorname{Cov}(U,S)
\ge
C_L-\sqrt{U_MV_U}
=
D_{\mathrm{env}}.
$$

If the input confidence event has probability at least:

$$
1-\delta,
$$

then:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_{\mathrm{env}}
\right)
\ge1-\delta.
$$

**Audit:** PASS.

## T — first-person lower bound

If the same event contains:

$$
E[S]\le U_S
$$

and the realized certificate is positive, then:

$$
E_{FP}[U]-E[U]
=
\frac{\operatorname{Cov}(U,S)}{E[S]}
\ge
\frac{D_{\mathrm{env}}}{U_S}.
$$

The positivity of the numerator is required for this denominator substitution direction.

**Audit:** PASS.

## D — why the four-corner product is necessary

A simplified expression such as:

$$
U_YU_S
$$

is not always an upper bound on the product if the entire `Y` interval is negative. For example, when:

$$
U_Y<0,
$$

the product is maximized by pairing the least-negative `Y` endpoint with the **smallest** nonnegative `S` endpoint.

Using all four corners removes this sign error.

**Audit:** PASS.

## C — simultaneous versus marginal confidence

S2.8 assumes one event containing all required moment bounds with probability at least `1-delta`.

Five marginal intervals each labeled `95%` do not imply a `95%` simultaneous event. The concentration or interval-construction layer must perform its own union bound, joint calibration, confidence-sequence construction, or other valid simultaneous accounting.

**Audit:** correctly explicit.

## C — modularity boundary

S2.8 does not establish the validity of any particular sub-Gaussian, empirical-Bernstein, bootstrap, median-of-means, or sequential interval. It only states:

$$
\text{valid simultaneous moment envelope}
\Longrightarrow
\text{valid covariance certificate}.
$$

This prevents the QBS theorem from inheriting unspoken distributional assumptions from a particular estimator.

**Audit:** PASS.

## U — role in theorem architecture

The post-v0.2 stack now separates:

$$
\text{QBS covariance algebra}
$$

from:

$$
\text{statistical concentration method}.
$$

S2.5 is a bounded Hoeffding instantiation. S2.8 is the generic composition layer. Future sub-Gaussian, empirical-Bernstein, robust, or sequential results should prove only that their own moment envelopes satisfy the S2.8 input event.

## ERROR CHECK

1. The covariance product bound uses all four corners because the score mean can be negative.
2. Nonnegative accessibility justifies `L_S^+=max(0,L_S)`.
3. The variance bound subtracts a **lower** bound on the squared mean.
4. The five moment bounds must hold simultaneously.
5. The theorem assumes valid input intervals; it does not validate the interval-construction method itself.
6. The FP denominator substitution uses `U_S` only when the certified covariance lower bound is positive.
7. `D_env<=0` remains inconclusive.
8. Selection among interval methods or candidate rules requires S2.6–S2.7-style accounting.
9. S2.8 is distribution-agnostic only at the composition layer; the upstream confidence method may impose strong distributional assumptions.
10. No Everettian physical conclusion follows from passing the certificate.

## Audit conclusion

**S2.8 IS MATHEMATICALLY SOUND AS A GENERIC COMPOSITION THEOREM FROM A VALID SIMULTANEOUS MOMENT CONFIDENCE ENVELOPE TO A POPULATION COVARIANCE LOWER CERTIFICATE.**
