# Supplementary Research Notes

This file preserves important results and modeling directions developed during the QBS research process that are not part of the five-experiment core release. The notes distinguish exact mathematical identities, simulation findings, and interpretation-level hypotheses.

## 1. Multi-observer normalization

For observer index `i`, define the first-person measure separately:

```math
d\mu_i^{FP}
=
\frac{S_i}{E[S_i]}
\,d\mu.
```

Each observer has a separately normalized first-person distribution. These distributions are not shares of one common probability budget and therefore are not required to sum across observers.

This matters in shared zero-sum worlds: several observers can each assign high first-person probability to their own favorable outcome without implying that the corresponding shared-world events are jointly likely.

**Status:** exact consequence of observer-specific normalization once separate accessibility functions are admitted.

## 2. Minimal binary soft-QBS model

Let the prior favorable probability be `p`. Give favorable branches accessibility weight 1 and unfavorable branches weight `lambda`. Then:

```math
p_{FP}
=
\frac{p}{p+(1-p)\lambda}.
```

A provisional execution/leakage parameterization used in early simulations was:

```math
\lambda
=
1-q(1-\alpha).
```

For positive execution strength and nontrivial selectivity:

```math
q>0,
\qquad
\alpha<1,
```

which implies:

```math
p_{FP}>p.
```

The interpretation of `alpha` is model-specific and should not be promoted to a universal physical parameter.

**Status:** exact within the binary weighting model; physical interpretation remains open.

## 3. Repeated adverse-trigger weighting

For a repeated process, let `N_B` count adverse triggers and define:

```math
S=\lambda^{N_B}.
```

Then the weighted value is:

```math
V(\lambda)
=
\frac{E[U\lambda^{N_B}]}{E[\lambda^{N_B}]}.
```

Differentiation with respect to log selectivity gives:

```math
\frac{dV}{d\log\lambda}
=
\mathrm{Cov}_{\lambda}(U,N_B).
```

This identity was numerically verified in the exploratory experiments.

**Status:** exact differentiable identity under the stated finite-expectation conditions.

## 4. Accessible-measure decay and extinction boundary

Repeated filtering can make total accessible measure small even when the normalized first-person mean remains finite. The normalized measure requires:

```math
E[S]>0.
```

At:

```math
E[S]=0,
```

the normalized first-person measure is undefined rather than merely low-valued.

This distinction is retained in the core theorem set.

**Status:** exact boundary condition.

## 5. Gaussian minimal model

An exploratory closed-form model used jointly standard normal outcome and score variables with correlation `rho`. Let accessibility equal 1 for nonnegative score and `lambda` for negative score. The first-person mean is:

```math
E_{FP}[L]
=
\frac{2(1-\lambda)\rho}
{(1+\lambda)\sqrt{2\pi}}.
```

Under the provisional parameterization:

```math
\lambda=1-q(1-\alpha),
```

this becomes:

```math
E_{FP}[L]
=
\frac{2q(1-\alpha)\rho}
{[2-q(1-\alpha)]\sqrt{2\pi}}.
```

Monte Carlo simulations matched the analytic expression.

**Status:** exact for this Gaussian toy model; not a general Everett prediction.

## 6. Endogenous predictive correlation in adapted agents

A central research direction replaced an exogenous correlation parameter with a learned internal world model.

Let:

- `X_t` be the world state,
- `B_t` be the agent's internal belief/world-model state,
- `Y_t` be an evaluation signal derived from the internal model,
- `U_T` be a later outcome.

Adaptation can be represented by predictive information such as:

```math
I(B_t;X_t)>0.
```

If the world has temporal structure:

```math
I(X_t;U_T)>0,
```

then an adapted belief state can carry information about later outcomes. If the evaluation signal is directionally calibrated, a useful sufficient ordering condition is that:

```math
E[U_T\mid Y_t=y]
```

is nondecreasing in `y`. If accessibility is also nondecreasing in the evaluation signal, positive outcome-accessibility covariance follows under the corresponding monotonicity conditions.

The preferred causal interpretation is:

```math
\text{world adaptation}
\longrightarrow
\text{predictive internal model}
\longrightarrow
\text{ordered evaluation signal}
\longrightarrow
\text{outcome-aligned accessibility}.
```

**Status:** mechanism hypothesis plus supporting classical-agent simulations. Adaptation alone does not guarantee positive Pearson correlation without additional calibration and environment assumptions.

## 7. Evidence-driven recognition activation

An exploratory experiment estimated positive score/outcome correlation from calibration data and activated the QBS policy only when a one-sided Fisher-transform confidence bound was positive.

The research question was whether recognition should be modeled as an endogenous evidence threshold rather than a fixed external switch:

```math
\text{data}
\longrightarrow
\widehat{\rho}
\longrightarrow
\text{confidence}
\longrightarrow
q
\longrightarrow
S
\longrightarrow
\mu^{FP}.
```

In the exploratory Monte Carlo study, weak true correlations required much larger calibration samples than strong correlations before activation became reliable.

A future extension is to make recognition time a stopping time:

```math
\tau_{\mathrm{recognition}}
=
\inf\{t:\text{evidence criterion is satisfied at time }t\}.
```

**Status:** simulation-supported modeling direction; not part of the five core experiments.

## 8. Selectivity frontier

Positive predictor/outcome correlation does not imply that maximally aggressive selection is optimal when prediction is imperfect. In exploratory simulations, increasingly selective thresholds initially improved first-person outcomes but eventually produced an interior optimum.

The general lesson is that selection strength interacts with predictor precision and surviving accessible measure. This is a model-selection tradeoff, not evidence against the monotone-accessibility theorem: the theorem concerns the ordering induced by a fixed accessibility function, whereas the frontier compares different accessibility functions.

**Status:** simulation result in toy models.

## 9. Branch-wide recognition and decision correlation

Recognition may be represented as a branch-indexed field rather than only a scalar marginal probability:

```math
R=R(\omega).
```

Actions are then generated by:

```math
A(\omega)
=
\pi_{R(\omega)}(B(\omega)).
```

This separates three quantities:

```math
P(R=1),
```

```math
\mathrm{Corr}(R_i,R_j),
```

and:

```math
\mathrm{Corr}(A_i,A_j).
```

The cross-branch experiments show that recognition correlation and shared environmental structure can change the decision-map correlation even when single-observer marginal first-person uplift changes little.

**Status:** classical correlated-copy simulation result; Everett mapping requires the separate bridge assumption.

## 10. What is deliberately not claimed

The mathematical framework does not establish that an external random-number generator becomes objectively lucky, nor does it establish the Everett accessibility bridge assumption. Pure reweighting also cannot create support that was absent under the fixed-policy base measure.

The intended separation is:

```math
\text{measure-theoretic theorem}
\neq
\text{classical simulation}
\neq
\text{Everett physical claim}.
```

These layers should remain distinct in later manuscript drafts.
