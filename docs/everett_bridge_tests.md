# Everett-QBS Bridge: Support, Constraint, and Rejection Criteria

## Purpose

The abstract QBS theorems require only a base measure and a nonnegative accessibility weight. An Everettian physical interpretation requires the additional bridge:

```math
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
```

This document states what would count as progress toward a physically serious bridge and what would count against it.

The bridge must not be described as an empirically confirmed physical law merely because the normalized weighting mathematics is internally consistent. The selection-equivalence result in [`../supplementary/selection_equivalence.md`](../supplementary/selection_equivalence.md) further shows that the weighted law itself has classical ascertainment / record-size-bias representations, so reproducing that law is not sufficient evidence for an Everettian mechanism.

## 1. Three levels of status

### Level A — abstract change of measure

At the mathematical level, `S_pi` is simply a nonnegative measurable weight with:

```math
0<E[S_\pi]<\infty.
```

This level is exact once the definitions are adopted.

### Level B — observer-model bridge

A stronger claim identifies `S_pi` with a quantity derived from a model of observers, records, persistence, or self-location in a branching theory.

This requires more than choosing a weight that gives desirable first-person outcomes and more than reproducing a distribution that can be matched by ordinary ascertainment.

### Level C — physical Everett bridge

The strongest claim identifies the observer-model weight with a physically justified first-person measure in Everettian quantum mechanics and explains its relation to decoherence, branch amplitude, Born-rule probability, and empirical confirmation.

The current project has not reached Level C.

## 2. Structural requirements for a defensible bridge

A candidate physical `S_pi` should satisfy at least the following constraints.

### 2.1 Nonnegativity and normalizability

```math
S_\pi(\omega)\ge0,
```

and:

```math
0<E_\mu[S_\pi]<\infty.
```

Failure makes the normalized first-person measure invalid.

### 2.2 Absolute continuity with respect to the physical base measure

The QBS bridge as currently written implies:

```math
\mu^{FP}_\pi\ll\mu.
```

A candidate implementation that assigns positive first-person probability to an event of zero base measure is incompatible with the present bridge and must either be rejected or formulated as a different model.

### 2.3 Representation invariance

Equivalent descriptions of the same physical observer/branch structure should not generate different first-person predictions merely because of relabeling, coordinate changes, or arbitrary branch bookkeeping.

If a branch is subdivided into mathematically redundant labels without a physical change, the induced observer measure should remain invariant after appropriate aggregation.

### 2.4 Coarse-graining consistency

For a coarse event `A` decomposed into physically meaningful disjoint subevents:

```math
A=\bigcup_i A_i,
```

first-person mass should aggregate consistently:

```math
\mu^{FP}(A)
=
\sum_i\mu^{FP}(A_i)
```

for countable disjoint decompositions in the probability space.

A proposed accessibility rule that changes predictions under arbitrary refinement of branch labels is structurally suspect.

### 2.5 No utility-by-definition circularity

Accessibility must not be defined as a monotone function of the outcome utility solely in order to guarantee favorable first-person results.

A physically meaningful bridge should specify `S_pi` from observer/branch physics or an independently motivated self-location rule. Otherwise:

```math
S=f(U)
```

is only a selection model, not an explanation of why Everettian self-location follows that selection.

### 2.6 Sequential consistency

If first-person conditioning is applied at multiple times, one-shot and sequential conditioning should be compatible with the proposed observer dynamics. A physical bridge should explain how accessibility updates when records, observer states, and branch structure evolve.

The stopping-time and recursive formulations in the supplementary material make this requirement explicit but do not solve it physically.

### 2.7 Compatibility with no-signaling and established quantum statistics

A physical implementation must not permit operational signaling or third-person outcome-frequency changes that contradict standard quantum mechanics unless it explicitly proposes and tests new physics.

The current abstract QBS framework changes policy trajectories and first-person weighting; it does not alter the external random generator or the base physical measure by definition.

### 2.8 Distinguishability from a behavior-matched classical selection null

For bounded `S_pi`, a classical ascertainment model can record a base trajectory with conditional probability proportional to `S_pi` and reproduce exactly the same normalized observer-conditioned law. For general integrable `S_pi`, a classical record-multiplicity model can reproduce the same law exactly through size bias.

Therefore a physical bridge is not identified merely by matching:

```math
\mu^{FP}_\pi(B)
=
\frac{E_\mu[\mathbf 1_BS_\pi]}{E_\mu[S_\pi]}.
```

A candidate bridge should specify at least one additional constraint or prediction not freely reproducible by choosing a behavior-matched classical selection channel. Examples include a physically derived functional dependence of `S_pi` on independently measurable quantum variables, intervention responses fixed before outcome observation, or sequential transition restrictions that differ from the classical null.

