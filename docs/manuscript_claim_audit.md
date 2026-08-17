# v0.2 Manuscript Claim Consistency Audit

**Audit date:** 2026-08-17

This document checks the manuscript's load-bearing claims against `STATUS.md` and `docs/claims_and_assumptions.md`. It is intended to prevent theorem, simulation, and Everett interpretation claims from drifting across categories during editing.

## Audit categories

- **PROVED** — exact mathematical result under stated assumptions.
- **SIMULATION** — result of a committed classical toy experiment.
- **MECHANISM** — model-level explanatory interpretation supported by simulations and assumptions.
- **BRIDGE** — conditional Everett interpretation, not derived physics.
- **OPEN / DEFERRED** — not established in v0.2.
- **NON-CLAIM** — explicitly excluded from the paper.

## Core manuscript claims

| Claim | Status | Manuscript location | Repository support | Audit |
|---|---|---|---|---|
| Weighted FP mean shift equals covariance divided by expected accessibility | PROVED | Main Theorems / Appendix | T1 | PASS |
| Tail-probability shift has the corresponding indicator covariance form | PROVED | Main Theorems / Appendix | T2 | PASS |
| Nondecreasing conditional accessibility implies FOSD | PROVED | Main Theorems / Appendix | T3 | PASS |
| Recognition effect decomposes into trajectory and conditioning contributions | PROVED | Main Theorems / Appendix | T4 | PASS |
| Policy-QBS interaction has the targeting plus selector-map-shift decomposition | PROVED | Main Theorems / Appendix | T5 | PASS |
| Adaptive rescue gives nonpositive fixed-selector interaction under opposite monotonicity | PROVED | Appendix / Experiments | C5.1 | PASS |
| Recognition labels alone have no effect when neither utility nor accessibility changes | PROVED / NULL CONTROL | Appendix / E3 | T4 corollary + E3 | PASS |
| Predictive alignment can arise endogenously in a minimal learned toy agent | SIMULATION / MECHANISM | Abstract / Adaptive Agent / E2 | E2 | PASS |
| Cross-copy policy coherence and single-observer FP uplift are distinct | PROVED UNDER S1 ASSUMPTIONS + SIMULATION | Discussion / E5 | S1 + E5 | PASS |
| Recognition can have nonnegative option value when it expands the feasible policy set and old policies remain available | PROVED | Discussion / Appendix | P1 | PASS |
| The current mathematical framework derives Everettian observer weighting | NON-CLAIM | Abstract / Everett / Limitations | Claims ledger | PASS: explicitly denied |
| External RNG outcomes become objectively favorable | NON-CLAIM | Claims ledger / README boundary | Claims ledger | PASS: not asserted |
| QBS establishes quantum immortality | NON-CLAIM | Related Work / Claims ledger | Mallah boundary + claims ledger | PASS: not asserted |
| Earlier recognition is always better | OPEN / DEFERRED | Supplementary recognition-time note | stopping-time extension | PASS: explicitly not claimed |

## Abstract audit

The abstract states that the paper establishes a formal decision-and-conditioning framework and explicitly says it does **not** derive observer weighting from Everettian quantum mechanics.

**Result:** PASS.

## Discussion audit

The Discussion frames the novelty structurally: recognition-dependent policy affects trajectories and accessibility, those effects decompose, adaptation can substitute for selection at the margin, and branch coherence differs from marginal uplift.

The strongest physical language is explicitly conditioned on the Everett bridge.

**Result:** PASS.

## Everett / limitations audit

The manuscript now distinguishes:

1. abstract weighted-measure mathematics;
2. an observer-model bridge;
3. a physical Everett bridge.

It also distinguishes structural inconsistency from empirical falsification and states that an interpretation preserving all standard operational predictions may be empirically underdetermined.

**Result:** PASS, subject to future physical derivation or rejection of the bridge.

## Novelty audit

The manuscript must not use the following as standalone novelty claims:

- normalized nonnegative weighting;
- change of measure;
- the elementary covariance identity by itself;
- observer selection in general;
- self-locating uncertainty in general;
- Everettian decision theory in general.

The current candidate novelty package is instead:

1. recognition as a causal policy variable;
2. joint policy dependence of trajectory utility and accessibility;
3. exact trajectory-versus-conditioning decomposition;
4. exact policy-QBS interaction decomposition;
5. endogenous predictive alignment in adaptive toy agents;
6. explicit separation of single-observer FP uplift from branch-policy coherence;
7. a shared-latent coherence theorem under explicit hierarchical assumptions.

**Result:** PASS in current Abstract, Related Work, and Discussion wording.

## Remaining audit-sensitive edits

Before cutting v0.2, re-run this audit after:

- final figure captions and placement;
- any substantial Abstract or Introduction rewrite;
- any new claim added in response to public review;
- any change in the Everett bridge language.

## ERROR CHECK

1. PASS means consistency with the present repository status, not external validation of the physical interpretation.
2. A simulation-supported mechanism remains a toy-model claim unless separately established empirically.
3. S1 requires explicit shared-latent/conditional-independence assumptions; it is not an unconditional theorem that recognition creates correlation.
4. The stopping-time formalization does not establish timing monotonicity.
5. The physical Everett bridge remains conditional even though structural test criteria are now specified.

## Current audit result

**NO LOAD-BEARING MANUSCRIPT CLAIM WAS FOUND TO EXCEED ITS CURRENT REPOSITORY STATUS.**
