# QBS Research Map

This is the canonical index from QBS claims to theorem sources, experiments, manuscript material, and interpretation status.

## 1. Core architecture

```math
R
\longrightarrow
\pi_R
\longrightarrow
(U_R,S_R).
```

For a policy `pi`, the normalized first-person measure requires nonnegative accessibility with positive finite mean. Finite value/covariance decompositions additionally require both base and weighted outcome integrability:

```math
S_\pi\ge0,
\qquad
0<E[S_\pi]<\infty,
\qquad
E[|U_\pi|]<\infty,
\qquad
E[|U_\pi|S_\pi]<\infty.
```

Then:

```math
V_{FP}(\pi)
=
\frac{E_\mu[U_\pi S_\pi]}{E_\mu[S_\pi]}.
```

For the general selector-changing T5 decomposition, the intermediate `Q(U_1,S_0)` term additionally requires:

```math
E[|U_1|S_0]<\infty.
```

The repository separates three questions:

1. what follows mathematically from the weighted-measure model;
2. what is reproduced in classical simulations or statistically certified under stated assumptions;
3. whether a physical Everett model supplies the proposed accessibility map.

## 2. Core theorem map: T1–T5

| ID | Claim | Type | Primary source | Computational check |
|---|---|---|---|---|
| T1 | FP mean shift equals normalized outcome/accessibility covariance | EXACT THEOREM | [`theory/core_theorems.md`](../theory/core_theorems.md) | E1 |
| T2 | Tail shift has the same covariance form | EXACT THEOREM | [`theory/core_theorems.md`](../theory/core_theorems.md) | E1 |
| T3 | Monotone conditional accessibility implies FOSD | EXACT THEOREM | [`theory/core_theorems.md`](../theory/core_theorems.md) | E1 |
| T4 | Recognition decomposes into trajectory and conditioning effects | EXACT THEOREM | [`theory/core_theorems.md`](../theory/core_theorems.md) | E3 |
| T5 | Policy–QBS interaction decomposes into targeting and selector-map effects | EXACT THEOREM | [`theory/core_theorems.md`](../theory/core_theorems.md) | E4 |

The locked core theorem set stops at T5. Current `main` preserves every identity/proof while making the finite-integrability domain explicit; the frozen v0.3 tag remains unchanged.

## 3. Core experiment map: E1–E5

| ID | Purpose | Evidence class | Card |
|---|---|---|---|
| E1 | covariance, tail shift, FOSD, independence null, nonmonotone counterexample | CLASSICAL SIMULATION | [`experiments/E1_FOSD.md`](../experiments/E1_FOSD.md) |
| E2 | endogenous predictive alignment in a minimal learned agent | CLASSICAL SIMULATION | [`experiments/E2_LEARNED_AGENT.md`](../experiments/E2_LEARNED_AGENT.md) |
| E3 | paired recognition decomposition and recognition-label null | CLASSICAL SIMULATION | [`experiments/E3_RECOGNITION.md`](../experiments/E3_RECOGNITION.md) |
| E4 | fixed/changing-selector interaction decomposition | CLASSICAL SIMULATION | [`experiments/E4_INTERACTION.md`](../experiments/E4_INTERACTION.md) |
| E5 | marginal FP uplift versus cross-copy policy coherence | CLASSICAL SIMULATION | [`experiments/E5_BRANCH_MAP.md`](../experiments/E5_BRANCH_MAP.md) |

These simulations reproduce the formal structure. They are not empirical evidence for an Everettian accessibility law.

## 4. Supplementary conceptual spine

The supplementary predictive-alignment line should be read as one argument:

```math
\text{predictive signal}
\longrightarrow
\text{conditional-mean alignment}
\longrightarrow
\text{outcome/accessibility covariance}
\longrightarrow
\text{first-person shift}.
```

The principal conceptual results are:

| ID | Role | Type | Primary source |
|---|---|---|---|
| S2 | score-measurable accessibility projects covariance onto conditional means | EXACT SUPPLEMENTARY THEOREM | [`supplementary/adaptive_agent.md`](../supplementary/adaptive_agent.md) |
| S2.2 | posterior-mean scores self-calibrate | EXACT COROLLARY | [`supplementary/adaptive_agent.md`](../supplementary/adaptive_agent.md) |
| S2.11 | general accessibility equals conditional-mean alignment plus residual conditional covariance | EXACT SUPPLEMENTARY THEOREM | [`supplementary/residual_covariance_extension.md`](../supplementary/residual_covariance_extension.md) |
| S2.12 | conditional variances give a sharp universal worst-case residual penalty | SUFFICIENT LOWER CERTIFICATE | [`supplementary/residual_variance_certificate.md`](../supplementary/residual_variance_certificate.md) |
| S2.13 | explained-variance fractions and conditional-mean correlation reparameterize S2.12 | SUFFICIENT NORMALIZED CERTIFICATE | [`supplementary/explained_variance_certificate.md`](../supplementary/explained_variance_certificate.md) |

