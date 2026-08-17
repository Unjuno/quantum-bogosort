# S2.12 Residual-Variance Certificate — Theorem Audit

**Status:** post-v0.2 stacked theorem candidate

## H — claim under review

S2.12 should replace the abstract residual tolerance in S2.11 by a universal conservative penalty based only on conditional variances.

## T — conditional Cauchy--Schwarz audit

For every conditioning state `Y`, conditional Cauchy--Schwarz gives:

$$
|\operatorname{Cov}(U,S\mid Y)|
\le
\sqrt{
\operatorname{Var}(U\mid Y)
\operatorname{Var}(S\mid Y)
}.
$$

Therefore:

$$
\operatorname{Cov}(U,S\mid Y)
\ge
-
\sqrt{v_U(Y)v_S(Y)}.
$$

Substitution into S2.11 yields:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
E[\sqrt{v_U(Y)v_S(Y)}].
$$

**Audit:** PASS.

## D — outer Cauchy--Schwarz audit

Because `v_U(Y)` and `v_S(Y)` are nonnegative:

$$
E[\sqrt{v_U(Y)v_S(Y)}]
\le
\sqrt{E[v_U(Y)]E[v_S(Y)]}.
$$

Replacing the tighter penalty by this larger upper bound gives the weaker but valid lower certificate:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
\sqrt{E[v_U(Y)]E[v_S(Y)]}.
$$

**Audit:** PASS. The inequality direction is correct.

## Residual-energy identity

With:

$$
\eta=U-E[U\mid Y],
$$

$$
\xi=S-E[S\mid Y],
$$

we have:

$$
E[\eta^2]
=E[\operatorname{Var}(U\mid Y)],
$$

and:

$$
E[\xi^2]
=E[\operatorname{Var}(S\mid Y)].
$$

**Audit:** PASS.

## C — sharpness audit

Let `Y` be constant and let centered residuals satisfy:

$$
\xi=-c\eta,
\qquad
c>0.
$$

Then:

$$
\operatorname{Cov}(U,S\mid Y)
=-cE[\eta^2],
$$

while:

$$
\sqrt{
\operatorname{Var}(U\mid Y)
\operatorname{Var}(S\mid Y)
}
=
cE[\eta^2].
$$

Thus equality holds in the negative conditional Cauchy--Schwarz bound. Adding a constant to `S` can enforce nonnegativity without changing covariance.

**Audit:** PASS. The universal conditional-variance penalty is sharp.

## U — scope conclusion

S2.12 gives a directly interpretable residual-uncertainty penalty but is intentionally conservative. It does not claim that actual residual dependence is maximally negative. Model-specific lower bounds on conditional correlation can tighten the result.

## ERROR CHECK

1. Square integrability is sufficient for all variance quantities.
2. Conditional Cauchy--Schwarz is used pointwise in `Y`.
3. Outer Cauchy--Schwarz makes the second certificate weaker, as required.
4. The sharpness construction preserves covariance under an accessibility constant shift.
5. S2.12 is a lower certificate on top of S2.11, not a replacement for the exact decomposition.
6. Everett interpretation remains separate.

## Audit conclusion

**S2.12 IS MATHEMATICALLY SOUND AND ITS BASIC CONDITIONAL-VARIANCE PENALTY IS SHARP WITHOUT ADDITIONAL STRUCTURAL ASSUMPTIONS.**
