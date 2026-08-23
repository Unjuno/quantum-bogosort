# QBS Research Roadmap

This file tracks **open work and decision gates**. Completed scientific details belong in [`docs/research_map.md`](docs/research_map.md), current review state in [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md), frozen snapshots in [`STATUS.md`](STATUS.md), and historical changes in [`CHANGELOG.md`](CHANGELOG.md) and the audit records under [`docs/`](docs/).

## Current phase

The project is in **v0.3 public review / preprint preparation** with later unnumbered recursive, selection/context-identifiability, randomized-diagnostic, and temporal/longitudinal extensions on current `main`.

The locked core remains T1–T5 and E1–E5. The numbered supplementary line remains complete through S2.13. Do not add T6, S2.14, or E6 by default.

## Highest-priority scientific gates

### External review

- [ ] Obtain external/public proof review of S2, S2.11, S2.12, and S2.13.
- [ ] Collect concrete counterexamples, assumption objections, and boundary corrections.
- [ ] Obtain focused prior-art review of the combined recognition-dependent architecture and its decompositions.
- [ ] Review whether the manuscript presentation still gives too much or too little prominence to S2.13 and the S2.5–S2.10 certification machinery.

### Everett/accessibility bridge

The abstract weighting mathematics is not the open problem. The open problem is whether a physical observer model supplies a constrained accessibility law with empirically distinguishable consequences.

- [ ] Specify a low-dimensional cross-policy/context law for `S_pi` motivated independently of the observer-conditioned outcomes it is meant to explain.
- [ ] State which base, observer, accessibility, and proxy quantities are operationally measurable or identifiable.
- [ ] Require representation/coarse-graining/sequential consistency of the proposed bridge.
- [ ] Compare the bridge against classical ascertainment/record-size-bias models with comparable freedom.
- [ ] Design held-out context/intervention tests that do not allow either model to retune one unconstrained selector per context.
- [ ] Determine whether any physically motivated bridge predicts an observable pattern after projection to realistic records rather than only on inaccessible latent branch states.

### Selection/context-identifiability

Completed foundations:

- [x] exact bounded ascertainment representation;
- [x] exact general record-size-biased representation;
- [x] total-variation truncation boundary;
- [x] context-by-context classical representability no-go;
- [x] shared-selection density-ratio restriction and common-base strengthening;
- [x] operational/projection caveat;
- [x] deterministic finite-state stress audit;
- [x] randomized-context finite-sample diagnostic;
- [x] randomization-regime / proxy stress diagnostic;
- [x] composition-shift countercontrol showing that regime homogeneity can fail without selector retuning.

Next questions:

- [ ] Identify proxy families that expose physically relevant latent heterogeneity without assuming full latent-state recovery.
- [ ] Derive power/identifiability results beyond the current finite-state diagnostics for realistic longitudinal or repeated-measures settings.
- [ ] Separate selector change from pre-treatment composition drift using independently measured or experimentally controlled variables.
- [ ] Decide whether additional sample-selection/MNAR references belong in the locked manuscript bibliography or remain repository prior-art support.

### Recognition / longitudinal sequence models

The current temporal boundary is past-adapted:

```math
(H_t,I_t)
\longrightarrow
I_{t+1}
\longrightarrow
\mathcal L(Y_{t+1:T}\mid H_t,I_{t+1})
\longrightarrow
Y_{t+1:T}.
```

The future realization is not assumed to be fixed at the transition time. The empirical question is whether constrained recognition/history-dependent latent-transition models imply later sequence distributions that differ from suitable ordinary behavioral/selection/null models.

- [ ] Specify a minimal latent transition/accessibility family with finite effective flexibility.
- [ ] Define observable longitudinal quantities that are sensitive to that family while remaining robust to ordinary policy adaptation, expectancy, information acquisition, and risk-taking.
- [ ] Model attrition, missingness, incapacitation, and selective reporting explicitly rather than treating observed survivorship as accessibility evidence.
- [ ] Compare natural-recognition follow-up with optional randomized-exposure designs; keep causal exposure effects distinct from observer-ontology claims.
- [ ] Determine which repeated/pooled sequence statistics can distinguish competing transition models even when a single hidden transition is locally unobservable.
- [ ] Stress-test whether the same data can be matched by flexible hidden-state classical models; reject any formulation that becomes trajectory-by-trajectory post hoc relabeling.

### Recursive observer-information model

