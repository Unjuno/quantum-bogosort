# Prospective recognition-longitudinal protocol

This unnumbered supplementary protocol specifies how a recognition-dependent observer model could be tested prospectively without using later favorable outcomes to relabel earlier self-location. It is not T6, S2.14, E6, or evidence for an Everett/QBS physical bridge.

## H — hypotheses and temporal restriction

Let `H_t` denote the information/history available by time `t`. Any recognition, policy, self-location, or observer-model state used to generate the next prediction must be adapted to the past and present information available at that time.

The protocol therefore forbids defining an earlier self-location state by conditioning on later realized outcomes. Formally, a prospective state or decision rule at time `t` must be measurable with respect to the predeclared information set `H_t`, not with respect to a larger sigma-field containing future outcomes.

This restriction separates two uses of future data:

1. **allowed**: future observations are used later to score a prediction that was fixed at time `t`;
2. **not allowed**: future observations are used to redefine what the observer state at time `t` supposedly was.

Thus favorable later history cannot by itself certify that an unobserved observer switch, branch transition, or favorable self-location change occurred earlier.

## Recognition exposure and longitudinal assignment

A weak design follows only people who independently chose to recognize or adopt the framework. That design is vulnerable to baseline selection, expectancy, reporting, survivorship, and policy differences.

A stronger design externally assigns **exposure** to a recognition intervention. For example:

- `Z=1`: a predeclared QBS/observer-selection explanation;
- `Z=0`: a matched control explanation with similar complexity, attention, and expectancy but without the target observer-selection claim.

The primary causal analysis should use assignment `Z` (intention-to-treat) rather than conditioning only on participants who subsequently report successful recognition. Post-assignment recognition/understanding can be measured as a secondary mediator or compliance variable, but conditioning on it can itself create selection bias.

Baseline covariates, behavior, information acquisition, attrition, and exposure timing should be recorded prospectively.

## Sequential outcome model

Let `Y_{t+1}` denote the next predeclared longitudinal outcome or outcome increment. Before observing `Y_{t+1}`, the competing models specify conditional predictive laws

```math
P_{1,t}(\cdot\mid H_t)
\qquad\text{and}\qquad
P_{0,t}(\cdot\mid H_t),
```

for the candidate QBS/observer model and a predeclared null model.

The realized sequence can then be scored by the cumulative log likelihood ratio

```math
L_T
=
\sum_{t=0}^{T-1}
\log
\frac{dP_{1,t}}{dP_{0,t}}(Y_{t+1}).
```

This is standard sequential model comparison. It is useful only when the competing conditional laws and stopping/analysis rules are specified before the outcomes being scored. Positive realized `L_T` is evidence relative to the chosen null, not proof of an Everett mechanism; misspecified alternatives can both be wrong.

## Separating ordinary policy effects from innovation

The recognition intervention can alter ordinary behavior. Therefore a favorable post-recognition trajectory is not by itself evidence for observer selection.

Relative to the predeclared information filtration, decompose

```math
m_{t+1}
=
E[Y_{t+1}\mid H_t],
\qquad
\varepsilon_{t+1}
=
Y_{t+1}-m_{t+1}.
```

Then cumulative outcome can be separated into

```math
A_T
=
\sum_t m_{t+1},
\qquad
M_T
=
\sum_t \varepsilon_{t+1}.
```

The prospective experiment should distinguish at least:

- changes in `A_T` attributable to ordinary policy, effort, information, risk exposure, or treatment effects;
- changes in the distribution of `M_T`, the decision-time-unpredictable residual under the declared filtration.

If recognition improves only the predictable component, ordinary policy improvement remains sufficient. A stronger observer-selection model must state in advance what residual/innovation pattern, if any, should differ after conditioning on the declared behavioral and baseline information.

Innovation is filtration-relative. Enlarging `H_t` can move variation from `M_T` into `A_T`; therefore the information set used for this decomposition must be preregistered or otherwise fixed before the scored outcomes.

## Required nulls

At minimum, the longitudinal design should compare against:

