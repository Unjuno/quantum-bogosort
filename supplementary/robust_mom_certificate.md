# S2.10 Robust Median-of-Means Instantiation

## H — objective

S2.9 covers unbounded light-tail observations through sub-Gaussian/Bernstein concentration. The next question is whether S2.8 can also be instantiated without exponential-tail assumptions.

A simple robust route is median-of-means (MoM). The key point is that S2.8 needs accurate means of five target variables, not merely finite variance of the raw score and outcome.

Define:

$$
Z_1=Y,
\qquad
Z_2=S,
\qquad
Z_3=YS,
\qquad
Z_4=S^2,
\qquad
Z_5=(U-Y)^2.
$$

S2.10 assumes finite variance bounds for these five `Z_j` directly.

## T — Corollary S2.10: robust median-of-means certificate

Assume:

$$
S\ge0,
\qquad
0<E[S]<\infty.
$$

Assume the five target variables have finite variances bounded by known constants:

$$
\mathrm{Var}(Z_j)\le v_j<\infty,
\qquad
j=1,\ldots,5.
$$

Let:

$$
0<\delta<1.
$$

Choose an odd integer `b` satisfying:

$$
b\ge8\log\frac{5}{\delta},
\qquad
b\le n.
$$

Let:

$$
m=\left\lfloor\frac{n}{b}\right\rfloor.
$$

Use the first `bm` held-out observations and split them into `b` disjoint blocks of size `m`. For target variable `Z_j`, let:

$$
\bar Z_{j,r}
$$

be the mean in block `r`, and define the median-of-means estimator:

$$
\widetilde\mu_j
=
\mathrm{median}
\left(
\bar Z_{j,1},\ldots,\bar Z_{j,b}
\right).
$$

Define radii:

$$
r_j
=
2\sqrt{\frac{v_j}{m}}.
$$

Then, simultaneously for all five targets, with probability at least:

$$
1-\delta,
$$

we have:

$$
|\widetilde\mu_j-E[Z_j]|
\le r_j,
\qquad
j=1,\ldots,5.
$$

Construct S2.8 envelopes:

$$
L_Y=\widetilde\mu_1-r_1,
\qquad
U_Y=\widetilde\mu_1+r_1,
$$

$$
L_S=\widetilde\mu_2-r_2,
\qquad
U_S=\widetilde\mu_2+r_2,
$$

$$
L_{YS}=\widetilde\mu_3-r_3,
$$

$$
U_{S^2}=\widetilde\mu_4+r_4,
$$

and:

$$
U_M=\widetilde\mu_5+r_5.
$$

Because:

$$
Z_4=S^2\ge0,
\qquad
Z_5=(U-Y)^2\ge0,
$$

one may safely replace the numerical upper envelopes by:

$$
U_{S^2}^+=\max\{0,U_{S^2}\},
\qquad
U_M^+=\max\{0,U_M\}.
$$

Let:

$$
L_S^+=\max\{0,L_S\},
$$

$$
P_U
=
\max\left\{
L_YL_S^+,
L_YU_S,
U_YL_S^+,
U_YU_S
\right\},
$$

$$
C_L=L_{YS}-P_U,
$$

$$
V_U
=
\max\left\{
0,
U_{S^2}^+-(L_S^+)^2
\right\},
$$

and:

$$
\boxed{
D_{\mathrm{MoM}}
=
C_L-\sqrt{U_M^+V_U}
}.
$$

Then:

$$
\boxed{
P\!\left(
\mathrm{Cov}(U,S)
\ge
D_{\mathrm{MoM}}
\right)
\ge1-\delta
}.
$$

Therefore:

$$
D_{\mathrm{MoM}}>0
$$

certifies positive population outcome/accessibility covariance at confidence at least `1-delta`.

If, on the same event:

$$
0<U_S<\infty,
$$

then T1 gives:

$$
\boxed{
E_{FP}[U]-E[U]
\ge
\frac{D_{\mathrm{MoM}}}{U_S}
>0
}.
$$

## D — proof

### Step 1: one target variable

Fix target `Z_j` with:

$$
\mathrm{Var}(Z_j)\le v_j.
$$

A block mean has variance at most:

$$
\mathrm{Var}(\bar Z_{j,r})
\le
\frac{v_j}{m}.
$$

By Chebyshev:

$$
P\!\left(
|\bar Z_{j,r}-E[Z_j]|>
2\sqrt{\frac{v_j}{m}}
\right)
\le
\frac14.
$$

Call a block `bad` when this event occurs. Blocks are independent because they are formed from disjoint i.i.d. observations.

Let `B_j` be the number of bad blocks. Then:

