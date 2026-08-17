# Quantum Bogosort (QBS)

**Status:** v0.1 — Public Technical Review

Formal theory and reproducible simulations of recognition-activated Quantum Bogosort, including policy-dependent trajectories, observer-indexed accessibility, and cross-branch decision correlations.

## Core model

Recognition may change both policy-dependent trajectories and the accessibility map:

$$
R \longrightarrow \pi_R \longrightarrow (U_R,S_R).
$$

First-person value is modeled as:

$$
V_{FP}(\pi)
=
\frac{E_\mu[U_\pi S_\pi]}{E_\mu[S_\pi]}.
$$

For the baseline with no pre-recognition selector:

$$
S_0\equiv1,
$$

so:

$$
V_1-V_0
=
E[U_1-U_0]
+
\frac{\operatorname{Cov}(U_1,S_1)}{E[S_1]}.
$$

The first term is the ordinary causal policy/trajectory effect. The second is the first-person conditioning contribution.

## Theory

GitHub-rendered theorem notes are indexed at [`theory/core_theorems.md`](theory/core_theorems.md):

1. QBS Covariance Identity
2. Tail Probability Identity
3. Monotone Accessibility implies First-Order Stochastic Dominance
4. Recognition Decomposition
5. Policy–QBS Interaction Decomposition

The notes also cover option value, support preservation under pure reweighting, the zero-accessible-measure boundary, counterexamples, and the separate Everett bridge assumption. LaTeX manuscript source remains available at [`theory/core_theorems.tex`](theory/core_theorems.tex).

## Experiments

The locked experiment map is [`experiments/manifest.csv`](experiments/manifest.csv).

- **E1:** covariance, tails, FOSD, independence null, and nonmonotone counterexample.
- **E2:** minimal learned agent and endogenous predictive correlation.
- **E3:** paired recognition decomposition and recognition-label null.
- **E4:** fixed-selector interaction identity plus the general selector-map-shift decomposition.
- **E5:** paired execution-strength and environment-correlation sweeps, plus shared versus branch-independent recognition.

Run all five from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python experiments/exp1_fosd_and_stress.py
python experiments/exp2_minimal_agent.py
python experiments/exp3_recognition_decomposition.py
python experiments/exp4_interaction.py
python experiments/exp5_branch_map.py
```

Historical locked summaries and current reproduction outputs are stored in [`data/processed/`](data/processed/).

## Supplementary research notes

Important results that are not part of the five-experiment core are preserved in [`supplementary/research_notes.md`](supplementary/research_notes.md), including multi-observer normalization, repeated-filter identities, the Gaussian minimal model, evidence-driven recognition activation, selectivity frontiers, and the information-theoretic adaptive-agent interpretation.

## Markdown math convention

Markdown math in this repository uses **double-dollar display blocks only**. Inline mathematical symbols are written as code spans or moved into display blocks. CI rejects legacy parenthesis/bracket math delimiters and single-dollar math delimiters.

## Validation

GitHub Actions runs:

- Python compilation checks,
- Markdown math-delimiter validation,
- all five reproduction scripts,
- manifest reference validation.

The corrected local validation run completed all five experiments in about 12 seconds. E4 identity errors were at floating-point precision. E5 gives exactly zero total effect at `q=0`, and the paired execution-strength decomposition error remains at floating-point precision.

## Everett interpretation

The mathematical results do **not** establish an Everett interpretation by themselves. The separate bridge assumption is:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

The repository keeps measure-theoretic results, classical simulations, and the Everett physical interpretation distinct.

## Falsifiability and boundaries

The framework predicts no pure weighting uplift when accessibility is independent of outcome. FOSD need not hold for nonmonotone accessibility. Recognition has no effect if it changes neither trajectory utility nor accessibility. If expected accessibility is zero, the normalized first-person measure is undefined.

## Public technical review

Corrections, counterexamples, prior-art pointers, implementation bugs, and challenges to the Everett bridge assumption are welcome through GitHub Issues. The intended sequence is public review, revision, then manuscript and arXiv preparation.

## License

This repository uses file-type split licensing:

- Source code: **MIT** — [`LICENSE`](LICENSE)
- Theory, documentation, manuscript text, and figures: **CC BY 4.0** — [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt)
- Generated research datasets: **CC0 1.0** — [`LICENSES/CC0-1.0.txt`](LICENSES/CC0-1.0.txt)

See [`LICENSES/README.md`](LICENSES/README.md) for the licensing map. `CITATION.cff` intentionally does not encode the split licensing as one interchangeable license list.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). Update it when a manuscript identifier becomes available.
