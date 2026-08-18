# S2.12 Residual-Variance Certificate — Theorem Audit

**Status:** post-v0.2 stacked theorem candidate; sharpness construction tightened in proof review

## H — claim under review

S2.12 should replace the abstract residual tolerance in S2.11 by a universal conservative penalty based only on conditional variances.

Assume:

$$
U,S\in L^2,
\qquad
S\ge0,
\qquad
0<E[S]<\infty.
$$

## T — conditional Cauchy--Schwarz audit

For every conditioning state `Y`, conditional Cauchy--Schwarz gives:

$$
|\mathrm{Cov}(U,S\mid Y)|
\le
\sqrt{
\mathrm{Var}(U\mid Y)
\mathrm{Var}(S\mid Y)
}.
$$

Therefore:

$$
\mathrm{Cov}(U,S\mid Y)
\ge
-
\sqrt{v_U(Y)v_S(Y)}.
$$

Substitution into S2.11 yields:

$$
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
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
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
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
E[\eta^2]=E[\mathrm{Var}(U\mid Y)],
$$

and:

$$
E[\xi^2]=E[\mathrm{Var}(S\mid Y)].
$$

**Audit:** PASS.

## C — sharpness audit

A previous draft stated the sharpness construction for arbitrary centered residuals and then invoked a constant accessibility shift. To guarantee nonnegativity with a finite shift, the proof-review version uses a bounded residual explicitly.

Let `Y` be constant, let `eta` be Rademacher, and for `c>0` set:

$$
U=\eta,
$$

$$
S=M-c\eta,
\qquad
M>c.
$$

Then:

$$
S>0
$$

almost surely and:

$$
\xi=-c\eta.
$$

Thus:

$$
\mathrm{Cov}(U,S\mid Y)=-c,
$$

while:

$$
\sqrt{
\mathrm{Var}(U\mid Y)
\mathrm{Var}(S\mid Y)
}=c.
$$

Equality holds in the negative conditional Cauchy--Schwarz bound.

**Audit:** PASS. The universal conditional-variance penalty is sharp while satisfying accessibility nonnegativity.

## U — scope conclusion

S2.12 gives a directly interpretable residual-uncertainty penalty but is intentionally conservative. It does not claim that actual residual dependence is maximally negative. Model-specific lower bounds on conditional correlation can tighten the result.

## ERROR CHECK

1. Square integrability is sufficient for all variance and covariance quantities.
2. Conditional Cauchy--Schwarz is used pointwise in `Y`.
3. Outer Cauchy--Schwarz makes the second certificate weaker, as required.
4. The sharpness construction uses bounded Rademacher residuals and strictly positive accessibility.
5. S2.12 is a lower certificate on top of S2.11, not a replacement for the exact decomposition.
6. Everett interpretation remains separate.

## Audit conclusion

**S2.12 IS MATHEMATICALLY SOUND AND ITS BASIC CONDITIONAL-VARIANCE PENALTY IS SHARP. THE PROOF-REVIEW REVISION MAKES THE NONNEGATIVE-ACCESSIBILITY SHARPNESS EXAMPLE FULLY EXPLICIT.**
