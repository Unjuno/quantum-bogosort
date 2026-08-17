# Claims, Assumptions, and Non-Claims

This document prevents theorem statements, simulation results, statistical validation results, and Everett interpretation claims from being conflated.

## Exact mathematical claims

### Core weighting identities

For integrable outcome `X` and nonnegative accessibility `S` with positive finite mean:

$$
E_{FP}[X]-E[X]
=
\frac{\operatorname{Cov}(X,S)}{E[S]}.
$$

For threshold `c`:

$$
P_{FP}(X\ge c)-P(X\ge c)
=
\frac{\operatorname{Cov}(\mathbf 1_{\{X\ge c\}},S)}{E[S]}.
$$

If:

$$
g(x)=E[S\mid X=x]
$$

is nondecreasing, then:

$$
F_{FP}(c)\le F(c)
$$

for every `c`.

### Recognition and interaction decompositions

$$
V_1-V_0
=
E[U_1-U_0]
+
Q(U_1,S_1)-Q(U_0,S_0).
$$

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

## S2 predictive-alignment family

### S2 — score-measurable alignment

Let:

$$
m(Y)=E[U\mid Y],
\qquad
S=s(Y).
$$

Then:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),s(Y)).
$$

Comonotonicity of the conditional mean and accessibility implies nonnegative covariance.

### S2.2 — posterior-mean self-calibration

If:

$$
Y=E[U\mid B],
$$

then:

$$
E[U\mid Y]=Y.
$$

### S2.3–S2.4 — robustness certificates

With:

$$
e(Y)=E[U\mid Y]-Y,
$$

S2.3 gives:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)}.
$$

S2.4 gives the conservative prediction-MSE form:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{E[(U-Y)^2]\operatorname{Var}(S)}.
$$

### S2.5–S2.10 — finite-sample statistical certification

S2.5 constructs a bounded independent-held-out lower certificate `D_L` satisfying:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_L
\right)
\ge1-\delta.
$$

S2.6 proves validity after arbitrary independent upstream training. S2.7 permits same-holdout selection among a finite predeclared candidate family after multiplicity correction.

S2.8 proves that any valid simultaneous confidence envelope for:

$$
E[Y],
\quad
E[S],
\quad
E[YS],
\quad
E[S^2],
\quad
E[(U-Y)^2]
$$

can be deterministically composed into a lower covariance certificate.

S2.9 supplies a light-tail sub-Gaussian/Bernstein instantiation. S2.10 supplies a median-of-means instantiation under finite variance bounds for the five target variables themselves.

S2.10 does not follow from finite variance of the raw variables alone. In particular:

$$
\operatorname{Var}(S^2)<\infty
$$

requires a finite fourth moment of `S`, and:

$$
\operatorname{Var}((U-Y)^2)<\infty
$$

requires a finite fourth moment of the prediction residual.

## S2.11 — residual conditional-covariance extension

S2.11 removes the deterministic assumption:

$$
S=s(Y).
$$

Define:

$$
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
$$

Then the law of total covariance gives the exact identity:

$$
\boxed{
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),a(Y))
+
E[\operatorname{Cov}(U,S\mid Y)]
}.
$$

If `m(Y)` and `a(Y)` are comonotone and:

$$
E[\operatorname{Cov}(U,S\mid Y)]
\ge-\varepsilon,
$$

then:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))-
\varepsilon.
$$

Therefore:

$$
\operatorname{Cov}(m(Y),a(Y))>\varepsilon
$$

is sufficient for positive total covariance.

S2 is recovered when `S` is `Y`-measurable, because then:

$$
\operatorname{Cov}(U,S\mid Y)=0
$$

almost surely.

## Simulation-supported claims

The repository's classical simulations support the following model-level statements:

1. Monotone outcome-aligned accessibility produces the predicted FOSD direction across several toy distributions.
2. A representation-capable minimal learner can generate useful predictive ordering while a misspecified learner fails.
3. Recognition effects can be decomposed on paired primitive randomness into trajectory and conditioning contributions.
4. Adaptive rescue can make policy and QBS partially substitutive.
5. Shared recognition/shared latent structure can increase cross-copy action correlation without proportionally changing marginal FP uplift.

These simulations do not establish Everettian physics or automatically satisfy the S2 finite-sample certificate assumptions.

## Model and statistical assumptions

The abstract weighted measure requires:

$$
S_\pi(\omega)\ge0,
\qquad
0<E[S_\pi]<\infty.
$$

S2 assumes score-measurable accessibility. S2.11 relaxes that assumption but requires the residual conditional-covariance component to be retained explicitly.

S2.5 assumes independent bounded held-out evaluation. S2.6 permits training-dependent rules only with independent certification data. S2.7 assumes a finite predeclared candidate family with multiplicity accounting. S2.8 assumes a valid simultaneous five-moment confidence envelope. S2.9 assumes valid light-tail concentration parameters. S2.10 assumes valid target-variable variance upper bounds and a valid i.i.d. block construction.

## Everett bridge assumption

A separate physical interpretation assumes:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

The repository does not derive this rule from unitary quantum mechanics, decoherence, observer dynamics, or the Born rule.

## Non-claims

The repository does **not** claim that:

- an external RNG becomes objectively biased toward favorable outcomes;
- the weighting identities establish quantum immortality;
- every recognition-dependent policy is beneficial;
- positive correlation alone implies FOSD;
- mutual information alone implies positive accessibility covariance;
- adaptation automatically learns the true posterior mean;
- score-level alignment remains sufficient after removing `S=s(Y)` while ignoring residual dependence;
- a negative residual conditional covariance can be dropped without affecting the result;
- a finite learned score necessarily passes an S2 statistical certificate;
- failure of a sufficient certificate implies negative covariance;
- uncorrected model search preserves nominal confidence;
- marginal sub-Gaussianity fixes all S2.9 product/square constants;
- finite variance of `Y`, `S`, and `U` individually is enough for S2.10;
- a statistical certificate establishes the Everett accessibility bridge.

## Falsification / failure conditions

- outcome/accessibility independence gives zero pure weighting uplift in expectation;
- nonmonotone conditional accessibility can break FOSD;
- dependence without conditional-mean prediction can defeat S2;
- a sufficiently negative S2.11 residual term can overturn positive score-level alignment;
- excessive calibration error or prediction MSE can make S2.3/S2.4 inconclusive;
- nonpositive finite-sample lower margins are inconclusive;
- training/evaluation leakage invalidates the simple held-out guarantee;
- uncorrected multiple-candidate search invalidates S2.7 family-wise coverage;
- invalid confidence envelopes invalidate S2.8;
- invalid tail parameters invalidate S2.9;
- invalid target-variable variance bounds or insufficient MoM blocks invalidate S2.10;
- zero expected accessibility makes the normalized FP measure undefined;
- rejecting the Everett bridge removes the physical interpretation while leaving the abstract mathematical/statistical results intact.
