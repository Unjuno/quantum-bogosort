# E1 — Pure QBS Weighting, Tail Identities, and FOSD

## H — Hypothesis

If accessibility is positively aligned with outcome quality, first-person weighted outcomes should shift upward. A stronger monotonicity condition on conditional accessibility should imply first-order stochastic dominance.

## T — Test

The experiment evaluates several base distributions and monotone soft-accessibility functions. It also includes two falsification controls:

1. accessibility independent of outcome;
2. nonmonotone accessibility.

The theoretical benchmark is:

$$
E_{FP}[X]-E[X]
=
\frac{\mathrm{Cov}(X,S)}{E[S]}.
$$

For FOSD, the sufficient condition is that:

$$
g(x)=E[S\mid X=x]
$$

is nondecreasing.

## D — Data / Result

Locked summaries:

- `data/processed/qbs_fosd_robustness_summary.csv`
- `data/processed/qbs_fosd_monotonicity_summary.csv`
- `data/processed/qbs_stress_independence_null.csv`
- `data/processed/qbs_stress_nonmonotone_fosd.csv`

Reproduction outputs:

- `data/processed/e1_fosd_reproduction.csv`
- `data/processed/e1_independence_null_reproduction.csv`
- `data/processed/e1_nonmonotone_counterexample_reproduction.csv`

Across the tested Gaussian, heavy-tail, bimodal, and skewed toy distributions, monotone accessibility produced the predicted FOSD direction within the configured numerical tolerance.

## C — Controls / Counterexamples

When `S` is independent of `X`, mean uplift is zero in expectation. When accessibility is nonmonotone, the FP and base CDFs can cross. Positive mean uplift alone therefore does not imply FOSD.

## U — Uncertainty / Interpretation Boundary

This experiment verifies the formal weighted-measure structure. It does not establish the physical origin of accessibility weights in Everettian quantum mechanics.

## ERROR CHECK

- Covariance identities are exact algebraic benchmarks.
- Independence null is required to remain near zero up to Monte Carlo error.
- Nonmonotone controls are expected to permit FOSD failure.
- CI re-runs the reproduction script on every relevant pull request.

## Linked theory

T1, T2, T3 in `theory/theorem_1_3.md`.
