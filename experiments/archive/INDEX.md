# Historical Experiment Archive Index

This index records exploratory and secondary QBS experiments developed before the E1–E5 core was frozen. It prevents discarded or superseded results from disappearing from the research history.

The current evidence hierarchy is:

1. **CORE** — E1–E5, rerun by CI and used directly in the manuscript.
2. **APPENDIX CANDIDATE** — useful robustness or analytic checks that may support the manuscript but are not central.
3. **SUPERSEDED** — an earlier formulation replaced by a corrected design.
4. **HISTORICAL LOCAL ARTIFACT** — generated during development but not yet reconstructed as a committed reproduction script.

## Recognition timing and recursive filtering

Historical files developed during the exploratory phase:

- `recognition_time_recursive_bogosort.csv`
- `recognition_time_measure_constrained_optima.csv`
- `long_horizon_measure_decay.csv`
- `recursive_generating_function_identity.csv`

**Research question:** how recognition time and repeated filtering affect normalized first-person outcomes and accessible measure over long horizons.

**Status:** APPENDIX CANDIDATE / HISTORICAL LOCAL ARTIFACT. The stopping-time formulation remains an open extension and should not be cited as a core result until a committed reproduction script exists.

## Multi-observer and zero-sum conditioning

Historical files:

- `zero_sum_observer_conditioning.csv`
- `multi_observer_correlation_experiment.csv`

**Research question:** whether separately normalized observer-indexed measures can each assign high probability to observer-relative favorable events without those events forming a single shared probability budget.

**Status:** mathematical normalization result retained in `supplementary/multi_observer.md`; historical simulation is APPENDIX CANDIDATE / HISTORICAL LOCAL ARTIFACT.

## Selectivity frontier and measure constraints

Historical files:

- `qbs_positive_threshold_frontier.csv`
- `qbs_positive_threshold_optima.csv`
- `qbs_positive_correlation_uplift_fit.csv`

**Research question:** whether stronger selectivity always increases first-person value under imperfect prediction.

**Result retained:** toy simulations showed an interior selectivity optimum can arise even with positive predictor/outcome correlation.

**Status:** APPENDIX CANDIDATE. Conceptual result retained in `supplementary/selectivity_frontier.md`.

## Evidence-driven recognition activation

Historical files:

- `qbs_evidence_activation_full.csv`
- `qbs_evidence_activation_sample_size.csv`

**Research question:** when noisy evidence for positive predictor/outcome alignment is strong enough to activate recognition-dependent policy.

**Status:** APPENDIX CANDIDATE / HISTORICAL LOCAL ARTIFACT. The conceptual mechanism is retained in `supplementary/evidence_activation.md`.

## Adaptation monotonicity and alignment boundaries

Historical files:

- `qbs_adaptation_monotonicity_robustness.csv`
- `qbs_adaptation_monotonicity_by_distribution.csv`
- `qbs_alignment_boundary_full.csv`
- `qbs_alignment_boundary_summary.csv`
- `qbs_adaptation_accuracy_replications.csv`
- `qbs_adaptation_accuracy_summary.csv`
- `qbs_adaptation_total_effect_replications.csv`
- `qbs_adaptation_total_effect_summary.csv`

**Research question:** robustness of the adaptive-rescue sign condition, the point at which policy targeting flips the interaction sign, and whether better adaptation can increase total value while reducing marginal QBS contribution.

**Status:** `qbs_adaptation_total_effect_summary.csv` remains committed and is used for Figure 5. The wider sweeps are APPENDIX CANDIDATES unless or until reproduction scripts are reconstructed.

## Earlier branch-recognition variants

Historical files:

- `qbs_branch_policy_map_correlation_sweep.csv`
- `qbs_branch_policy_map_replications.csv`
- `qbs_branch_policy_map_replication_summary.csv`
- `qbs_probabilistic_execution_corrected.csv`
- `qbs_shared_vs_independent_recognition.csv`
- `qbs_shared_recognition_contrasts.csv`

**Research question:** separate marginal recognition prevalence from cross-branch recognition correlation and decision-map coherence.

**Status:** the corrected paired version is incorporated into E5. Older unmatched or differently seeded variants are retained only as historical context.

## Explicitly superseded result

An early probabilistic-execution sweep left the selector active when execution strength was zero. That formulation failed the intended recognition null because the `q=0` cell was not actually the baseline model.

**Status:** SUPERSEDED and must not be cited. The corrected design uses:

$$
S_q
=
1-q(1-S_{\mathrm{full}}),
$$

so `q=0` reproduces the baseline policy/accessibility state and `q=1` gives full recognition-dependent policy plus selector.

## Archive reconstruction policy

Before an archived result is promoted back into the manuscript, it must have:

- a committed script or derivation;
- explicit seed/parameter conventions;
- committed output data or a deterministic analytic source;
- a short H/T/D/C/U + ERROR CHECK note;
- a statement of whether it updates, supplements, or supersedes any E1–E5 result.

This index documents research history; it does not elevate every historical experiment to current evidence.
