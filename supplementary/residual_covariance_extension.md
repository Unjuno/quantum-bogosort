# S2.11 Residual Conditional-Covariance Extension

## H — objective

S2 uses the score-measurability assumption:

```math
S=s(Y),
```

which forces all accessibility variation to be determined by the score `Y`. This makes the residual conditional covariance vanish and yields the exact projection identity:

```math
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(E[U\mid Y],s(Y)).
```

A more general accessibility variable may contain additional branch-level randomness or structure even after conditioning on `Y`. The correct extension is obtained from the law of total covariance.

## T — Supplementary Theorem S2.11: residual-covariance alignment

Let `U` and `S` be square-integrable random variables with:

```math
S\ge0,
\qquad
0<E[S]<\infty.
```

Let `Y` be any conditioning signal and define:

```math
m(Y)=E[U\mid Y],
```

```math
a(Y)=E[S\mid Y].
```

Square integrability guarantees that all covariance and residual terms below are finite. Then the following identity is exact:

```math
\boxed{
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),a(Y))
+
E[\mathrm{Cov}(U,S\mid Y)]
}.
```

Suppose the conditional-mean terms are comonotone. Equivalently, for an independent copy `Y'`:

```math
[m(Y)-m(Y')]
[a(Y)-a(Y')]
\ge0
```

almost surely. Then:

```math
\mathrm{Cov}(m(Y),a(Y))\ge0.
```

If, for some:

```math
\varepsilon\ge0,
```

the average residual conditional covariance obeys:

```math
E[\mathrm{Cov}(U,S\mid Y)]
\ge-\varepsilon,
```

then:

```math
\boxed{
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
\varepsilon
}.
```

Therefore the sufficient condition:

```math
\boxed{
\mathrm{Cov}(m(Y),a(Y))
>
\varepsilon
}
```

implies:

```math
\mathrm{Cov}(U,S)>0.
```

Under T1, this further implies:

```math
E_{FP}[U]-E[U]>0.
```

## Corollary S2.11.1 — nonnegative residual dependence

If:

```math
E[\mathrm{Cov}(U,S\mid Y)]\ge0
```

and `m(Y)` and `a(Y)` are comonotone, then:

```math
\boxed{
\mathrm{Cov}(U,S)\ge0
}.
```

If either the conditional-mean covariance is strictly positive or the average residual covariance is strictly positive, then:

```math
\mathrm{Cov}(U,S)>0.
```

## Corollary S2.11.2 — monotone scalar conditional means

If versions of:

```math
m(y)=E[U\mid Y=y]
```

and:

```math
a(y)=E[S\mid Y=y]
```

are both nondecreasing on the support of a scalar `Y`, then:

```math
\mathrm{Cov}(m(Y),a(Y))\ge0.
```

Thus the residual-tolerance conclusion above applies even when:

```math
S\ne s(Y)
```

almost surely.

## Corollary S2.11.3 — decomposition by residuals

Define residuals:

```math
\eta
=
U-m(Y),
```

```math
\xi
=
S-a(Y).
```

Then:

```math
E[\eta\mid Y]=0,
\qquad
E[\xi\mid Y]=0,
```

and:

```math
\boxed{
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),a(Y))
+
E[\eta\xi]
}.
```

Moreover:

```math
E[\eta\xi]
=
E[\mathrm{Cov}(U,S\mid Y)].
```

This form makes the two mechanisms explicit:

1. score-level alignment between conditional expected outcome and conditional expected accessibility;
2. residual branch-level alignment or anti-alignment not explained by the score.

## D — proof

The law of total covariance gives:

```math
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(E[U\mid Y],E[S\mid Y])
+
E[\mathrm{Cov}(U,S\mid Y)].
```

Substituting:

```math
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y]
```

gives the stated identity.

For an independent copy `Y'`, the independent-copy covariance identity gives:

```math
2\mathrm{Cov}(m(Y),a(Y))
=
E\!\left[
(m(Y)-m(Y'))(a(Y)-a(Y'))
\right].
```

Under comonotonicity, the integrand is nonnegative almost surely, hence:

```math
\mathrm{Cov}(m(Y),a(Y))\ge0.
```

If the residual term satisfies:

```math
E[\mathrm{Cov}(U,S\mid Y)]
\ge-\varepsilon,
```

then adding the two components yields:

```math
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))-
\varepsilon.
```

Strict positivity follows whenever the conditional-mean alignment margin is larger than the permitted negative residual term.

For the residual form, expand:

```math
U=m(Y)+\eta,
\qquad
S=a(Y)+\xi.
```

Because:

```math
E[\eta\mid Y]=E[\xi\mid Y]=0,
```

the cross terms between `Y`-measurable conditional means and the zero-conditional-mean residuals vanish. Thus:

```math
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),a(Y))+E[\eta\xi].
```

Conditioning on `Y` shows:

```math
E[\eta\xi\mid Y]
=
\mathrm{Cov}(U,S\mid Y),
```

and taking expectations gives the final equality.

## C — counterexample boundary

Comonotone conditional means alone are not sufficient when the residual conditional covariance is sufficiently negative.

For a fully explicit bounded example, let `Y` be constant and let `eta` be a Rademacher variable:

```math
P(\eta=1)=P(\eta=-1)=\frac12.
```

Set:

```math
U=\eta,
\qquad
S=M-\eta,
```

with:

```math
M>1.
```

Then `S>0` almost surely, both conditional means are constant, and the residuals satisfy:

```math
\xi=-\eta.
```

Therefore:

```math
\mathrm{Cov}(m(Y),a(Y))=0,
```

while:

```math
E[\eta\xi]
=-E[\eta^2]
=-1<0.
```

Thus:

```math
\mathrm{Cov}(U,S)<0.
```

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
