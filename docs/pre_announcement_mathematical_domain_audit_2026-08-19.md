# Pre-announcement mathematical-domain audit — 2026-08-19

## Purpose

This pass audits whether the expressions in the core T1–T5 framework are actually finite and well-defined under the assumptions stated on the public theorem surfaces. It is separate from the proof-algebra audit: an identity can be algebraically correct while its stated domain is too weak to make one side of the identity exist.

The frozen `v0.3-public-review` tag/Release at commit `58038763127258bd3e2f0d41708c4dfa01f81fd6` is not modified. Corrections described here apply to current `main`.

## Finding 1 — T1 needs both base and weighted integrability

The frozen canonical TeX version of T1 required:

```math
E[|X|S]<\infty,
```

but did not separately require:

```math
E[|X|]<\infty.
```

That is insufficient because the identity also contains `E[X]` and `Cov(X,S)`.

The omission is real, not cosmetic. On the probability space `(0,1)` with Lebesgue measure, let:

```math
X(x)=\frac1x,
\qquad
S(x)=x^2.
```

Then:

```math
0<E[S]=\frac13<\infty,
```

and:

```math
E[|X|S]
=
\int_0^1 x\,dx
=
\frac12<\infty,
```

while:

```math
E[|X|]
=
\int_0^1\frac{dx}{x}
=
\infty.
```

Thus the weighted first-person expectation is finite while the base mean and covariance decomposition are not defined as finite quantities.

The public Markdown T1 had the opposite asymmetry: it called `X` integrable and assumed positive finite `E[S]`, but did not state weighted integrability locally. Base integrability of `X` and integrability of `S` do not imply integrability of their product. For example, on `(0,1)` let:

```math
X(x)=S(x)=x^{-1/2}.
```

Then:

```math
E[|X|]=E[S]=2<\infty,
```

but:

```math
E[|X|S]
=
\int_0^1\frac{dx}{x}
=
\infty.
```

Therefore the correct finite-domain contract for T1 is:

```math
E[|X|]<\infty,
\qquad
0<E[S]<\infty,
\qquad
E[|X|S]<\infty.
```

T2 remains automatically covered because its outcome is a bounded indicator and `E[S]<∞` supplies the weighted-integrability requirement.

## Finding 2 — T4 needs base integrability of each policy outcome

The formal model and frozen canonical setup required positive finite accessibility expectation and weighted outcome integrability for each recognition state, but T4 also uses:

```math
E[U_1-U_0],
```

and:

```math
Q(U_R,S_R)
=
\frac{\mathrm{Cov}(U_R,S_R)}{E[S_R]}.
```

Accordingly current `main` now states, for each recognition state:

```math
0<E[S_R]<\infty,
\qquad
E[|U_R|]<\infty,
\qquad
E[|U_R|S_R]<\infty.
```

This changes no decomposition identity; it makes every displayed finite expectation and covariance term well-defined.

## Finding 3 — general T5 needs cross-integrability

The selector-changing T5 proof adds and subtracts the intermediate term:

```math
Q(U_1,S_0).
```

The state-specific T4 assumptions do not imply that this cross-weighted quantity is finite.

Again the gap is explicit. On `(0,1)` let:

```math
U_1(x)=x^{-1/2},
\qquad
S_1(x)=1,
```

and:

```math
U_0(x)=0,
\qquad
S_0(x)=x^{-1/2}.
```

Then both recognition states satisfy positive finite accessibility mean, finite base outcome mean, and finite own-state weighted outcome mean. However:

```math
E[|U_1|S_0]
=
\int_0^1\frac{dx}{x}
=
\infty.
```

So `Q(U_1,S_0)` and the targeting decomposition are not finite under the state-specific assumptions alone.

Current `main` therefore adds:

```math
E[|U_1|S_0]<\infty
```

for the general selector-changing T5 identity. Under the fixed-selector case `S_1=S_0`, this condition is already supplied by the state-1 weighted-integrability assumption.

## Finding 4 — discrete present-self-location formula needs a positive-probability atom

The general event identity:

```math
P_{FP}(Z\in A)
=
\frac{E[\mathbf 1_{\{Z\in A\}}S_T]}{E[S_T]}
```

is well-defined under the normalized accessibility measure assumptions.

The pointwise discrete rewrite:

```math
P_{FP}(Z=z)
=
\frac{E[S_T\mid Z=z]P(Z=z)}{E[S_T]}
```

should be stated for atoms satisfying:

```math
P(Z=z)>0.
```

At a null atom the pointwise conditional expectation is not canonically determined. No special value is needed there: absolute continuity of the weighted measure already gives `P_FP(Z=z)=0` whenever `P(Z=z)=0`.

## Surfaces synchronized

The domain correction is being synchronized across:

- `theory/core_theorems.tex`;
- `theory/core_theorems.md`;
- `theory/theorem_1_3.md`;
- `theory/theorem_4_5.md`;
- `paper/sections/formal_model.tex`;
- `docs/notation.md`;
- `docs/claims_and_assumptions.md`;
- `docs/research_map.md`;
- the root `README.md`;
- current review/audit documentation.

The compiled manuscript appendix already contained a blanket assumption that displayed expectations are finite whenever required; the formal-model section now makes the concrete core conditions explicit before the theorem/proof material is used.

## Core-lock behavior after the correction

The canonical theorem lock continues to compare current `theory/core_theorems.tex` against frozen v0.3 blob:

`82986d7197e79446d6574aab538d1edaeff47eb6`.

It normalizes exactly four approved textual differences back to the frozen form:

1. the version-neutral document title;
2. explicit base integrability in the policy setup;
3. explicit base integrability in the generic T1 assumption;
4. explicit T5 cross-integrability for `Q(U_1,S_0)`.

After those four exact replacements, the entire Git blob must equal the frozen v0.3 canonical blob. Thus every theorem identity, proof step, sign result, proposition, boundary, and Everett bridge paragraph remains frozen unless a further scientific review deliberately changes the lock contract.

The lock implementation itself was also corrected during this pass: an earlier stale-frozen-substring check would have rejected the approved T5 line because the old `Let D=...` text appears as a substring of the strengthened sentence. The redundant substring test was removed; exact approved-phrase occurrence plus whole-normalized-blob identity is the actual invariant.

## Supplementary-domain checks

The same failure mode was checked in the main supplementary probability results.

- S1 assumes finite second moments before applying total covariance, which is sufficient.
- S2 assumes `U` integrable, positive finite `E[S]`, and `E[|U|S]<∞`, which supplies both sides needed by its covariance/uplift statement.
- S2.11–S2.13 use square-integrability assumptions, which are stronger than the core first-moment requirements and make the covariance/residual products finite.

No analogous domain correction was identified in those supplementary statements during this pass.

## Scientific boundary

This correction does **not** change:

- the T1 covariance identity;
- the T2 tail identity;
- the T3 FOSD conclusion or proof;
- the T4 recognition decomposition;
- the T5 interaction decomposition or fixed-selector sign result;
- the S1/S2-family results;
- any E1–E5 numerical result;
- the base probability law;
- the Everett accessibility bridge status.

It strengthens only the stated domains needed to make the existing finite expectation/covariance formulas mathematically well-defined.

## Remaining execution gate

The corrected sources and validators still require the final `main` GitHub Actions workflow to complete successfully. Source-level reasoning and local logic-level negative tests are not substituted for the unavailable direct-push Actions check-run state in the audit connector.