- [ ] Stress-test the recursive extension under bridge/null misspecification.
- [ ] Compare against survivorship-only and alternative observer models.
- [ ] Review whether `innovation selection` is stable enough across motivated filtrations to be a useful diagnostic rather than merely a decomposition label.
- [ ] Keep the recursive simulation supplementary unless external review identifies a reason to promote it.

## Repository and reproducibility gates

Completed:

- [x] main is the canonical current source of truth; frozen v0.2/v0.3 snapshots are named commit-pinned tags/Releases.
- [x] repository-wide Markdown math, links, GFM rendering, SVG safety, bibliography provenance, runtime contract, issue-template structure, E1–E5 scientific invariants, reproduction outputs, and manuscript build are covered by CI.
- [x] current floating-point reproduction outputs use exact structure plus tight numerical equivalence and canonical-byte restoration.
- [x] recursive, selection/context-identifiability, randomized-diagnostic, and temporal/longitudinal supplementary surfaces are indexed and/or inventory-validated without changing the locked T1–T5/E1–E5 core.
- [x] all nine non-`main` development refs were verified to contain no unique work, then fast-forwarded without force to current `main` and rechecked as identical on 2026-08-24.
- [x] final PR #37 run #1093 passed repository-validation 27/27 and manuscript-build; its green synthetic merge tree matched actual merged `main`.

Open repository tasks:

- [ ] Delete the nine cleanup-only development refs when branch-ref deletion is available.
- [ ] Change repository-header description from stale `recognition-activated` wording to `recognition-dependent` wording when repository-settings write access is available.
- [ ] Add useful repository topics when settings write access is available.
- [ ] Consider enabling `delete_branch_on_merge`.
- [ ] Configure an appropriate `main` branch ruleset/protection policy after review workflow stabilizes.
- [ ] Consider a tag ruleset if platform-level immutability is desired for frozen release tags.
- [ ] Directly inspect representative GitHub pages in desktop/mobile layouts when browser access is available; server-side GFM and SVG checks do not substitute for pixel-level UI review.
- [ ] Directly observe a push-triggered `main` validation run if connector tooling later exposes it; until then use green PR synthetic-tree equality with actual `main` as the fallback audit.

## Publication gates

- [ ] Resolve review-driven mathematical/citation corrections.
- [ ] Decide whether the additional selection-identifiability references enter the manuscript bibliography fact lock.
- [ ] Decide whether the recursive observer-information extension remains repository-only or enters a later manuscript version.
- [ ] Decide whether the randomized diagnostics and temporal/longitudinal boundary belong in the first preprint or remain repository supplementary material.
- [ ] Freeze the manuscript candidate only after substantive review stabilizes.
- [ ] Finalize author/citation metadata for the preprint version.
- [ ] Prepare `v1.0-preprint` only after those gates are satisfied.
- [ ] Add DOI/arXiv metadata only when identifiers actually exist.

## Public-review / announcement gate

The repository is already suitable for public technical review. Broad promotion should continue to state that the physical Everett bridge is unresolved.

Before directing substantially broader traffic:

- [ ] complete the browser/UI pass when possible;
- [ ] either complete or explicitly defer repository-header metadata, branch deletion, and ruleset governance;
- [ ] ensure the current settled review PR is fully green and its merged tree matches the validated tree;
- [ ] keep the README and canonical claim map explicit that normalized weighting and randomized diagnostic success are not Everett confirmation.

External criticism is especially valuable on:

- proof/counterexample validity;
- direct prior art and novelty overlap;
- whether the classical nulls are broad enough;
- projection and measurement limits;
- longitudinal hidden-state identifiability;
- recursive-model misspecification;
- the physical Everett/accessibility bridge.

## Deferred mathematical work

Do not automatically expand theorem numbering or the locked experiment suite. Defer unless a concrete review objection or operational need appears:

- finite-sample confidence bounds for S2.13 explained-variance quantities;
- more explicit Orlicz/mgf conditions for S2.9;
- stronger robust estimators for S2.10;
- infinite or certification-data-dependent candidate classes;
- a stronger universal recognition-time ordering theorem;
- additional selection representations that do not improve identification;
- a numbered recursive theorem family;
- a sixth locked experiment merely to document supplementary diagnostics.

## Stop rule

A new theorem, experiment family, or bridge mechanism should be added only if it does at least one of the following:

1. removes a material modeling assumption;
2. answers a concrete review objection;
3. introduces an operationally measurable quantity;
4. separates QBS from a comparably flexible classical null;
5. materially improves reproducibility or public auditability.

Otherwise prioritize external review, counterexamples, model compression, repository clarity, and publication readiness.
