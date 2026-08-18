# S2.11 Residual Conditional-Covariance Extension

## H — objective

S2 uses the score-measurability assumption:

$$
S=s(Y),
$$

which forces all accessibility variation to be determined by the score `Y`. This makes the residual conditional covariance vanish and yields the exact projection identity:

$$
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(E[U\mid Y],s(Y)).
$$

A more general accessibility variable may contain additional branch-level randomness or structure even after conditioning on `Y`. The correct extension is obtained from the law of total covariance.

## T — Supplementary Theorem S2.11: residual-covariance alignment

Let `U` and `S` be square-integrable random variables with:

$$
S\ge0,
\qquad
0<E[S]<\infty.
$$

Let `Y` be any conditioning signal and define:

$$
m(Y)=E[U\mid Y],
$$

$$
a(Y)=E[S\mid Y].
$$

Square integrability guarantees that all covariance and residual terms below are finite. Then the following identity is exact:

$$
\boxed{
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),a(Y))
+
E[\mathrm{Cov}(U,S\mid Y)]
}.
$$

Suppose the conditional-mean terms are comonotone. Equivalently, for an independent copy `Y'`:

$$
[m(Y)-m(Y')]
[a(Y)-a(Y')]
\ge0
$$

almost surely. Then:

$$
\mathrm{Cov}(m(Y),a(Y))\ge0.
$$

If, for some:

$$
\varepsilon\ge0,
$$

the average residual conditional covariance obeys:

$$
E[\mathrm{Cov}(U,S\mid Y)]
\ge-\varepsilon,
$$

then:

$$
\boxed{
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
\varepsilon
}.
$$

Therefore the sufficient condition:

$$
\boxed{
\mathrm{Cov}(m(Y),a(Y))
>
\varepsilon
}
$$

implies:

$$
\mathrm{Cov}(U,S)>0.
$$

Under T1, this further implies:

$$
E_{FP}[U]-E[U]>0.
$$

## Corollary S2.11.1 — nonnegative residual dependence

If:

$$
E[\mathrm{Cov}(U,S\mid Y)]\ge0
$$

and `m(Y)` and `a(Y)` are comonotone, then:

$$
\boxed{
\mathrm{Cov}(U,S)\ge0
}.
$$

If either the conditional-mean covariance is strictly positive or the average residual covariance is strictly positive, then:

$$
\mathrm{Cov}(U,S)>0.
$$

## Corollary S2.11.2 — monotone scalar conditional means

If versions of:

$$
m(y)=E[U\mid Y=y]
$$

and:

$$
a(y)=E[S\mid Y=y]
$$

are both nondecreasing on the support of a scalar `Y`, then:

$$
\mathrm{Cov}(m(Y),a(Y))\ge0.
$$

Thus the residual-tolerance conclusion above applies even when:

$$
S\ne s(Y)
$$

almost surely.

## Corollary S2.11.3 — decomposition by residuals

Define residuals:

$$
\eta
=
U-m(Y),
$$

$$
\xi
=
S-a(Y).
$$

Then:

$$
E[\eta\mid Y]=0,
\qquad
E[\xi\mid Y]=0,
$$

and:

$$
\boxed{
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),a(Y))
+
E[\eta\xi]
}.
$$

Moreover:

$$
E[\eta\xi]
=
E[\mathrm{Cov}(U,S\mid Y)].
$$

This form makes the two mechanisms explicit:

1. score-level alignment between conditional expected outcome and conditional expected accessibility;
2. residual branch-level alignment or anti-alignment not explained by the score.

## D — proof

The law of total covariance gives:

$$
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(E[U\mid Y],E[S\mid Y])
+
E[\mathrm{Cov}(U,S\mid Y)].
$$

Substituting:

$$
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y]
$$

gives the stated identity.

For an independent copy `Y'`, the independent-copy covariance identity gives:

$$
2\mathrm{Cov}(m(Y),a(Y))
=
E\!\left[
(m(Y)-m(Y'))(a(Y)-a(Y'))
\right].
$$

Under comonotonicity, the integrand is nonnegative almost surely, hence:

$$
\mathrm{Cov}(m(Y),a(Y))\ge0.
$$

If the residual term satisfies:

$$
E[\mathrm{Cov}(U,S\mid Y)]
\ge-\varepsilon,
$$

then adding the two components yields:

$$
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))-
\varepsilon.
$$

Strict positivity follows whenever the conditional-mean alignment margin is larger than the permitted negative residual term.

For the residual form, expand:

$$
U=m(Y)+\eta,
\qquad
S=a(Y)+\xi.
$$

Because:

$$
E[\eta\mid Y]=E[\xi\mid Y]=0,
$$

the cross terms between `Y`-measurable conditional means and the zero-conditional-mean residuals vanish. Thus:

$$
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),a(Y))+E[\eta\xi].
$$

Conditioning on `Y` shows:

$$
E[\eta\xi\mid Y]
=
\mathrm{Cov}(U,S\mid Y),
$$

and taking expectations gives the final equality.

## C — counterexample boundary

Comonotone conditional means alone are not sufficient when the residual conditional covariance is sufficiently negative.

For a fully explicit bounded example, let `Y` be constant and let `eta` be a Rademacher variable:

$$
P(\eta=1)=P(\eta=-1)=\frac12.
$$

Set:

$$
U=\eta,
\qquad
S=M-\eta,
$$

with:

$$
M>1.
$$

Then `S>0` almost surely, both conditional means are constant, and the residuals satisfy:

$$
\xi=-\eta.
$$

Therefore:

$$
\mathrm{Cov}(m(Y),a(Y))=0,
$$

while:

$$
E[\eta\xi]
=-E[\eta^2]
=-1<0.
$$

Thus:

$$
\mathrm{Cov}(U,S)<0.
$$

Once score-measurability is removed, the residual conditional covariance cannot be ignored.

## U — interpretation boundary

S2.11 weakens one of the cleanest but strongest assumptions in S2. Accessibility need not be a deterministic function of the predictive score. Instead, the theorem separates score-level alignment from unexplained residual dependence.

This is useful for agent models in which accessibility depends on additional branch variables not summarized by `Y`.

The theorem remains an abstract probability result. It does not identify the physical source, sign, or magnitude of the residual term in an Everettian model.

## ERROR CHECK

1. Square integrability guarantees all covariance and residual terms used by the total-covariance identity are finite.
2. `S=s(Y)` is a special case because then `Cov(U,S|Y)=0` almost surely.
3. Comonotonicity controls only the conditional-mean covariance term.
4. A negative residual term can overturn positive score-level alignment.
5. The epsilon bound is sufficient, not necessary, for positive total covariance.
6. Scalar monotonicity is only one sufficient route to comonotonicity.
7. The residual decomposition uses zero conditional means, so the cross terms vanish correctly.
8. The bounded Rademacher counterexample enforces `S>0` with a finite constant and gives strictly negative covariance.
9. T1 additionally requires positive finite `E[S]`, already included here.
10. No claim is made about the physical sign of the Everettian residual term.
11. The core five theorem set remains unchanged.

## Status

**S2.11 RESIDUAL CONDITIONAL-COVARIANCE EXTENSION PROVED. SCORE-MEASURABILITY IS REPLACED BY AN EXACT TOTAL-COVARIANCE DECOMPOSITION PLUS AN EXPLICIT RESIDUAL-SIGN OR RESIDUAL-MAGNITUDE CONDITION.**
