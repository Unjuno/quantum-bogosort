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
| Mean-calibrated predictive scores with monotone score-measurable accessibility imply nonnegative outcome-accessibility covariance | Exact supplementary theorem | S2 | E2/E3 illustrate premises | Agent mechanism |
| Posterior-mean scores satisfy conditional-mean calibration exactly | Exact corollary | S2.2 | none required | Agent inference |
| Approximate calibration preserves positive covariance when alignment margin exceeds the calibration-error bound | Exact sufficient bound | S2.3 | future calibration diagnostics | Agent-learning mechanism |
| Ordinary prediction MSE gives a conservative population sufficient certificate | Exact sufficient bound | S2.4 | future held-out prediction diagnostics | Agent-learning mechanism |
| Bounded independent held-out samples give a high-probability covariance certificate | Exact finite-sample theorem | S2.5 | no new core experiment required | Statistical validation layer |
| Arbitrary independent training preserves the held-out certificate conditional on the realized trained rule | Exact conditional-validity theorem | S2.6 | no new core experiment required | Statistical validation layer |
| Same-holdout selection among a finite predeclared candidate family is valid with multiplicity correction | Exact simultaneous-validity theorem | S2.7 | no new core experiment required | Statistical validation layer |
| Any valid simultaneous five-moment envelope composes into a covariance certificate | Exact generic composition theorem | S2.8 | no new core experiment required | Statistical validation layer |
| Explicit light-tail concentration controls instantiate the generic envelope without deterministic boundedness | Exact light-tail instantiation | S2.9 | no new core experiment required | Statistical validation layer |
| Learning can approximate the calibration premises used by S2 | Simulation-supported, not guaranteed by theorem | S2 boundary | E2/E3 | Agent-learning mechanism |
| Shared recognition can create cross-copy decision coherence under explicit shared-latent assumptions | Exact supplementary theorem + simulation | S1 | E5 | Hierarchical branch model |
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

## Adaptive alignment and certification map

Let:

$$
m(Y)=E[U\mid Y],
\qquad
S=s(Y).
$$

S2 proves:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),s(Y)).
$$

If `m` and `s` are comonotone, then:

$$
\operatorname{Cov}(U,S)\ge0.
$$

### Posterior-mean calibration

If:

$$
Y=E[U\mid B],
$$

then:

$$
E[U\mid Y]=Y.
$$

### Calibration-error robustness

For:

$$
e(Y)=E[U\mid Y]-Y,
$$

S2.3 gives:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)}.
$$

### Prediction-MSE population certificate

S2.4 uses:

$$
\operatorname{Var}(e(Y))
\le
E[(U-Y)^2]
$$

so that:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{E[(U-Y)^2]\operatorname{Var}(S)}.
$$

### Finite-sample held-out certificate

S2.5 assumes independent i.i.d. evaluation and valid bounds on `Y`, `S`, and `U-Y`. It constructs:

$$
D_L
=
C_L-\sqrt{M_UV_U}
$$

such that:

$$
P\left(
\operatorname{Cov}(U,S)\ge D_L
\right)
\ge1-\delta.
$$

### Training-selection validity

S2.6 conditions on the entire random training state `T`. If the final certification sample is independent of training, then:

$$
P\!\left(
C(T)\ge D_L(T)
\mid T
\right)
\ge1-\delta.
$$

### Finite candidate post-selection validity

For `K` candidates fixed before the certification sample is inspected, S2.7 applies candidate-level error budgets satisfying:

$$
\sum_{k=1}^K\delta_k\le\delta.
$$

Then all candidate lower bounds hold simultaneously with probability at least `1-delta`, so any data-dependent selected index from that predeclared family retains its own lower bound.

### Generic confidence-envelope composition

S2.8 requires only a simultaneous event controlling:

$$
E[Y],
\quad
E[S],
\quad
E[YS],
\quad
E[S^2],
\quad
E[(U-Y)^2].
$$

Given valid simultaneous bounds:

$$
L_Y\le E[Y]\le U_Y,
\qquad
L_S\le E[S]\le U_S,
$$

$$
E[YS]\ge L_{YS},
\qquad
E[S^2]\le U_{S^2},
\qquad
E[(U-Y)^2]\le U_M,
$$

it forms:

$$
L_S^+=\max\{0,L_S\},
$$

