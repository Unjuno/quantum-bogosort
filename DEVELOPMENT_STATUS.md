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

A temporary `research/recursive-qbs` branch still exists, but it has been verified against `main` at commit `27cb425d49a760f06c057f5eeace37d0cc7d1b7c` with `ahead=0`, `behind=0`, no file differences, and no associated pull request. It contains no unmerged work and is not a separate scientific source of truth. Deleting that redundant ref is therefore branch housekeeping only.

The frozen tags are commit-pinned historical snapshots. They are not described as platform-immutable unless a GitHub tag ruleset is actually configured and verified.

## Scientific state

The locked core theorem family remains **T1–T5** and the locked core experiment family remains **E1–E5**. The numbered supplementary line remains complete through **S2.13**.

Recognition is an information/policy-selection state. It has no privileged physical causal power merely by being recognized. Recognition can matter by changing policy, and policy can change both downstream trajectory outcomes and the modeled accessibility map. The base probability law itself is not changed by QBS weighting.

The first-person measure is a normalized change of measure. Future accessibility can reweight present self-location, but favorable/upward reweighting requires alignment with the relevant favorability/utility statistic. The Everett accessibility bridge remains a separate unresolved physical assumption.

### Current-main domain corrections

Current `main` preserves T1–T5 identity, numbering, proof algebra, sign/FOSD conclusions, support/extinction boundaries, and Everett-bridge statement while making the audited finite-integrability domains explicit. The frozen v0.3 snapshot itself is unchanged.

The detailed domain audit is [`docs/pre_announcement_mathematical_domain_audit_2026-08-19.md`](docs/pre_announcement_mathematical_domain_audit_2026-08-19.md). Existing theorem/supplementary validators retain the reviewed cross-surface contracts.

### Recursive observer-information extension

Current `main` now also contains an **unnumbered supplementary dynamic extension** in [`supplementary/evidence_activation.md`](supplementary/evidence_activation.md). It does not add `T6`, `S2.14`, or `E6`.

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

The exploratory [`supplementary/recursive_qbs_simulation.py`](supplementary/recursive_qbs_simulation.py) is outside the locked E1–E5 suite. Its aligned, anti-aligned, and policy-only controls check that ordinary/predictable effects and innovation selection can be separated, including a counterexample where predictable selection is positive while innovation selection and total first-person uplift are negative. The current validation branch also requires this file in the repository inventory and executes the aligned, anti-aligned, decomposition, and policy-only-null mechanism checks independently of the script's own assertions.

The recursive extension is now indexed in [`docs/research_map.md`](docs/research_map.md) and classified in [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md).

## Reproducibility state

The primary execution environment remains pinned to:

- Ubuntu 24.04;
- Python 3.11.15;
- NumPy 2.4.6;
- pandas 3.0.5;
- Matplotlib 3.11.1.

The 16 locked historical E1–E5 CSVs remain Git-blob locked. Current reproduction CSVs retain exact schema, row order, and non-numeric cells and are numerically compared to committed `HEAD` with `rtol=1e-12`, `atol=1e-14`; this avoids treating host-dependent last-bit floating-point decimal serialization as scientific drift. E1–E5 continue to execute independent scientific regression assertions before that comparison. After a successful current-output check, committed canonical CSV bytes are restored before the final clean-worktree gate. Deterministic committed SVGs and the Figure 2 theorem-illustration CSV retain their byte-for-byte regeneration checks.

The recursive toy simulation remains deliberately supplementary and is not part of the manifest-locked E1–E5 reproduction set.

Detailed execution and validator audits remain in:

- [`docs/pre_announcement_execution_audit_2026-08-19.md`](docs/pre_announcement_execution_audit_2026-08-19.md);
- [`docs/pre_announcement_validator_audit_2026-08-19.md`](docs/pre_announcement_validator_audit_2026-08-19.md);
- [`docs/pre_announcement_bibliography_audit_2026-08-19.md`](docs/pre_announcement_bibliography_audit_2026-08-19.md);
- [`docs/pre_announcement_mathematical_domain_audit_2026-08-19.md`](docs/pre_announcement_mathematical_domain_audit_2026-08-19.md).

## Bibliography and prior art

The bibliography fact lock and prior-art ledgers remain the reviewed source for publication chronology and claim boundaries. The recursive extension has not yet received a separate targeted prior-art review, so no novelty claim is made for standard sequential weighting, martingale/predictable decompositions, Bayesian likelihood-ratio updating, or KL identities by themselves.

The provisional novelty question remains about the combined recognition-dependent architecture and decompositions, not any standard mathematical component in isolation.

## Everett bridge

The physical bridge remains open. A concrete accessibility rule must independently justify why observer persistence/self-location should induce the proposed first-person measure and must satisfy the structural constraints in [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md).

The repository does not claim quantum immortality, guaranteed survival, backward causation, objective RNG bias, or that a favorable observed history proves the bridge.

## Announcement readiness

### Completed source cleanup

- [x] recursive extension indexed in the canonical research map;
- [x] recursive claims/non-claims classified in the authoritative claim ledger;
- [x] landing-page wording synchronized with the current recursive extension;
- [x] frozen v0.3 versus current-main boundary made explicit;
- [x] current development status refreshed;
- [x] locked T1–T5 / E1–E5 identities left unchanged;
- [x] recursive simulation brought under repository/executable CI coverage;
- [x] CI false positives found by PR execution corrected without changing theorem or locked-data content;
- [x] redundant `research/recursive-qbs` branch verified identical to `main`, with no unmerged commits, file differences, or associated pull request.

### Remaining external/UI gates

- [ ] confirm the final settled `main` `validate` workflow is green for the exact announcement commit;
- [ ] directly inspect the rendered GitHub README and representative math/SVG pages in the browser, especially MathJax, Mermaid, SVG sizing, tables, and mobile layout;
- [ ] delete the verified-redundant `research/recursive-qbs` branch ref when branch-ref deletion is available;
- [ ] normalize repository-header metadata from stale `recognition-activated` wording to `recognition-dependent` wording and add useful repository topics when repository-settings write access is available;
- [ ] optionally configure a `main` branch ruleset/protection policy and tag ruleset after CI is stable.

The remaining items are presentation, governance, or final-CI confirmation gates. They are not known missing core mathematical results. The redundant branch has no unique content and is not a scientific or reproducibility blocker.

## Current announcement position

The repository is suitable for **public technical review** once the final `main` workflow and rendered-page checks above pass. Announcement copy should describe the current repository rather than imply that the frozen `v0.3-public-review` tag already contains the later recursive extension.

External criticism is specifically welcome on:

- proofs and counterexamples;
- direct prior art / structural overlap;
- the recursive observer-information model and its misspecification boundaries;
- whether innovation selection is a useful filtration-relative diagnostic;
- the Everett/multiverse accessibility bridge;
- reproducibility and repository presentation.
