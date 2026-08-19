# E3 — Recognition Decomposition on Paired Primitive Branches

## H — Hypothesis

Recognition can change both ordinary trajectories and first-person accessibility. These contributions should be exactly separable when pre- and post-recognition policies are evaluated on the same primitive randomness.

## T — Test

The experiment uses paired counterfactual simulation on common primitive random seeds. Recognition-off and recognition-on policies generate different trajectory outcomes and accessibility maps from the same underlying realizations.

For each recognition state, the T4 benchmark assumes:

```math
0<E[S_R]<\infty,
\qquad
E[|U_R|]<\infty,
\qquad
E[|U_R|S_R]<\infty.
```

The benchmark decomposition is:

```math
V_1-V_0
=
E[U_1-U_0]
+
Q(U_1,S_1)-Q(U_0,S_0).
```

For the baseline with no pre-recognition selector:

```math
S_0\equiv1.
```

## D — Data / Result

Locked summaries:

- `data/processed/qbs_paired_policy_selection_decomposition.csv`
- `data/processed/qbs_paired_decomposition_replication_summary.csv`
- `data/processed/qbs_stress_recognition_null_corrected.csv`

Reproduction outputs:

- `data/processed/e3_recognition_decomposition_reproduction.csv`
- `data/processed/e3_recognition_null_reproduction.csv`

The numerical decomposition closes to floating-point precision. The paired recognition-label null gives exactly zero effect when recognition changes neither trajectory nor accessibility.

## C — Controls / Counterexamples

The recognition-label null is essential. A mere label change with:

```math
U_1=U_0
```

and:

```math
S_1=S_0
```

must imply:

```math
V_1-V_0=0.
```

## U — Uncertainty / Interpretation Boundary

The decomposition is exact inside the formal model under the stated domain conditions. Whether a real Everettian recognition event induces a physically meaningful accessibility change is a separate question.

## ERROR CHECK

- Use paired primitive randomness rather than independent pre/post samples.
- Verify the decomposition residual is at floating-point precision.
- Verify the recognition-label null remains exactly zero up to numerical representation.
- Keep ordinary causal policy improvement distinct from the conditioning term.

## Linked theory

T4 in `theory/theorem_4_5.md`.
