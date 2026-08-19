# Manuscript Source

This directory contains the evolving QBS manuscript source for technical review and later preprint preparation.

## Manuscript structure

1. Abstract
2. Introduction
3. Related Work
4. Formal Model
5. Main Theorems
6. Adaptive-Agent Mechanism
7. General Accessibility Beyond Score-Measurability
8. Experiments
9. Everett Interpretation
10. Limitations and Falsifiability
11. Discussion
12. Appendices
13. References

## Claim discipline

Substantive statements should remain identifiable as one of:

- exact theorem or proposition;
- sufficient condition;
- statistical certificate;
- classical simulation result;
- model assumption;
- Everett bridge assumption;
- interpretation;
- open problem.

The manuscript must not promote a classical simulation or a statistical covariance certificate into an Everettian physical result.

The repository-wide claim boundary is [`../docs/claims_and_assumptions.md`](../docs/claims_and_assumptions.md).

## Main-text S2 presentation

Repository completeness does not imply equal manuscript prominence. The current main text presents one conceptual spine:

```math
\text{S2 predictive alignment}
\longrightarrow
\text{S2.11 general accessibility}
\longrightarrow
\text{S2.12 residual penalty}
\longrightarrow
\text{S2.13 explained-variance interpretation}.
```

S2.2 appears as the posterior-mean calibration corollary.

Detailed statistical machinery is Appendix-first:

- S2.3–S2.4 — calibration/MSE robustness;
- S2.5–S2.7 — held-out and selection-safe finite-sample validity;
- S2.8–S2.10 — generic, light-tail, and robust confidence-envelope machinery;
- S2.12 — full residual-variance proof and sharpness analysis.

`sections/robust_mom_summary.tex` is intentionally retained as a standalone historical/editorial source but is **not** part of the compiled `main.tex` input graph. The compiled robust-MoM treatment is `sections/robust_mom_certificate_appendix.tex`. The LaTeX preflight locks this single-file uncompiled allowlist so that accidentally omitting any other manuscript section from `main.tex` becomes a CI failure rather than merely increasing an informational count.

The dependency and editorial map is [`../docs/s2_stack_review_map.md`](../docs/s2_stack_review_map.md). The dedicated proof review is [`../docs/post_v02_core_s2_proof_review.md`](../docs/post_v02_core_s2_proof_review.md).

No new S2-numbered theorem should be added by default. New theorem work should respond to a material modeling gap or concrete review objection.

## Interpretation boundary

The S2 family concerns probability, prediction, accessibility variables, and statistical certification. It does not derive the physical bridge:

```math
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E[S_\pi]}
\,d\mu(\omega)
```

from Everettian quantum mechanics. The bridge remains a separate physical assumption and review target.

## Figures

GitHub-readable SVG previews are committed under `../figures/generated/`. LaTeX uses PDF variants generated from the same committed source data by:

```bash
python ../figures/generate_pdf_figures.py
```

The manuscript currently places six figures covering the QBS framework, FOSD boundary, recognition decomposition, interaction sign, adaptation quality, and branch coherence. Captions identify whether each figure is a mathematical schematic, theorem illustration, or classical simulation.

## Local build

From the repository root:

```bash
pip install -r requirements.txt
python scripts/validate_runtime_contract.py
python figures/generate_pdf_figures.py
python scripts/validate_latex_sources.py
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

GitHub Actions performs runtime-contract validation, figure generation, compiled-input-graph LaTeX/PDF validation, and manuscript compilation automatically, then uploads `paper/main.pdf` as an artifact.

## Current review state

The current frozen public-review snapshot is tag/Release `v0.3-public-review`. The previous v0.2 snapshot remains archived at tag/Release `v0.2-public-review`.

The manuscript files on `main` are the current review/development surface. Historical PRs #11–#21 remain available for derivation provenance only.

Current manuscript decisions are review-driven:

1. verify S2, S2.11, S2.12, and S2.13 under external proof review;
2. decide whether S2.13 remains in the main text;
3. decide whether some S2.5–S2.10 material moves from the paper Appendix to repository-only supplementary material;
4. preserve the Everett bridge as a separate physical question.
