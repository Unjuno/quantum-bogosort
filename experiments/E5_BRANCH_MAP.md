# E5 — Cross-Branch Recognition and Correlated Decision Maps

## H — Hypothesis

Recognition prevalence and cross-branch recognition structure are distinct quantities. Shared recognition and shared environmental history can induce correlated decisions across branch copies without producing the same change in single-observer marginal first-person uplift.

## T — Test

The experiment uses branch families with shared ancestral/environmental structure and local branch noise. Recognition changes the policy map from a baseline action rule to an adapted state-dependent rule.

Three comparisons are performed:

1. paired execution-strength sweep over `q` using common primitive randomness;
2. paired sweep over environmental correlation;
3. shared recognition versus branch-independent recognition at matched marginal prevalence.

The action map is conceptually:

```math
A(\omega)
=
\pi_{R(\omega)}(B(\omega)).
```

The experiment distinguishes:

```math
P(R=1),
```

```math
\mathrm{Corr}(R_i,R_j),
```

and:

```math
\mathrm{Corr}(A_i,A_j).
```

## D — Data / Result

Locked summaries:

- `data/processed/qbs_branch_policy_map_correlation_sweep.csv`
- `data/processed/qbs_branch_policy_map_replication_summary.csv`
- `data/processed/qbs_probabilistic_execution_corrected.csv`
- `data/processed/qbs_shared_recognition_contrasts.csv`

Reproduction outputs:

- `data/processed/e5_q_paired_reproduction.csv`
- `data/processed/e5_rho_paired_reproduction.csv`
- `data/processed/e5_shared_vs_independent_recognition.csv`
- `data/processed/e5_shared_recognition_contrasts.csv`

The paired execution-strength sweep gives exactly zero policy, QBS, and total recognition effect at `q=0`. Increasing shared environmental structure increases cross-copy action correlation. Shared versus independent recognition changes correlation structure substantially while leaving matched-marginal single-copy FP outcomes much closer.

## C — Controls / Counterexamples

Shared recognition by itself does not guarantee realized action correlation if branch-local states are independent and the fixed policy map does not introduce shared variation. A shared policy shift and realized Pearson action correlation must therefore be distinguished.

## U — Uncertainty / Interpretation Boundary

The experiment is a hierarchical classical-copy model. It demonstrates a structural distinction between marginal recognition and branch-wide coherence, but it does not establish that Everett branches should be statistically organized in the same way.

## ERROR CHECK

- Use the same primitive random realization across each paired `q` sweep.
- Confirm `q=0` reproduces the recognition-off baseline exactly.
- Separate recognition correlation from action correlation.
- Match marginal recognition prevalence in shared-versus-independent comparisons.
- Do not treat branch count as a fundamental physical measure.

## Linked theory

See `supplementary/branch_recognition.md` after supplementary decomposition and the recognition framework in `docs/research_map.md`.
