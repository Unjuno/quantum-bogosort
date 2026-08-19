# Quantum Bogosort (QBS)

[![validate](https://github.com/Unjuno/quantum-bogosort/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/Unjuno/quantum-bogosort/actions/workflows/validate.yml)

Quantum Bogosort is a formal research program for recognition-dependent policies whose trajectories and observer-indexed accessibility can change together.

The motivating question is self-referential: if an agent recognizes a QBS-type rule and that information changes the policy it uses, while the resulting policy also changes which future continuations are observer-accessible, how does accessibility conditioning change the agent's first-person distribution over trajectories and present self-location? The model keeps the base probability law fixed; interpreting the accessibility weighting as an Everettian physical self-location rule is a separate bridge assumption.

The name **Quantum Bogosort** labels this observer-selection intuition. The formal object studied here is the recognition-dependent weighted-measure model below, not a claim that quantum mechanics literally sorts branches by utility.

The core structure is:

```math
R
\longrightarrow
\pi_R
\longrightarrow
(U_R,S_R).
```

Here `R` is recognition, `pi_R` is the policy used under that recognition state, `U_R` is the resulting outcome or utility, and `S_R` is a nonnegative observer-indexed accessibility weight.

In the self-referential case motivating QBS, `R=1` may represent recognition of a QBS-type rule itself. Recognition has no privileged causal power in the formal model: it matters only through any policy change it induces and the resulting changes in `U_R` and/or `S_R`. If recognition changes neither quantity, the recognition-label null gives no QBS effect.

## Visual model

```mermaid
flowchart LR
    R[Recognition / information state] --> P[Policy selection]
    P --> U[Trajectory outcome / utility]
    P --> S[Observer-indexed accessibility]
    U --> FP[First-person weighted distribution]
    S --> FP
    FP --> SL[Self-location / first-person value]
```

The Mermaid diagram is an interpretation-neutral map of the formal dependencies. It is not a literal diagram of quantum branching.

The same dependency structure is also committed as a static SVG fallback for renderers that do not display Mermaid:

[![Recognition-dependent QBS framework](figures/generated/fig1_framework.svg)](figures/README.md)

## Core first-person quantity

For:

```math
0<E_\mu[S_\pi]<\infty,
```

define:

```math
V_{FP}(\pi)
=
\frac{E_\mu[U_\pi S_\pi]}{E_\mu[S_\pi]}.
```

For the baseline:

```math
S_0\equiv1,
```

the recognition effect decomposes as:

```math
V_1-V_0
=
E[U_1-U_0]
+
\frac{\mathrm{Cov}(U_1,S_1)}{E[S_1]}.
```

The first term is the ordinary policy/trajectory effect. The second is the first-person conditioning contribution.

A positive conditioning contribution means that the first-person measure gives greater weight to favorable accessible trajectories. It does **not** mean that the base measure or an external random-number generator is causally changed.

## Present self-location under future accessibility

The same weighted measure can be restricted to a present state while accessibility is determined over a future continuation. Let `Z` denote a present state or present trajectory descriptor and let `S_T` denote future-continuation accessibility. Then:

```math
P_{FP}(Z\in A)
=
\frac{E[\mathbf 1_{\{Z\in A\}}S_T]}{E[S_T]}.
```

For a discrete present state:

```math
P_{FP}(Z=z)
=
\frac{E[S_T\mid Z=z]P(Z=z)}{E[S_T]}.
```

Thus, when expected future accessibility differs across present states, the first-person measure can reweight present self-location toward states with greater expected future accessibility. This is a conditioning/change-of-measure statement, not backward causation and not a causal change in the base probability law.

A favorable or upward shift requires additional alignment between the relevant outcome/favorability statistic and future accessibility; differential accessibility alone gives reweighting, not a guaranteed favorable direction.

## What is established

### Core mathematics

The locked core theorem set is T1–T5:

1. covariance identity for the first-person mean shift;
2. tail-probability covariance identity;
3. a monotone-accessibility sufficient condition for FOSD;
4. recognition decomposition;
5. policy–QBS interaction decomposition.

See [`theory/core_theorems.md`](theory/core_theorems.md) and the canonical [`docs/research_map.md`](docs/research_map.md).

### Supplementary predictive-alignment line

The current supplementary argument is organized around one conceptual spine:

```math
\text{predictive signal}
\longrightarrow
\text{conditional-mean alignment}
\longrightarrow
\text{outcome/accessibility covariance}
\longrightarrow
\text{first-person shift}.
```

Its principal results are S2, S2.11, S2.12, and S2.13. S2.3–S2.10 provide calibration, finite-sample, selection-validity, light-tail, and robust statistical-certification machinery. See [`supplementary/README.md`](supplementary/README.md).

### Reproducible simulations

The locked core experiment suite is E1–E5:

- [`experiments/E1_FOSD.md`](experiments/E1_FOSD.md) — covariance, tails, FOSD, independence null, and a nonmonotone counterexample;
- [`experiments/E2_LEARNED_AGENT.md`](experiments/E2_LEARNED_AGENT.md) — endogenous predictive alignment in a minimal learned agent;
- [`experiments/E3_RECOGNITION.md`](experiments/E3_RECOGNITION.md) — paired recognition decomposition;
- [`experiments/E4_INTERACTION.md`](experiments/E4_INTERACTION.md) — policy–QBS interaction decomposition;
- [`experiments/E5_BRANCH_MAP.md`](experiments/E5_BRANCH_MAP.md) — marginal first-person uplift versus cross-copy policy coherence.

These are classical simulations of the formal model.

## Visual results

The committed SVGs below are regenerated from three explicitly separated source classes: deterministic theorem illustrations, current reproduction outputs, and locked historical summaries. Every locked experiment family E1–E5 has a direct visual route from the repository landing page; [`figures/README.md`](figures/README.md) records the figure-level provenance.

| E1 — FOSD theorem boundary | E2 — learned predictive alignment |
|---|---|
| [![Base and first-person CDF comparison](figures/generated/fig2_fosd.svg)](experiments/E1_FOSD.md) | [![Interaction-capable, misspecified, and random evaluators across noise levels](figures/generated/fig7_predictive_alignment.svg)](experiments/E2_LEARNED_AGENT.md) |
| Deterministic theorem illustration: monotone accessibility versus a nonmonotone control. | Locked E2 summary: predictive correlation under increasing environmental noise; current rerun output is stored separately. |

| E3 — recognition decomposition | E4 — interaction sign |
|---|---|
| [![Policy, QBS, and total recognition effects](figures/generated/fig3_recognition_decomposition.svg)](experiments/E3_RECOGNITION.md) | [![Policy-QBS interaction sign](figures/generated/fig4_interaction_sign.svg)](experiments/E4_INTERACTION.md) |
| Current reproduction: ordinary policy, QBS conditioning, and total effects. | Current reproduction: rescue-bad, neutral, and amplify-good interaction regimes. |

| E4 — adaptation quality | E5 — branch coherence |
|---|---|
| [![Adaptation quality sweep](figures/generated/fig5_adaptation_quality.svg)](experiments/E4_INTERACTION.md) | [![Cross-copy action correlation and first-person gain](figures/generated/fig6_branch_coherence.svg)](experiments/E5_BRANCH_MAP.md) |
| Locked E4 adaptation summary; the current E4 script reproduces the fixed-selector and general interaction identities, not this historical sweep. | Current reproduction: cross-copy action-correlation increment versus single-observer first-person gain. |

See [`experiments/README.md`](experiments/README.md) for the H/T/D/C/U experiment map and [`figures/README.md`](figures/README.md) for figure provenance.

## Interpretation boundary

The mathematical weighting results do not by themselves derive an Everettian physical interpretation. The separate bridge assumption is:

```math
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
```

A concrete physical account must explain why an Everettian observer should be described by the proposed accessibility map. Structural and empirical review criteria are in [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md).

The repository does not claim that statistical covariance certification establishes Everettian observer selection, that positive correlation alone implies FOSD, or that external random generators become objectively lucky. The complete claim boundary is maintained in [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md).

## Where to read next

| Goal | Start here |
|---|---|
| Understand the complete claim structure | [`docs/research_map.md`](docs/research_map.md) |
| Check theorem statements and assumptions | [`theory/core_theorems.md`](theory/core_theorems.md) and [`supplementary/README.md`](supplementary/README.md) |
| Check claim strength and non-claims | [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md) |
| Check notation and terminology | [`docs/notation.md`](docs/notation.md) |
| Inspect experiments visually | [`experiments/README.md`](experiments/README.md) and [`figures/README.md`](figures/README.md) |
| Reproduce the simulations | [`experiments/manifest.csv`](experiments/manifest.csv) and [`experiments/`](experiments/) |
| Review the Everett bridge | [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md) |
| Read the manuscript | [`paper/`](paper/) |
| Review prior art and novelty boundaries | [`literature/`](literature/) |
| See current review/development state | [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md) |
| See the frozen snapshot ledger | [`STATUS.md`](STATUS.md) |

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
python scripts/validate_reproduction_outputs.py
```

The primary numerical/plotting package versions in `requirements.txt` are pinned because committed-output verification is byte-level; using a different NumPy/Pandas/Matplotlib stack can change serialization even when the numerical model is unchanged. The reproduction validator derives the current output set from `experiments/manifest.csv`, compares those outputs byte-for-byte with `HEAD`, and rejects side effects on other files under `data/processed/`.

Historical locked summaries and current reproduction outputs are stored in [`data/processed/`](data/processed/). Superseded experiment designs are kept under [`experiments/archive/`](experiments/archive/).

## Public review

Use [`CONTRIBUTING.md`](CONTRIBUTING.md) and the issue templates for proof/counterexample reports, prior-art overlap, reproducibility failures, and Everett-bridge criticism.

The focused v0.3 S2 technical-review thread is [Issue #14](https://github.com/Unjuno/quantum-bogosort/issues/14).

The current review priority is external proof, novelty, manuscript, statistical-assumption, and Everett-bridge scrutiny rather than automatic theorem expansion.

## Repository state

The repository has a single active branch: `main`. Frozen scientific snapshots are preserved as named, commit-pinned tags/GitHub Releases rather than as active branches, so they remain distinct from pending development work. Their commit targets are recorded explicitly below and rechecked during pre-announcement audit; platform-level tag immutability is not assumed without an active tag ruleset.

- current review/development surface: `main`;
- current frozen snapshot: tag/Release `v0.3-public-review` at commit `58038763127258bd3e2f0d41708c4dfa01f81fd6`;
- previous frozen snapshot: tag/Release `v0.2-public-review` at commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`;
- current snapshot ledger: [`STATUS.md`](STATUS.md);
- current development/review ledger: [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md);
- historical derivation provenance: PRs #11–#21;
- post-snapshot rendering/visualization/reproducibility QA provenance: PRs #27–#29.

The locked core theorem set T1–T5 and experiment set E1–E5 are unchanged in v0.3. The principal v0.3 addition is the integrated S2 predictive-alignment/general-accessibility/certification line plus its proof, manuscript, prior-art, and repository-structure audits.

## Validation

The current `main` validation state is visible in the badge at the top of this README. GitHub Actions checks:

- Python/runtime consistency under the pinned Python and primary numerical-package contract;
- required repository structure, including core theory, archival provenance, licensing/configuration, and validator sources;
- GitHub issue-template chooser front matter;
- repository-wide fenced Markdown math syntax and structural TeX balance;
- repository-relative Markdown links, including rejection of relative targets that escape the repository root;
- GFM structure conversion of every Markdown file through GitHub's Markdown API, with heading/table/image preservation checks;
- E1–E5 scientific regression invariants;
- manifest ID/order/LOCK/provenance validation and byte-for-byte verification of all manifest-declared current reproduction CSVs;
- post-experiment cleanliness of the complete `data/processed/` tree, including rejection of undeclared ignored files;
- deterministic SVG regeneration, static/self-contained SVG browser-safety validation, and byte-for-byte committed-output verification;
- manuscript figure generation, compiled-input-graph LaTeX dependency/citation/reference preflight, LaTeX build, and PDF verification.

The workflow runs on push and pull request and can also be repeated manually from **Actions → validate → Run workflow**. Reusable GitHub Actions are pinned to full commit SHAs rather than mutable major-version tags, checkout credentials are not persisted into later shell steps, and the workflow token is limited to `contents: read`.

The GitHub API GFM check is a structural parser check; direct browser inspection remains the release gate for MathJax, Mermaid, SVG sizing, and page layout.

## License

This repository uses file-type split licensing:

- source code: **MIT** — [`LICENSE`](LICENSE);
- theory, documentation, manuscript text, and figures: **CC BY 4.0** — [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt);
- generated research datasets: **CC0 1.0** — [`LICENSES/CC0-1.0.txt`](LICENSES/CC0-1.0.txt).

See [`LICENSES/README.md`](LICENSES/README.md) for the licensing map. GitHub's repository-level license badge may show MIT because it detects the root `LICENSE`; that does not override the file-type licensing map.

## Citation

Citation metadata is in [`CITATION.cff`](CITATION.cff) and tracks the frozen v0.3 public-review snapshot.
