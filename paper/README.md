# Manuscript Source

This directory contains the evolving QBS manuscript source for the public-review process.

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
11. Appendix
12. References

## Writing rule

Every substantive statement should be identifiable as one of:

- theorem / proposition,
- simulation result,
- model assumption,
- Everett bridge assumption,
- interpretation,
- open problem.

The manuscript must not state a simulation-supported classical mechanism as an Everettian physical result.

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

The core theorem set, proof appendix, five experiment families, Related Work, Everett bridge limitations, figure placement, and PDF build pipeline are integrated. Remaining pre-v0.2 work is primarily final prose/cross-reference review, release auditing, and any targeted prior-art update justified by review.