1. a fixed-policy/no-recognition baseline;
2. an adaptive history-dependent policy without a QBS-awareness term;
3. a behavior-matched Bayesian/RL or equivalent-information model;
4. a matched expectancy/placebo exposure;
5. explicit survivorship/attrition and missing-data models;
6. classical selection/ascertainment models with comparable degrees of freedom;
7. a candidate observer-accessibility model only if it supplies additional predeclared predictions.

The null set must not be weakened after observing the favorable trajectories.

## Attrition and survivorship

Loss to follow-up, nonresponse, death, incapacitation, selective reporting, or retrospective exclusion can induce exactly the kind of selected longitudinal sample that the project is trying to distinguish from an observer-selection mechanism.

Therefore the protocol should:

- define the analysis population before follow-up;
- preserve randomized assignment in the primary analysis;
- report attrition by assignment and baseline strata;
- avoid dropping unfavorable or incomplete trajectories merely because they are hard to classify;
- use explicit sensitivity models when outcome observability depends on post-assignment state;
- distinguish missing records from zero/negative outcomes and from genuine observer-accessibility assumptions.

A survivorship-only dataset cannot by itself identify an Everett/QBS mechanism.

## Consciousness gaps and observer continuity

Periods without reportable conscious observation, such as ordinary sleep, can create an interval over which multiple latent continuity/identity descriptions are observationally equivalent at the level of the available record.

This protocol does **not** infer a branch switch or observer reassignment from such a gap. Nor does it assume that ordinary continuity is empirically identified solely because no switch was experienced.

Instead, it treats the continuity ontology as underdetermined whenever competing latent descriptions induce the same prospectively observable history. Empirical leverage must come from additional predeclared longitudinal predictions, not from retrospective reinterpretation of a later favorable outcome.

Accordingly:

```math
\text{observational underdetermination}
\neq
\text{unconstrained mechanism}.
```

Any candidate latent transition or accessibility rule must still obey its own normalization, temporal-adaptation, sequential-coherence, and cross-context constraints.

## Preregistration / failure criteria

Before scoring the longitudinal sequence, the study should specify:

- assignment and exposure procedure;
- baseline variables and information filtration `H_t`;
- primary outcomes and observation schedule;
- what counts as predictable versus innovation variation;
- competing conditional predictive models;
- attrition and missing-data handling;
- stopping rule or sequential evidence boundary;
- multiplicity correction where several outcomes/model variants are tested;
- explicit outcomes that would count against the candidate observer model.

A candidate model should be revised or rejected if its preregistered predictive law repeatedly underperforms a comparably constrained null on held-out future observations, or if its supposed success disappears after controlling the predeclared ordinary-policy, expectancy, attrition, and selection channels.

## C — current conclusion

The framework is not forced to remain purely retrospective or metaphysical. A concrete recognition-dependent observer model can, in principle, generate prospective longitudinal predictions that are scored after recognition/exposure.

However, this does not make the latent ontology itself directly observable. The empirical object is the **future sequence predicted in advance**, not a post hoc claim about which unobserved continuation the observer occupied.

The strongest currently defensible experimental direction is therefore:

```math
\text{externally assigned recognition exposure}
+
\text{predeclared sequential predictions}
+
\text{behavior/expectancy controls}
+
\text{attrition/selection controls}
+
\text{predictable-versus-innovation decomposition}
+
\text{held-out scoring}.
```

## U — unresolved / non-claims

- A favorable post-recognition sequence does not by itself prove observer selection.
- Recognition assignment may change ordinary behavior, beliefs, effort, risk, and information acquisition; these are ordinary causal channels unless an additional residual prediction is specified.
- Failure of a classical null does not uniquely identify Everett.
- Failure to distinguish latent continuity descriptions during sleep or another consciousness gap does not prove branch switching.
- Later favorable outcomes cannot be used to retroactively define earlier self-location under the past-adapted protocol.
- No claim is made here that human consciousness causes branching, controls branch choice, changes objective quantum probabilities, or guarantees favorable continuation.

## Error check

The protocol is deliberately asymmetric in time: predictions may use the recorded past to constrain the future, while realized future outcomes only score those prior predictions. This prevents retrospective self-location relabeling from making the model unfalsifiable.
