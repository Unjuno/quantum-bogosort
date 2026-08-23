# QBS Current Research Status

**Updated:** 2026-08-24

This file is the concise source of truth for current review/development state. Historical scientific snapshots are recorded in [`STATUS.md`](STATUS.md); detailed audit history remains under [`docs/`](docs/); future work is tracked in [`ROADMAP.md`](ROADMAP.md).

## Public source of truth

- canonical current development/review surface: `main`;
- current `main` commit: `c3dafc6c07e4c36bdd7ff0c926e63434291dd2f8`;
- frozen v0.3 public-review snapshot: tag/Release `v0.3-public-review` at `58038763127258bd3e2f0d41708c4dfa01f81fd6`;
- archived v0.2 public-review snapshot: tag/Release `v0.2-public-review` at `7405f7408f74fa32b16d1cc9f624070cc14624ab`;
- canonical claim/theorem/evidence map: [`docs/research_map.md`](docs/research_map.md);
- authoritative claim boundaries: [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md);
- supplementary index: [`supplementary/README.md`](supplementary/README.md).

All non-`main` development refs were audited on 2026-08-24. Before cleanup, each had `ahead_by=0` and no unique file differences versus `main`; all nine were then fast-forwarded without force to the current `main` commit and rechecked as identical:

- `fix/past-adapted-future-law`;
- `fix/recursive-qbs-validation`;
- `research/context-identifiability-boundary`;
- `research/context-identifiability-boundary-review`;
- `research/prospective-recognition-test`;
- `research/randomization-regime-proxy`;
- `research/randomized-context-diagnostic`;
- `research/recursive-qbs`;
- `research/selection-equivalence-boundary`.

They are cleanup-only refs, not separate scientific sources of truth. Deleting them remains a hosting-layer task because branch-ref deletion is not exposed by the current connector.

## Scientific state

The locked core remains:

- **T1–T5** as the core theorem family;
- **E1–E5** as the locked reproducibility suite;
- numbered supplementary results through **S2.13**.

Later recursive, selection/context-identifiability, randomized diagnostic, and temporal/longitudinal work is intentionally **unnumbered**. No T6, S2.14, or E6 has been introduced.

Recognition is an information/policy-selection state, not a privileged physical force. The base probability law remains fixed. First-person weighting changes only the modeled observer-conditioned measure. The Everett accessibility bridge remains unresolved.

## Current post-v0.3 extensions

### 1. Recursive observer-information loop

[`supplementary/evidence_activation.md`](supplementary/evidence_activation.md) closes the dynamic feedback

```math
\text{experienced observer history}
\longrightarrow
\text{belief / recognition update}
\longrightarrow
\text{adoption and policy}
\longrightarrow
\text{trajectory and accessibility}
\longrightarrow
\text{next experienced observer history}.
```

It includes sequential weighting, a filtration-relative predictable/innovation decomposition, and standard likelihood-ratio/KL model-comparison identities. `Innovation selection` is not an objective luck parameter.

The exploratory [`supplementary/recursive_qbs_simulation.py`](supplementary/recursive_qbs_simulation.py) remains outside E1–E5 and is executed by CI as a supplementary mechanism check.

### 2. Classical selection-equivalence and identifiability boundary

[`supplementary/selection_equivalence.md`](supplementary/selection_equivalence.md) proves that the normalized weighted law has exact classical ascertainment / record-size-biased representations under the stated assumptions.

The result extends across contexts: if a null may retune selection independently by context, arbitrary absolutely continuous observer-conditioned laws remain classically representable. Therefore one or many weighted observer laws do not by themselves identify an Everettian mechanism.

A shared-selection restriction creates cross-context density-ratio constraints, but those constraints are empirically useful only when the relevant base and selected laws are identifiable on a common observable state space. Latent violations may disappear under projection.

The proof/stress audit is [`docs/context_identifiability_audit_2026-08-23.md`](docs/context_identifiability_audit_2026-08-23.md).

### 3. Randomized-context and proxy diagnostics

Two supplementary diagnostics make restricted classical nulls operational without promoting them into the locked experiment suite:

- [`supplementary/randomized_context_diagnostic.md`](supplementary/randomized_context_diagnostic.md): under exogenous binary context randomization and context-invariant Bernoulli inclusion, selected pre-treatment strata preserve the randomized context probability, enabling exact finite-sample binomial/Bonferroni tests of observable shared-selection violations;
- [`supplementary/randomization_regime_proxy.md`](supplementary/randomization_regime_proxy.md): multiple known assignment regimes and informative pre-treatment proxies can expose some latent selector heterogeneity, while regime variation alone does not cure projection blindness.