The central general-accessibility identity is:

```math
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(E[U\mid Y],E[S\mid Y])
+
E[\mathrm{Cov}(U,S\mid Y)].
```

S2.12 and S2.13 are sufficient worst-case certificates. Failure of either certificate does not imply negative total covariance.

## 5. Statistical certification layer

S2.3–S2.10 support the conceptual spine but are not separate conceptual pillars.

| IDs | Role | Type | Primary source |
|---|---|---|---|
| S2.3–S2.4 | calibration-error and prediction-MSE population robustness | SUFFICIENT POPULATION BOUNDS | [`supplementary/adaptive_agent.md`](../supplementary/adaptive_agent.md) |
| S2.5 | bounded independent-held-out finite-sample certificate | STATISTICAL CERTIFICATE | [`supplementary/finite_sample_certificate.md`](../supplementary/finite_sample_certificate.md) |
| S2.6–S2.7 | independent training and multiplicity-corrected finite candidate selection | STATISTICAL VALIDITY | [`supplementary/selection_validity.md`](../supplementary/selection_validity.md) |
| S2.8 | generic simultaneous moment-envelope composition | STATISTICAL CERTIFICATE | [`supplementary/confidence_envelope_certificate.md`](../supplementary/confidence_envelope_certificate.md) |
| S2.9 | sub-Gaussian/Bernstein light-tail instantiation | STATISTICAL INSTANTIATION | [`supplementary/light_tail_certificate.md`](../supplementary/light_tail_certificate.md) |
| S2.10 | median-of-means finite-moment instantiation | ROBUST STATISTICAL INSTANTIATION | [`supplementary/robust_mom_certificate.md`](../supplementary/robust_mom_certificate.md) |

Training/certification leakage, uncorrected model selection, or invalid moment assumptions invalidate the corresponding finite-sample guarantee.

## 6. Other supplementary results

| ID/topic | Role | Source |
|---|---|---|
| S1 | hierarchical recognition can produce nonnegative cross-copy action covariance under the stated conditional-independence structure | [`supplementary/branch_recognition.md`](../supplementary/branch_recognition.md) |
| recognition time | recognition as a stopping-time extension; no universal early-recognition ordering theorem | [`supplementary/recognition_time.md`](../supplementary/recognition_time.md) |
| repeated filtering | repeated adverse-trigger accessibility identities | [`supplementary/repeated_filtering.md`](../supplementary/repeated_filtering.md) |
| recursive observer-information loop | unnumbered dynamic extension closing the feedback from experienced observer history to bridge belief, adoption/policy, accessibility, and later observer history; includes sequential weighting and predictable/innovation selection | [`supplementary/evidence_activation.md`](../supplementary/evidence_activation.md) |
| recursive simulation | exploratory classical implementation with aligned, anti-aligned, and policy-only controls; not part of locked E1–E5 | [`supplementary/recursive_qbs_simulation.py`](../supplementary/recursive_qbs_simulation.py) |
| selectivity frontier | tradeoff between selectivity, prediction quality, and accessible measure | [`supplementary/selectivity_frontier.md`](../supplementary/selectivity_frontier.md) |

The complete supplementary index is [`supplementary/README.md`](../supplementary/README.md).

## 7. First-person shift versus objective chance

QBS changes the first-person weighting in the model when accessibility and outcome are aligned. The base measure itself is not thereby changed.

A convenient summary is:

```math
\text{base chance unchanged}
\qquad\text{while}\qquad
\text{first-person trajectory weight changes}.
```

The same change of measure can be applied to a present state when accessibility is determined over a future continuation. Let `Z` denote a present state and `S_T` future accessibility. Then:

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

If `P(Z=z)=0`, absolute continuity of the weighted measure gives `P_FP(Z=z)=0`; no pointwise conditional expectation at that null atom is needed.

Thus differential future accessibility can reweight present self-location toward states associated with higher expected future accessibility. This is a conditioning/change-of-measure statement, not backward causation or a causal change in the base probability law.

