# Supplementary QBS Notes

These notes contain exact secondary results, statistical certification layers, and exploratory extensions outside the locked T1–T5 / E1–E5 core.

## Conceptual theorem spine

Read the post-v0.2 predictive-alignment line in this order:

1. [`adaptive_agent.md`](adaptive_agent.md) — S2 and S2.1–S2.4: predictive conditional-mean alignment, posterior-mean self-calibration, population robustness, and the mutual-information boundary.
2. [`residual_covariance_extension.md`](residual_covariance_extension.md) — S2.11: exact extension beyond score-measurable accessibility using residual conditional covariance.
3. [`residual_variance_certificate.md`](residual_variance_certificate.md) — S2.12: sharp worst-case residual lower bounds from conditional variances.
4. [`explained_variance_certificate.md`](explained_variance_certificate.md) — S2.13: explained-variance / conditional-mean-correlation form of the S2.12 certificate.

The conceptual chain is:

```math
\text{predictive signal}
\longrightarrow
\text{conditional-mean alignment}
\longrightarrow
\text{outcome/accessibility covariance}
\longrightarrow
\text{first-person shift}.
```

S2.12 and S2.13 are sufficient worst-case certificates rather than necessary conditions.

## Statistical certification layer

These files support the conceptual spine but are primarily technical validation machinery:

- [`finite_sample_certificate.md`](finite_sample_certificate.md) — S2.5: bounded independent-held-out high-probability covariance certificate;
- [`selection_validity.md`](selection_validity.md) — S2.6–S2.7: validity after arbitrary independent training and multiplicity-corrected finite candidate selection;
- [`confidence_envelope_certificate.md`](confidence_envelope_certificate.md) — S2.8: generic composition of simultaneous moment confidence envelopes;
- [`light_tail_certificate.md`](light_tail_certificate.md) — S2.9: sub-Gaussian/Bernstein light-tail instantiation;
- [`robust_mom_certificate.md`](robust_mom_certificate.md) — S2.10: median-of-means instantiation under finite variance bounds for the five S2.8 targets.

These results require their stated sampling, moment, and selection assumptions. Statistical certificate failure is inconclusive about the sign of the population covariance.

## Other exact and exploratory extensions

- [`branch_recognition.md`](branch_recognition.md) — S1: hierarchical recognition prevalence, sharedness, and cross-copy policy coherence;
- [`multi_observer.md`](multi_observer.md) — separate first-person normalization across observers;
- [`binary_soft_qbs.md`](binary_soft_qbs.md) — minimal favorable/unfavorable weighting model;
- [`repeated_filtering.md`](repeated_filtering.md) — repeated adverse-trigger weighting and sensitivity identities;
- [`gaussian_model.md`](gaussian_model.md) — analytic Gaussian closed form;
- [`selection_equivalence.md`](selection_equivalence.md) — unnumbered exact boundary results: bounded accessibility is ordinary ascertainment conditioning; general integrable accessibility has an exact classical record-size-bias representation; arbitrary context-specific observer laws remain classically representable when the null may retune by context; a shared-selection null yields cross-context density-ratio restrictions, but operational testing additionally requires identifiable base/selected laws on a common observable state space;
- [`context_identifiability_stress.py`](context_identifiability_stress.py) — deterministic 20,000-trial finite-state sanity checks plus projection counterexamples for the context-identifiability boundary; supplementary audit code, not E6 and not physical bridge evidence;
- [`randomized_context_diagnostic.md`](randomized_context_diagnostic.md) — exact randomized-design diagnostic: under context randomization and a context-invariant binary selector, selected pre-treatment strata preserve the randomized context probability; exact finite-sample binomial/Bonferroni testing can falsify observable shared-selection violations while projection-blind latent violations remain undetectable;
- [`randomized_context_diagnostic.py`](randomized_context_diagnostic.py) — deterministic Monte Carlo calibration/power stress test for the randomized-context diagnostic; supplementary code, not E6 and not Everett evidence;
- [`randomization_regime_proxy.md`](randomization_regime_proxy.md) — extension with assignment regimes `p_r in {0.2,0.5,0.8}` and noisy pre-treatment proxies: a regime-invariant selector implies one common selected log-odds offset across regimes; varying assignment odds does not cure projection blindness, while informative proxy refinement can restore power;
- [`randomization_regime_proxy_stress.py`](randomization_regime_proxy_stress.py) — deterministic 5,000-repetition calibration/power stress test separating shared selection, stable context effects, regime retuning, and projection-blind latent effects; supplementary code, not E6 and not Everett evidence;
- [`prospective_recognition_protocol.md`](prospective_recognition_protocol.md) — longitudinal recognition-follow-up protocol: a past-dependent latent transition may be unobservable when it occurs while changing the conditional law of later sequences; future realizations remain unfixed, and empirical comparison targets sequence distributions against ordinary behavioral, survivorship, and classical-selection alternatives;
- [`evidence_activation.md`](evidence_activation.md) — evidence-driven recognition plus an unnumbered recursive observer-information extension: sequential weighting, predictable/innovation selection, and bridge-belief likelihood updates;
- [`recursive_qbs_simulation.py`](recursive_qbs_simulation.py) — exploratory classical recursive simulation with aligned, anti-aligned, and policy-only controls; not part of locked E1–E5;
- [`recognition_time.md`](recognition_time.md) — sequential recognition as a stopping time, with no general early-versus-late ordering theorem;
- [`selectivity_frontier.md`](selectivity_frontier.md) — selectivity versus predictor precision and accessible measure.

[`research_notes.md`](research_notes.md) is a **historical consolidated note** retained for research provenance. Current statements, assumptions, and status should be updated in the topic-specific files above first.

## Status vocabulary

- **EXACT / PROVED** — theorem or identity under stated assumptions;
- **SUFFICIENT CERTIFICATE** — one-sided sufficient condition, not a necessary characterization;
- **STATISTICAL CERTIFICATE** — finite-sample or population guarantee under explicit data and moment assumptions;
- **SIMULATION-SUPPORTED** — reproduced in the repository's classical toy experiments;
- **MODEL ASSUMPTION** — definitional modeling choice;
- **FORMALIZED / DEFERRED** — mathematical object defined while a stronger result is intentionally postponed;
- **OPEN** — unresolved theoretical or physical question.

The authoritative repository-wide claim classification is [`../docs/claims_and_assumptions.md`](../docs/claims_and_assumptions.md), and the claim-to-source index is [`../docs/research_map.md`](../docs/research_map.md).
