# Quantum Bogosort (QBS)

Quantum Bogosort is a formal research program for recognition-dependent policies whose trajectories and observer-indexed accessibility can change together.

The core structure is:

$$
R
\longrightarrow
\pi_R
\longrightarrow
(U_R,S_R).
$$

Here `R` is recognition, `pi_R` is the policy used under that recognition state, `U_R` is the resulting outcome or utility, and `S_R` is a nonnegative observer-indexed accessibility weight.

## Core first-person quantity

For:

$$
0<E_\mu[S_\pi]<\infty,
$$

the first-person value is:

$$
V_{FP}(\pi)
=
\frac{E_\mu[U_\pi S_\pi]}{E_\mu[S_\pi]}.
$$

For the baseline:

$$
S_0\equiv1,
$$

the recognition effect decomposes as:

$$
V_1-V_0
=
E[U_1-U_0]
+
\frac{\operatorname{Cov}(U_1,S_1)}{E[S_1]}.
$$

The first term is the ordinary policy/trajectory effect. The second is the first-person conditioning contribution.

A positive conditioning contribution means that the first-person measure gives greater weight to favorable accessible trajectories. It does **not** mean that the base measure or an external random-number generator is causally changed.

## What is established

### Core mathematics

The locked core theorem set is T1–T5:

1. covariance identity for the first-person mean shift;
2. tail-probability covariance identity;
3. a monotone-accessibility sufficient condition for FOSD;
4. recognition decomposition;
5. policy–QBS interaction decomposition.

See [`theory/core_theorems.md`](theory/core_theorems.md) and the canonical [`docs/research_map.md`](docs/research_map.md).

### Post-v0.2 supplementary line

The current supplementary argument is organized around one conceptual spine:

$$
\text{predictive alignment}
\longrightarrow
\text{general accessibility}
\longrightarrow
\text{residual penalty}
\longrightarrow
\text{explained-variance certificate}.
$$

Its principal results are S2, S2.11, S2.12, and S2.13. S2.3–S2.10 provide calibration, finite-sample, selection-validity, light-tail, and robust statistical certification machinery. See [`supplementary/README.md`](supplementary/README.md).

### Reproducible simulations

The locked core experiment suite is E1–E5:

- [`experiments/E1_FOSD.md`](experiments/E1_FOSD.md) — covariance, tails, FOSD, independence null, and a nonmonotone counterexample;
- [`experiments/E2_LEARNED_AGENT.md`](experiments/E2_LEARNED_AGENT.md) — endogenous predictive alignment in a minimal learned agent;
- [`experiments/E3_RECOGNITION.md`](experiments/E3_RECOGNITION.md) — paired recognition decomposition;
- [`experiments/E4_INTERACTION.md`](experiments/E4_INTERACTION.md) — policy–QBS interaction decomposition;
- [`experiments/E5_BRANCH_MAP.md`](experiments/E5_BRANCH_MAP.md) — marginal first-person uplift versus cross-copy policy coherence.

These are classical simulations of the formal model.

## What remains open

The mathematical weighting results do not by themselves derive an Everettian physical interpretation. The separate bridge assumption is:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

A concrete physical account must explain why an Everettian observer should be described by the proposed accessibility map. The structural and empirical review criteria are in [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md).

The repository also does not claim that statistical covariance certification establishes Everettian observer selection, that positive correlation alone implies FOSD, or that external random generators become objectively lucky. The complete claim boundary is maintained in [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md).

## Where to read next

| Goal | Start here |
|---|---|
| Understand the complete claim structure | [`docs/research_map.md`](docs/research_map.md) |
| Check theorem statements and assumptions | [`theory/core_theorems.md`](theory/core_theorems.md) and [`supplementary/README.md`](supplementary/README.md) |
| Check claim strength and non-claims | [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md) |
| Check notation and terminology | [`docs/notation.md`](docs/notation.md) |
| Reproduce the simulations | [`experiments/manifest.csv`](experiments/manifest.csv) and [`experiments/`](experiments/) |
| Review the Everett bridge | [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md) |
| Read the manuscript | [`paper/`](paper/) |
| Review prior art and novelty boundaries | [`literature/`](literature/) |
| See the current post-v0.2 state | [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md) |

## Reproduce E1–E5

From the repository root:

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

Historical locked summaries and current reproduction outputs are stored in [`data/processed/`](data/processed/). Superseded experiment designs are kept under [`experiments/archive/`](experiments/archive/).

## Public review

Use [`CONTRIBUTING.md`](CONTRIBUTING.md) and the issue templates for:

- proof or counterexample reports;
- prior-art overlap;
- reproducibility failures;
- Everett-bridge criticism.

The current review priority is proof and novelty review of the compressed post-v0.2 conceptual spine rather than further theorem expansion.

## Repository state

The repository distinguishes the frozen v0.2 snapshot from the current integrated review state:

- stable v0.2 snapshot: branch `release/v0.2-public-review`, commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`;
- stable snapshot ledger: [`STATUS.md`](STATUS.md);
- current integrated post-v0.2 review surface: `main`;
- post-v0.2 integration merge commit: `042fb12d070a51b37310792b882136a0ea6a58f8`;
- current development ledger: [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md);
- historical development provenance: PRs #11–#21.

The locked core theorem set T1–T5 and experiment set E1–E5 are unchanged by the post-v0.2 supplementary work.

## Validation

GitHub Actions currently checks:

- Python compilation;
- GitHub Markdown math delimiters;
- repository-relative Markdown links;
- required repository structure;
- E1–E5 reproduction;
- figure regeneration and output existence;
- experiment-manifest references;
- manuscript LaTeX build and PDF verification.

## License

This repository uses file-type split licensing:

- source code: **MIT** — [`LICENSE`](LICENSE);
- theory, documentation, manuscript text, and figures: **CC BY 4.0** — [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt);
- generated research datasets: **CC0 1.0** — [`LICENSES/CC0-1.0.txt`](LICENSES/CC0-1.0.txt).

See [`LICENSES/README.md`](LICENSES/README.md) for the licensing map. GitHub's repository-level license badge may show MIT because it detects the root `LICENSE`; that does not override the file-type licensing map.

## Citation

`CITATION.cff` currently describes the frozen v0.2 public-review snapshot. It should receive a new version only when the next formal repository/manuscript version is designated.
