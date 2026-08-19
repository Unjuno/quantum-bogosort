# Pre-announcement mathematical-domain audit — 2026-08-19

## Purpose

This pass audits whether the expressions in the core T1–T5 framework and the principal statistical certificate stack are actually finite, real-valued, and well-defined under the assumptions stated on the public theorem surfaces. It is separate from the proof-algebra audit: an identity can be algebraically correct while its stated domain is too weak to make one side of the identity exist, and a confidence statement can be correct on its validity event while the reported statistic is not defined on the full sample space.

The frozen `v0.3-public-review` tag/Release at commit `58038763127258bd3e2f0d41708c4dfa01f81fd6` is not modified. Corrections described here apply to current `main`.

## Finding 1 — T1 needs a complete generic accessibility/outcome domain

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

A later literal-source audit found one further issue in the compact canonical TeX: the policy setup quantified `S_\pi`, while T1 introduced a generic symbol `S` without locally binding the selector assumptions. Although the intended interpretation was clear from context, a standalone theorem statement should not rely on a differently indexed setup variable to supply its domain.

The current T1 contract is therefore explicitly:

```math
S\ge0,
\qquad
0<E[S]<\infty,
\qquad
E[|X|]<\infty,
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

Accordingly current `main` states, for each recognition state:

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

## Finding 5 — S2.8 needed a total real-valued certificate off the confidence event

S2.8 originally defined the generic confidence-envelope statistic as:

```math
D_{\mathrm{env}}
=
C_L-\sqrt{U_MV_U}.
```

On the simultaneous validity event this is mathematically sound because:

```math
E[(U-Y)^2]\le U_M
```

forces `U_M>=0` there. However, the theorem uses `D_env` as a random statistic in a probability statement over the full sample space. Outside the simultaneous event, the generic input procedure was not required to report a nonnegative numerical `U_M`. A negative off-event value would make the square root non-real.

Current `main` therefore defines:

```math
U_M^+=\max\{0,U_M\},
```

and uses:

```math
D_{\mathrm{env}}
=
C_L-\sqrt{U_M^+V_U}.
```

On the simultaneous event `U_M^+=U_M`, so the certified lower bound and its coverage are unchanged. The clipping only makes the statistic total and real-valued on the full sample space.

## Finding 6 — S2.9 concentration parameters need an explicit nonnegative domain

S2.9 defines its own sub-Gaussian/Bernstein mean-concentration forms and constructs radii containing:

```math
\sigma_X,
\qquad
\sqrt{v_W},
\qquad
b_W.
```

The intended parameter convention is standard, but the theorem previously did not state the sign domain. Because it defines the concentration form directly rather than importing a single named parameterization, current `main` now requires:

```math
\sigma_X\ge0,
\qquad
v_W\ge0,
\qquad
b_W\ge0.
```

This makes every radius real/nonnegative by definition. It also gives, for the residual-square upper envelope,

```math
U_M
=
\overline{(U-Y)^2}+r_{R^2}
\ge0
```

on every sample, so S2.8's generic clipping satisfies `U_M^+=U_M` identically in the S2.9 instantiation.

The concentration constants and `log(10/delta)` union-bound factor are otherwise unchanged.

## Finding 7 — S2.10 needs a separate zero-variance proof branch

S2.10 permits finite variance upper bounds:

```math
0\le\mathrm{Var}(Z_j)\le v_j<\infty.
```

The original proof immediately applied Chebyshev at radius:

```math
2\sqrt{\frac{v_j}{m}}.
```

For `v_j>0`, this gives the intended per-block bad probability at most `1/4`. For `v_j=0`, however, the threshold is zero and the ordinary Chebyshev division step cannot simply be reused.

The conclusion remains exact. If `v_j=0`, then:

```math
\mathrm{Var}(Z_j)=0,
```

so `Z_j=E[Z_j]` almost surely. Every block mean and the median-of-means estimator equal the population mean almost surely, the radius is zero, and the deviation probability is exactly zero.

Current `main` explicitly separates this boundary case from the `v_j>0` Chebyshev argument. The subsequent Hoeffding amplification and five-target union bound are unchanged.

## Surfaces synchronized

The core-domain correction is synchronized across:

- `theory/core_theorems.tex`;
- `theory/core_theorems.md`;
- `theory/theorem_1_3.md`;
- `theory/theorem_4_5.md`;
- `experiments/E1_FOSD.md`;
- `experiments/E3_RECOGNITION.md`;
- `experiments/E4_INTERACTION.md`;
- `paper/sections/formal_model.tex`;
- `paper/sections/theorems.tex`;
- `paper/sections/appendix.tex`;
- `docs/notation.md`;
- `docs/claims_and_assumptions.md`;
- `docs/research_map.md`;
- the root `README.md`;
- current review/audit documentation.

The supplementary corrections are synchronized across each theorem's canonical note, manuscript appendix, and dedicated audit record:

- S2.8 — `supplementary/confidence_envelope_certificate.md`, `paper/sections/confidence_envelope_appendix.tex`, `docs/s2_confidence_envelope_audit.md`;
- S2.9 — `supplementary/light_tail_certificate.md`, `paper/sections/light_tail_certificate_appendix.tex`, `docs/s2_light_tail_certificate_audit.md`;
- S2.10 — `supplementary/robust_mom_certificate.md`, `paper/sections/robust_mom_certificate_appendix.tex`, `docs/s2_robust_mom_certificate_audit.md`.

`scripts/validate_supplementary_consistency.py` makes those three source/manuscript/audit synchronization boundaries executable in CI.

## Core-lock behavior after the correction

The canonical theorem lock continues to compare current `theory/core_theorems.tex` against frozen v0.3 blob:

`82986d7197e79446d6574aab538d1edaeff47eb6`.

It normalizes exactly four approved textual differences back to the frozen form:

1. the version-neutral document title;
2. explicit base integrability in the policy setup;
3. the complete generic T1 accessibility/outcome domain, including `S>=0`, positive finite `E[S]`, base integrability of `X`, and weighted integrability of `XS`;
4. explicit T5 cross-integrability for `Q(U_1,S_0)`.

After those four exact replacements, the entire Git blob must equal the frozen v0.3 canonical blob. Thus every theorem identity, proof step, sign result, proposition, boundary, and Everett bridge paragraph remains frozen unless a further scientific review deliberately changes the lock contract.

The lock also requires the approved T1/T4/T5 domain assumptions across nine theory/card/manuscript surfaces, preventing a later explanatory edit from reintroducing incomplete theorem domains outside the compact canonical TeX.

## Supplementary results rechecked without further correction

The remaining main supplementary probability results were rechecked for the same class of failure.

- S1 assumes finite second moments before applying total covariance, which is sufficient.
- S2 assumes `U` integrable, positive finite `E[S]`, and `E[|U|S]<∞`, which supplies both sides needed by its covariance/uplift statement.
- S2.11–S2.13 use square-integrability assumptions, which are stronger than the core first-moment requirements and make the covariance/residual products finite.
- S2.5's bounded Hoeffding construction and its five-event constants remain valid.
- S2.6–S2.7's independent-holdout and finite-candidate selection accounting remain valid.

No additional domain correction was identified in those statements in this pass.

## Scientific boundary

These corrections do **not** change:

- the T1 covariance identity;
- the T2 tail identity;
- the T3 FOSD conclusion or proof;
- the T4 recognition decomposition;
- the T5 interaction decomposition or fixed-selector sign result;
- the S2.8 on-validity-event covariance lower bound or coverage level;
- the S2.9 concentration constants or union-bound level;
- the S2.10 positive-variance MoM radius or Hoeffding amplification;
- any E1–E5 numerical result;
- the base probability law;
- the Everett accessibility bridge status.

They strengthen only the stated domains, total-definedness, and boundary-case proof needed to make the existing formulas mathematically complete.

## Remaining execution gate

The corrected sources and validators still require the final `main` GitHub Actions workflow to complete successfully. Source-level reasoning and local logic-level checks are not substituted for the unavailable direct-push Actions check-run state in the audit connector.
