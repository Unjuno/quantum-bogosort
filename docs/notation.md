# QBS Notation

This document fixes notation used across theorem notes, experiment cards, and the manuscript.

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
| `pi_R` | policy available/used under recognition state `R` |
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

## Adaptive-agent notation

| Symbol | Meaning |
|---|---|
| `X_t` | environment/world state at time `t` |
| `B_t` | agent internal belief/world-model state |
| `Y_t` | evaluation or recognition signal derived from the internal model |
| `U_T` | future outcome at horizon `T` |

Predictive-information direction:

$$
I(B_t;X_t)>0,
$$

and when the environment has temporal structure:

$$
I(X_t;U_T)>0.
$$

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

## Convention

Markdown math in this repository uses double-dollar display blocks only. Inline symbols are written as code spans or moved into display blocks.
