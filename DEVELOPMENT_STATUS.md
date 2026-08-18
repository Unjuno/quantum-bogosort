# QBS Current Research Status

**Updated:** 2026-08-19

This file records the current review and development state. It complements the frozen snapshot ledger in [`STATUS.md`](STATUS.md) and the future-work ledger in [`ROADMAP.md`](ROADMAP.md).

## Source of truth

- current frozen public-review snapshot: `release/v0.3-public-review`;
- current review/development surface: `main`;
- current snapshot ledger: [`STATUS.md`](STATUS.md);
- canonical claim/theorem/evidence index: [`docs/research_map.md`](docs/research_map.md);
- authoritative claim boundaries: [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md);
- future work: [`ROADMAP.md`](ROADMAP.md);
- archived v0.2 snapshot: `release/v0.2-public-review` at commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

PRs #11–#20 preserve the staged derivation history. PR #21 preserves the cumulative integration history. PRs #27–#29 preserve the pre-announcement rendering, visualization, reproducibility, and final landing-page QA history. Current authoritative statements are the files in the v0.3 snapshot and on `main`.

## Branch state

The repository currently keeps only three branches:

- `main` — current review/development surface;
- `release/v0.3-public-review` — frozen v0.3 scientific snapshot;
- `release/v0.2-public-review` — archived v0.2 scientific snapshot.

The two `release/*` branches are intentional immutable review snapshots, not unmerged development work. Merged/superseded `agent/*` branches have been removed. There are no active development branches outside `main`.

## Post-snapshot `main` clarifications

The frozen `release/v0.3-public-review` snapshot is unchanged. Subsequent `main` changes are editorial, interpretive, visualization, repository-hygiene, or CI-hardening changes rather than new theorem or experiment content.

Current `main` now makes the following points explicit:

- recognition may include recognition of a QBS-type rule itself, while recognition has no privileged causal power beyond the policy and trajectory/accessibility changes it induces;
- future accessibility can reweight present self-location under the same first-person change of measure;
- this present-self-location statement is conditioning/change of measure, not backward causation or objective-probability modification;
- a favorable present self-location shift additionally requires alignment between expected future accessibility and the relevant favorability/utility statistic;
- the root README states the self-referential motivating question, includes a Mermaid dependency diagram, and exposes direct previews for every locked experiment family E1–E5;
- `experiments/README.md` exposes the E1–E5 H/T/D/C/U map and visual result previews;
- a dedicated E2 predictive-alignment figure closes the previous visualization gap;
- committed SVGs are deterministic generator outputs, checked byte-for-byte in CI and given explicit backgrounds for dark-mode readability;
- Markdown validation rejects malformed double-dollar display blocks whose delimiters are not on lines by themselves;
- manuscript LaTeX installation is routed through explicit Ubuntu archive/security sources to reduce runner-mirror failures;
- current public headings and research-map language avoid stale development-version labels;
- merged/superseded development branches have been removed while frozen release branches remain preserved;
- CI uses concurrency cancellation and runtime limits to prevent indefinitely stalled validation jobs.

No T1–T5 theorem, E1–E5 experiment, S2-family result, or Everett-bridge status is changed by these post-snapshot clarifications.

## Pre-announcement QA status

The automated/source-level pre-announcement QA is complete through merged PR #29:

- strict GitHub Markdown display-math structure is enforced;
- Mermaid source is present on the landing page and experiment index;
- every locked experiment family E1–E5 has a direct SVG review route;
- visual results link back to their experiment cards and provenance;
- committed SVGs are deterministically reproducible;
- manuscript PDF validation passed on the merged visual-QA line.

The repository is **not yet marked ready for broad announcement** because one presentation gate remains intentionally human-facing: directly inspect the rendered GitHub UI on desktop/mobile and confirm display math, Mermaid rendering, SVG sizing/readability, and overall landing-page flow. This is a presentation check, not a new-theory requirement.

## Locked core

The core theorem set remains T1–T5.

The core experiment set remains E1–E5.

Neither set is renumbered or replaced by the supplementary work integrated in v0.3.

## Current supplementary result

The supplementary line is complete through S2.13 and is presented as one conceptual spine:

$$
\text{predictive alignment}
\longrightarrow
\text{general accessibility}
\longrightarrow
\text{residual penalty}
\longrightarrow
\text{explained-variance certificate}.
$$

The principal review targets are S2, S2.11, S2.12, and S2.13. S2.3–S2.10 remain technical robustness and statistical-certification layers.

For theorem statements, assumptions, proof sources, and evidence classes, use [`docs/research_map.md`](docs/research_map.md) rather than this status file.

## Proof-review status

[`docs/post_v02_core_s2_proof_review.md`](docs/post_v02_core_s2_proof_review.md) records the dedicated second-pass review of S2, S2.11, S2.12, and S2.13.

Result: **PASS WITH THREE CORRECTIONS APPLIED**.

The corrections concern explicit square-integrability assumptions, bounded positive-accessibility counterexample/sharpness constructions, and the valid domain of the symmetric S2.13 threshold. The central covariance identities and inequalities are unchanged.

## Computational status

E1–E5 remain locked and reproducible under GitHub Actions. CI validates Markdown math structure, repository-relative Markdown links, repository structure, E1–E5 reproduction, deterministic committed SVG regeneration, manifest references, manuscript build, and PDF output.

No sixth core experiment is planned by default.

## Manuscript state

The main text is compressed to the conceptual S2 line, with detailed S2.3–S2.10 machinery Appendix-first. The manuscript compression audit, proof review, and targeted prior-art audit are integrated.

## Physical interpretation status

The abstract weighted-measure mathematics and statistical certificates do not establish an Everettian accessibility law.

The Everett accessibility bridge remains a separate physical open problem. See [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md).

The repository does not claim that an external random-number generator becomes objectively biased. Favorable QBS effects are first-person measure shifts under the model, not causal changes in the base measure.

## Current review gates

Work should now prioritize:

1. direct human GitHub-UI visual inspection before broad announcement;
2. external/public proof review of S2, S2.11, S2.12, and S2.13;
3. prior-art and novelty review of the combined recognition-dependent architecture;
4. manuscript claim consistency and compression;
5. statistical-certificate assumption review, including leakage and selection boundaries;
6. independent scrutiny of the Everett accessibility bridge.

Do not add another S2-numbered theorem by default. Add new mathematical machinery only in response to a concrete modeling gap or review-identified need.