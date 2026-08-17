# Manuscript Source

This directory contains the evolving QBS manuscript source for public technical review and later preprint preparation.

## Structure

1. Abstract
2. Introduction
3. Related Work
4. Formal Model
5. Main Theorems
6. Adaptive-Agent Mechanism
7. Experiments
8. Everett Interpretation
9. Limitations and Falsifiability
10. Discussion
11. Appendices
12. References

## Writing rule

Every substantive statement should be identifiable as one of:

- theorem / proposition,
- simulation result,
- model assumption,
- statistical validation result,
- Everett bridge assumption,
- interpretation,
- open problem.

The manuscript must not state a simulation-supported classical mechanism or a statistical covariance certificate as an Everettian physical result.

## S2 theorem-stack editorial policy

The repository contains a deliberately modular post-v0.2 S2 theorem stack. Repository completeness does **not** imply that every theorem should receive equal prominence in the paper.

The current editorial recommendation is:

### Main-text candidates

- **S2** — predictive conditional-mean alignment;
- **S2.2** — posterior-mean self-calibration;
- **S2.11** — exact general-accessibility / residual covariance decomposition;
- **S2.13** — explained-variance form, if it materially improves interpretation.

### Appendix-first results

- S2.3–S2.4 — calibration/MSE robustness;
- S2.5–S2.7 — held-out and selection-safe finite-sample validity;
- S2.8–S2.10 — generic, light-tail, and robust confidence-envelope machinery;
- S2.12 — worst-case residual-variance certificate.

The rationale and dependency graph are maintained in `../docs/s2_stack_review_map.md`.

A new S2-numbered theorem should not be added by default. New theorem work should be driven by a material modeling gap, a concrete review objection, a genuinely new operational quantity, or a substantial sharpening under motivated assumptions.

## Interpretation boundary

The S2 family concerns probability, prediction, accessibility variables, and statistical certification. It does not derive the physical bridge:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E[S_\pi]}
\,d\mu(\omega)
$$

from Everettian quantum mechanics. The bridge remains a separate assumption and review target.

## Figures

GitHub-readable SVG previews are committed under `../figures/generated/`. LaTeX uses PDF variants generated from the same committed source data by:

```bash
python ../figures/generate_pdf_figures.py
```

The manuscript currently places:

- Figure 1: QBS recognition/policy/trajectory/accessibility schematic;
- Figure 2: FOSD theorem-boundary illustration;
- Figure 3: E3 paired recognition decomposition;
- Figure 4: E4 interaction-sign control;
- Figure 5: adaptation-quality / substitution sweep;
- Figure 6: E5 branch coherence versus marginal FP uplift.

Captions explicitly state whether each figure is a mathematical schematic, theorem illustration, or classical simulation.

## Local build

From the repository root:

```bash
pip install -r requirements.txt
python figures/generate_pdf_figures.py
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

GitHub Actions performs the same figure-generation and LaTeX/PDF validation automatically and uploads `paper/main.pdf` as an artifact.

## Current status

The v0.2 public-review baseline on `main` remains frozen. Post-v0.2 S2 developments are kept in stacked review PRs so proof review, statistical-validity review, and manuscript editorial decisions can be made separately before any later preprint merge.
