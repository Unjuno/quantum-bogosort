# E2 — Minimal Learned Agent and Endogenous Predictive Correlation

## H — Hypothesis

Positive outcome/accessibility alignment need not be inserted as an external correlation parameter. An adapted predictor can generate the relevant ordering if its model class can represent the environment's predictive structure.

## T — Test

The toy environment uses a nonlinear interaction structure. Competing evaluators include:

- a misspecified linear model,
- a small model with the required interaction feature,
- a random-score control.

The learned score is converted into an accessibility rule, and the resulting score/outcome correlation and first-person uplift are measured.

## D — Data / Result

Locked summaries:

- `data/processed/qbs_nonlinear_minimal_mock_summary.csv`
- `data/processed/qbs_correlation_uplift_relation.csv`

Reproduction output:

- `data/processed/e2_minimal_agent_reproduction.csv`

The interaction-capable evaluator learns a strong positive predictive relationship that weakens as environmental noise increases. The misspecified linear evaluator and random control remain near zero. In the locked toy study, positive-correlation levels were closely associated with positive first-person uplift.

## C — Controls / Counterexamples

The misspecified linear model is the key control: access to data alone is insufficient if the representation cannot encode the predictive interaction. The random-score control checks that arbitrary selection does not create systematic uplift.

## U — Uncertainty / Interpretation Boundary

This is evidence for an endogenous predictor-selector mechanism in a classical toy model. It does not show that biological or physical adaptation guarantees positive Pearson correlation, nor does it establish an Everett accessibility rule.

## ERROR CHECK

- Compare learned versus misspecified versus random evaluators on the same environment family.
- Verify that the learned relationship weakens with increasing noise.
- Treat the empirical uplift/correlation fit as toy-model evidence, not a universal law.
- CI re-runs the experiment.

## Linked theory

T1 and T3, plus `supplementary/adaptive_agent.md` after supplementary decomposition.
