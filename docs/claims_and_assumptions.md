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

These are probability identities conditional on the model definitions. They do not by themselves imply Everettian physics.

## Simulation-supported claims

The repository simulations support the following model-level statements:

1. Monotone outcome-aligned accessibility produces the predicted FOSD direction across several toy base distributions.
2. A minimal learned agent can generate predictive outcome/accessibility alignment when its model class can represent the relevant structure.
3. Recognition effects can be numerically decomposed into ordinary trajectory changes and first-person conditioning changes on paired primitive randomness.
4. Adaptive rescue policies can reduce the marginal QBS contribution by rescuing branches that a selector would otherwise downweight.
5. Shared recognition and shared environmental structure can increase cross-copy action correlation without proportionally changing single-observer FP uplift.

These are classical simulations of the formal structure, not empirical evidence for Everettian observer selection.

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

## Everett bridge assumption

A separate physical interpretation assumes:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

The repository does not currently derive this rule from unitary quantum mechanics, decoherence, or the Born rule. Establishing, replacing, or rejecting this bridge is a central open problem.

## Non-claims

The repository does **not** claim that:

- an external random-number generator becomes objectively biased toward favorable outcomes;
- the mathematical weighting identities establish quantum immortality;
- every recognition-dependent policy is rational or beneficial;
- positive correlation alone implies FOSD;
- pure reweighting creates outcomes absent from the fixed-policy support;
- negative policy–QBS interaction means either policy effect is itself negative;
- the classical simulations prove an Everett interpretation.

## Falsification / failure conditions

The formal conclusions weaken or fail when their assumptions are violated:

- outcome/accessibility independence gives zero pure weighting uplift in expectation;
- nonmonotone conditional accessibility can break FOSD;
- no change in trajectory or accessibility gives zero recognition effect;
- zero expected accessibility makes the normalized FP measure undefined;
- rejecting the Everett bridge removes the physical Everett interpretation while leaving the measure-theoretic identities intact.
