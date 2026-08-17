# Claims, Assumptions, and Non-Claims

This document prevents theorem statements, simulation results, statistical validation results, and Everett interpretation claims from being conflated.

## Exact mathematical claims

### Mean-shift identity

For integrable outcome `X` and nonnegative accessibility `S` with positive finite mean:

$$
E_{FP}[X]-E[X]
=
\frac{\operatorname{Cov}(X,S)}{E[S]}.
$$

### Tail identity

For threshold `c`:

$$
P_{FP}(X\ge c)-P(X\ge c)
=
\frac{\operatorname{Cov}(\mathbf 1_{\{X\ge c\}},S)}{E[S]}.
$$

### FOSD condition

If:

$$
g(x)=E[S\mid X=x]
$$

is nondecreasing, then:

$$
F_{FP}(c)\le F(c)
$$

for every threshold `c`.

### Recognition decomposition

$$
V_1-V_0
=
E[U_1-U_0]
+
Q(U_1,S_1)-Q(U_0,S_0).
$$

### Interaction decomposition

With:

$$
D=U_1-U_0,
$$

we have:

$$
I
=
\frac{\operatorname{Cov}(D,S_0)}{E[S_0]}
+
\left[Q(U_1,S_1)-Q(U_1,S_0)\right].
$$

### S2 predictive-calibration alignment

Let:

$$
m(Y)=E[U\mid Y],
\qquad
S=s(Y)\ge0.
$$

Then:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),s(Y)).
$$

If versions of `m(y)` and `s(y)` are both nondecreasing, then:

$$
\operatorname{Cov}(U,S)\ge0.
$$

### S2.2 posterior-mean self-calibration

If:

$$
Y=E[U\mid B],
$$

then:

$$
E[U\mid Y]=Y.
$$

### S2.3 approximate-calibration robustness

With:

$$
e(Y)=E[U\mid Y]-Y,
$$

square integrability gives:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)}.
$$

### S2.4 prediction-MSE certificate

Conditional Jensen gives:

$$
\operatorname{Var}(e(Y))
\le
E[(U-Y)^2],
$$

and therefore:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{E[(U-Y)^2]\operatorname{Var}(S)}.
$$

### S2.5 finite-sample held-out certificate

Under independent i.i.d. evaluation and valid boundedness assumptions, S2.5 constructs a lower certificate `D_L` satisfying:

$$
P\left(
\operatorname{Cov}(U,S)\ge D_L
\right)
\ge1-\delta.
$$

### S2.6 validity after arbitrary independent training

Let `T` denote the entire random training procedure. Conditional on `T`, if the final certification sample is independent and the trained rule/bounds are valid for fresh draws, then:

$$
P\!\left(
C(T)\ge D_L(T)
\mid T
\right)
\ge1-\delta.
$$

### S2.7 finite candidate post-selection validity

For a finite predeclared candidate family with confidence budgets:

$$
\delta_k>0,
\qquad
\sum_{k=1}^K\delta_k\le\delta,
$$

simultaneous candidate certificates hold with probability at least:

$$
1-\delta.
$$

Any data-dependent selected index from that predeclared family retains its lower bound.

### S2.8 generic confidence-envelope certificate

Suppose a statistical procedure supplies a simultaneous event of probability at least:

$$
1-\delta
$$

on which:

$$
L_Y\le E[Y]\le U_Y,
\qquad
L_S\le E[S]\le U_S,
$$

$$
E[YS]\ge L_{YS},
\qquad
E[S^2]\le U_{S^2},
\qquad
E[(U-Y)^2]\le U_M.
$$

Define:

$$
L_S^+=\max\{0,L_S\},
$$

$$
P_U
=
\max\{L_YL_S^+,L_YU_S,U_YL_S^+,U_YU_S\},
$$

$$
C_L=L_{YS}-P_U,
$$

$$
V_U
=
\max\{0,U_{S^2}-(L_S^+)^2\},
$$

and:

$$
D_{\mathrm{env}}
=
C_L-\sqrt{U_MV_U}.
$$

Then:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_{\mathrm{env}}
\right)
\ge1-\delta.
$$

### S2.9 light-tail instantiation

S2.9 assumes valid sub-Gaussian sample-mean controls for `Y` and `S`, and valid Bernstein/sub-exponential sample-mean controls for:

$$
YS,
\qquad
S^2,
\qquad
(U-Y)^2.
$$

These five controls generate the S2.8 simultaneous event and a light-tail lower margin:

$$
D_{\mathrm{LT}}
$$

satisfying:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_{\mathrm{LT}}
\right)
\ge1-\delta.
$$

### S2.10 robust median-of-means instantiation

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

Assume known variance bounds:

$$
\operatorname{Var}(Z_j)\le v_j<\infty,
\qquad
j=1,\ldots,5.
$$

Choose an odd block count `b` satisfying:

$$
b\ge8\log\frac{5}{\delta},
$$

with block size:

$$
m=\left\lfloor\frac{n}{b}\right\rfloor.
$$

For each target, the median-of-means estimator has radius:

$$
r_j
=
2\sqrt{\frac{v_j}{m}}
$$

and failure probability at most:

