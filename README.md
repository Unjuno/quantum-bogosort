# Quantum Bogosort (QBS)

**Status:** v0.1 — Public Technical Review

Formal theory and reproducible simulations of recognition-activated Quantum Bogosort, including policy-dependent trajectories, observer-indexed accessibility, and cross-branch decision correlations.

## Core idea

Recognition of a QBS rule may change both:

1. the branch-wise trajectory policy, producing a different outcome map \(U_\pi(\omega)\); and
2. the observer-indexed accessibility map \(S_\pi(\omega)\).

The first-person value is modeled as

\[
V_{FP}(\pi)=\frac{E_\mu[U_\pi S_\pi]}{E_\mu[S_\pi]}.
\]

For pre-recognition \(S_0\equiv1\),

\[
V_{FP}(\pi_1)-V_{FP}(\pi_0)
=
E[U_1-U_0]
+
\frac{\operatorname{Cov}(U_1,S_1)}{E[S_1]}.
\]

The first term is the causal trajectory/policy effect. The second term is the QBS first-person conditioning effect.

## Mathematical status

The core theorem set is in [`theory/core_theorems.md`](theory/core_theorems.md) and [`theory/core_theorems.tex`](theory/core_theorems.tex).

The current theorem set includes:

1. QBS Covariance Identity
2. Tail Probability Identity
3. Monotone Accessibility ⇒ First-Order Stochastic Dominance
4. Recognition Decomposition
5. Policy–QBS Interaction Decomposition

Additional propositions cover nonnegative option value of costless recognition, support preservation under pure reweighting, and the \(E[S]=0\) extinction/undefined-measure boundary.

## Principal experiments

The locked experiment manifest is [`experiments/manifest.csv`](experiments/manifest.csv).

- **E1 — Pure QBS / FOSD.** Tests covariance, tails, monotone accessibility, and FOSD. Stress tests include \(S\perp U\) and nonmonotone accessibility.
- **E2 — Minimal learned agent.** Tests whether predictive structure and QBS uplift arise when a small model can represent the relevant world structure, versus misspecified controls.
- **E3 — Recognition decomposition.** Uses identical primitive branch seeds to separate policy/trajectory effects from QBS conditioning effects. Includes an exact paired recognition-null test.
- **E4 — Adaptive-policy / QBS interaction.** Tests the covariance sign rule and the generalized \(S_0\neq S_1\) interaction decomposition.
- **E5 — Cross-branch recognition map.** Tests how shared recognition and shared world structure induce correlated decisions across branch copies.

Reproduction scripts are in [`experiments/`](experiments/). Locked outputs and reproduction outputs are in [`data/processed/`](data/processed/).

## Reproduction

Python 3.10+ is recommended.

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

All five scripts were re-run successfully before the v0.1 public-review release.

## Everett interpretation

The mathematical results do **not** establish an Everett interpretation by themselves.

The separate Everett-QBS bridge assumption is

\[
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
d\mu(\omega),
\]

where \(S_\pi\) is interpreted as observer-indexed branch accessibility.

The repository intentionally separates:

- measure-theoretic results,
- classical agent simulations, and
- the Everett physical interpretation.

## Falsifiability / failure modes

The framework predicts no pure QBS uplift when accessibility is independent of outcome. FOSD is not guaranteed when accessibility is nonmonotone in outcome quality. Recognition has no effect if it changes neither trajectory policy nor accessibility. If \(E[S]=0\), the normalized first-person measure is undefined.

Counterexamples and stress tests are included rather than treating these assumptions as automatic.

## Public technical review

This repository is being released before the manuscript is finalized. Mathematical corrections, counterexamples, prior-art pointers, implementation bugs, and challenges to the Everett bridge assumption are welcome through GitHub Issues.

The intended sequence is:

1. public technical review of v0.1;
2. approximately two weeks of feedback collection;
3. revision of proofs, experiments, and literature positioning;
4. manuscript and arXiv submission preparation.

## License

This repository uses a split license:

- **Source code:** MIT License — see [`LICENSE`](LICENSE).
- **Manuscript, theoretical notes, documentation, and figures:** Creative Commons Attribution 4.0 International (CC BY 4.0) — see [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt).
- **Generated research datasets:** Creative Commons CC0 1.0 Universal — see [`LICENSES/CC0-1.0.txt`](LICENSES/CC0-1.0.txt).

Unless a file states otherwise, Python source files are MIT-licensed, prose/LaTeX/figures are CC BY 4.0, and generated CSV research outputs are CC0 1.0.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). The repository is currently a pre-publication research artifact; citation details should be updated when a manuscript identifier becomes available.
