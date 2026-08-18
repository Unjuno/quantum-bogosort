# Supplementary QBS Notes

These notes contain exact secondary results, statistical certification layers, and exploratory extensions outside the locked T1–T5 / E1–E5 core.

## Conceptual theorem spine

Read the post-v0.2 predictive-alignment line in this order:

1. [`adaptive_agent.md`](adaptive_agent.md) — S2 and S2.1–S2.4: predictive conditional-mean alignment, posterior-mean self-calibration, population robustness, and the mutual-information boundary.
2. [`residual_covariance_extension.md`](residual_covariance_extension.md) — S2.11: exact extension beyond score-measurable accessibility using residual conditional covariance.
3. [`residual_variance_certificate.md`](residual_variance_certificate.md) — S2.12: sharp worst-case residual lower bounds from conditional variances.
4. [`explained_variance_certificate.md`](explained_variance_certificate.md) — S2.13: explained-variance / conditional-mean-correlation form of the S2.12 certificate.

The conceptual chain is:

$$
\text{predictive signal}
\longrightarrow
\text{conditional-mean alignment}
\longrightarrow
\text{outcome/accessibility covariance}
\longrightarrow
\text{first-person shift}.
$$

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
- [`evidence_activation.md`](evidence_activation.md) — recognition activated by statistical evidence;
- [`recognition_time.md`](recognition_time.md) — sequential recognition as a stopping time, with no general early-versus-late ordering theorem;
- [`selectivity_frontier.md`](selectivity_frontier.md) — selectivity versus predictor precision and accessible measure.

`research_notes.md` remains a historical consolidated note. Current work should update the topic-specific files first.

## Status vocabulary

- **EXACT / PROVED** — theorem or identity under stated assumptions;
- **SUFFICIENT CERTIFICATE** — one-sided sufficient condition, not a necessary characterization;
- **STATISTICAL CERTIFICATE** — finite-sample or population guarantee under explicit data and moment assumptions;
- **SIMULATION-SUPPORTED** — reproduced in the repository's classical toy experiments;
- **MODEL ASSUMPTION** — definitional modeling choice;
- **FORMALIZED / DEFERRED** — mathematical object defined while a stronger result is intentionally postponed;
- **OPEN** — unresolved theoretical or physical question.

The authoritative repository-wide claim classification is [`../docs/claims_and_assumptions.md`](../docs/claims_and_assumptions.md), and the claim-to-source index is [`../docs/research_map.md`](../docs/research_map.md).
