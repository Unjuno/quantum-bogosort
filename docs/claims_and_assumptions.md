# Claims, Assumptions, and Non-Claims

This document prevents theorem statements, simulation results, and Everett interpretation claims from being conflated.

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

Strict pairwise comonotonicity on a positive-probability set gives strict positivity. Consequently, the QBS covariance identity yields nonnegative first-person mean uplift under these assumptions.

A useful special case is:

$$
S=r(m(Y))
$$

with `r` nondecreasing. If `m(Y)` is nonconstant and `r` is strictly increasing on its essential range, covariance is strictly positive.

These are probability identities and sufficient conditions conditional on the model definitions. They do not by themselves imply Everettian physics.

## Simulation-supported claims

The repository simulations support the following model-level statements:

1. Monotone outcome-aligned accessibility produces the predicted FOSD direction across several toy base distributions.
2. A minimal learned agent can generate the conditional-mean ordering required by S2 when its model class can represent the relevant structure.
3. Recognition effects can be numerically decomposed into ordinary trajectory changes and first-person conditioning changes on paired primitive randomness.
4. Adaptive rescue policies can reduce the marginal QBS contribution by rescuing branches that a selector would otherwise downweight.
5. Shared recognition and shared environmental structure can increase cross-copy action correlation without proportionally changing single-observer FP uplift.

These are classical simulations of the formal structure, not empirical evidence for Everettian observer selection.

## Adaptive-learning assumption boundary

S2 proves the implication from an ordered conditional-mean predictor to nonnegative covariance. It does **not** prove that learning or adaptation necessarily creates the required ordering.

For square-integrable `U`, the relevant mean-predictive strength is:

$$
M(U;Y)
=
\operatorname{Var}(E[U\mid Y]).
$$

Positive mutual information is not a substitute for this directional condition. There exist distributions with:

$$
I(U;Y)>0
$$

but:

$$
E[U\mid Y]=E[U]
$$

almost surely. In such cases, every accessibility map of the form `S=s(Y)` has zero covariance with `U`.

Therefore the remaining learning problem is to justify, derive, or empirically test the calibration condition:

$$
y\mapsto E[U_T\mid Y_t=y]
$$

being ordered in the direction used by accessibility.

## Model assumptions

The formal model assumes that policy-dependent accessibility can be represented by a nonnegative measurable weight:

$$
S_\pi(\omega)\ge0.
$$

The normalized FP measure requires:

$$
0<E[S_\pi]<\infty.
$$

The common-randomness comparison additionally assumes policies can be evaluated on the same primitive sample space.

S2 additionally assumes score-measurable accessibility `S=s(Y)` for its clean projection identity. If accessibility contains residual randomness, the general law of total covariance includes an additional conditional-covariance term.

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

The current project is not claiming the third level as established.

### Structural constraints on a candidate physical bridge

A candidate should satisfy:

- nonnegativity and finite positive normalization;
- absolute continuity with respect to the stated base measure;
- invariance under physically equivalent relabeling or redundant branch bookkeeping;
- consistent aggregation under coarse graining;
- sequentially coherent observer conditioning;
- compatibility with no-signaling and established operational quantum statistics unless explicit new physics is proposed;
- independence from post-hoc utility fitting.

### Layer-specific falsifiability

The phrase "falsifiable QBS" is too coarse unless a layer is named.

- theorem assumptions can fail mathematically;
- a proposed observer model can fail structural consistency tests;
- a physical Everett bridge is empirically falsifiable only if a concrete physical `S_pi` generates observational predictions that differ from competing physical accounts.

If all operational predictions remain identical to standard Everettian quantum mechanics, the bridge may be interpretively underdetermined rather than independently empirically testable.

## Non-claims

The repository does **not** claim that:

- an external random-number generator becomes objectively biased toward favorable outcomes;
- the mathematical weighting identities establish quantum immortality;
- every recognition-dependent policy is rational or beneficial;
- positive correlation alone implies FOSD;
- mutual information alone implies positive accessibility covariance;
- adaptation automatically produces a calibrated evaluation signal;
- pure reweighting creates outcomes absent from the fixed-policy support;
- negative policy–QBS interaction means either policy effect is itself negative;
- the classical simulations prove an Everett interpretation;
- internal consistency of a weighted measure confirms the Everett bridge;
- a utility-favoring accessibility function is physical merely because it produces favorable first-person statistics.

## Falsification / failure conditions

The formal conclusions weaken or fail when their assumptions are violated:

- outcome/accessibility independence gives zero pure weighting uplift in expectation;
- nonmonotone conditional accessibility can break FOSD;
- a score can be statistically informative while having constant conditional outcome mean, defeating the S2 uplift premise;
- no change in trajectory or accessibility gives zero recognition effect;
- zero expected accessibility makes the normalized FP measure undefined;
- arbitrary-label dependence or inconsistent coarse graining counts against a proposed physical bridge;
- operational predictions conflicting with established quantum statistics count empirically against a concrete physical accessibility model;
- rejecting the Everett bridge removes the physical Everett interpretation while leaving the measure-theoretic identities intact.
