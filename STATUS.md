# QBS Research Status — v0.3 Public Review

**Snapshot date:** 2026-08-18

This file records the current frozen public-review scientific snapshot.

The v0.3 snapshot is preserved at:

- branch: `release/v0.3-public-review`
- current review/development surface: `main`

The previous v0.2 snapshot remains archived at:

- branch: `release/v0.2-public-review`
- commit: `7405f7408f74fa32b16d1cc9f624070cc14624ab`

For current review priorities and future work, see [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md) and [`ROADMAP.md`](ROADMAP.md).

## Core mathematical results

| ID | Result | Status | Primary source |
|---|---|---|---|
| T1 | QBS covariance identity | PROVED | `theory/core_theorems.md` |
| T2 | Tail probability identity | PROVED | `theory/core_theorems.md` |
| T3 | Monotone conditional accessibility implies FOSD | PROVED | `theory/core_theorems.md` |
| T4 | Recognition decomposition | PROVED | `theory/core_theorems.md` |
| T5 | Policy–QBS interaction decomposition | PROVED | `theory/core_theorems.md` |
| S1 | Shared-latent branch-policy coherence under conditional independence | PROVED (SUPPLEMENTARY) | `supplementary/branch_recognition.md` |

The locked core theorem set remains T1–T5.

## v0.3 supplementary predictive-alignment line

The integrated supplementary line is complete through S2.13 and should be read as one conceptual chain:

$$
\text{predictive signal}
\longrightarrow
\text{conditional-mean alignment}
\longrightarrow
\text{outcome/accessibility covariance}
\longrightarrow
\text{first-person shift}.
$$

Principal results:

| ID | Role | Status |
|---|---|---|
| S2 | score-measurable predictive alignment | PROVED |
| S2.2 | posterior-mean self-calibration | PROVED |
| S2.11 | general-accessibility total-covariance decomposition | PROVED |
| S2.12 | residual-variance lower certificate | PROVED SUFFICIENT BOUND |
| S2.13 | explained-variance / conditional-mean-correlation certificate | PROVED SUFFICIENT BOUND |

S2.3–S2.10 provide calibration, prediction-MSE, finite-sample, selection-validity, generic-envelope, light-tail, and robust median-of-means certification layers under their stated assumptions.

The dedicated proof review in `docs/post_v02_core_s2_proof_review.md` records three corrections already applied: explicit square-integrability assumptions for S2.11, bounded positive-accessibility counterexample/sharpness constructions, and the valid domain of the S2.13 symmetric threshold. The central identities and inequalities are unchanged.

## Core computational results

| ID | Experiment | Status |
|---|---|---|
| E1 | covariance, FOSD, nulls, and counterexample | REPRODUCIBLE |
| E2 | minimal learned agent / endogenous predictive alignment | REPRODUCIBLE |
| E3 | paired recognition decomposition | REPRODUCIBLE |
| E4 | fixed/changing-selector interaction decomposition | REPRODUCIBLE |
| E5 | branch-map sweeps and shared-recognition comparison | REPRODUCIBLE |

The locked core experiment set remains E1–E5. No sixth core experiment is introduced in v0.3.

## Manuscript and reproducibility state

| Item | Status |
|---|---|
| Main-text S2 presentation | COMPRESSED TO CONCEPTUAL SPINE |
| S2.3–S2.10 statistical machinery | APPENDIX-FIRST |
| Dedicated S2 proof review | PASS WITH CORRECTIONS APPLIED |
| Targeted post-v0.2 prior-art review | INTEGRATED |
| E1–E5 reproduction | VALIDATED BY CI |
| SVG/PDF figure generation | VALIDATED BY CI |
| Repository-relative Markdown links | VALIDATED BY CI |
| LaTeX/PDF manuscript build | VALIDATED BY CI |

## Interpretation-level status

The abstract weighted-measure mathematics is distinct from the Everett physical bridge.

A separate physical interpretation assumes:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

This bridge remains physically open. The repository does not claim that an external random-number generator becomes objectively biased, that statistical certification establishes Everettian observer selection, or that the weighting identities establish quantum immortality.

## Current review questions

1. External proof review of S2, S2.11, S2.12, and S2.13.
2. Prior-art review of the combined recognition-dependent architecture and decompositions.
3. Manuscript placement of S2.13 and the amount of S2.5–S2.10 material retained in the paper appendix.
4. Statistical-assumption review, especially training/certification leakage and selection boundaries.
5. Independent scrutiny, derivation, replacement, or rejection of the Everett accessibility bridge.

## Release state

Scientific snapshot: **v0.3 — Public Review**.

The previous v0.2 snapshot remains preserved for archival comparison. Historical PRs #11–#21 preserve the derivation path of the post-v0.2 work; current authoritative statements are the files in the v0.3 snapshot and on `main`.