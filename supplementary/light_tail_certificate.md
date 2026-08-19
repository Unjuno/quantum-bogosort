# S2.9 Light-Tail Confidence-Envelope Instantiation

## H — objective

S2.8 reduces finite-sample certification to a simultaneous confidence envelope for five population moments:

```math
E[Y],
\qquad
E[S],
\qquad
E[YS],
\qquad
E[S^2],
\qquad
E[(U-Y)^2].
```

S2.5 supplies these envelopes under boundedness via Hoeffding. This note gives an unbounded light-tail instantiation using sub-Gaussian concentration for the first moments and Bernstein/sub-exponential concentration for the product and squared quantities.

The QBS composition step remains S2.8. S2.9 only supplies one statistically valid input layer.

## Definitions

Let:

```math
R=U-Y.
```

For an i.i.d. sample of size `n`, write empirical averages as:

```math
\bar Y,
\qquad
\bar S,
\qquad
\overline{YS},
\qquad
\overline{S^2},
\qquad
\overline{R^2}.
```

### Sub-Gaussian mean control

A centered random variable `X-E[X]` is said here to have sub-Gaussian mean parameter:

```math
\sigma_X\ge0
```

when its i.i.d. sample mean satisfies, for every `t>0`:

```math
P\!\left(
|\bar X-E[X]|>
\sigma_X\sqrt{\frac{2t}{n}}
\right)
\le
2e^{-t}.
```

This is the only sub-Gaussian property used below.

### Bernstein / sub-exponential mean control

A random variable `W` is said here to have Bernstein mean parameters:

```math
v_W\ge0,
\qquad
b_W\ge0
```

when, for every `t>0`:

```math
P\!\left(
|\bar W-E[W]|>
\sqrt{\frac{2v_Wt}{n}}
+
\frac{b_Wt}{n}
\right)
\le
2e^{-t}.
```

This is a standard sub-exponential/Bernstein-type concentration form. Stating the required tail property directly avoids ambiguity across competing parameterizations of the phrase `sub-exponential`. A separate application may derive valid `(v_W,b_W)` from Orlicz norms, mgf bounds, or a specific parametric model.

## T — Corollary S2.9: light-tail confidence-envelope certificate

Assume:

```math
S\ge0,
\qquad
0<E[S]<\infty.
```

Assume `Y` and `S` have sub-Gaussian mean parameters:

```math
\sigma_Y,
\qquad
\sigma_S.
```

Assume the three derived variables:

```math
YS,
\qquad
S^2,
\qquad
R^2=(U-Y)^2
```

have Bernstein mean parameters:

```math
(v_{YS},b_{YS}),
\qquad
(v_{S^2},b_{S^2}),
\qquad
(v_{R^2},b_{R^2}).
```

For confidence level:

```math
0<\delta<1,
```

define:

```math
t_\delta
=
\log\frac{10}{\delta}.
```

Define the radii:

```math
r_Y
=
\sigma_Y\sqrt{\frac{2t_\delta}{n}},
\qquad
r_S
=
\sigma_S\sqrt{\frac{2t_\delta}{n}},
```

```math
r_{YS}
=
\sqrt{\frac{2v_{YS}t_\delta}{n}}
+
\frac{b_{YS}t_\delta}{n},
```

```math
r_{S^2}
=
\sqrt{\frac{2v_{S^2}t_\delta}{n}}
+
\frac{b_{S^2}t_\delta}{n},
```

and:

```math
r_{R^2}
=
\sqrt{\frac{2v_{R^2}t_\delta}{n}}
+
\frac{b_{R^2}t_\delta}{n}.
```

Construct the S2.8 input envelopes:

```math
L_Y=\bar Y-r_Y,
\qquad
U_Y=\bar Y+r_Y,
```

```math
L_S=\bar S-r_S,
\qquad
U_S=\bar S+r_S,
```

```math
L_{YS}
=
\overline{YS}-r_{YS},
```

```math
U_{S^2}
=
\overline{S^2}+r_{S^2},
```

and:

```math
U_M
=
\overline{R^2}+r_{R^2}.
```

The concentration-parameter domain above makes all radii nonnegative. Since `R^2>=0`, `U_M>=0` on every sample; therefore the S2.8 clipping `U_M^+=max(0,U_M)` equals `U_M` identically for this instantiation.

Let:

```math
L_S^+
=
\max\{0,L_S\},
```

```math
P_U
=
\max\left\{
L_YL_S^+,
L_YU_S,
U_YL_S^+,
U_YU_S
\right\},
```

```math
C_L
=
L_{YS}-P_U,
```

```math
V_U
=
\max\left\{
0,
U_{S^2}-(L_S^+)^2
\right\},
```

and finally:

```math
\boxed{
D_{\mathrm{LT}}
=
C_L-\sqrt{U_MV_U}
}.
```

Then:

```math
\boxed{
P\!\left(
\mathrm{Cov}(U,S)
\ge
D_{\mathrm{LT}}
\right)
\ge
1-\delta
}.
```

Therefore:

```math
D_{\mathrm{LT}}>0
```

certifies positive population outcome/accessibility covariance with confidence at least `1-delta`.

If, on the same simultaneous event, the reported upper mean bound satisfies:

```math
0<U_S<\infty,
```

then T1 gives:

```math
\boxed{
E_{FP}[U]-E[U]
\ge
\frac{D_{\mathrm{LT}}}{U_S}
>0
}.
```

## D — proof

### Step 1: simultaneous light-tail event

Each of the two sub-Gaussian mean bounds fails with probability at most:

```math
2e^{-t_\delta}
=
\frac{\delta}{5}.
```

Each of the three Bernstein mean bounds also fails with probability at most:

```math
\frac{\delta}{5}.
```

A union bound over the five events gives simultaneous coverage at least:

```math
1-\delta.
```

On this event:

```math
L_Y\le E[Y]\le U_Y,
```

```math
L_S\le E[S]\le U_S,
```

```math
E[YS]\ge L_{YS},
```

```math
E[S^2]\le U_{S^2},
```

and:

```math
E[(U-Y)^2]\le U_M.
```

These are exactly the five input envelopes required by S2.8, with `U_M^+=U_M` identically in this construction.

### Step 2: invoke S2.8

S2.8 deterministically transforms every valid simultaneous event of the form above into:

```math
\mathrm{Cov}(U,S)
\ge
D_{\mathrm{LT}}.
```

Therefore the lower bound holds with probability at least `1-delta`.

The positive-certificate and first-person conclusions are exactly the corresponding S2.8 consequences.

## Corollary S2.9.1 — finite candidate selection

Suppose `K` candidate predictor/accessibility rules are fixed independently of the certification sample. Give candidate `k` a predeclared failure budget:

```math
\delta_k>0,
\qquad
\sum_{k=1}^K\delta_k\le\delta.
```

Apply S2.9 to candidate `k` using:

```math
t_k
=
\log\frac{10}{\delta_k}.
```

Then, with probability at least `1-delta`, every candidate's light-tail certificate is simultaneously valid. Any data-dependent choice among those predeclared candidates therefore inherits its corresponding lower bound, exactly as in S2.7.

For equal allocation:

```math
\delta_k=\frac{\delta}{K},
```

the common logarithmic factor becomes:

```math
\log\frac{10K}{\delta}.
```

## Corollary S2.9.2 — relation to S2.5

S2.5 and S2.9 are parallel instantiations of S2.8:

```math
\text{bounded Hoeffding envelopes}
\longrightarrow
\text{S2.8}
```

versus:

```math
\text{light-tail sub-Gaussian/Bernstein envelopes}
\longrightarrow
\text{S2.8}.
```

Neither dominates the other uniformly. The bounded version uses deterministic ranges; the light-tail version permits unbounded variables when valid concentration parameters are available.

## C — controls and failure boundaries

### Product and square tails must be controlled

Sub-Gaussian control of `Y` and `S` alone is not, by itself, the full input to this theorem. The proof explicitly requires valid concentration parameters for:

```math
YS,
\qquad
S^2,
\qquad
(U-Y)^2.
```

In many standard light-tail models these derived variables are sub-exponential, but the constants depend on the precise norm or mgf convention. S2.9 therefore takes their Bernstein parameters as explicit inputs rather than silently assuming universal constants.

### Estimated tail parameters require their own validity argument

If `sigma_Y`, `sigma_S`, or any Bernstein parameter is estimated from the same certification data, the simple stated coverage does not automatically follow. They should be known from the model, fixed from independent data, or upper-confidently estimated with the additional failure probability included in the total error budget.

### Heavy tails are not covered

Finite variance alone does not imply the sub-Gaussian/Bernstein concentration assumed here. Heavy-tailed applications require robust estimators or another valid S2.8 envelope construction.

### Certificate failure is inconclusive

If:

```math
D_{\mathrm{LT}}\le0,
```

S2.9 does not certify positive covariance at the selected confidence level. This is not evidence that the true covariance is nonpositive.

## U — interpretation boundary

S2.9 is a statistical instantiation of the generic S2.8 composition theorem. It enlarges the validation layer from bounded observations to explicitly controlled light tails.

It does not change the QBS measure-theoretic assumptions, does not prove that learned-agent outputs have the stated tail parameters, and does not establish any Everettian accessibility law.

## ERROR CHECK

1. The five-event union bound explains `log(10/delta)` because each two-sided tail has failure probability `2 exp(-t)`.
2. The theorem states the Bernstein concentration form directly, avoiding silent dependence on a particular sub-exponential parameterization.
3. All sub-Gaussian/Bernstein concentration parameters are explicitly nonnegative, so every reported radius and `U_M` is real/nonnegative on the full sample space.
4. `YS`, `S^2`, and `(U-Y)^2` receive their own concentration parameters; marginal sub-Gaussian assumptions are not incorrectly treated as sufficient without constants.
5. The covariance product envelope still uses all four interval corners because `E[Y]` may be negative.
6. `S>=0` justifies `L_S^+=max(0,L_S)`.
7. Tail-parameter estimation from the certification sample requires extra accounting.
8. Finite variance alone is not enough for S2.9.
9. `D_LT<=0` is inconclusive.
10. Candidate selection requires S2.7-style multiplicity control.
11. The Everett bridge remains logically separate.

## Status

**S2.9 LIGHT-TAIL SUB-GAUSSIAN/BERNSTEIN INSTANTIATION PROVED CONDITIONAL ON THE STATED FIVE MEAN-CONCENTRATION CONTROLS AND NONNEGATIVE CONCENTRATION-PARAMETER DOMAIN.**
