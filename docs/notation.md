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

```math
\omega_R(z)
```

for the history generated under recognition state `R` from the same primitive realization `z`.

## Recognition and policy

| Symbol | Meaning |
|---|---|
| `R` | recognition state, typically 0 or 1 |
| `pi_R` | policy available or used under recognition state `R` |
| `U_R` | outcome or utility induced by `pi_R` |
| `S_R` | observer-indexed accessibility weight induced under `pi_R` |

Core causal structure:

```math
R
\longrightarrow
\pi_R
\longrightarrow
(U_R,S_R).
```

In the self-referential QBS case, `R=1` may represent recognition of a QBS-type rule itself. Recognition has no privileged causal power in the formal model: it matters only through any policy change it induces and the resulting changes in `U_R` and/or `S_R`. If recognition changes neither quantity, the recognition-label null applies.

## First-person measure and value

The normalized first-person **measure** needs only nonnegative accessibility with positive finite mean:

```math
S_\pi\ge0,
\qquad
0<E[S_\pi]<\infty.
```

Then:

```math
\mu^{FP}_\pi(A)
=
\frac{E_\mu[\mathbf 1_A S_\pi]}{E_\mu[S_\pi]}.
```

To use a finite first-person **value** together with the ordinary-mean/covariance decomposition, also require:

```math
E[|U_\pi|]<\infty,
\qquad
E[|U_\pi|S_\pi]<\infty.
```

These are separate conditions; neither base integrability nor weighted integrability implies the other in general.

First-person value:

```math
V_{FP}(\pi)
=
\frac{E_\mu[U_\pi S_\pi]}{E_\mu[S_\pi]}.
```

Normalized covariance contribution:

```math
Q(U,S)
=
\frac{\mathrm{Cov}(U,S)}{E[S]}.
```

For the general selector-changing T5 decomposition, the intermediate term `Q(U_1,S_0)` additionally requires:

```math
E[|U_1|S_0]<\infty.
```

## Canonical terminology

### Base measure / objective chance

`mu` is the base probability or branch measure used by the model before first-person accessibility reweighting.

A QBS first-person shift does not by itself change `mu`. When the repository says that objective or base chance is unchanged, it means that the underlying base measure has not been causally modified by the reweighting operation.

### Accessibility

`S` is a nonnegative observer-indexed weight. Mathematically it controls the reweighting from the base measure to the normalized first-person measure.

Accessibility is not automatically a physical Everett quantity. A physical interpretation requires the separate bridge discussed in `docs/everett_bridge_tests.md`.

### First-person uplift

First-person uplift means that an outcome statistic is larger under the first-person measure than under the base measure. For an outcome satisfying the base and weighted integrability conditions:

```math
E_{FP}[U]-E[U]
=
\frac{\mathrm{Cov}(U,S)}{E[S]}.
```

This is a distributional statement about observer-conditioned weighting.

### Trajectory reweighting

Trajectory reweighting means replacing the base weighting of histories by normalized accessibility-weighted histories. It does not create histories outside the support of the fixed-policy base measure.

### Self-location

Self-location refers to indexical uncertainty about which observer/history position within the modeled collection is the first-person position. In QBS, accessibility can change the normalized measure used for that indexical weighting.

### Present self-location under future accessibility

Let `Z` denote a present state or present trajectory descriptor, and let `S_T` denote an accessibility weight determined over the future continuation of the trajectory. The first-person probability of a present event is the direct restriction of the same weighted measure:

```math
P_{FP}(Z\in A)
=
\frac{E[\mathbf 1_{\{Z\in A\}}S_T]}{E[S_T]}.
```

For a discrete atom with positive base probability:

```math
P(Z=z)>0,
```

we may write:

```math
P_{FP}(Z=z)
=
\frac{E[S_T\mid Z=z]P(Z=z)}{E[S_T]}.
```

If `P(Z=z)=0`, absolute continuity of the weighted measure gives `P_FP(Z=z)=0`; a pointwise conditional-expectation value at that null atom is not required. Therefore future accessibility can reweight present self-location whenever expected future accessibility differs across positive-probability present states. This is a conditioning/change-of-measure statement, not backward causation: the base probability law for `Z` is not thereby changed.

### Predictable selection

In the recursive extension, let `H_t` be the information available when the decision for step `t+1` is made and define:

```math
m_{t+1}=E_\mu[X_{t+1}\mid H_t].
```

The cumulative predictable component is:

```math
A_T
=
\sum_{t=0}^{T-1}m_{t+1}.
```

**Predictable selection** is the first-person reweighting contribution associated with `A_T`:

```math
\frac{\mathrm{Cov}_\mu(A_T,S_T)}{E_\mu[S_T]}.
```

It captures first-person selection among trajectory value that was predictable from the information used at decision time.

### Innovation selection

Define the filtration-relative innovation:

```math
\varepsilon_{t+1}
=
X_{t+1}-E_\mu[X_{t+1}\mid H_t],
```

with cumulative innovation:

```math
M_T
=
\sum_{t=0}^{T-1}\varepsilon_{t+1}.
```

Under the stated integrability conditions:

