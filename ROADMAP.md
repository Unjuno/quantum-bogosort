# QBS Research Roadmap

This roadmap turns the public repository into the source of truth for the theory, experiments, and manuscript.

## Phase 1 — Research map and claim discipline

- [x] Publish core theorem set.
- [x] Publish E1–E5 reproduction code and outputs.
- [x] Add CI for math delimiters, Python compilation, experiments, and manifest validation.
- [ ] Maintain `STATUS.md` as the canonical claim ledger.
- [ ] Add notation and assumptions documents.
- [ ] Add a research map linking every claim to proof, code, and data.

## Phase 2 — Supplementary decomposition

Split the current monolithic supplementary notes into topic files:

- multi-observer normalization,
- binary soft-QBS,
- repeated filtering,
- Gaussian closed form,
- adaptive-agent mechanism,
- evidence-driven recognition,
- selectivity frontier,
- branch-wide recognition.

Each note should contain motivation, definitions, result, derivation or experiment, interpretation, limitations, status, and linked files.

## Phase 3 — Experiment cards

Create one human-readable card for each core experiment E1–E5 using the same structure:

- H — Hypothesis,
- T — Test design,
- D — Data/result,
- C — Controls/counterexamples,
- U — Uncertainty/interpretation boundary,
- ERROR CHECK.

## Phase 4 — Literature and novelty

Build `literature/prior_art.md` and `paper/references.bib` covering:

- Everett / Many-Worlds probability and self-location,
- quantum suicide / immortality,
- anthropic and observer-selection decision theory,
- value of information,
- change of measure / importance weighting,
- related agent-selection models.

For each source record what it establishes, what it does not establish, and how QBS differs.

## Phase 5 — Figures

Produce publication-quality figures from locked/reproducible outputs:

1. causal framework diagram,
2. FOSD illustration,
3. recognition decomposition,
4. interaction-sign experiment,
5. adaptation accuracy / total-effect relation,
6. branch-correlation versus marginal FP effect.

## Phase 6 — Manuscript

Create and maintain:

- abstract,
- introduction,
- formal model,
- main theorems,
- adaptive-agent mechanism,
- experiments,
- Everett interpretation,
- limitations and falsifiability,
- discussion,
- appendix,
- bibliography.

The manuscript must distinguish theorem, simulation, and physical interpretation at every stage.

## Phase 7 — Public review and release

- Keep GitHub Issues open for proof corrections, counterexamples, prior art, and implementation bugs.
- Integrate review feedback into `main` through PRs.
- Cut a `v0.2-public-review` release when the manuscript scaffold and literature ledger are complete.
- Prepare `v1.0-preprint` only after the manuscript and references are stable enough for arXiv submission.