$$
P_U
=
\max\{L_YL_S^+,L_YU_S,U_YL_S^+,U_YU_S\},
$$

$$
C_L=L_{YS}-P_U,
$$

$$
V_U
=
\max\{0,U_{S^2}-(L_S^+)^2\},
$$

and:

$$
D_{\mathrm{env}}
=
C_L-\sqrt{U_MV_U}.
$$

Then:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_{\mathrm{env}}
\right)
\ge1-\delta.
$$

### Light-tail instantiation

S2.9 supplies one concrete unbounded-data envelope. It assumes sub-Gaussian sample-mean control for `Y` and `S`, plus explicit Bernstein/sub-exponential sample-mean controls for:

$$
YS,
\qquad
S^2,
\qquad
(U-Y)^2.
$$

With:

$$
t_\delta=\log\frac{10}{\delta},
$$

a union bound over the five two-sided concentration events gives an S2.8 simultaneous envelope with probability at least:

$$
1-\delta.
$$

The resulting certificate:

$$
D_{\mathrm{LT}}
$$

satisfies:

$$
P\!\left(
\operatorname{Cov}(U,S)\ge D_{\mathrm{LT}}
\right)
\ge1-\delta.
$$

The theorem intentionally treats product/square concentration parameters as explicit inputs rather than claiming marginal sub-Gaussianity supplies universal constants automatically.

The theorem family deliberately does **not** use:

$$
I(U;Y)>0
$$

as a sufficient condition. Mutual information can be positive while the conditional mean `E[U|Y]` is constant, yielding zero covariance for every score-measurable accessibility map.

## What the core experiments establish

### E1

Shows that aligned accessibility changes conditional means and tails, verifies the FOSD direction under monotone accessibility, and includes null/counterexample cases.

### E2

Shows that positive alignment need not be inserted as an external correlation parameter: a small model that can represent the relevant nonlinear structure can learn a predictive score, while a misspecified model fails. S2 proves the covariance consequence once the learned score is conditionally mean-calibrated and accessibility respects its ordering.

### E3

Uses paired primitive randomness to separate ordinary trajectory changes from first-person conditioning changes. It also supplies an endogenous-policy setting in which internal evaluation remains aligned with post-policy outcome.

### E4

Tests both the fixed-selector interaction identity and the more general selector-map-shift decomposition.

### E5

Separates marginal FP uplift from cross-copy recognition and action correlation. Sharedness and marginal prevalence are treated as distinct variables.

## Remaining adaptive/statistical question

S2 through S2.9 now provide the chain:

$$
\text{conditional-mean alignment}
\to
\text{calibration robustness}
\to
\text{MSE population certificate}
\to
\text{generic finite-sample envelopes}
\to
\text{selection-safe certification}
\to
\text{bounded or light-tail instantiations}.
$$

The next theorem-level questions are:

- robust finite-moment moment envelopes, such as median-of-means constructions;
- explicit Orlicz/mgf sufficient conditions yielding the S2.9 product/square Bernstein parameters;
- infinite or certification-data-dependent candidate classes requiring uniform-convergence or selective-inference methods;
- general accessibility variables with a nonzero residual conditional-covariance term.

A new experiment should be added only if public review requires direct evaluation of these certificates on a learned-agent dataset.

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
- If a predictive signal changes dependence but not the conditional mean, S2 need not produce positive covariance.
- If calibration error is too large relative to the score/accessibility covariance margin, S2.3 does not certify positive covariance.
- If prediction MSE is too large for S2.4, the conservative certificate is inconclusive; this does not imply negative covariance.
- If a finite-sample lower margin is nonpositive, the corresponding S2 certificate is inconclusive at the selected confidence level.
- If the final certification sample is not independent of training, the simple S2.6 proof does not apply.
- If multiple candidates are searched without multiplicity correction, the S2.7 family-wise guarantee does not apply.
- If a confidence-envelope method is used outside its own assumptions, S2.8 does not repair its coverage.
- If S2.9 tail parameters are invalid or estimated without accounting, the light-tail coverage claim does not apply.
- If recognition changes neither trajectory nor accessibility, recognition effect is zero.
- If expected accessibility is zero, the normalized FP measure is undefined.
- If the Everett bridge is rejected, the measure-theoretic identities remain true but their physical interpretation does not follow.