The regime/proxy audit also fixes an important confounding boundary: a common nonzero selected log-odds offset across regimes requires stable proxy-level selector means. A regime-composition shift can reject the same homogeneity restriction even when the selector itself is unchanged. The test therefore targets a joint structural restriction, not selector retuning alone.

The deterministic stress scripts are supplementary audit code, not E6 and not Everett evidence.

### 4. Temporal / longitudinal interpretation boundary

[`docs/temporal_interpretation_boundary.md`](docs/temporal_interpretation_boundary.md) separates retrospective future-weighted descriptions from a past-adapted latent transition model.

The intended causal/statistical direction is

```math
(H_t,I_t)
\longrightarrow
I_{t+1}
\longrightarrow
\mathcal L(Y_{t+1:T}\mid H_t,I_{t+1})
\longrightarrow
Y_{t+1:T}.
```

The transition/accessibility rule may depend on recorded past/history; the realized future sequence is not assumed to be fixed in advance. An unobserved transition during a consciousness gap can remain locally unobservable while different latent continuations induce different later sequence laws.

[`supplementary/prospective_recognition_protocol.md`](supplementary/prospective_recognition_protocol.md) is therefore a longitudinal distribution/model-identification protocol, not a requirement that a specific future path be preregistered or predetermined. Later favorable outcomes do not by themselves prove an individual hidden switch.

## Reproducibility state

The primary runtime/reproduction contract remains pinned to Ubuntu 24.04, Python 3.11.15, NumPy 2.4.6, pandas 3.0.5, and Matplotlib 3.11.1.

The 16 historical E1–E5 CSVs remain Git-blob locked. Current reproduction CSVs use exact schema/order/non-numeric matching plus tight numerical equivalence (`rtol=1e-12`, `atol=1e-14`) and are restored to canonical committed bytes before the clean-worktree gate. Committed SVGs retain deterministic regeneration/structural checks.

Final PR #37 Actions run **#1093** passed both jobs on the merged tree:

- `repository-validation`: all 27 stages succeeded;
- `manuscript-build`: LaTeX build, PDF verification, and artifact upload succeeded.

The final green synthetic merge tree and actual merged `main` tree were both `4e0623d1fa4eb0051c54b4b69697280d078e8964`.

## Novelty and physical-bridge position

No novelty claim is made for normalized weighting, ascertainment/size-biased sampling, generic sample-selection/MNAR identifiability, standard likelihood-ratio/KL updating, martingale/predictable decompositions, or randomized experimental design by themselves.

The provisional novelty question concerns the combined recognition-dependent policy/trajectory/accessibility architecture and its decompositions, plus whether an independently motivated physical accessibility model supplies additional constraints that survive comparably flexible classical alternatives.

A concrete Everett bridge must independently derive or constrain `S_pi`, respect representation/coarse-graining/sequential consistency, expose operationally identifiable quantities, and produce consequences not reproduced by behavior-matched classical selection models.

## Public-review position

The repository is suitable for **public technical review** on scientific-content grounds. Public claims should continue to state explicitly that:

- the base probability law is not made objectively lucky;
- the normalized weighted law is classically selection-equivalent;
- rejection of one restricted classical null does not identify Everett;
- randomized/proxy diagnostics are supplementary falsification tools, not physical confirmation;
- hidden observer/continuation transitions are model variables, not directly observed events;
- the Everett accessibility bridge remains unresolved.

External criticism is especially useful on proof/counterexample validity, direct prior art, selection-null breadth, projection/measurement limits, longitudinal model identifiability, recursive-model misspecification, and the physical Everett bridge.

## Remaining hosting / governance gates

These are repository-hosting or presentation tasks, not missing core mathematics:

- repository header description still uses stale `recognition-activated` wording; preferred wording is `recognition-dependent`;
- repository topics are empty;
- `delete_branch_on_merge=false`;
- `main` classic branch protection/ruleset is not configured;
- nine merged development refs remain because branch deletion is unavailable through the current connector, although all are now identical to `main`;
- direct desktop/mobile browser inspection of rendered GitHub pages remains unavailable in the current environment;
- push-triggered `main` workflow runs are not directly enumerated by the connector, so green PR synthetic-tree equality with actual `main` remains the strongest observed fallback.
