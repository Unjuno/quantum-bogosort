# Quantum Bogosort (QBS)

**Status:** v0.2 — Public Review

Formal theory and reproducible simulations of recognition-activated Quantum Bogosort, including policy-dependent trajectories, observer-indexed accessibility, and cross-branch decision correlations.

## Repository map

For the current state of the research, start with:

- [`STATUS.md`](STATUS.md) — canonical ledger of proved, simulated, assumed, open, and non-claimed results.
- [`ROADMAP.md`](ROADMAP.md) — public-review and manuscript milestones.
- [`docs/research_map.md`](docs/research_map.md) — claim-to-proof-to-experiment map.
- [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md) — theorem / simulation / bridge-assumption separation.
- [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md) — support, constraint, and rejection criteria for a physical Everett bridge.
- [`docs/manuscript_claim_audit.md`](docs/manuscript_claim_audit.md) — manuscript claim and figure-caption audit.
- [`docs/v0.2_release_audit.md`](docs/v0.2_release_audit.md) — final v0.2 public-review release audit.
- [`docs/notation.md`](docs/notation.md) — shared notation.
- [`theory/`](theory/) — core theorem statements and proofs.
- [`experiments/`](experiments/) — E1–E5 cards and reproducible code.
- [`supplementary/`](supplementary/) — secondary exact results and exploratory mechanisms.
- [`literature/`](literature/) — prior-art and novelty-boundary review.
- [`paper/`](paper/) — illustrated manuscript source.
- [`figures/README.md`](figures/README.md) — publication figures and provenance.
- [`CHANGELOG.md`](CHANGELOG.md) — public research-package changes.

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

The notes also cover option value, support preservation under pure reweighting, the zero-accessible-measure boundary, counterexamples, and the separate Everett bridge assumption. The manuscript appendix contains complete proofs and supplementary derivations. A supplementary hierarchical policy-coherence theorem is in [`supplementary/branch_recognition.md`](supplementary/branch_recognition.md).

## Experiments

The locked experiment map is [`experiments/manifest.csv`](experiments/manifest.csv). Human-readable H/T/D/C/U cards are also provided:

- [`E1_FOSD.md`](experiments/E1_FOSD.md) — covariance, tails, FOSD, independence null, and nonmonotone counterexample.
- [`E2_LEARNED_AGENT.md`](experiments/E2_LEARNED_AGENT.md) — minimal learned agent and endogenous predictive correlation.
- [`E3_RECOGNITION.md`](experiments/E3_RECOGNITION.md) — paired recognition decomposition and recognition-label null.
- [`E4_INTERACTION.md`](experiments/E4_INTERACTION.md) — fixed-selector interaction identity plus the general selector-map-shift decomposition.
- [`E5_BRANCH_MAP.md`](experiments/E5_BRANCH_MAP.md) — paired execution-strength and environment-correlation sweeps, plus shared versus branch-independent recognition.

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

Historical locked summaries and current reproduction outputs are stored in [`data/processed/`](data/processed/). Secondary and superseded work is documented under [`experiments/archive/`](experiments/archive/), with superseded designs explicitly excluded from current evidence.

## Supplementary research notes

Secondary results are indexed in [`supplementary/README.md`](supplementary/README.md), including:

- multi-observer normalization,
- binary soft-QBS,
- repeated-filter identities and accessible-measure decay,
- Gaussian closed form,
- adaptive-agent predictive structure,
- evidence-driven recognition activation,
- recognition time as a stopping-time extension,
- selectivity frontier,
- branch-wide recognition and policy coherence.

The recognition-time note explicitly does **not** claim that earlier recognition is universally better.

## Manuscript, figures, and literature

The evolving illustrated manuscript is in [`paper/`](paper/). It contains Abstract, Introduction, Related Work, Formal Model, Main Theorems, Adaptive-Agent Mechanism, Experiments, Everett Interpretation, Limitations/Falsifiability, Discussion, a full proof appendix, and bibliography.

Six GitHub-readable SVG figures are committed under `figures/generated/`. LaTeX-ready PDF variants are regenerated from committed data during CI before the manuscript build. Captions explicitly distinguish mathematical schematics, theorem illustrations, and classical toy simulations.

The literature review is in [`literature/`](literature/). It includes supportive and critical Everett probability work, anthropic decision theory, classical change-of-measure context, and direct self-locating policy-optimization prior art. The novelty claim is therefore intentionally narrower than "self-location affects decisions" or "weighted expectations change outcomes."

## Markdown math convention

Markdown math in this repository uses **double-dollar display blocks only**. Inline mathematical symbols are written as code spans or moved into display blocks. CI rejects legacy parenthesis/bracket math delimiters and single-dollar math delimiters.

## Validation

GitHub Actions validates the research package by:

- compiling experiment, figure, and validation scripts;
- enforcing the Markdown math-delimiter convention;
- validating the required research-repository structure;
- rerunning E1–E5;
- regenerating SVG and PDF publication figures;
- validating experiment-manifest references;
- generating the illustrated manuscript PDF with `latexmk`;
- verifying and uploading the manuscript PDF as a CI artifact.

## Everett interpretation

The mathematical results do **not** establish an Everett interpretation by themselves. The separate bridge assumption is:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

The repository keeps measure-theoretic results, classical simulations, observer-model assumptions, and the Everett physical interpretation distinct. A concrete physical bridge must satisfy the structural and empirical criteria documented in [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md).

## Falsifiability and boundaries

The framework predicts no pure weighting uplift when accessibility is independent of outcome. FOSD need not hold for nonmonotone accessibility. Recognition has no effect if it changes neither trajectory utility nor accessibility. If expected accessibility is zero, the normalized first-person measure is undefined.

Falsifiability is layer-specific: theorem assumptions can fail mathematically; an observer model can fail structural consistency; a physical Everett bridge is empirically falsifiable only when a concrete physical accessibility rule makes observational predictions that differ from competing accounts.

## Public review

Corrections, counterexamples, prior-art pointers, implementation bugs, and challenges to the Everett bridge assumption are welcome through GitHub Issues. The intended sequence is v0.2 public review, revision, manuscript stabilization, and then later arXiv preparation.

## License

This repository uses file-type split licensing:

- Source code: **MIT** — [`LICENSE`](LICENSE)
- Theory, documentation, manuscript text, and figures: **CC BY 4.0** — [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt)
- Generated research datasets: **CC0 1.0** — [`LICENSES/CC0-1.0.txt`](LICENSES/CC0-1.0.txt)

See [`LICENSES/README.md`](LICENSES/README.md) for the licensing map. `CITATION.cff` intentionally does not encode the split licensing as one interchangeable license list.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). It should be updated again when a manuscript identifier becomes available.
