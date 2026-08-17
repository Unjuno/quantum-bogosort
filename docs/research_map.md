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
| Conditional variances give a sharp universal lower bound on the residual term | Exact lower certificate | S2.12 | future variance diagnostics | Agent / observer model |
| Explained-variance fractions and conditional-mean correlation reparameterize the residual certificate | Exact normalized certificate | S2.13 | future predictive diagnostics | Agent / observer model |
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

## Predictive alignment and statistical chain

For:

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

S2.2 gives posterior-mean calibration. S2.3–S2.4 give calibration/MSE population bounds. S2.5–S2.10 supply bounded, selection-safe, generic-envelope, light-tail, and MoM finite-sample layers.

## General accessibility and residual structure

Define:

$$
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
$$

S2.11 gives:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),a(Y))
+
E[\operatorname{Cov}(U,S\mid Y)].
$$

S2.12 bounds the unknown residual term by conditional variances:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
\sqrt{E[v_U(Y)]E[v_S(Y)]}.
$$

## Explained-variance form: S2.13

Define:

$$
A_U
=
\frac{\operatorname{Var}(m(Y))}{\operatorname{Var}(U)},
\qquad
A_S
=
\frac{\operatorname{Var}(a(Y))}{\operatorname{Var}(S)}.
$$

When both explained fractions are positive, define:

$$
\rho_{ma}
=
\operatorname{Corr}(m(Y),a(Y)).
$$

Then:

$$
\operatorname{Cov}(U,S)
\ge
\sqrt{\operatorname{Var}(U)\operatorname{Var}(S)}
\left[
\rho_{ma}\sqrt{A_UA_S}
-
\sqrt{(1-A_U)(1-A_S)}
\right].
$$

Thus:

$$
\rho_{ma}\sqrt{A_UA_S}
>
\sqrt{(1-A_U)(1-A_S)}
$$

is sufficient for positive total covariance.

For:

$$
\rho_{ma}=1,
$$

this simplifies to:

$$
A_U+A_S>1.
$$

For:

$$
A_U=A_S=A,
$$

the sufficient threshold is:

$$
A>
\frac{1}{1+\rho_{ma}}.
$$

This is a worst-case residual certificate, not a necessary condition.

## What E1–E5 establish

- **E1:** weighting/FOSD, independence null, nonmonotone counterexample.
- **E2:** endogenous predictive ordering in a minimal learned agent.
- **E3:** paired recognition decomposition.
- **E4:** policy–QBS interaction decomposition.
- **E5:** marginal FP uplift versus cross-copy coherence.

These are classical simulations of the formal structure, not evidence that the Everett bridge is physically correct.

## Current unresolved questions

- What physical mechanism, if any, induces the Everett accessibility map?
- How can `A_U`, `A_S`, and `rho_ma` be estimated with finite-sample confidence in learned-agent models?
- Can robust estimators weaken S2.10's higher-moment requirements?
- What explicit Orlicz/mgf assumptions give convenient S2.9 constants?
- How should certification extend to infinite/data-dependent candidate classes?
- Under what assumptions can recognition time be ordered?

## Failure structure

- independence gives zero pure weighting uplift;
- nonmonotone conditional accessibility can break FOSD;
- dependence without conditional-mean ordering is insufficient for S2;
- negative residual dependence can overturn score-level alignment;
- S2.12/S2.13 can be conservative because they use worst-case residual penalties;
- statistical certificate failure is inconclusive;
- invalid concentration/moment assumptions invalidate their finite-sample certificate;
- rejecting the Everett bridge removes the physical interpretation but not the abstract mathematical results.
