# QBS Development Status

**Updated:** 2026-08-18

This file records the active research state. It is intentionally separate from `STATUS.md`, which records the stable v0.2 public-review snapshot.

## Stable scientific snapshot

The frozen v0.2 public-review snapshot is preserved at:

- branch: `release/v0.2-public-review`
- commit: `7405f7408f74fa32b16d1cc9f624070cc14624ab`

The stable snapshot contains the locked core theorem set T1–T5, core experiments E1–E5, the v0.2 manuscript, figures, audits, and the physically open Everett bridge.

## Active post-v0.2 candidate

The single active post-v0.2 review candidate is:

- PR #21 — `Consolidate post-v0.2 theory stack into the preprint review candidate`

PR #21 is based directly on `main` and contains the cumulative post-v0.2 development.

The main new mathematical line is the supplementary predictive-alignment family S2 through S2.13. It includes:

- conditional-mean predictive alignment;
- posterior-mean self-calibration;
- calibration-error and prediction-MSE robustness;
- finite-sample and selection-safe statistical certificates;
- generic confidence-envelope composition;
- light-tail and robust finite-moment instantiations;
- exact general-accessibility decomposition with residual conditional covariance;
- residual-variance and explained-variance sufficient certificates.

The locked core theorem set T1–T5 is unchanged.

The locked core experiments E1–E5 are unchanged.

The Everett accessibility bridge remains physically open and is not inferred from the supplementary mathematics or statistical certificates.

## Historical stacked PRs

PRs #11–#20 are development history. Their cumulative content is superseded for active review by PR #21.

They are retained to preserve the derivation path, but reviewers should not treat an older PR body as the current statement when a later proof audit corrected wording or boundary conditions.

## Current review priorities

Review the active candidate in this order:

1. S2, S2.11, S2.12, and S2.13 proofs and boundary conditions;
2. manuscript claim consistency;
3. statistical certificate assumptions and selection leakage boundaries;
4. prior-art overlap;
5. separation of mathematical results from the Everett physical bridge.

## Stop rule

Do not add another supplementary theorem number by default.

A new theorem should be added only if it removes a material modeling assumption, closes a concrete review-identified gap, introduces a genuinely new operational quantity, or materially sharpens an existing result under motivated assumptions.

## Source-of-truth rule

Use:

- `STATUS.md` for the stable v0.2 snapshot;
- this file for current post-v0.2 development;
- PR #21 for the active cumulative diff;
- `docs/research_integrity.md` for the rule separating mathematical corrections, interpretation changes, and non-scientific operational constraints.
