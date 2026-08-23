# QBS Current Research Status

**Updated:** 2026-08-23

This file is the concise source of truth for the current review/development state. Frozen snapshot identity is recorded in [`STATUS.md`](STATUS.md); detailed audit history remains in the pre-announcement audit files; future work is tracked in [`ROADMAP.md`](ROADMAP.md).

## Public source of truth

- canonical current development/review surface: `main`;
- frozen v0.3 public-review snapshot: tag/Release `v0.3-public-review` at commit `58038763127258bd3e2f0d41708c4dfa01f81fd6`;
- archived v0.2 snapshot: tag/Release `v0.2-public-review` at commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`;
- canonical claim/theorem/evidence map: [`docs/research_map.md`](docs/research_map.md);
- authoritative claim boundaries: [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md);
- current supplementary index: [`supplementary/README.md`](supplementary/README.md).

The temporary `fix/recursive-qbs-validation` and `research/recursive-qbs` branches contain no commits ahead of `main` and no file differences relative to `main`; they are cleanup-only refs, not separate scientific sources of truth. Branch deletion is a hosting-governance task rather than a scientific blocker.

The frozen tags are commit-pinned historical snapshots. They are not described as platform-immutable unless a GitHub tag ruleset is actually configured and verified.

## Scientific state

The locked core theorem family remains **T1–T5** and the locked core experiment family remains **E1–E5**. The numbered supplementary line remains complete through **S2.13**.

Recognition is an information/policy-selection state. It has no privileged physical causal power merely by being recognized. Recognition can matter by changing policy, and policy can change both downstream trajectory outcomes and the modeled accessibility map. The base probability law itself is not changed by QBS weighting.

The first-person measure is a normalized change of measure. Future accessibility can reweight present self-location, but favorable/upward reweighting requires alignment with the relevant favorability/utility statistic. The Everett accessibility bridge remains a separate unresolved physical assumption.

### Current-main domain corrections

Current `main` preserves T1–T5 identity, numbering, proof algebra, sign/FOSD conclusions, support/extinction boundaries, and Everett-bridge statement while making the audited finite-integrability domains explicit. The frozen v0.3 snapshot itself is unchanged.

The detailed domain audit is [`docs/pre_announcement_mathematical_domain_audit_2026-08-19.md`](docs/pre_announcement_mathematical_domain_audit_2026-08-19.md). Existing theorem/supplementary validators retain the reviewed cross-surface contracts.

### Selection-equivalence / context-identifiability boundary

The current development line makes the strongest classical selection null explicit in [`supplementary/selection_equivalence.md`](supplementary/selection_equivalence.md).

For bounded nonnegative accessibility `S`, the normalized first-person law is exactly the conditional law obtained by recording a base trajectory with probability proportional to `S`. For general integrable nonnegative `S`, the same law is exactly representable as a classical record-size-biased distribution whose conditional expected record multiplicity is proportional to `S`; bounded truncations converge to the general law in total variation.

This yields a direct single-context identifiability boundary: if a proposed Everett accessibility model and a classical ascertainment/recording model induce the same relevant joint law of observables and accessibility, observer-conditioned data from that weighted law cannot distinguish them. The probability-law equivalence does not prove that the underlying physical mechanisms are identical or classical.

The boundary is now extended across policies/interventions. For each context `c`, any observer-conditioned law `Q_c` satisfying `Q_c << mu_c` can be reproduced exactly by a classical record-size-biased model using conditional expected record multiplicity

```math
r_c
=
\frac{dQ_c}{d\mu_c}.
```

Therefore observing several contexts does not identify the mechanism if the classical null may retune its selection channel independently in every context.

A restricted context-invariant selector creates a structural test: if one `a(omega)` is shared across contexts, then

```math
\frac{dQ_c}{d\mu_c}
=
\frac{a}{Z_c},
```

so pairwise density-ratio ratios must be constant on the common support. With one common base law this strengthens to equality of the normalized density ratios.

The audit also identified an important operational qualification. This structural restriction is not automatically an empirical test: the base and selected laws must be identifiable on a common observable state space. Latent violations can disappear under projection, while policy-dependent outcome/observation maps can create observed distribution changes even with shared latent selection.

The dedicated proof/stress audit is [`docs/context_identifiability_audit_2026-08-23.md`](docs/context_identifiability_audit_2026-08-23.md). A 20,000-case finite-state property test reproduced the context-specific representation to floating-point error, verified the shared-selection ratio condition, and found no false shared-null fits among tested nonproportional cases. Explicit projection counterexamples are recorded in the audit.

The practical consequence is that a physical QBS/Everett bridge must do more than reproduce one or many normalized weighted observer laws. It must independently derive or constrain `S_pi` across contexts, expose identifiable base/selected quantities, and generate held-out/interventional/sequential predictions that differ from comparably constrained classical selection nulls.

The prior-art ledgers connect the single-context boundary to Fisher (1934), Rao (1965), and Patil--Rao (1978) ascertainment / weighted-distribution theory. The context-identifiability audit additionally connects the methodological burden to Heckman-style sample selection and modern missing-not-at-random identification work. The latter references are currently recorded in the research ledger/audit; promoting them into the manuscript bibliography fact lock is a separate bibliography-governance change rather than a prerequisite for the mathematical result.

### Recursive observer-information extension

Current `main` also contains an **unnumbered supplementary dynamic extension** in [`supplementary/evidence_activation.md`](supplementary/evidence_activation.md). It does not add `T6`, `S2.14`, or `E6`.

The extension closes the feedback arrow:

```math
\text{experienced observer history}
\longrightarrow
\text{belief / recognition update}
\longrightarrow
\text{adoption and policy}
\longrightarrow
\text{trajectory and accessibility}
\longrightarrow
\text{next experienced observer history}.
```

Its exact mathematical components are:

- sequential application of the existing T1 change-of-measure identity;
- a filtration-relative predictable/innovation decomposition of cumulative outcome;
- exact separation of first-person uplift into predictable selection and innovation selection;
- standard likelihood-ratio / KL-divergence identities for model-based bridge-belief updating under stated absolute-continuity and correct-specification conditions.

`Innovation selection` is a formal diagnostic for reweighting of decision-time-unpredictable variation relative to a chosen information filtration. It is not a claim that objective chance or an external RNG has been causally improved.

The exploratory [`supplementary/recursive_qbs_simulation.py`](supplementary/recursive_qbs_simulation.py) is outside the locked E1–E5 suite. Its aligned, anti-aligned, and policy-only controls check that ordinary/predictable effects and innovation selection can be separated, including a counterexample where predictable selection is positive while innovation selection and total first-person uplift are negative. Current validation also requires this file in the repository inventory and executes the aligned, anti-aligned, decomposition, and policy-only-null mechanism checks independently of the script's own assertions.

## Reproducibility state

The primary execution environment remains pinned to:

- Ubuntu 24.04;
- Python 3.11.15;
- NumPy 2.4.6;
- pandas 3.0.5;
- Matplotlib 3.11.1.

The 16 locked historical E1–E5 CSVs remain Git-blob locked. Current reproduction CSVs retain exact schema, row order, and non-numeric cells and are numerically compared to committed `HEAD` with `rtol=1e-12`, `atol=1e-14`; this avoids treating host-dependent last-bit floating-point decimal serialization as scientific drift. E1–E5 continue to execute independent scientific regression assertions before that comparison. After a successful current-output check, committed canonical CSV bytes are restored before the final clean-worktree gate. Committed SVGs retain byte-for-byte regeneration checks. The deterministic Figure 2 theorem-illustration CSV uses the same exact-structure plus tight numeric-equivalence contract and is restored to committed canonical bytes before the exact worktree check.

The recursive toy simulation remains deliberately supplementary and is not part of the manifest-locked E1–E5 reproduction set.

Detailed execution and validator audits remain in:

- [`docs/pre_announcement_execution_audit_2026-08-19.md`](docs/pre_announcement_execution_audit_2026-08-19.md);
- [`docs/pre_announcement_validator_audit_2026-08-19.md`](docs/pre_announcement_validator_audit_2026-08-19.md);
- [`docs/pre_announcement_bibliography_audit_2026-08-19.md`](docs/pre_announcement_bibliography_audit_2026-08-19.md);
- [`docs/pre_announcement_mathematical_domain_audit_2026-08-19.md`](docs/pre_announcement_mathematical_domain_audit_2026-08-19.md);
- [`docs/context_identifiability_audit_2026-08-23.md`](docs/context_identifiability_audit_2026-08-23.md).

## Bibliography and novelty position

The bibliography fact lock and prior-art ledgers remain the reviewed source for publication chronology and claim boundaries. The selection-equivalence pass adds classical ascertainment/weighted-distribution prior art and narrows the novelty hypothesis further.

No novelty claim is made for normalized weighting, size-biased/ascertainment distributions, generic sample-selection/MNAR identifiability, standard sequential weighting, martingale/predictable decompositions, Bayesian likelihood-ratio updating, or KL identities by themselves.

The provisional novelty question remains about the combined recognition-dependent policy/trajectory/accessibility architecture and its decompositions, plus whether an independently motivated physical accessibility model supplies cross-context restrictions that survive classical selection alternatives.

## Everett bridge

The physical bridge remains open. A concrete accessibility rule must independently justify why observer persistence/self-location should induce the proposed first-person measure and must satisfy the structural constraints in [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md).

The selection-equivalence result strengthens this requirement: matching the weighted first-person law is insufficient because a classical behavior-matched selection mechanism can reproduce the same law. The context-indexed extension further rules out context-by-context refitting as mechanism evidence.

The next bridge gate is therefore a **predeclared, low-dimensional cross-policy law for `S_pi` plus an operationally identifiable held-out test**. A restriction stated only on inaccessible latent branch variables is not yet an empirical bridge test.

The repository does not claim quantum immortality, guaranteed survival, backward causation, objective RNG bias, or that a favorable observed history proves the bridge.

## Announcement readiness

### Completed source cleanup

- [x] recursive extension indexed in the canonical research map;
- [x] recursive claims/non-claims classified in the authoritative claim ledger;
- [x] recursive simulation brought under repository/executable CI coverage;
- [x] selection-equivalence / ascertainment boundary proved and indexed;
- [x] arbitrary context-specific observer-law representability proved and indexed;
- [x] shared-selection density-ratio restriction proved with same-base strengthening;
- [x] operational/projection limits of the cross-context restriction audited;
- [x] dedicated context-identifiability proof/stress audit added to the repository inventory;
- [x] classical ascertainment and selection-identifiability prior art added to the research ledgers;
- [x] weighted-law and context-indexed observational non-identifiability classified as bridge limitations;
- [x] landing-page scientific wording remains bounded by the unresolved physical bridge;
- [x] frozen v0.3 versus current-main boundary made explicit;
- [x] locked T1–T5 / E1–E5 identities left unchanged;
- [x] CI false positives found by PR execution corrected without changing theorem or locked-data content;
- [x] redundant development branches verified to contain no work ahead of `main`.

### Remaining external/UI/governance gates

- [ ] directly observe a push-triggered `main` Actions run if tooling exposes it; the final green PR synthetic merge and actual merged `main` have the identical Git tree and the workflow has no event-dependent execution branches;
- [ ] directly inspect rendered GitHub pages in a browser at desktop/mobile pixel level; server-side GitHub GFM rendering and static SVG validation already pass, but the current environment blocks direct GitHub browser navigation;
- [ ] delete redundant `fix/recursive-qbs-validation` and `research/recursive-qbs` branch refs when branch-ref deletion is available;
- [ ] normalize repository-header metadata from stale `recognition-activated` wording to `recognition-dependent` wording and add useful repository topics when repository-settings write access is available;
- [ ] optionally configure a `main` branch ruleset/protection policy and tag ruleset after CI is stable.

The remaining items are hosting-layer presentation/governance checks, not known missing core mathematical results.

## Current announcement position

The repository is suitable for **public technical review** on scientific-content grounds. Broad promotion should retain the explicit statement that the Everett accessibility bridge is unresolved and should not present normalized weighting, repeated context-specific weighted laws, or favorable recursive histories as evidence for a physical observer-selection mechanism.

External criticism is specifically welcome on:

- proofs and counterexamples;
- direct prior art / structural overlap;
- whether the context-specific classical null is formulated broadly enough;
- whether any independently justified cross-context restriction survives projection to observable records;
- what held-out observation or intervention could identify a physical accessibility mechanism beyond comparably constrained classical selection nulls;
- the recursive observer-information model and its misspecification boundaries;
- whether innovation selection is a useful filtration-relative diagnostic;
- the Everett/multiverse accessibility bridge;
- reproducibility and repository presentation.
