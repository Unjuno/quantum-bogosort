# QBS Development Status

**Updated:** 2026-08-18

This file records the current post-v0.2 research state. It does not duplicate the stable v0.2 snapshot ledger or the detailed theorem map.

## Source of truth

- stable v0.2 scientific snapshot: branch `release/v0.2-public-review` at commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`;
- stable snapshot ledger: [`STATUS.md`](STATUS.md);
- current integrated post-v0.2 review surface: `main`;
- post-v0.2 integration merge commit: `042fb12d070a51b37310792b882136a0ea6a58f8`;
- canonical claim/theorem/evidence index: [`docs/research_map.md`](docs/research_map.md);
- authoritative claim boundaries: [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md);
- future work: [`ROADMAP.md`](ROADMAP.md).

PRs #11–#20 preserve the staged derivation history. PR #21 is the cumulative integration PR that brought the corrected post-v0.2 review candidate onto `main`.

## Locked core

The core theorem set remains T1–T5.

The core experiment set remains E1–E5.

Neither set is renumbered or replaced by post-v0.2 supplementary work.

## Current post-v0.2 result

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

The corrections concern:

1. explicit square-integrability assumptions for S2.11;
2. bounded Rademacher counterexample/sharpness constructions for S2.11–S2.12;
3. the domain and feasibility of the symmetric S2.13 threshold.

The central covariance identities and inequalities are unchanged.

## Computational status

E1–E5 remain locked and reproducible under GitHub Actions. CI also validates Markdown math delimiters, repository-relative Markdown links, repository structure, manifest references, figure generation, manuscript build, and PDF output.

No sixth core experiment is planned by default.

## Manuscript state

The post-v0.2 main text is compressed to:

1. S2 predictive alignment;
2. S2.2 posterior-mean calibration;
3. S2.11 general accessibility;
4. compact S2.12 residual penalty;
5. S2.13 explained-variance interpretation.

Detailed S2.3–S2.10 machinery is Appendix-first. The manuscript compression audit and targeted prior-art audit are integrated.

## Physical interpretation status

The abstract weighted-measure mathematics and statistical certificates do not establish an Everettian accessibility law.

The Everett accessibility bridge remains a separate physical open problem. See [`docs/everett_bridge_tests.md`](docs/everett_bridge_tests.md).

The repository does not claim that an external random-number generator becomes objectively biased. Favorable QBS effects are first-person measure shifts under the model, not causal changes in the base measure.

## Current review gates

Work should now prioritize:

1. external/public proof review of S2, S2.11, S2.12, and S2.13;
2. prior-art and novelty review of the combined recognition-dependent architecture;
3. manuscript claim consistency and compression;
4. statistical-certificate assumption review, including leakage and selection boundaries;
5. independent scrutiny of the Everett accessibility bridge.

Do not add another S2-numbered theorem by default. Add new mathematical machinery only in response to a concrete modeling gap or review-identified need.

## Historical provenance

PRs #11–#20 preserve the staged derivation path and earlier review surfaces. PR #21 preserves the cumulative integration history. Current authoritative post-v0.2 statements are the files on `main`.