A favorable first-person shift is therefore a statement about the observer-conditioned distribution, not a claim that an external random-number generator becomes causally biased.

### Dynamic recursive extension

The unnumbered recursive extension makes the previously implicit feedback step explicit:

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

On a filtered base probability space, outcome increments can be decomposed relative to the information available when the decision is made:

```math
m_{t+1}=E_\mu[X_{t+1}\mid H_t],
\qquad
\varepsilon_{t+1}=X_{t+1}-m_{t+1}.
```

For cumulative predictable and innovation components `A_T` and `M_T`, with `U_T=A_T+M_T` and `E_\mu[M_T]=0`, T1 gives the exact horizon decomposition:

```math
E_{FP}[U_T]-E_\mu[U_T]
=
\frac{\mathrm{Cov}_\mu(A_T,S_T)}{E_\mu[S_T]}
+
\frac{\mathrm{Cov}_\mu(M_T,S_T)}{E_\mu[S_T]}.
```

The first term is called **predictable selection** and the second **innovation selection**. Innovation selection is filtration-relative: enlarging the information state can move variation from the innovation component into the predictable component. It is a formal diagnostic for first-person reweighting of decision-time-unpredictable variation, not a claim that objective chance has been causally improved.

The same extension allows a specified bridge model to be compared with a null observer model through sequential likelihood-ratio updates. Under correctly specified conditional models, the expected one-step log likelihood ratio has KL-divergence sign under the corresponding model. These are standard Bayesian/information-theoretic identities used to close the feedback arrow; they do not validate the physical bridge.

Canonical terminology is maintained in [`docs/notation.md`](notation.md).

## 8. Everett bridge

The physical bridge is a separate model assumption:

```math
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
```

The abstract change-of-measure mathematics is exact after the model is defined. A physical Everett interpretation additionally requires an independent account of why observer persistence or self-location induces the proposed `S_pi`.

See [`docs/everett_bridge_tests.md`](everett_bridge_tests.md) for support, constraint, and rejection criteria.

## 9. Claim boundaries

The authoritative classification of theorem claims, simulations, assumptions, bridge claims, and non-claims is [`docs/claims_and_assumptions.md`](claims_and_assumptions.md).

Important boundaries include:

- finite mean/covariance decompositions require both base and weighted outcome integrability;
- the general T5 selector-changing identity requires the cross-integrability of `U_1` against `S_0`;
- positive covariance does not by itself imply FOSD;
- pure reweighting does not create support absent from the fixed-policy base measure;
- zero expected accessibility makes the normalized FP measure undefined;
- mutual information alone does not imply positive QBS covariance;
- S2.11 requires the residual conditional-covariance term outside score-measurable accessibility;
- innovation selection depends on the chosen information filtration and is not synonymous with objective luck;
- recursive bridge-belief updates are model-comparison statements and can be misleading under misspecification;
- statistical or recursive-simulation success does not establish the Everett bridge.

## 10. Manuscript and proof-review path

The manuscript is in [`paper/`](../paper/). The current main-text S2 presentation is intentionally compressed to the conceptual spine, while S2.3–S2.10 are Appendix-first. The recursive observer-information extension currently remains repository supplementary material and has not been promoted into the locked core or manuscript claim set.

The dedicated post-v0.2 proof review is [`docs/post_v02_core_s2_proof_review.md`](post_v02_core_s2_proof_review.md). The editorial dependency map is [`docs/s2_stack_review_map.md`](s2_stack_review_map.md).

## 11. Current open research questions

The current review gate is external proof, novelty, physical-bridge scrutiny, and recursive-model stress testing rather than automatic theorem expansion.

Open questions include:

- what physical mechanism, if any, induces the Everett accessibility map;
- whether the recursive bridge-belief loop remains informative under realistic model misspecification, survivorship-only controls, and alternative observer models;
- whether innovation selection is a useful stable diagnostic under motivated information filtrations;
- whether the current S2.13 explained-variance summary should remain in the manuscript main text after review;
- whether some S2.5–S2.10 material belongs only in repository supplementary material;
- whether reviewers identify a concrete need for stronger finite-sample or model-selection theory;
- under what motivated assumptions recognition time admits a useful ordering theorem.

Future work is tracked in [`ROADMAP.md`](../ROADMAP.md). Current state is tracked in [`DEVELOPMENT_STATUS.md`](../DEVELOPMENT_STATUS.md).