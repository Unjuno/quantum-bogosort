# S2 Stack Semantic Preservation Audit

**Status:** historical editorial / semantic audit  
**Scope:** pre-v0.3 post-v0.2 stacked-branch integration history

This document records the semantic-preservation audit performed while the S2 family was still developed through post-v0.2 stacked branches. Those branches were later consolidated and removed. The current review/development surface is `main`; frozen v0.2 and v0.3 scientific snapshots are preserved as tags/GitHub Releases. For current status, use `DEVELOPMENT_STATUS.md`, `STATUS.md`, and `docs/research_map.md`.

At the time of this audit, the baseline on `main` was the v0.2 snapshot:

`7405f7408f74fa32b16d1cc9f624070cc14624ab`

The checks below therefore describe preservation across that historical integration step. They are retained for provenance rather than as a statement that stacked development branches still exist.

## 1. Core theorem set remains unchanged

The core paper theorem set is still:

- T1 — covariance identity;
- T2 — tail identity;
- T3 — monotone-accessibility FOSD;
- T4 — recognition decomposition;
- T5 — policy–QBS interaction decomposition.

Source files remain:

- `theory/theorem_1_3.md`;
- `theory/theorem_4_5.md`;
- `theory/propositions_boundaries.md`.

**Audit:** PASS.

The S2 family is supplementary and must not silently renumber or replace T1–T5.

## 2. FOSD boundary remains preserved

The repository does not claim:

```math
\mathrm{Cov}(U,S)>0
\Longrightarrow
U_{FP}\succeq_{\mathrm{FOSD}}U.
```

The stronger monotonicity condition remains necessary for the stated T3 theorem. Nonmonotone selector counterexamples remain in E1 and the processed data.

**Audit:** PASS.

## 3. Recognition null remains preserved

The exact null remains:

```math
U_1=U_0,
\qquad
S_1=S_0
```

almost surely implies:

```math
V_1-V_0=0.
```

This prevents recognition labels from being treated as causally magical.

Primary sources remain T4, E3, and the recognition-null reproduction outputs.

**Audit:** PASS.

## 4. Support-preservation boundary remains preserved

For a fixed policy, pure accessibility reweighting is absolutely continuous with respect to the stated base measure. Therefore:

```math
\mu(A)=0
\Longrightarrow
\mu^{FP}(A)=0.
```

Pure reweighting does not create outcomes absent from the fixed-policy support.

Primary source: `theory/propositions_boundaries.md`.

**Audit:** PASS.

## 5. Extinction / zero-normalization boundary remains preserved

The normalized FP measure requires:

```math
0<E[S]<\infty.
```

When:

```math
E[S]=0,
```

the normalized FP measure is undefined rather than merely low-valued.

Primary source: `theory/propositions_boundaries.md`.

**Audit:** PASS.

## 6. Everett bridge remains separate

The abstract model may define:

```math
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E[S_\pi]}
\,d\mu(\omega),
```

but the repository does not derive this rule from unitary quantum mechanics, decoherence, Born-rule probability, or an independently established observer theory.

Primary sources remain:

- `docs/everett_bridge_tests.md`;
- manuscript Everett and Limitations sections;
- `docs/claims_and_assumptions.md`.

**Audit:** PASS.

## 7. External-randomness non-claim remains preserved

The repository does not claim that an external random-number generator becomes objectively biased toward favorable outcomes.

QBS results concern policy-dependent trajectories and observer-indexed conditional measures under stated assumptions.

**Audit:** PASS.

## 8. Mutual-information boundary is strengthened, not lost

The post-v0.2 S2 family explicitly records that:

```math
I(U;Y)>0
```

does not imply:

```math
\mathrm{Cov}(U,S)>0.
```

A signal may change conditional variance while leaving:

```math
E[U\mid Y]
```

constant.

Primary sources:

- `supplementary/adaptive_agent.md`;
- `docs/s2_adaptive_alignment_audit.md`.

**Audit:** PASS.

## 9. Statistical certificate failure remains inconclusive

For every sufficient finite-sample certificate in S2.5–S2.10, a nonpositive lower margin means only that the selected sufficient condition was not certified at the stated confidence level.

It does not imply:

```math
\mathrm{Cov}(U,S)\le0.
```

**Audit:** PASS.

## 10. Training and selection leakage boundaries remain preserved

The statistical stack does not permit arbitrary reuse of certification data.

S2.6 requires independent final certification data conditional on training. S2.7 permits same-holdout finite-candidate selection only under simultaneous multiplicity-corrected coverage.

Post-hoc candidate invention, uncorrected best-of-many search, or unaccounted tail/variance parameter tuning remains outside the stated guarantees.

**Audit:** PASS.

## 11. Robust-statistics assumptions remain explicit

S2.9 does not claim marginal sub-Gaussianity automatically supplies universal constants for:

```math
YS,
\qquad
S^2,
\qquad
(U-Y)^2.
```

S2.10 does not claim raw-variable finite variance is enough. It requires finite variance of the five S2.8 target variables themselves, including the associated fourth-moment-type conditions for squared targets.

**Audit:** PASS.

## 12. General-accessibility residual boundary remains explicit

After removing:

```math
S=s(Y),
```

S2.11 retains the residual term:

```math
E[\mathrm{Cov}(U,S\mid Y)].
```

It is not silently set to zero.

S2.12 and S2.13 provide sufficient worst-case lower certificates, but neither claims the actual residual dependence is maximally negative.

**Audit:** PASS.

## 13. S2.13 remains sufficient, not necessary

The explained-variance condition:

```math
\rho_{ma}\sqrt{A_UA_S}
>
\sqrt{(1-A_U)(1-A_S)}
```

is inherited from the worst-case S2.12 residual penalty.

Failure of this inequality does not imply nonpositive total covariance.

**Audit:** PASS.

## 14. Simulation / theorem / physics separation remains preserved

E1–E5 are classical simulations of formal mechanisms. They do not prove Everettian observer selection.

Theorem status, simulation status, statistical-validation status, and bridge-assumption status remain separate categories.

**Audit:** PASS.

## 15. Historical and superseded artifacts remain non-authoritative

The archive policy continues to distinguish:

- CORE;
- APPENDIX CANDIDATE;
- SUPERSEDED;
- HISTORICAL LOCAL ARTIFACT.

Earlier exploratory designs are not silently promoted into active evidence.

**Audit:** PASS.

## Historical promotion gate

At the time of the stacked-branch integration, promotion required verifying all of the following:

1. `docs/s2_stack_review_map.md` still matched the intended manuscript structure;
2. all theorem audits remained present;
3. `docs/everett_bridge_tests.md` remained unchanged or intentionally revised;
4. `theory/propositions_boundaries.md` remained present;
5. E1–E5 remained the locked core experiment set unless a deliberate versioned decision changed that policy;
6. all statistical failure-is-inconclusive language remained present;
7. the S2.11 residual term was not dropped in the general-accessibility presentation;
8. S2.12/S2.13 remained labeled sufficient worst-case certificates;
9. manuscript and Markdown CI remained green.

Those branch-integration steps are historical. Current publication/review gates are tracked in `ROADMAP.md`.

## ERROR CHECK

1. This is a semantic preservation audit, not an additional theorem.
2. The v0.2 `main` baseline statement is explicitly historical rather than a description of current `main`.
3. This audit identifies authoritative source files rather than duplicating every proof.
4. It explicitly preserves both mathematical and interpretation boundaries.
5. Current branch/archive state is delegated to `DEVELOPMENT_STATUS.md`; this file preserves the historical integration audit.
