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

Therefore positive mean uplift is equivalent to positive covariance under the weighted-measure model.

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

When accessibility is measurable with respect to the score `Y` and the relevant moments are finite:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),s(Y)).
$$

If versions of `m(y)` and `s(y)` are both nondecreasing, then:

$$
\operatorname{Cov}(U,S)\ge0.
$$

Strict pairwise comonotonicity on a positive-probability set gives strict positivity.

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
E[e(Y)^2]
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

Let a fixed predictor/accessibility rule be evaluated on an independent i.i.d. sample and assume known bounds:

$$
|Y|\le B_Y,
\qquad
0\le S\le B_S,
\qquad
|U-Y|\le B_R.
$$

S2.5 constructs a data-dependent lower certificate:

$$
D_L
=
C_L-\sqrt{M_UV_U}
$$

such that:

$$
P\left(
\operatorname{Cov}(U,S)\ge D_L
\right)
\ge1-\delta.
$$

### S2.6 validity after arbitrary independent training

Let `T` denote the entire random training procedure. Conditional on `T`, suppose the trained predictor/accessibility rule and valid population bounds are fixed before an independent certification sample is evaluated. Then:

$$
P\!\left(
C(T)\ge D_L(T)
\mid T
\right)
\ge1-\delta
$$

almost surely, and therefore:

$$
P\!\left(
C(T)\ge D_L(T)
\right)
\ge1-\delta.
$$

### S2.7 finite candidate post-selection validity

Suppose `K` candidate rules are fixed before the certification sample is inspected and receive predeclared failure budgets:

$$
\delta_k>0,
\qquad
\sum_{k=1}^K\delta_k\le\delta.
$$

If each candidate has a valid S2.5 or S2.8 certificate at level `1-delta_k`, then all candidate certificates hold simultaneously with probability at least:

$$
1-\delta.
$$

Therefore any data-dependent selected index from that predeclared family retains its corresponding lower bound.

### S2.8 generic confidence-envelope certificate

Suppose a statistical procedure supplies a simultaneous event with probability at least:

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

Because `S>=0`, define:

$$
L_S^+=\max\{0,L_S\}.
$$

Let:

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

S2.8 is a deterministic composition theorem conditional on the validity of the input simultaneous confidence envelope.

### S2.9 light-tail instantiation

S2.9 assumes two-sided sample-mean concentration for `Y` and `S` of the form:

$$
P\!\left(
|\bar X-E[X]|>
\sigma_X\sqrt{\frac{2t}{n}}
\right)
\le2e^{-t},
$$

for `X=Y,S`, and Bernstein/sub-exponential sample-mean concentration:

$$
P\!\left(
|\bar W-E[W]|>
\sqrt{\frac{2v_Wt}{n}}
+
\frac{b_Wt}{n}
\right)
\le2e^{-t}
$$

for:

$$
W\in\{YS,S^2,(U-Y)^2\}.
$$

With:

$$
t=\log\frac{10}{\delta},
$$

a union bound supplies the five simultaneous S2.8 moment envelopes at confidence at least `1-delta`. The resulting light-tail margin `D_LT` therefore satisfies:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_{\mathrm{LT}}
\right)
\ge1-\delta.
$$

S2.9 is an unbounded light-tail statistical instantiation, not a new physical claim.

## Simulation-supported claims

The repository simulations support the following model-level statements:

1. Monotone outcome-aligned accessibility produces the predicted FOSD direction across several toy base distributions.
2. A minimal learned agent can generate useful predictive ordering when its model class can represent the relevant structure.
3. Recognition effects can be numerically decomposed into ordinary trajectory changes and first-person conditioning changes on paired primitive randomness.
4. Adaptive rescue policies can reduce the marginal QBS contribution by rescuing branches that a selector would otherwise downweight.
5. Shared recognition and shared environmental structure can increase cross-copy action correlation without proportionally changing single-observer FP uplift.

E2/E3 illustrate premise generation for S2. They do not establish any finite-sample certificate without a separate evaluation satisfying the corresponding statistical assumptions.

## Adaptive-learning and statistical-validation boundary

