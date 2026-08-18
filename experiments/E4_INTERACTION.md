# E4 — Adaptive-Policy / QBS Interaction

## H — Hypothesis

Ordinary policy improvement and QBS conditioning need not add independently. Their interaction is governed by where policy improvement is concentrated relative to accessibility.

For a fixed selector:

```math
D=U_1-U_0,
```

and:

```math
I
=
\frac{\mathrm{Cov}(D,S)}{E[S]}.
```

If ordinary adaptation preferentially rescues low-accessibility bad states, the interaction should be nonpositive.

## T — Test

The experiment has two parts.

### Fixed-selector sign test

Construct policy improvements concentrated in:

- bad / low-accessibility states,
- neutral states,
- good / high-accessibility states.

Compare observed interaction with the exact covariance prediction.

### Changing-selector decomposition

Allow policy to change both outcome and selector map. Decompose:

```math
I
=
I_{target}+I_{map},
```

where:

```math
I_{target}
=
\frac{\mathrm{Cov}(D,S_0)}{E[S_0]},
```

and:

```math
I_{map}
=
Q(U_1,S_1)-Q(U_1,S_0).
```

## D — Data / Result

Locked summaries:

- `data/processed/qbs_interaction_theorem_sign_test.csv`
- `data/processed/qbs_general_interaction_summary.csv`
- `data/processed/qbs_adaptation_total_effect_summary.csv`

Reproduction outputs:

- `data/processed/e4_fixed_selector_sign_reproduction.csv`
- `data/processed/e4_general_interaction_reproduction.csv`

The fixed-selector sign follows the predicted covariance sign. Rescue-bad policies produce negative interaction, neutral policies approximately zero interaction, and amplify-good policies positive interaction. In the general changing-selector case, the identity again closes to floating-point precision.

## C — Controls / Counterexamples

Negative interaction is not a universal QBS law. It arises when policy improvement is negatively associated with accessibility. Policies that disproportionately improve high-accessibility states can instead produce positive interaction.

## U — Uncertainty / Interpretation Boundary

A negative interaction does not imply that either ordinary adaptation or QBS conditioning is harmful. Both component effects can be positive while partially substituting for one another.

The adaptive-rescue result is a sufficient-condition theorem under explicit monotonicity assumptions, not a universal statement about all adaptive agents.

## ERROR CHECK

- Compare observed interaction with the exact covariance benchmark.
- Verify both fixed-selector and changing-selector identities numerically.
- Preserve sign controls for rescue-bad, neutral, and amplify-good policies.
- Do not infer the sign of either component effect from the sign of interaction.

## Linked theory

T5 and Corollary 5.1 in `theory/theorem_4_5.md`.