$$
\frac{\delta}{5}.
$$

A union bound gives a simultaneous S2.8 envelope and a robust lower margin:

$$
D_{\mathrm{MoM}}
$$

satisfying:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_{\mathrm{MoM}}
\right)
\ge1-\delta.
$$

S2.10 is a robust finite-moment statistical instantiation, not a physical Everettian claim.

## Simulation-supported claims

The repository simulations support the following model-level statements:

1. Monotone outcome-aligned accessibility produces the predicted FOSD direction across several toy base distributions.
2. A minimal learned agent can generate useful predictive ordering when its model class can represent the relevant structure.
3. Recognition effects can be numerically decomposed into ordinary trajectory changes and first-person conditioning changes on paired primitive randomness.
4. Adaptive rescue policies can reduce the marginal QBS contribution by rescuing branches that a selector would otherwise downweight.
5. Shared recognition and shared environmental structure can increase cross-copy action correlation without proportionally changing single-observer FP uplift.

E2/E3 illustrate premise generation for S2. They do not establish any finite-sample certificate without a separate evaluation satisfying the corresponding statistical assumptions.

## Adaptive-learning and statistical-validation boundary

S2 proves conditional-mean alignment. S2.2 proves posterior-mean calibration. S2.3/S2.4 provide population robustness certificates. S2.5 provides a bounded held-out certificate. S2.6–S2.7 handle independent training and finite candidate selection. S2.8 separates QBS composition from the concentration method. S2.9 supplies a light-tail instantiation. S2.10 supplies a median-of-means robust finite-moment instantiation.

S2.10 does **not** require only finite variance of the raw variables. It requires finite variance of all five S2.8 target variables. In particular:

$$
\operatorname{Var}(S^2)<\infty
$$

requires:

$$
E[S^4]<\infty,
$$

and:

$$
\operatorname{Var}((U-Y)^2)<\infty
$$

requires:

$$
E[(U-Y)^4]<\infty.
$$

Likewise:

$$
\operatorname{Var}(YS)<\infty
$$

requires:

$$
E[Y^2S^2]<\infty.
$$

Positive mutual information is not sufficient for the S2 covariance premise.

## Model assumptions

The formal model assumes nonnegative measurable accessibility:

$$
S_\pi(\omega)\ge0
$$

and normalized FP measure requires:

$$
0<E[S_\pi]<\infty.
$$

S2 assumes score-measurable accessibility `S=s(Y)`. S2.2 assumes the score is the true conditional expectation under the analyzed probability model. S2.3/S2.4 assume square integrability. S2.5 assumes independent bounded held-out evaluation. S2.6 permits training-dependent rules only with independent certification data. S2.7 assumes a finite predeclared candidate family with multiplicity accounting. S2.8 assumes a valid simultaneous five-moment confidence envelope. S2.9 assumes valid light-tail concentration parameters. S2.10 assumes valid population variance upper bounds for the five target variables and enough observations to form the requested blocks.

## Everett bridge assumption

A separate physical interpretation assumes:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

The repository does not currently derive this rule from unitary quantum mechanics, decoherence, observer dynamics, or the Born rule.

## Non-claims

The repository does **not** claim that:

- an external random-number generator becomes objectively biased toward favorable outcomes;
- the mathematical weighting identities establish quantum immortality;
- every recognition-dependent policy is rational or beneficial;
- positive correlation alone implies FOSD;
- mutual information alone implies positive accessibility covariance;
- adaptation automatically learns the true posterior mean;
- a finite learned score necessarily satisfies any S2 finite-sample certificate;
- failure of an S2 certificate implies negative covariance;
- the same sample may be reused arbitrarily for training and certification while preserving nominal confidence;
- uncorrected best-of-K selection preserves the certificate confidence level;
- marginal sub-Gaussianity alone fixes all product/square concentration constants needed by S2.9;
- finite variance of `Y`, `S`, and `U` individually is enough for S2.10;
- variance bounds estimated from certification data can be plugged into S2.10 without additional accounting;
- a statistical S2 certificate establishes the Everett accessibility bridge;
- internal consistency of a weighted measure confirms the Everett bridge.

## Falsification / failure conditions

The formal conclusions weaken or fail when their assumptions are violated:

- outcome/accessibility independence gives zero pure weighting uplift in expectation;
- nonmonotone conditional accessibility can break FOSD;
- a statistically informative score can still have constant conditional outcome mean, defeating the S2 premise;
- excessive calibration error can make S2.3 inconclusive;
- large irreducible conditional variance can make S2.4 inconclusive;
- a nonpositive finite-sample lower margin is inconclusive;
- training/evaluation leakage removes the simple S2.5/S2.6 guarantee;
- uncorrected multiple-candidate search removes the S2.7 family-wise guarantee;
- invalid or non-simultaneous input intervals invalidate S2.8;
- invalid light-tail parameters invalidate S2.9;
- invalid target-variable variance bounds, insufficient blocks, or missing fourth-moment-type conditions invalidate S2.10 as stated;
- zero expected accessibility makes the normalized FP measure undefined;
- rejecting the Everett bridge removes the physical Everett interpretation while leaving the mathematical and statistical identities intact.
