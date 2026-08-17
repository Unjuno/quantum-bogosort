# QBS Research Map

This document links claims to proofs, experiments, statistical validation, and interpretation status.

## Core causal structure

$$
R
\longrightarrow
\pi_R
\longrightarrow
(U_R,S_R).
$$

Policies are compared on common primitive randomness whenever paired counterfactuals are used.

## Claim-to-evidence map

| Claim | Type | Mathematical source | Computational source | Interpretation status |
|---|---|---|---|---|
| FP mean shift equals normalized outcome/accessibility covariance | Exact theorem | T1 | E1 | Measure-theoretic |
| Tail shift has the same covariance form | Exact theorem | T2 | E1 | Measure-theoretic |
| Monotone conditional accessibility implies FOSD | Exact theorem | T3 | E1 | Measure-theoretic |
| Recognition effect decomposes into trajectory and conditioning terms | Exact theorem | T4 | E3 | Policy model |
| Policy–QBS interaction decomposes into targeting and selector-map effects | Exact theorem | T5 | E4 | Policy model |
| Adaptive rescue can make policy and QBS partially substitutive | Exact sufficient condition + simulation | C5.1 | E4 | Agent mechanism |
| Conditional-mean alignment plus score-measurable accessibility implies nonnegative covariance | Exact supplementary theorem | S2 | E2/E3 illustrate premises | Agent mechanism |
| Posterior-mean scores self-calibrate | Exact corollary | S2.2 | none required | Agent inference |
| Calibration error / prediction MSE yield population sufficient bounds | Exact sufficient bounds | S2.3–S2.4 | none required | Agent-learning layer |
| Bounded independent held-out data can certify covariance | Exact finite-sample theorem | S2.5 | none required | Statistical validation |
| Independent training and finite candidate selection can preserve coverage | Exact validity theorems | S2.6–S2.7 | none required | Statistical validation |
| Any valid five-moment simultaneous envelope composes into a certificate | Exact composition theorem | S2.8 | none required | Statistical validation |
| Light-tail envelopes instantiate S2.8 | Exact instantiation | S2.9 | none required | Statistical validation |
| Median-of-means envelopes instantiate S2.8 | Exact robust instantiation | S2.10 | none required | Statistical validation |
| General accessibility decomposes into conditional-mean alignment plus residual conditional covariance | Exact extension | S2.11 | future model diagnostics | Agent / observer model |
| Conditional variances give a sharp universal lower bound on the unknown residual term | Exact lower certificate | S2.12 | future variance diagnostics | Agent / observer model |
| Shared recognition can create cross-copy decision coherence under hierarchical assumptions | Exact supplementary theorem + simulation | S1 | E5 | Hierarchical branch model |
| Everett self-location follows the QBS accessibility bridge | Assumption | bridge documents | none establishes it physically | Open physical mapping |

## Main value decomposition

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

## Predictive alignment chain

For score-measurable accessibility:

$$
m(Y)=E[U\mid Y],
\qquad
S=s(Y),
$$

S2 gives:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),s(Y)).
$$

For:

$$
Y=E[U\mid B],
$$

S2.2 gives:

$$
E[U\mid Y]=Y.
$$

The robustness/certification chain is:

$$
\text{conditional-mean alignment}
\to
\text{calibration-error bound}
\to
\text{prediction-MSE bound}
\to
\text{generic finite-sample confidence envelopes}.
$$

S2.5 supplies a bounded Hoeffding route. S2.9 supplies a light-tail route. S2.10 supplies a median-of-means route. S2.8 is their common composition interface.

## General accessibility: S2.11

When accessibility contains residual variation beyond `Y`, define:

$$
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
$$

Then:

$$
\boxed{
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),a(Y))
+
E[\operatorname{Cov}(U,S\mid Y)]
}.
$$

S2 is the special case:

$$
S=s(Y)
\Longrightarrow
\operatorname{Cov}(U,S\mid Y)=0.
$$

## Residual-variance control: S2.12

Let:

$$
v_U(Y)=\operatorname{Var}(U\mid Y),
\qquad
v_S(Y)=\operatorname{Var}(S\mid Y).
$$

Conditional Cauchy--Schwarz yields:

$$
\boxed{
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
E[\sqrt{v_U(Y)v_S(Y)}]
}.
$$

Outer Cauchy--Schwarz gives the simpler certificate:

$$
\boxed{
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
\sqrt{E[v_U(Y)]E[v_S(Y)]}
}.
$$

This penalty is universally sharp if residual outcome and accessibility variation can be perfectly conditionally anti-correlated. Any model-specific restriction on residual anti-correlation can therefore only improve the bound.

## What E1–E5 establish

### E1

Tests pure weighting, FOSD, the independence null, and nonmonotone counterexamples.

### E2

Shows a minimal representationally adequate learner can generate predictive ordering while a misspecified learner fails.

### E3

Uses paired primitive randomness to separate ordinary policy trajectory effects from FP conditioning effects.

### E4

Tests the interaction decomposition, including fixed and changing selectors.

### E5

Separates marginal FP uplift from cross-copy recognition/action correlation.

These are classical simulations of the formal structure, not evidence that the Everett bridge is physically correct.

## Current unresolved questions

- What physical observer/branch mechanism, if any, induces the Everett accessibility map?
- How can the S2.12 conditional-variance penalty be estimated or upper-bounded with finite-sample confidence in concrete agent models?
- Can robust estimators weaken S2.10's higher-moment requirements for squared targets?
- What explicit Orlicz/mgf assumptions give convenient S2.9 product/square constants?
- How should certification extend to infinite or certification-data-dependent candidate classes?
- Under what additional assumptions can recognition time be ordered?

## Failure structure

- independence of outcome and accessibility gives zero pure weighting uplift;
- nonmonotone conditional accessibility can break FOSD;
- general statistical dependence without conditional-mean ordering is insufficient for S2;
- a sufficiently negative S2.11 residual term can overturn conditional-mean alignment;
- S2.12 quantifies the worst-case residual penalty but can be conservative;
- statistical certificate failure is inconclusive, not proof of nonpositive covariance;
- invalid concentration/moment assumptions invalidate the corresponding finite-sample certificate;
- rejecting the Everett bridge removes the physical interpretation but not the abstract probability identities.
