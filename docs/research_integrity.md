# Research Integrity and Separation Rules

This document defines how the repository separates mathematical content, empirical evidence, physical interpretation, and operational constraints.

Its purpose is to prevent silent distortion of the research record.

## 1. Mathematical claims change only for mathematical reasons

A theorem, proof, counterexample, or boundary condition should be changed only because of a mathematical issue such as:

- an invalid implication;
- a missing assumption;
- an integrability or domain problem;
- an incorrect inequality direction;
- a defective counterexample;
- a stronger or weaker statement proved under explicit assumptions.

When this happens, the correction should be recorded in an audit, PR description, or changelog entry.

A non-mathematical concern must not be rewritten as if it were a mathematical correction.

## 2. Abstract theory and real-world implementation are separate layers

The repository may study abstract termination, absorption, accessibility, observer-selection, and stopping-time mathematics.

Operational constraints on real-world implementation do not alter the abstract probability model. If a concrete implementation is intentionally excluded from operational guidance, that exclusion must not be presented as a theorem about the abstract model.

## 3. Interpretation does not back-propagate into proofs

The measure-theoretic and statistical results are interpretation-neutral unless a theorem explicitly states otherwise.

The Everett bridge is a separate physical assumption:

$$
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
$$

Failure to justify this bridge does not invalidate the abstract weighted-measure identities. Conversely, validity of the abstract identities does not establish the Everett bridge.

## 4. Evidence classes must remain distinct

Every major claim should be classifiable as one of:

- exact theorem or identity;
- corollary or sufficient condition;
- classical simulation result;
- statistical certificate under stated assumptions;
- model assumption;
- physical bridge assumption;
- hypothesis or open problem;
- explicit non-claim.

A result must not be promoted from one class to another without an explicit argument and repository update.

## 5. No silent sanitization of the research record

If wording is changed for reasons other than mathematical correctness, reproducibility, citation accuracy, or scientific clarity, that reason should be visible in the repository history rather than disguised as a theorem correction.

Historical development PRs may contain superseded formulations. The current review candidate must identify those PRs as historical and point to the corrected current statement.

## 6. Proof corrections require an error trail

When a proof review finds a defect, record:

- the original statement or construction;
- the specific defect;
- whether the central theorem changes;
- the corrected statement;
- the files updated;
- an `ERROR CHECK` conclusion.

The current post-v0.2 example is `docs/post_v02_core_s2_proof_review.md`, which records corrections to integrability assumptions, bounded sharpness constructions, and a threshold domain without changing the central covariance identities.

## 7. Novelty claims must be narrower than the mathematics alone

Standard probability identities such as normalized weighting, covariance decompositions, the law of total covariance, and standard concentration inequalities are not treated as standalone QBS novelty.

Novelty claims must be grounded in the combined research architecture and remain provisional under prior-art review.

## 8. Repository source-of-truth hierarchy

Use:

- `release/v0.2-public-review` for the frozen v0.2 scientific snapshot;
- `STATUS.md` for that snapshot's status ledger;
- `DEVELOPMENT_STATUS.md` for current post-v0.2 work;
- PR #21 for the active cumulative post-v0.2 review diff;
- historical PRs only for development provenance.

## ERROR CHECK

1. This document does not add or remove any theorem.
2. It does not alter the Everett bridge assumption.
3. It does not convert operational constraints into scientific claims.
4. It requires non-mathematical editing reasons to remain distinguishable from proof corrections.
5. It preserves historical development while making the current corrected statement authoritative for review.