### 2.9 Cross-context restriction rather than context-by-context refitting

Varying policy or experimental context does not by itself identify the bridge. If a classical null is allowed to choose an unrestricted selection function separately in each context, then every target observer law `Q_c` that is absolutely continuous with respect to its base law `mu_c` has an exact classical record-size-biased representation.

Accordingly, a serious bridge must state **before seeing the selected outcomes** what structure is shared across contexts. Examples include:

- one functional law for `S_pi` with parameters shared across policies;
- an invariance relation under physically equivalent interventions;
- a fixed observer-state transition rule;
- dependence on independently measured physical variables with a predeclared functional form.

The comparison must be symmetric: an Everett model cannot be allowed arbitrary policy-specific `S_pi` while the classical null is forbidden comparable policy dependence unless that asymmetry follows from independent physical assumptions.

### 2.10 Operational identifiability of the proposed restriction

A mathematical cross-context restriction is not automatically an empirical test. For density-ratio restrictions such as those in the selection-equivalence note, the relevant base and observer-conditioned laws must be identifiable on a common state space.

In particular, a proposed test should state:

1. which state or observable is aligned across contexts;
2. how the base law is known or estimated independently of the selected observer sample;
3. how the observer-conditioned law is estimated;
4. whether the claimed restriction survives projection from latent branch states to the actually observed records.

If only a context-dependent projection of a latent state is observed, a violation that exists on the latent branch space may disappear after projection. Conversely, observed distribution changes may come from policy-dependent trajectory maps or base-law changes even under a shared latent selection rule. Such cases do not falsify the shared-selection mechanism without additional identification arguments.

## 3. What would support the bridge

The following would strengthen the Everett interpretation without by themselves proving it.

### 3.1 Independent derivation of accessibility

A model derives `S_pi` from observer persistence, records, decoherence structure, or another independently specified physical quantity rather than from desired utility.

### 3.2 Agreement across equivalent observer descriptions

Different physically equivalent representations lead to the same normalized first-person predictions.

### 3.3 Connection to established Everett probability accounts

A candidate bridge explains whether `S_pi`:

- modifies a Born-weight base measure;
- represents additional conditional self-location within a Born-weighted branch space;
- is reducible to an already established self-locating rule;
- or predicts a genuine departure from standard Everettian credence.

These possibilities must not be conflated.

### 3.4 New quantitative predictions from a physical `S`

If a concrete observer model fixes `S_pi` before outcomes are examined, it may generate quantitative predictions that can be compared with data or with established quantum statistics.

Only at this stage does the bridge approach an independently testable physical hypothesis.

### 3.5 Survival of the classical selection-equivalence challenge

A stronger bridge supplies information that the behavior-matched classical selection null does not. This can occur if the physical theory constrains `S_pi` across multiple interventions, times, observables, or equivalent descriptions so that the competing classical null cannot independently retune its selection channel for each case without violating a predeclared model.

Evidence counts for the bridge only to the extent that competing models are specified before the relevant observations and make different predictions.

### 3.6 Out-of-context prediction under a shared structural law

A particularly informative test would fit or specify a low-dimensional bridge law in one set of contexts and then predict observer-conditioned data in held-out contexts without retuning the accessibility mechanism.

Such success would still not uniquely identify Everett unless competing classical structural models fail the same held-out test, but it would provide more information than post hoc context-by-context weighting.

## 4. What would constrain or reject a candidate bridge

A particular physical bridge should be rejected or revised if any of the following occurs.

### 4.1 Non-normalizability

```math
E[S_\pi]=0
```

or:

```math
E[S_\pi]=\infty
```

in the domain where a normalized first-person distribution is claimed.

### 4.2 Dependence on arbitrary branch labeling

Physically equivalent refinements or relabelings produce different observer probabilities without a corresponding physical difference.

### 4.3 Positive mass on base-null events

The proposed rule contradicts the absolute-continuity structure of the current bridge.

### 4.4 Conflict with established operational quantum predictions

If a physical model predicts observable frequencies or signaling behavior incompatible with well-tested quantum mechanics, the model is empirically disfavored unless such deviations are observed.

### 4.5 Purely post hoc utility fitting

If `S_pi` is chosen after observing outcomes or tuned directly to utility without an independent observer model, the result does not support the Everett bridge. It only demonstrates the abstract selection identity.

### 4.6 Inconsistent sequential self-location

If repeated conditioning yields incompatible probabilities depending on arbitrary choice of temporal partition or bookkeeping, the proposed observer measure requires revision.

### 4.7 No predictive content beyond behavior-matched ascertainment

