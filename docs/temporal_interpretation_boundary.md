# Temporal interpretation boundary

This document separates three distinct ideas that must not be conflated in QBS-style observer models:

1. retrospective restriction of a future-weighted measure to an earlier state;
2. a past-adapted latent transition or accessibility process;
3. the later empirical sequence generated after that latent state has changed.

The key correction is that **past-adapted does not mean that the future sequence is fixed in advance**. The future remains unrealized. A past-dependent latent transition may instead change the conditional law from which later observations are generated.

## 1. Retrospective weighted description

The normalized weighted measure can be restricted to a present-state variable `Z_t` even when the accessibility weight `S_T` is defined on a later continuation:

```math
P_{FP}(Z_t\in A)
=
\frac{E[\mathbf 1_{\{Z_t\in A\}}S_T]}{E[S_T]}.
```

This is an exact change-of-measure identity once the weighted measure is adopted. It can be used retrospectively to describe how earlier states are represented inside a future-weighted ensemble.

It does **not** by itself imply that a future outcome causally determines or changes the earlier observer state.

## 2. Past-adapted latent transition

Let `H_t` denote the record/history available by time `t`, and let `I_t` denote a latent observer/continuation state in a candidate model.

A past-adapted transition has the form

```math
I_{t+1}
\sim
K_t(\cdot\mid I_t,H_t),
```

where the transition kernel depends on the state and history available by `t`, not on later realized outcomes.

The temporal direction is therefore

```math
(H_t,I_t)
\longrightarrow
I_{t+1}
\longrightarrow
\mathcal L(Y_{t+1:T}\mid H_t,I_{t+1})
\longrightarrow
Y_{t+1:T},
```

not

```math
Y_{t+1:T}
\longrightarrow
I_{t+1}.
```

The later sequence `Y_{t+1:T}` is **not fixed at time `t`**. It remains stochastic or otherwise unrealized according to the candidate dynamics. What can differ after a latent transition is the conditional distribution of that future sequence.

## 3. Consciousness gaps and observational equivalence

During an interval with no reportable conscious observation, such as ordinary sleep, more than one latent continuity description may be compatible with the same available record before and after the interval.

If two candidate latent transitions produce the same observable record through the end of the gap, the transition itself is not directly observable from that record. This underdetermination is symmetric:

- it does not prove that a branch switch, observer reassignment, or other latent transition occurred;
- it also does not prove that one continuity ontology is uniquely identified by the absence of an experienced switch.

However, observational equivalence **at the gap boundary** does not imply equivalence of the entire later process. Two latent continuations can agree on the currently available record while having different later conditional laws:

```math
\mathcal L(Y_{t+1:T}\mid H_t,I^{(1)}_{t+1})
\neq
\mathcal L(Y_{t+1:T}\mid H_t,I^{(2)}_{t+1}).
```

In that case the latent transition remains individually unobserved, while longitudinal data can still contain statistical information about which transition model better describes the population or sequence law.

## 4. Later data are evidence about a model, not retroactive causes

Later observations may update our **inference** about which latent model or transition law is more compatible with the data. That is ordinary statistical smoothing or model comparison.

This should not be confused with saying that the later realized outcome caused the earlier transition.

Accordingly, the model permits

```math
\text{later sequence}
\longrightarrow
\text{later statistical evidence about a transition model},
```

while rejecting the causal reading

```math
\text{later realized outcome}
\longrightarrow
\text{earlier latent transition}.
```

This distinction also means that an individual later favorable history does not, by itself, prove that a favorable latent transition occurred. The relevant empirical object is the distribution or sequential structure across repeated observations, people, or comparable histories.

## 5. Underdetermination is not unconstrained freedom

Observational non-identification does not permit arbitrary latent stories. A candidate observer model still needs a coherent specification of:

- its state space;
- its transition/accessibility rule;
- the dependence of that rule on past history;
- normalization and support conditions;
- sequential coherence;
- cross-context restrictions where claimed;
- the induced law of later observable sequences.

These constraints can be estimated, compared, stress-tested, and potentially rejected. They do **not** require the realized future trajectory to be specified or determined in advance.

Thus:

```math
\text{underdetermined transition}
\neq
\text{arbitrary explanation}.
```

## 6. Empirical consequence

The latent transition itself may be unobservable at the moment it occurs, yet the model can still have later empirical consequences if different latent states induce different longitudinal laws.

The companion note [`../supplementary/prospective_recognition_protocol.md`](../supplementary/prospective_recognition_protocol.md) therefore treats recognition-follow-up as a longitudinal model-identification problem. It asks whether the post-recognition sequence is better described by a specified history-dependent latent-transition/accessibility model than by ordinary policy, expectancy, survivorship, and classical-selection alternatives.

The protocol does **not** require the realized future sequence to have been fixed in advance. It also does not identify an individual hidden transition merely because a later outcome was favorable.

## Non-claims

This boundary does not claim that observer switching occurs during sleep, that consciousness controls quantum branching, that future outcomes causally alter the past, that a favorable later outcome proves a hidden switch, or that ordinary identity continuity is false.

It states only that a past-dependent latent transition can be observationally invisible when it occurs while still changing the probability law of later observations, and that this distinction can in principle be investigated statistically without treating the future as predetermined.
