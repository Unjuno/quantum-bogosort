# Quantum Bogosort — Core Theorem Set (T1–T5)

This is the GitHub-rendered index for the locked core theorem set. Mathematical display blocks use GitHub-compatible Markdown math syntax.

## Setup

Let the base probability space be represented by the usual triplet of sample space, sigma algebra, and base measure. For policy `pi`, let `U_pi` denote trajectory utility and `S_pi` denote nonnegative observer-indexed accessibility.

Assume:

```math
0<E_\mu[S_\pi]<\infty,
\qquad
E_\mu[|U_\pi|S_\pi]<\infty.
```

Define the first-person measure by:

```math
\mu^{FP}_\pi(A)
=
\frac{E_\mu[\mathbf 1_A S_\pi]}{E_\mu[S_\pi]}.
```

The full theorem set is split for readability:

- [`theorem_1_3.md`](theorem_1_3.md): Covariance Identity, Tail Identity, and FOSD.
- [`theorem_4_5.md`](theorem_4_5.md): Recognition Decomposition and Policy–QBS Interaction.
- [`propositions_boundaries.md`](propositions_boundaries.md): option value, support, extinction boundary, counterexamples, and Everett bridge assumption.
- [`core_theorems.tex`](core_theorems.tex): LaTeX source for manuscript integration.

## Central recognition decomposition

Recognition can change both trajectory utility and accessibility:

```math
R
\longrightarrow
\pi_R
\longrightarrow
(U_R,S_R).
```

For the no-pre-recognition-selector baseline:

```math
S_0\equiv 1,
```

we obtain:

```math
V_1-V_0
=
E[U_1-U_0]
+
\frac{\mathrm{Cov}(U_1,S_1)}{E[S_1]}.
```

The first term is the ordinary causal policy/trajectory effect. The second term is the observer-indexed conditioning contribution.

## Interpretation boundary

The measure-theoretic results do not establish an Everett interpretation by themselves. The physical mapping requires a separate bridge assumption, stated in [`propositions_boundaries.md`](propositions_boundaries.md).
