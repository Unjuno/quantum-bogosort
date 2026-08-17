# QBS Research Map

This document links the main claims to their mathematical source, computational test, and interpretation status.

## Core causal structure

Recognition is modeled as a causal input to policy:

$$
R
\longrightarrow
\pi_R
\longrightarrow
(U_R,S_R).
$$

The base branch randomness is represented on a common sample space so paired counterfactual policies can be compared on the same primitive realization.

## Claim-to-evidence map

| Claim | Type | Mathematical source | Computational source | Interpretation status |
|---|---|---|---|---|
| FP mean shift equals normalized outcome-accessibility covariance | Exact theorem | T1 | E1 | Measure-theoretic |
| Tail-probability shift has the same covariance form | Exact theorem | T2 | E1 | Measure-theoretic |
| Monotone conditional accessibility implies FOSD | Exact theorem | T3 | E1 | Measure-theoretic |
| Recognition effect decomposes into trajectory and conditioning terms | Exact theorem | T4 | E3 | Policy model |
| Policy–QBS interaction sign is controlled by improvement/accessibility covariance | Exact theorem | T5 | E4 | Policy model |
| Adaptive rescue can make policy and QBS partially substitutive | Exact sufficient condition + simulation | C5.1 | E4 | Agent mechanism |
| Learned predictive structure can create positive outcome-accessibility alignment | Simulation-supported | — | E2 | Agent mechanism |
| Shared recognition can create cross-copy decision coherence | Simulation-supported | branch-map extension | E5 | Hierarchical branch model |
| Separate observers have separately normalized FP measures | Exact once separate accessibility functions are assumed | supplementary | historical multi-observer simulations | Observer-indexed model |
| Everett self-location is represented by the QBS accessibility bridge | Assumption | propositions/boundaries | none can establish it physically | Open physical mapping |

## Main value decomposition

For general pre- and post-recognition accessibility maps:

$$
V_1-V_0
=
E[U_1-U_0]
+
Q(U_1,S_1)-Q(U_0,S_0),
$$

where:

$$
Q(U,S)
=
\frac{\operatorname{Cov}(U,S)}{E[S]}.
$$

For the baseline with no pre-recognition selector:

$$
S_0\equiv1,
$$

so:

$$
V_1-V_0
=
E[U_1-U_0]
+
\frac{\operatorname{Cov}(U_1,S_1)}{E[S_1]}.
$$

## What the core experiments establish

### E1

Shows that aligned accessibility changes conditional means and tails, verifies the FOSD direction under monotone accessibility, and includes null/counterexample cases.

### E2

Shows that positive alignment need not be inserted as an external correlation parameter: a small model that can represent the relevant nonlinear structure can learn a predictive signal, while a misspecified model fails.

### E3

Uses paired primitive randomness to separate ordinary trajectory changes from first-person conditioning changes.

### E4

Tests both the fixed-selector interaction identity and the more general selector-map-shift decomposition.

### E5

Separates marginal FP uplift from cross-copy recognition and action correlation. Sharedness and marginal prevalence are treated as distinct variables.

## Main unresolved bridge

The central unresolved physical question is whether Everettian first-person self-location should be represented by an accessibility weight of the form:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

The repository treats this as an explicit bridge assumption rather than a theorem.

## Falsification structure

The framework has clear failure modes:

- If accessibility is independent of outcome, pure weighting uplift is zero in expectation.
- If conditional accessibility is nonmonotone, FOSD can fail.
- If recognition changes neither trajectory nor accessibility, recognition effect is zero.
- If expected accessibility is zero, the normalized FP measure is undefined.
- If the Everett bridge is rejected, the measure-theoretic identities remain true but their physical interpretation does not follow.
