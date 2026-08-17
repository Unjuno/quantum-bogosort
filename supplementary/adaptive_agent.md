# Adaptive-Agent Mechanism

## Motivation

A major objective is to avoid treating score/outcome correlation as an arbitrary external parameter. In an adapted agent, predictive structure can arise from the agent's learned internal model of the environment.

## Definitions

Let:

- `X_t` be the environment/world state,
- `B_t` be the internal belief or world-model state,
- `Y_t` be an evaluation signal derived from the internal model,
- `U_T` be a later outcome.

Adaptation can be represented by predictive information:

$$
I(B_t;X_t)>0.
$$

If the environment has temporal structure:

$$
I(X_t;U_T)>0,
$$

then the internal model can carry information about later outcomes.

## Ordering condition

A useful calibration condition is that:

$$
E[U_T\mid Y_t=y]
$$

is nondecreasing in `y`.

If accessibility is also nondecreasing in the evaluation signal, the outcome/accessibility covariance is naturally pushed in the positive direction under the corresponding regularity conditions.

## Mechanism

The preferred causal interpretation is:

$$
\text{world adaptation}
\longrightarrow
\text{predictive internal model}
\longrightarrow
\text{ordered evaluation signal}
\longrightarrow
\text{outcome-aligned accessibility}.
$$

## Experiment

E2 provides a minimal nonlinear example. A model that can represent the relevant interaction learns a predictive signal and produces positive weighted uplift; a misspecified linear model and random control do not.

Paired endogenous-agent simulations also show the same qualitative structure when policy itself changes trajectories.

## Limitations

Adaptation alone does not mathematically guarantee positive Pearson correlation. The claim requires assumptions about environmental persistence, model quality, calibration, and how accessibility depends on the learned signal.

## Open theorem direction

A stronger result would connect information and monotone calibration conditions to a sufficient condition for:

$$
\operatorname{Cov}(U_T,S_T)>0.
$$

## Status

**SIMULATION-SUPPORTED mechanism. Formal information-to-covariance theorem OPEN.**
