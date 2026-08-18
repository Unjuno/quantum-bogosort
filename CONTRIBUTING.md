# Contributing and Public Review

QBS is currently in public technical review. The highest-value contributions are corrections, counterexamples, reproducibility failures, prior-art overlap, and precise criticism of the Everett bridge.

## Before opening an issue

Identify which layer the concern applies to:

1. exact mathematics or proof;
2. statistical certificate or assumption;
3. classical simulation or reproducibility;
4. prior art or novelty positioning;
5. observer/accessibility model;
6. Everett physical bridge;
7. documentation or repository structure.

Do not collapse these layers. For example, failure of the Everett bridge is not by itself a counterexample to the abstract covariance identity.

## Active and stable review targets

- Stable v0.2 snapshot: `release/v0.2-public-review`
- Stable status ledger: `STATUS.md`
- Current development status: `DEVELOPMENT_STATUS.md`
- Active cumulative post-v0.2 candidate: PR #21
- Historical development stack: PRs #11–#20

Review current post-v0.2 mathematics against PR #21, not an isolated historical stacked PR.

## Proof or counterexample reports

Please include:

- exact theorem/corollary identifier;
- file and section;
- assumptions being used;
- the exact implication or equality you dispute;
- a derivation, counterexample, or smallest failing case when possible;
- whether the issue affects the central result or only a boundary condition.

## Reproducibility reports

Please include:

- operating system and Python version;
- command run;
- relevant traceback or output;
- experiment ID;
- whether the failure reproduces on a clean environment.

Core experiments E1–E5 are expected to run under GitHub Actions.

## Prior-art reports

Please provide a primary source where possible and explain the structural overlap. The useful question is not merely whether another work mentions Everett, anthropics, observer selection, or decision theory, but whether it duplicates a specific QBS construction or decomposition.

## Everett bridge criticism

Please distinguish:

- mathematical inconsistency of a proposed accessibility map;
- observer-model inadequacy;
- conflict with an Everettian probability account;
- lack of physical derivation;
- empirical rejection of a concrete physical prediction.

The repository does not treat the abstract weighted measure as a derivation of Everettian physics.