If every claimed bridge success consists only of reproducing an observer-conditioned law that a predeclared classical ascertainment/record-size-bias model also reproduces, then the evidence does not identify the physical bridge. The bridge may remain an interpretation, but it has not acquired distinct empirical support.

### 4.8 Context-by-context retuning masquerading as prediction

If a purported cross-policy or cross-experiment success is obtained by fitting an unrelated accessibility function after seeing the selected data in each context, the result does not survive the context-indexed classical no-go. It is descriptive fit, not mechanism identification.

### 4.9 Non-operational identifying restriction

If a claimed identifying restriction is formulated only on an unobserved latent branch state and no argument connects that restriction to identifiable base and selected observable laws, failure or success of the proposed statistic cannot be interpreted as a bridge test.

## 5. Empirical falsifiability versus interpretive underdetermination

There is an important distinction between a bridge that predicts new physical observations and a bridge that only reinterprets first-person credence while preserving all standard Born statistics.

If the bridge is constructed so that every operational prediction agrees with standard Everettian quantum mechanics and with a behavior-matched classical selection account of the observer-conditioned data, then the bridge is empirically underdetermined by those observations. In that case it should be evaluated as an interpretive/self-location proposal using coherence, derivability, invariance, and explanatory criteria rather than advertised as independently falsifiable new physics.

Multiple contexts do not remove this underdetermination when the competing null can retune its selection channel separately in every context. A genuine cross-context test needs a predeclared structural restriction shared across contexts, plus enough observable information to identify the quantities entering that restriction.

If a concrete physical `S_pi` predicts deviations from competing models in observer frequencies, intervention responses, sequential record statistics, or other operational quantities, those differences create genuine empirical tests.

Therefore the statement:

> "QBS is falsifiable"

must always specify **which layer** is meant:

- theorem assumptions can be mathematically violated or experimentally instantiated in toy models;
- a proposed observer model can fail structural consistency or classical-null distinguishability tests;
- a cross-context structural model can fail held-out or density-ratio restrictions when those quantities are identifiable;
- a physical Everett bridge becomes empirically falsifiable only when it makes observations differ from competing physical accounts.

## 6. Relation to the existing literature

Everettian probability has multiple competing foundations: decision-theoretic derivations, caring-measure accounts, self-locating uncertainty, branch/chance accounts, observer-selection mechanisms, and explicit critiques of those programs. Classical statistics separately has a long ascertainment and weighted-distribution literature showing how unequal observation propensities create weighted encountered distributions.

Sample-selection and missing-not-at-random literatures provide a further methodological analogue: nonrandom observation mechanisms are generally not identified from selected data without additional model structure, exclusion restrictions, instruments, auxiliary variables, or other independently justified information. This analogy supports the need for explicit identifying restrictions; it does not establish the QBS bridge.

The existence of these literatures means QBS cannot treat a policy-dependent accessibility map as the default Everett probability rule or treat normalized observer weighting as uniquely quantum.

The current bridge must instead be positioned as a conditional extension whose physical justification remains to be supplied.

See:

- `literature/prior_art.md`
- `literature/extended_prior_art.md`
- `supplementary/selection_equivalence.md`
- `paper/references.bib`

## 7. Current project status

The Everett-QBS bridge is retained as:

**A CLEARLY LABELED CONDITIONAL INTERPRETATION, NOT A DERIVED PHYSICAL RESULT. THE NORMALIZED WEIGHTED LAW ALONE IS CLASSICALLY SELECTION-EQUIVALENT; ARBITRARY CONTEXT-SPECIFIC OBSERVER LAWS REMAIN CLASSICALLY REPRESENTABLE IF THE NULL MAY RETUNE BY CONTEXT. PHYSICAL IDENTIFICATION REQUIRES PREDECLARED CROSS-CONTEXT STRUCTURE AND AN OPERATIONALLY IDENTIFIABLE TEST.**

A future revision may strengthen, replace, or reject the bridge without invalidating T1–T5 or the classical E1–E5 simulations.

## ERROR CHECK

1. Structural coherence is not the same as empirical confirmation.
2. Agreement with Born statistics does not uniquely establish the QBS bridge.
3. Agreement with the normalized weighted observer law does not distinguish the bridge from a behavior-matched classical selection model.
4. Observing multiple contexts does not identify the mechanism if the null can retune selection freely by context.
5. A shared-selection density-ratio restriction is not operational unless base and selected laws are identifiable on a common observable state space.
6. A physically derived accessibility map must be independent of post hoc utility fitting.
7. The current bridge cannot create positive mass on base-null events.
8. Probability-law equivalence does not imply physical or causal equivalence of mechanisms.
9. A restriction imposed only on an inaccessible latent representation may have no empirical content after projection.
10. Physical rejection of the bridge does not refute the abstract weighted-measure theorems.