S2 proves the conditional-mean alignment implication. S2.2 proves exact posterior-mean calibration. S2.3 and S2.4 provide population robustness certificates. S2.5 supplies a bounded independent-held-out confidence certificate. S2.6 proves that arbitrary independent training can be conditioned away for certification. S2.7 permits same-holdout selection among a finite predeclared candidate family after multiplicity correction. S2.8 makes the finite-sample QBS step concentration-method agnostic. S2.9 supplies one unbounded light-tail instantiation.

Positive mutual information is not sufficient. There exist distributions with:

$$
I(U;Y)>0
$$

but constant:

$$
E[U\mid Y],
$$

so every accessibility map `S=s(Y)` has zero covariance with `U`.

S2.9 does not claim that marginal sub-Gaussianity automatically determines valid product/square concentration constants. The required controls for `YS`, `S^2`, and `(U-Y)^2` are explicit statistical inputs.

## Model assumptions

The formal model assumes nonnegative measurable accessibility:

$$
S_\pi(\omega)\ge0
$$

and normalized FP measure requires:

$$
0<E[S_\pi]<\infty.
$$

The common-randomness comparison assumes policies can be evaluated on the same primitive sample space.

S2 assumes score-measurable accessibility `S=s(Y)`. S2.2 assumes the score is the true conditional expectation under the analyzed probability model. S2.3/S2.4 assume square integrability. S2.5 additionally assumes i.i.d. independent held-out evaluation and known finite bounds on the score, accessibility, and prediction residual. S2.6 permits training-dependent rules and bounds only when the certification sample is independent and those bounds are valid for fresh draws. S2.7 assumes a finite candidate family and confidence allocation fixed before the certification sample is inspected. S2.8 assumes a valid simultaneous five-moment confidence envelope. S2.9 assumes valid light-tail concentration parameters for all five required sample means.

## Everett bridge assumption

A separate physical interpretation assumes:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

The repository does not currently derive this rule from unitary quantum mechanics, decoherence, observer dynamics, or the Born rule. Establishing, replacing, or rejecting this bridge remains a physical open problem.

The detailed bridge criteria are in `docs/everett_bridge_tests.md`.

### Bridge status levels

- **Abstract change of measure:** exact once `S_pi` is specified.
- **Observer-model bridge:** requires an independent account of why observer persistence or self-location induces `S_pi`.
- **Physical Everett bridge:** additionally requires a defensible relation to branch amplitude, decoherence, Born-rule probability, and operational quantum predictions.

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
- predictor/accessibility candidates may be invented after inspecting certification data without additional statistical accounting;
- marginal sub-Gaussianity alone fixes all product/square concentration constants needed by S2.9;
- tail parameters estimated from the certification sample can be plugged in without additional coverage accounting;
- finite variance alone is enough for the light-tail S2.9 theorem;
- low prediction MSE is necessary for positive covariance;
- pure reweighting creates outcomes absent from the fixed-policy support;
- negative policy–QBS interaction means either policy effect is itself negative;
- the classical simulations prove an Everett interpretation;
- a statistical S2 certificate establishes the Everett accessibility bridge;
- internal consistency of a weighted measure confirms the Everett bridge.

## Falsification / failure conditions

The formal conclusions weaken or fail when their assumptions are violated:

- outcome/accessibility independence gives zero pure weighting uplift in expectation;
- nonmonotone conditional accessibility can break FOSD;
- a score can be statistically informative while having constant conditional outcome mean, defeating the S2 uplift premise;
- a finite score can fail the S2.3 robustness certificate when calibration error dominates the alignment margin;
- large irreducible conditional variance can make S2.4 inconclusive even when actual covariance is positive;
- a nonpositive finite-sample lower margin is inconclusive at the selected confidence level;
- training/evaluation leakage or invalid post-hoc bounds remove the simple S2.5/S2.6 coverage guarantee;
- uncorrected multiple-candidate search removes the S2.7 family-wise guarantee;
- invalid or non-simultaneous input intervals invalidate the S2.8 certificate;
- invalid light-tail parameters or unaccounted tail-parameter estimation invalidate the S2.9 coverage guarantee;
- no change in trajectory or accessibility gives zero recognition effect;
- zero expected accessibility makes the normalized FP measure undefined;
- rejecting the Everett bridge removes the physical Everett interpretation while leaving the measure-theoretic and statistical identities intact.