$$
E[B_j]\le\frac{b}{4}.
$$

If the median-of-means estimator lies outside the interval:

$$
E[Z_j]\pm2\sqrt{\frac{v_j}{m}},
$$

at least half of the blocks must be bad. Hoeffding's inequality for the independent bad-block indicators gives:

$$
P\!\left(
B_j\ge\frac{b}{2}
\right)
\le
\exp\left(-\frac{b}{8}\right).
$$

Therefore:

$$
P\!\left(
|\widetilde\mu_j-E[Z_j]|>r_j
\right)
\le
\exp\left(-\frac{b}{8}\right)
\le
\frac{\delta}{5}.
$$

### Step 2: simultaneous five-target event

A union bound over:

$$
j=1,\ldots,5
$$

gives:

$$
P\!\left(
|\widetilde\mu_j-E[Z_j]|\le r_j
\text{ for every }j
\right)
\ge
1-\delta.
$$

This simultaneous event supplies exactly the five confidence envelopes required by S2.8.

### Step 3: invoke S2.8

On the simultaneous event, S2.8 gives:

$$
\mathrm{Cov}(U,S)
\ge
D_{\mathrm{MoM}}.
$$

The positive-certificate and first-person conclusions follow exactly as in S2.8.

## Corollary S2.10.1 — finite candidate selection

For `K` predeclared candidate rules, choose candidate failure budgets:

$$
\delta_k>0,
\qquad
\sum_{k=1}^K\delta_k\le\delta.
$$

Candidate `k` may use an odd block count:

$$
b_k
\ge
8\log\frac{5}{\delta_k}.
$$

If all candidate definitions, variance bounds, and confidence allocations are fixed independently of certification outcomes, then the candidate-level MoM certificates are simultaneously valid with probability at least:

$$
1-\delta.
$$

Any data-dependent selection among those predeclared candidates therefore retains its own lower bound, as in S2.7.

## C — controls and failure boundaries

### Finite variance of raw variables is not enough

S2.10 requires finite variance of:

$$
Y,
\quad
S,
\quad
YS,
\quad
S^2,
\quad
(U-Y)^2.
$$

In particular:

$$
\mathrm{Var}(S^2)<\infty
$$

requires a finite fourth moment of `S`, and:

$$
\mathrm{Var}((U-Y)^2)<\infty
$$

requires a finite fourth moment of the prediction residual. Likewise:

$$
\mathrm{Var}(YS)<\infty
$$

requires:

$$
E[Y^2S^2]<\infty.
$$

Therefore the theorem must not be summarized as requiring only finite variance of `Y`, `S`, and `U` individually.

### Variance bounds must be valid

The constants:

$$
v_1,\ldots,v_5
$$

must be valid population upper bounds, fixed independently of certification outcomes or themselves covered by additional confidence accounting.

### Small samples

The theorem requires enough observations to form the requested number of independent blocks:

$$
n\ge b.
$$

If this fails, S2.10 is not available at the requested confidence level with this construction.

### MoM is robust but conservative

Median-of-means provides exponential confidence from finite target-variable variances, but the radius:

$$
2\sqrt{\frac{v_j}{m}}
$$

can be wider than a correctly specified light-tail certificate. The method trades efficiency for robustness.

### Certificate failure is inconclusive

If:

$$
D_{\mathrm{MoM}}\le0,
$$

S2.10 does not certify positive covariance. This does not imply nonpositive true covariance.

## U — interpretation boundary

S2.10 is a robust statistical instantiation of S2.8. It demonstrates that exponential-tail assumptions are not conceptually required by the QBS covariance-composition step.

The theorem still requires enough finite moments to estimate the five S2.8 target expectations with finite variance. It does not establish the Everett accessibility bridge.

## ERROR CHECK

1. The block count is chosen so `exp(-b/8) <= delta/5`.
2. Chebyshev gives bad-block probability at most `1/4` at radius `2 sqrt(v_j/m)`.
3. Independence is required across blocks, not among `Y`, `S`, and `U` within one observation.
4. The five MoM estimators may be statistically dependent; the union bound does not require independence across target variables.
5. The theorem uses finite variance of all five target variables, not merely raw-variable finite variance.
6. Variance bounds estimated from certification data require additional accounting.
7. The same S2.7 multiplicity logic applies to finite candidate selection.
8. `D_MoM<=0` is inconclusive.
9. The first-person lower bound uses an upper confidence bound on the positive denominator.
10. The Everett bridge remains logically separate.

## Status

**S2.10 MEDIAN-OF-MEANS INSTANTIATION PROVED UNDER FINITE VARIANCE BOUNDS FOR THE FIVE S2.8 TARGET VARIABLES.**
