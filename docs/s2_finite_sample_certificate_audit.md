# S2.5 Finite-Sample Held-Out Certificate — Audit

**Date:** 2026-08-17  
**Status:** stacked post-v0.2 theorem candidate

## H — audit target

S2.4 gives a population sufficient condition for positive covariance. S2.5 claims that bounded independent held-out observations can convert that population condition into an explicit high-probability certificate.

The audit checks:

1. the simultaneous Hoeffding constants;
2. the covariance lower bound;
3. the prediction-MSE upper bound;
4. the accessibility-variance upper bound;
5. the final S2.4 substitution;
6. the first-person uplift lower bound;
7. the certificate's sampling and adaptivity boundaries.

## T — theorem quantities

Assume:

$$
|Y|\le B_Y,
\qquad
0\le S\le B_S,
\qquad
|U-Y|\le B_R.
$$

For `n` i.i.d. held-out observations and confidence level `delta`, define:

$$
\tau
=
\sqrt{\frac{\log(10/\delta)}{2n}}.
$$

The five empirical means are based on:

- `Y`;
- `S`;
- `YS`;
- `S^2`;
- `(U-Y)^2`.

Their range widths are respectively:

$$
2B_Y,
\quad
B_S,
\quad
2B_YB_S,
\quad
B_S^2,
\quad
B_R^2.
$$

Hoeffding therefore assigns failure probability at most `delta/5` to each two-sided deviation when the tolerance is range-width times `tau`. A union bound gives simultaneous coverage at least `1-delta`.

**Audit:** PASS.

## D — covariance lower-bound audit

The simultaneous event gives:

$$
E[YS]
\ge
\overline{YS}-2B_YB_S\tau.
$$

For the product of means:

$$
E[Y]E[S]-\bar Y\bar S
=
(E[Y]-\bar Y)E[S]
+
\bar Y(E[S]-\bar S).
$$

Using:

$$
|E[Y]-\bar Y|\le2B_Y\tau,
\qquad
E[S]\le B_S,
$$

$$
|\bar Y|\le B_Y,
\qquad
|E[S]-\bar S|\le B_S\tau,
$$

we obtain:

$$
E[Y]E[S]
\le
\bar Y\bar S+3B_YB_S\tau.
$$

Hence:

$$
\operatorname{Cov}(Y,S)
\ge
\widehat C-5B_YB_S\tau.
$$

The coefficient `5` is therefore:

$$
2+2+1.
$$

**Audit:** PASS.

## D — MSE upper-bound audit

Since:

$$
0\le(U-Y)^2\le B_R^2,
$$

Hoeffding gives:

$$
E[(U-Y)^2]
\le
\widehat M+B_R^2\tau.
$$

The deterministic bound:

$$
E[(U-Y)^2]\le B_R^2
$$

is also valid, so taking the minimum of the two upper bounds is valid.

**Audit:** PASS.

## D — accessibility-variance upper-bound audit

The moment event gives:

$$
E[S^2]
\le
\overline{S^2}+B_S^2\tau.
$$

Because `S` is nonnegative:

$$
E[S]
\ge
\max\{0,\bar S-B_S\tau\}.
$$

Therefore:

$$
\operatorname{Var}(S)
=
E[S^2]-E[S]^2
$$

is upper-bounded by:

$$
\overline{S^2}+B_S^2\tau
-
\left(\max\{0,\bar S-B_S\tau\}\right)^2.
$$

Popoviciu independently gives:

$$
\operatorname{Var}(S)\le\frac{B_S^2}{4}.
$$

The minimum of valid upper bounds remains a valid upper bound.

**Audit:** PASS.

## D — final certificate audit

S2.4 gives:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{E[(U-Y)^2]\operatorname{Var}(S)}.
$$

Replacing the positive first term by its lower bound and the nonnegative terms under the square root by upper bounds gives:

$$
\operatorname{Cov}(U,S)
\ge
D_L.
$$

Thus:

$$
D_L>0
$$

certifies positive covariance on the simultaneous event, which has probability at least `1-delta`.

**Audit:** PASS.

For the first-person value shift:

$$
\Delta_{FP}
=
\frac{\operatorname{Cov}(U,S)}{E[S]}.
$$

When `D_L>0`, use:

$$
\operatorname{Cov}(U,S)\ge D_L
$$

and:

$$
E[S]\le B_S
$$

to obtain:

$$
\Delta_{FP}
\ge
\frac{D_L}{B_S}.
$$

**Audit:** PASS, conditional on `D_L>0` and `E[S]>0`.

## C — consistency audit

All empirical moments are bounded and therefore obey the strong law. For fixed `delta`:

$$
\tau_{n,\delta}\to0.
$$

The covariance lower bound converges to `Cov(Y,S)`, the MSE upper bound converges to the population MSE, and the variance upper bound converges to `Var(S)` because the Popoviciu cap cannot fall below the true variance. Therefore:

$$
D_L\to D_*
$$

almost surely, where:

$$
D_*
=
\operatorname{Cov}(Y,S)
-
\sqrt{E[(U-Y)^2]\operatorname{Var}(S)}.
$$

If `D_*>0`, eventual positive certification follows.

**Audit:** PASS.

## C — sampling and adaptivity boundaries

### Independent evaluation

The proof treats the predictor/accessibility map and the bounds as fixed relative to the held-out sample. If the same sample is used to train the predictor or tune the rule, the simple Hoeffding/union-bound guarantee no longer follows without accounting for data-dependent selection.

**Audit:** explicit boundary required and present.

### A-priori bounds

`B_Y`, `B_S`, and `B_R` must be valid population bounds. Choosing them after inspecting the certification sample can invalidate the advertised coverage.

**Audit:** explicit boundary required and present.

### Unbounded variables

The theorem does not cover unbounded heavy-tailed outcomes or scores. Sub-Gaussian, sub-exponential, empirical-Bernstein, or robust-mean versions would be separate extensions.

**Audit:** OPEN extension, not hidden.

### Certificate failure

If:

$$
D_L\le0,
$$

the theorem is inconclusive. It does not imply:

$$
\operatorname{Cov}(U,S)\le0.
$$

**Audit:** PASS; one-sided certificate interpretation is explicit.

## U — relation to the theorem stack

The post-v0.2 chain is now:

$$
\text{S2: conditional-mean alignment}
$$

$$
\Downarrow
$$

$$
\text{S2.2: posterior-mean exact calibration}
$$

$$
\Downarrow
$$

$$
\text{S2.3: calibration-error robustness}
$$

$$
\Downarrow
$$

$$
\text{S2.4: prediction-MSE population certificate}
$$

$$
\Downarrow
$$

$$
\text{S2.5: finite held-out high-probability certificate}.
$$

Each step is still within the abstract agent/probability layer. No step derives the Everett bridge.

## ERROR CHECK

1. The five-event union bound matches `log(10/delta)`.
2. The covariance error coefficient `5 B_Y B_S tau` is conservative but valid.
3. The variance upper bound subtracts a lower confidence bound on `E[S]^2`, not a point estimate.
4. The Popoviciu cap is valid only because `S` lies in `[0,B_S]`.
5. The MSE cap is valid only because `|U-Y|<=B_R`.
6. The theorem is conditional on independent held-out evaluation or an equivalent conditional-on-training formulation.
7. `D_L<=0` is not a negative result.
8. The theorem inherits the conservatism of S2.4.
9. The finite-sample certificate does not require a new physical assumption.
10. Passing the certificate does not establish the Everett accessibility bridge.

## Audit conclusion

**S2.5 IS A VALID HIGH-PROBABILITY SUFFICIENT CERTIFICATE UNDER THE STATED I.I.D., BOUNDEDNESS, FIXED-MODEL, AND HELD-OUT-EVALUATION ASSUMPTIONS.**
