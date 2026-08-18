# S2.5 Finite-Sample Held-Out Certificate

## H — hypothesis

S2.4 gives a population-level sufficient condition:

```math
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(Y,S)
-
\sqrt{E[(U-Y)^2]\mathrm{Var}(S)}.
```

For a learned agent, the right-hand side is unknown. The next question is whether an independent held-out sample can certify positive population covariance with an explicit confidence level.

## T — Corollary S2.5: bounded finite-sample certificate

Let:

```math
(U_i,Y_i,S_i)_{i=1}^n
```

be an i.i.d. held-out sample from the population analyzed by S2.4. The predictor and accessibility rule must be fixed before this sample is evaluated, or the theorem must be applied conditionally on an independently trained fixed model.

Assume known finite bounds:

```math
|Y|\le B_Y,
\qquad
0\le S\le B_S,
\qquad
|U-Y|\le B_R,
```

with:

```math
B_S>0,
\qquad
0<E[S].
```

For confidence level:

```math
0<\delta<1,
```

define:

```math
\tau_{n,\delta}
=
\sqrt{\frac{\log(10/\delta)}{2n}}.
```

Define empirical moments:

```math
\bar Y
=
\frac1n\sum_{i=1}^nY_i,
\qquad
\bar S
=
\frac1n\sum_{i=1}^nS_i,
```

```math
\overline{YS}
=
\frac1n\sum_{i=1}^nY_iS_i,
\qquad
\overline{S^2}
=
\frac1n\sum_{i=1}^nS_i^2,
```

and prediction MSE:

```math
\widehat M
=
\frac1n\sum_{i=1}^n(U_i-Y_i)^2.
```

Let:

```math
\widehat C
=
\overline{YS}-\bar Y\bar S.
```

Define the covariance lower bound:

```math
C_L
=
\widehat C
-
5B_YB_S\tau_{n,\delta}.
```

Define the MSE upper bound:

```math
M_U
=
\min\left\{
B_R^2,
\widehat M+B_R^2\tau_{n,\delta}
\right\}.
```

Define the accessibility-variance upper bound:

```math
V_U
=
\min\left\{
\frac{B_S^2}{4},
\max\left[
0,
\overline{S^2}
+B_S^2\tau_{n,\delta}
-
\left(
\max\{0,\bar S-B_S\tau_{n,\delta}\}
\right)^2
\right]
\right\}.
```

Finally define the empirical certificate margin:

```math
\boxed{
D_L
=
C_L-\sqrt{M_UV_U}
}.
```

Then, with probability at least:

```math
1-\delta,
```

over the held-out sample:

```math
\boxed{
\mathrm{Cov}(U,S)\ge D_L
}.
```

Therefore, if the observed held-out sample satisfies:

```math
\boxed{D_L>0},
```

then with confidence at least `1-delta`:

```math
\mathrm{Cov}(U,S)>0.
```

Under the QBS weighted-measure model, the same event gives the quantitative lower bound:

```math
\boxed{
E_{FP}[U]-E[U]
\ge
\frac{D_L}{B_S}
>0
}.
```

## D — proof

### Step 1: simultaneous Hoeffding event

For any bounded random variable with range width `w`, Hoeffding gives:

```math
P\left(
|\widehat E[X]-E[X]|>w\tau_{n,\delta}
\right)
\le
\frac{\delta}{5}.
```

Apply this to the five variables:

- `Y`, range width `2 B_Y`;
- `S`, range width `B_S`;
- `YS`, range width `2 B_Y B_S`;
- `S^2`, range width `B_S^2`;
- `(U-Y)^2`, range width `B_R^2`.

By a union bound, with probability at least `1-delta`, all five inequalities hold simultaneously:

```math
|E[Y]-\bar Y|
\le
2B_Y\tau_{n,\delta},
```

```math
|E[S]-\bar S|
\le
B_S\tau_{n,\delta},
```

```math
|E[YS]-\overline{YS}|
\le
2B_YB_S\tau_{n,\delta},
```

```math
|E[S^2]-\overline{S^2}|
\le
B_S^2\tau_{n,\delta},
```

and:

```math
\left|
E[(U-Y)^2]-\widehat M
\right|
\le
B_R^2\tau_{n,\delta}.
```

All following statements are made on this simultaneous event.

### Step 2: lower-bound `Cov(Y,S)`

Write:

```math
\mathrm{Cov}(Y,S)
=
E[YS]-E[Y]E[S].
```

The first term obeys:

```math
E[YS]
\ge
\overline{YS}
-
2B_YB_S\tau_{n,\delta}.
```

For the product term:

```math
E[Y]E[S]-\bar Y\bar S
=
(E[Y]-\bar Y)E[S]
+
\bar Y(E[S]-\bar S).
```

Using:

```math
E[S]\le B_S,
\qquad
|\bar Y|\le B_Y,
```

we obtain:

```math
E[Y]E[S]
\le
\bar Y\bar S
+
3B_YB_S\tau_{n,\delta}.
```

Hence:

```math
\mathrm{Cov}(Y,S)
\ge
\widehat C
-
5B_YB_S\tau_{n,\delta}
=
C_L.
```

### Step 3: upper-bound prediction MSE

The Hoeffding event gives:

```math
E[(U-Y)^2]
\le
\widehat M+B_R^2\tau_{n,\delta}.
```

The deterministic bound:

```math
E[(U-Y)^2]\le B_R^2
```

also holds, so:

```math
E[(U-Y)^2]\le M_U.
```

### Step 4: upper-bound `Var(S)`

The simultaneous event implies:

```math
E[S^2]
\le
\overline{S^2}+B_S^2\tau_{n,\delta},
```

and because `S` is nonnegative:

```math
E[S]
\ge
\max\{0,\bar S-B_S\tau_{n,\delta}\}.
```

Therefore:

```math
\mathrm{Var}(S)
=
E[S^2]-E[S]^2
```

is bounded above by the second expression inside the definition of `V_U`. Independently, Popoviciu's inequality for:

```math
0\le S\le B_S
```

gives:

```math
\mathrm{Var}(S)\le\frac{B_S^2}{4}.
```

Taking the smaller valid upper bound gives:

```math
\mathrm{Var}(S)\le V_U.
```

### Step 5: invoke S2.4

S2.4 gives:

```math
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(Y,S)
-
\sqrt{
E[(U-Y)^2]\mathrm{Var}(S)
}.
```

Using the simultaneous lower and upper bounds:

```math
\mathrm{Cov}(U,S)
\ge
C_L-\sqrt{M_UV_U}
=
D_L.
```

Thus:

```math
P(\mathrm{Cov}(U,S)\ge D_L)
\ge
1-\delta.
```

If `D_L>0`, positive covariance is certified at confidence at least `1-delta`.

Finally, because:

```math
E[S]\le B_S,
```

and the certified covariance lower bound is positive:

```math
E_{FP}[U]-E[U]
=
\frac{\mathrm{Cov}(U,S)}{E[S]}
\ge
\frac{D_L}{B_S}.
```

## Corollary S2.5.1 — consistency of the certificate

Under the S2.5 boundedness assumptions, if the population S2.4 margin is strictly positive:

```math
D_*
=
\mathrm{Cov}(Y,S)
-
\sqrt{
E[(U-Y)^2]\mathrm{Var}(S)
}
>0,
```

then for every fixed confidence level `delta`, the empirical certificate satisfies:

```math
D_L\to D_*
```

almost surely as:

```math
n\to\infty.
```

Therefore the certificate eventually becomes positive almost surely.

This follows from the strong law of large numbers for the bounded empirical moments and:

```math
\tau_{n,\delta}\to0.
```

## C — controls and failure boundaries

### Training/evaluation leakage

The concentration statement is a held-out guarantee. If the same observations are used to choose or tune the predictor, accessibility map, clipping bounds, or certificate threshold, the stated probability guarantee does not automatically hold.

A clean application should either:

- fix the model and accessibility map before drawing the test sample; or
- condition on a training sample and use an independent test sample.

### Boundedness

S2.5 uses Hoeffding and therefore requires valid finite bounds on `Y`, `S`, and prediction residual `U-Y`. If the variables are unbounded, S2.5 does not apply as stated. Sub-Gaussian/sub-exponential or robust-mean extensions are separate results.

### Certificate failure is inconclusive

If:

```math
D_L\le0,
```

the data do not establish the S2.5 sufficient condition at the selected confidence level. This is not evidence that the true covariance is nonpositive.

### Conservatism inherited from S2.4

Even with a very large held-out sample, S2.5 converges to the S2.4 margin, not the sharper S2.3 calibration margin. Large irreducible conditional outcome variance can therefore prevent this certificate from becoming positive even when actual covariance is positive.

## U — interpretation boundary

S2.5 converts the post-v0.2 adaptive-agent theorem family into a statistically testable statement on independent held-out data. It does not require a new QBS-specific simulator: the required empirical inputs are prediction outputs, realized outcomes, and the accessibility rule.

The theorem remains entirely within the abstract probability/agent layer. Passing S2.5 would certify a positive covariance premise under the selected statistical assumptions; it would not establish a physical Everett accessibility law.

## ERROR CHECK

1. The coefficient `5 B_Y B_S tau` comes from simultaneous Hoeffding errors for `YS`, `Y`, and `S`; it is intentionally conservative.
2. The five-moment union bound explains the factor `log(10/delta)`.
3. The predictor/accessibility rule must be fixed independently of the held-out sample for the stated guarantee.
4. The boundedness constants must be valid a priori; post-hoc clipping-bound selection requires separate accounting.
5. `V_U` uses both a moment confidence bound and Popoviciu's deterministic variance bound.
6. `M_U` is capped by the deterministic residual-squared bound `B_R^2`.
7. `D_L>0` is sufficient, not necessary, for positive covariance.
8. `D_L<=0` is inconclusive.
9. The quantitative FP lower bound uses `E[S]<=B_S` and requires the certified covariance margin to be positive.
10. S2.5 inherits S2.4's conservatism with respect to irreducible outcome noise.
11. No Everettian physical conclusion follows from the statistical certificate alone.

## Status

**S2.5 FINITE-SAMPLE HELD-OUT CERTIFICATE PROVED UNDER I.I.D., BOUNDEDNESS, AND INDEPENDENT-EVALUATION ASSUMPTIONS.**
