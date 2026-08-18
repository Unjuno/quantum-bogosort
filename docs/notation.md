# QBS Notation and Terminology

This document fixes notation and terminology used across theorem notes, experiment cards, repository documentation, and the manuscript.

## Base probability structure

| Symbol | Meaning |
|---|---|
| `Omega` | common primitive branch/history sample space |
| `F` | sigma algebra on the sample space |
| `mu` | base probability or branch measure |
| `z` | primitive branch realization used for paired counterfactuals |

The preferred paired-counterfactual representation is:

$$
\omega_R(z)
$$

for the history generated under recognition state `R` from the same primitive realization `z`.

## Recognition and policy

| Symbol | Meaning |
|---|---|
| `R` | recognition state, typically 0 or 1 |
| `pi_R` | policy available or used under recognition state `R` |
| `U_R` | outcome or utility induced by `pi_R` |
| `S_R` | observer-indexed accessibility weight induced under `pi_R` |

Core causal structure:

$$
R
\longrightarrow
\pi_R
\longrightarrow
(U_R,S_R).
$$

## First-person measure and value

For nonnegative accessibility with positive finite mean:

$$
0<E[S_\pi]<\infty,
$$

define:

$$
\mu^{FP}_\pi(A)
=
\frac{E_\mu[\mathbf 1_A S_\pi]}{E_\mu[S_\pi]}.
$$

First-person value:

$$
V_{FP}(\pi)
=
\frac{E_\mu[U_\pi S_\pi]}{E_\mu[S_\pi]}.
$$

Normalized covariance contribution:

$$
Q(U,S)
=
\frac{\operatorname{Cov}(U,S)}{E[S]}.
$$

## Canonical terminology

### Base measure / objective chance

`mu` is the base probability or branch measure used by the model before first-person accessibility reweighting.

A QBS first-person shift does not by itself change `mu`. When the repository says that objective or base chance is unchanged, it means that the underlying base measure has not been causally modified by the reweighting operation.

### Accessibility

`S` is a nonnegative observer-indexed weight. Mathematically it controls the reweighting from the base measure to the normalized first-person measure.

Accessibility is not automatically a physical Everett quantity. A physical interpretation requires the separate bridge discussed in `docs/everett_bridge_tests.md`.

### First-person uplift

First-person uplift means that an outcome statistic is larger under the first-person measure than under the base measure. For the mean:

$$
E_{FP}[U]-E[U]
=
\frac{\operatorname{Cov}(U,S)}{E[S]}.
$$

This is a distributional statement about observer-conditioned weighting.

### Trajectory reweighting

Trajectory reweighting means replacing the base weighting of histories by normalized accessibility-weighted histories. It does not create histories outside the support of the fixed-policy base measure.

### Self-location

Self-location refers to indexical uncertainty about which observer/history position within the modeled collection is the first-person position. In QBS, accessibility can change the normalized measure used for that indexical weighting.

### Present self-location under future accessibility

Let `Z` denote a present state or present trajectory descriptor, and let `S_T` denote an accessibility weight determined over the future continuation of the trajectory. The first-person probability of a present event is the direct restriction of the same weighted measure:

$$
P_{FP}(Z\in A)
=
\frac{E[\mathbf 1_{\{Z\in A\}}S_T]}{E[S_T]}.
$$

For a discrete present state:

$$
P_{FP}(Z=z)
=
\frac{E[S_T\mid Z=z]P(Z=z)}{E[S_T]}.
$$

Therefore future accessibility can reweight present self-location whenever expected future accessibility differs across present states. This is a conditioning/change-of-measure statement, not backward causation: the base probability law for `Z` is not thereby changed.

## Informal interpretation only: effective or indexical luck

`effective luck` and `indexical luck` are **not formal QBS variables or theorem names**. If used in explanatory prose, they are shorthand for a favorable first-person distributional shift: the observer-conditioned measure places greater weight on favorable accessible trajectories.

Formal writing should prefer `first-person uplift`, `trajectory reweighting`, `first-person measure`, or `self-location` as appropriate.

The informal language must not be read as a claim that the objective/base probability law or an external random-number generator is causally biased toward favorable outcomes.

A compact distinction is:

$$
\text{objective/base chance unchanged}
\qquad\neq\qquad
\text{first-person trajectory weight unchanged}.
$$

QBS can change the second quantity under its assumptions without claiming a causal change in the first.

## Policy interaction notation

Policy improvement:

$$
D
=
U_1-U_0.
$$

QBS interaction change:

$$
I
=
Q(U_1,S_1)-Q(U_0,S_0).
$$

For a fixed selector:

$$
S_1=S_0=S,
$$

so:

$$
I
=
\frac{\operatorname{Cov}(D,S)}{E[S]}.
$$

## Predictive-alignment notation

For a signal `Y`:

$$
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
$$

Conditional residual variances are:

$$
v_U(Y)=\operatorname{Var}(U\mid Y),
\qquad
v_S(Y)=\operatorname{Var}(S\mid Y).
$$

Explained-variance fractions are:

$$
A_U
=
\frac{\operatorname{Var}(m(Y))}{\operatorname{Var}(U)},
\qquad
A_S
=
\frac{\operatorname{Var}(a(Y))}{\operatorname{Var}(S)}.
$$

When both explained fractions are positive:

$$
\rho_{ma}
=
\operatorname{Corr}(m(Y),a(Y)).
$$

## Adaptive-agent notation

| Symbol | Meaning |
|---|---|
| `X_t` | environment/world state at time `t` |
| `B_t` | agent internal belief/world-model state |
| `Y_t` | evaluation or recognition signal derived from the internal model |
| `U_T` | future outcome at horizon `T` |

Mutual information can quantify predictive dependence, but positive mutual information alone is not sufficient for positive outcome/accessibility covariance.

## Repeated-filter notation

| Symbol | Meaning |
|---|---|
| `N_B` | number of adverse triggers |
| `lambda` | residual accessibility multiplier per adverse trigger |

Repeated accessibility:

$$
S
=
\lambda^{N_B}.
$$

## Branch-correlation notation

For branch/copy indices `i` and `j`:

$$
\operatorname{Corr}(R_i,R_j)
$$

measures recognition correlation, while:

$$
\operatorname{Corr}(A_i,A_j)
$$

measures realized action correlation.

These are distinct from marginal recognition prevalence:

$$
P(R=1).
$$

## Markdown convention

Markdown math in this repository uses double-dollar display blocks only. Inline mathematical symbols are written as code spans or moved into display blocks.
