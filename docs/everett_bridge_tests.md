# Everett-QBS Bridge: Support, Constraint, and Rejection Criteria

## Purpose

The abstract QBS theorems require only a base measure and a nonnegative accessibility weight. An Everettian physical interpretation requires the additional bridge:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

This document states what would count as progress toward a physically serious bridge and what would count against it.

The bridge must not be described as an empirically confirmed physical law merely because the normalized weighting mathematics is internally consistent.

## 1. Three levels of status

### Level A — abstract change of measure

At the mathematical level, `S_pi` is simply a nonnegative measurable weight with:

$$
0<E[S_\pi]<\infty.
$$

This level is exact once the definitions are adopted.

### Level B — observer-model bridge

A stronger claim identifies `S_pi` with a quantity derived from a model of observers, records, persistence, or self-location in a branching theory.

This requires more than choosing a weight that gives desirable first-person outcomes.

### Level C — physical Everett bridge

The strongest claim identifies the observer-model weight with a physically justified first-person measure in Everettian quantum mechanics and explains its relation to decoherence, branch amplitude, Born-rule probability, and empirical confirmation.

The current project has not reached Level C.

## 2. Structural requirements for a defensible bridge

A candidate physical `S_pi` should satisfy at least the following constraints.

### 2.1 Nonnegativity and normalizability

$$
S_\pi(\omega)\ge0,
$$

and:

$$
0<E_\mu[S_\pi]<\infty.
$$

Failure makes the normalized first-person measure invalid.

### 2.2 Absolute continuity with respect to the physical base measure

The QBS bridge as currently written implies:

$$
\mu^{FP}_\pi\ll\mu.
$$

A candidate implementation that assigns positive first-person probability to an event of zero base measure is incompatible with the present bridge and must either be rejected or formulated as a different model.

### 2.3 Representation invariance

Equivalent descriptions of the same physical observer/branch structure should not generate different first-person predictions merely because of relabeling, coordinate changes, or arbitrary branch bookkeeping.

If a branch is subdivided into mathematically redundant labels without a physical change, the induced observer measure should remain invariant after appropriate aggregation.

### 2.4 Coarse-graining consistency

For a coarse event `A` decomposed into physically meaningful disjoint subevents:

$$
A=\bigcup_i A_i,
$$

first-person mass should aggregate consistently:

$$
\mu^{FP}(A)
=
\sum_i\mu^{FP}(A_i)
$$

for countable disjoint decompositions in the probability space.

A proposed accessibility rule that changes predictions under arbitrary refinement of branch labels is structurally suspect.

### 2.5 No utility-by-definition circularity

Accessibility must not be defined as a monotone function of the outcome utility solely in order to guarantee favorable first-person results.

A physically meaningful bridge should specify `S_pi` from observer/branch physics or an independently motivated self-location rule. Otherwise:

$$
S=f(U)
$$

is only a selection model, not an explanation of why Everettian self-location follows that selection.

### 2.6 Sequential consistency

If first-person conditioning is applied at multiple times, one-shot and sequential conditioning should be compatible with the proposed observer dynamics. A physical bridge should explain how accessibility updates when records, observer states, and branch structure evolve.

The stopping-time formulation in `supplementary/recognition_time.md` makes this requirement explicit but does not solve it physically.

### 2.7 Compatibility with no-signaling and established quantum statistics

A physical implementation must not permit operational signaling or third-person outcome-frequency changes that contradict standard quantum mechanics unless it explicitly proposes and tests new physics.

The current abstract QBS framework changes policy trajectories and first-person weighting; it does not alter the external random generator or the base physical measure by definition.

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

## 4. What would constrain or reject a candidate bridge

A particular physical bridge should be rejected or revised if any of the following occurs.

### 4.1 Non-normalizability

$$
E[S_\pi]=0
$$

or:

$$
E[S_\pi]=\infty
$$

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

## 5. Empirical falsifiability versus interpretive underdetermination

There is an important distinction between a bridge that predicts new physical observations and a bridge that only reinterprets first-person credence while preserving all standard Born statistics.

If the bridge is constructed so that every operational prediction agrees with standard Everettian quantum mechanics, then the bridge may be empirically underdetermined by ordinary experiments. In that case it should be evaluated as an interpretive/self-location proposal using coherence, derivability, and explanatory criteria rather than advertised as independently falsifiable new physics.

If a concrete physical `S_pi` predicts deviations from standard observer frequencies, record statistics, or other operational quantities, those deviations create genuine empirical tests.

Therefore the statement:

> "QBS is falsifiable"

must always specify **which layer** is meant:

- theorem assumptions can be mathematically violated or experimentally instantiated in toy models;
- a proposed observer model can fail structural consistency tests;
- a physical Everett bridge becomes empirically falsifiable only when it makes observations differ from competing physical accounts.

## 6. Relation to the existing literature

Everettian probability has multiple competing foundations: decision-theoretic derivations, caring-measure accounts, self-locating uncertainty, branch/chance accounts, observer-selection mechanisms, and explicit critiques of those programs. The existence of this literature means QBS cannot treat a policy-dependent accessibility map as the default Everett probability rule.

The current bridge must instead be positioned as a conditional extension whose physical justification remains to be supplied.

See:

- `literature/prior_art.md`
- `literature/extended_prior_art.md`
- `paper/references.bib`

## 7. Current project decision

For v0.2, the Everett-QBS bridge is retained as:

**A CLEARLY LABELED CONDITIONAL INTERPRETATION, NOT A DERIVED PHYSICAL RESULT.**

A future version may strengthen, replace, or reject the bridge without invalidating T1–T5 or the classical E1–E5 simulations.

## ERROR CHECK

1. Structural coherence is not the same as empirical confirmation.
2. Agreement with Born statistics does not uniquely establish the QBS bridge.
3. A physically derived accessibility map must be independent of post hoc utility fitting.
4. The current bridge cannot create positive mass on base-null events.
5. Physical rejection of the bridge does not refute the abstract weighted-measure theorems.