```math
E_\mu[\varepsilon_{t+1}\mid H_t]=0,
\qquad
E_\mu[M_T]=0.
```

**Innovation selection** is the first-person reweighting contribution:

```math
\frac{\mathrm{Cov}_\mu(M_T,S_T)}{E_\mu[S_T]}.
```

Innovation selection is relative to the chosen information filtration. Enlarging the information state can move variation from the innovation component into the predictable component. It is therefore not a filtration-independent physical `luck` parameter and does not mean that objective chance has been causally changed.

## Informal interpretation only: effective or indexical luck

`effective luck` and `indexical luck` are **not formal QBS variables or theorem names**. If used in explanatory prose, they are shorthand for a favorable first-person distributional shift: the observer-conditioned measure places greater weight on favorable accessible trajectories.

When discussion specifically concerns decision-time-unpredictable variation in the recursive extension, formal writing should use `innovation selection` rather than introducing a separate `luck` variable.

Formal writing should otherwise prefer `first-person uplift`, `trajectory reweighting`, `first-person measure`, or `self-location` as appropriate.

The informal language must not be read as a claim that the objective/base probability law or an external random-number generator is causally biased toward favorable outcomes.

A compact distinction is:

```math
\text{objective/base chance unchanged}
\qquad\neq\qquad
\text{first-person trajectory weight unchanged}.
```

QBS can change the second quantity under its assumptions without claiming a causal change in the first.

## Policy interaction notation

Policy improvement:

```math
D
=
U_1-U_0.
```

QBS interaction change:

```math
I
=
Q(U_1,S_1)-Q(U_0,S_0).
```

For a fixed selector:

```math
S_1=S_0=S,
```

so:

```math
I
=
\frac{\mathrm{Cov}(D,S)}{E[S]}.
```

For a changing selector, the general T5 decomposition also uses `Q(U_1,S_0)` and therefore requires the cross-integrability condition stated above.

## Predictive-alignment notation

For a signal `Y`:

```math
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
```

Conditional residual variances are:

```math
v_U(Y)=\mathrm{Var}(U\mid Y),
\qquad
v_S(Y)=\mathrm{Var}(S\mid Y).
```

Explained-variance fractions are:

```math
A_U
=
\frac{\mathrm{Var}(m(Y))}{\mathrm{Var}(U)},
\qquad
A_S
=
\frac{\mathrm{Var}(a(Y))}{\mathrm{Var}(S)}.
```

When both explained fractions are positive:

```math
\rho_{ma}
=
\mathrm{Corr}(m(Y),a(Y)).
```

## Adaptive-agent notation

| Symbol | Meaning |
|---|---|
| `X_t` | environment/world state or outcome-relevant state at time `t` |
| `B_t` | agent internal belief/world-model state |
| `Y_t` | evaluation or recognition signal derived from the internal model |
| `U_T` | future outcome at horizon `T` |

Mutual information can quantify predictive dependence, but positive mutual information alone is not sufficient for positive outcome/accessibility covariance.

## Recursive observer-information notation

| Symbol | Meaning |
|---|---|
| `O_t` | current observer record/state used by the recursive model |
| `H_t` | information available when the next decision is selected |
| `b_t` | epistemic belief in a specified observer-selection bridge/model |
| `q_t` | adoption or execution strength selected from current information |
| `G_t` | nonnegative incremental accessibility factor |
| `S_t` | cumulative accessibility through time `t` |
| `m_{t+1}` | base conditional-mean/predictable outcome increment given `H_t` |
| `epsilon_{t+1}` | filtration-relative innovation increment |
| `A_T` | cumulative predictable component |
| `M_T` | cumulative innovation component |
| `ell_{t+1}` | one-step log likelihood ratio for specified competing observer models |

Cumulative accessibility is:

```math
S_t
=
\prod_{j=1}^{t}G_j,
\qquad
S_0=1.
```

A generic recursive dependency is:

```math
O_t
\longrightarrow
H_t
\longrightarrow
(b_t,q_t,\pi_t)
\longrightarrow
(X_{t+1},G_{t+1})
\longrightarrow
O_{t+1}.
```

The likelihood-ratio update is a model-comparison device. It does not give `b_t` privileged physical causal power and does not establish the physical accessibility bridge.

## Repeated-filter notation

| Symbol | Meaning |
|---|---|
| `N_B` | number of adverse triggers |
| `lambda` | residual accessibility multiplier per adverse trigger |

Repeated accessibility:

```math
S
=
\lambda^{N_B}.
```

## Branch-correlation notation

For branch/copy indices `i` and `j`:

```math
\mathrm{Corr}(R_i,R_j)
```

measures recognition correlation, while:

```math
\mathrm{Corr}(A_i,A_j)
```

measures realized action correlation.

These are distinct from marginal recognition prevalence:

```math
P(R=1).
```

## Markdown convention

Repository Markdown uses fenced `math` blocks for display mathematics. Inline mathematical symbols are written as code spans or moved into display blocks. Named quantities use a repository-wide roman-form convention such as `\mathrm{Cov}`, `\mathrm{Var}`, and `\mathrm{Corr}`. This is a consistency policy, not a claim that MathJax lacks other operator macros.