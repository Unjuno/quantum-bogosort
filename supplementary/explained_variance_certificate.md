# S2.13 Explained-Variance Alignment Certificate

## H — objective

S2.12 gives the general-accessibility lower bound:

$$
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(E[U\mid Y],E[S\mid Y])
-
\sqrt{
E[\mathrm{Var}(U\mid Y)]
E[\mathrm{Var}(S\mid Y)]
}.
$$

The residual-variance terms can be rewritten using the law of total variance. This produces a normalized certificate in terms of how much variance the signal `Y` explains in outcome and accessibility, together with the correlation between the two conditional means.

## T — Supplementary Theorem S2.13: explained-variance certificate

Assume `U` and `S` are square-integrable with:

$$
S\ge0,
\qquad
0<E[S]<\infty,
$$

and:

$$
\mathrm{Var}(U)>0,
\qquad
\mathrm{Var}(S)>0.
$$

Let:

$$
m(Y)=E[U\mid Y],
$$

$$
a(Y)=E[S\mid Y].
$$

Define explained-variance fractions:

$$
A_U
=
\frac{\mathrm{Var}(m(Y))}
{\mathrm{Var}(U)},
$$

and:

$$
A_S
=
\frac{\mathrm{Var}(a(Y))}
{\mathrm{Var}(S)}.
$$

By the law of total variance:

$$
0\le A_U\le1,
\qquad
0\le A_S\le1.
$$

Then S2.12 implies:

$$
\boxed{
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
\sqrt{
\mathrm{Var}(U)
\mathrm{Var}(S)
(1-A_U)(1-A_S)
}
}.
$$

If:

$$
A_U>0,
\qquad
A_S>0,
$$

define the conditional-mean correlation:

$$
\rho_{ma}
=
\mathrm{Corr}(m(Y),a(Y)).
$$

Then:

$$
\mathrm{Cov}(m(Y),a(Y))
=
\rho_{ma}
\sqrt{
\mathrm{Var}(U)
\mathrm{Var}(S)
A_UA_S
}.
$$

Therefore:

$$
\boxed{
\mathrm{Cov}(U,S)
\ge
\sqrt{
\mathrm{Var}(U)
\mathrm{Var}(S)
}
\left[
\rho_{ma}\sqrt{A_UA_S}
-
\sqrt{(1-A_U)(1-A_S)}
\right]
}.
$$

Consequently, the sufficient condition:

$$
\boxed{
\rho_{ma}\sqrt{A_UA_S}
>
\sqrt{(1-A_U)(1-A_S)}
}
$$

implies:

$$
\mathrm{Cov}(U,S)>0.
$$

Under T1, this implies positive first-person mean uplift.

## Corollary S2.13.1 — correlation threshold

When:

$$
A_UA_S>0,
$$

a sufficient condition is:

$$
\boxed{
\rho_{ma}
>
\sqrt{
\frac{(1-A_U)(1-A_S)}
{A_UA_S}
}
}.
$$

This form makes the tradeoff explicit:

- stronger conditional-mean alignment lowers the required explained variance;
- stronger predictive/explanatory power lowers the required conditional-mean correlation;
- large unexplained residual variation raises the certification threshold.

Because the right-hand side is nonnegative, this sufficient condition necessarily requires positive conditional-mean correlation.

## Corollary S2.13.2 — perfectly aligned conditional means

If:

$$
\rho_{ma}=1,
$$

then the sufficient condition becomes:

$$
A_UA_S
>
(1-A_U)(1-A_S).
$$

After cancellation:

$$
\boxed{
A_U+A_S>1
}.
$$

Thus under perfectly positively correlated conditional means, explaining more than one unit of variance fraction in total across outcome and accessibility is sufficient to overcome the worst-case residual anti-correlation allowed by S2.12.

## Corollary S2.13.3 — symmetric explained variance

If:

$$
A_U=A_S=A,
$$

with:

$$
A>0,
$$

then the sufficient condition is:

$$
\rho_{ma}A
>
1-A.
$$

When:

$$
\rho_{ma}>-1,
$$

this is algebraically equivalent to:

$$
\boxed{
A
>
\frac{1}{1+\rho_{ma}}
}.
$$

Because:

$$
0<A\le1,
$$

the strict certificate is feasible only when:

$$
\rho_{ma}>0.
$$

At `rho_ma=0`, the divided threshold is `A>1`, which is impossible. For `rho_ma<0`, the threshold exceeds one, and for `rho_ma=-1` the divided form is undefined. For:

$$
\rho_{ma}=1,
$$

this reduces to:

$$
A>\frac12.
$$

## D — proof

The law of total variance gives:

$$
\mathrm{Var}(U)
=
\mathrm{Var}(E[U\mid Y])
+
E[\mathrm{Var}(U\mid Y)].
$$

Therefore:

$$
E[\mathrm{Var}(U\mid Y)]
=
\mathrm{Var}(U)(1-A_U).
$$

Similarly:

$$
E[\mathrm{Var}(S\mid Y)]
=
\mathrm{Var}(S)(1-A_S).
$$

Substituting these identities into the coarser S2.12 bound yields:

$$
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
\sqrt{
\mathrm{Var}(U)
\mathrm{Var}(S)
(1-A_U)(1-A_S)
}.
$$

When:

$$
A_UA_S>0,
$$

we have:

$$
\mathrm{Var}(m(Y))
=
A_U\mathrm{Var}(U),
$$

and:

$$
\mathrm{Var}(a(Y))
=
A_S\mathrm{Var}(S).
$$

By the definition of `rho_ma`:

$$
\mathrm{Cov}(m(Y),a(Y))
=
\rho_{ma}
\sqrt{
A_UA_S
\mathrm{Var}(U)
\mathrm{Var}(S)
}.
$$

Factoring out:

$$
\sqrt{
\mathrm{Var}(U)
\mathrm{Var}(S)
}
$$

gives the normalized certificate.

The perfect-alignment corollary follows by elementary expansion and cancellation. In the symmetric case, division by `1+rho_ma` is valid only when `rho_ma>-1`; feasibility under `0<A<=1` further requires positive `rho_ma`.

## C — boundary cases

### No explained variance

If:

$$
A_U=0
$$

or:

$$
A_S=0,
$$

then the normalized correlation `rho_ma` may be undefined because one conditional mean is constant. The unnormalized S2.13 bound remains valid and should be used instead.

### Certificate is sufficient, not necessary

Actual residual covariance may be much less negative than the S2.12 worst case. Therefore positive total covariance can occur even when the S2.13 normalized inequality fails.

### High explained variance does not replace alignment

Large `A_U` and `A_S` alone do not guarantee positive covariance if:

$$
\rho_{ma}\le0.
$$

Indeed, the normalized worst-case certificate itself cannot be strictly positive when `rho_ma<=0` because its first term is nonpositive and its residual penalty is nonnegative.

The conditional means therefore need favorable directional alignment unless stronger information about the residual term is available.

## U — interpretation boundary

S2.13 connects the general-accessibility theorem to correlation-ratio / explained-variance quantities. It makes the sufficient condition easier to interpret in predictive-agent terms:

- `A_U` measures how much outcome variance is explained by `Y` through the conditional mean;
- `A_S` measures how much accessibility variance is explained by `Y`;
- `rho_ma` measures whether those two explained components move in the same direction.

The theorem remains a worst-case residual certificate. It does not claim that unexplained components are actually maximally anti-correlated.

No Everettian physical conclusion follows without an independent accessibility bridge.

## ERROR CHECK

1. The law of total variance gives `0 <= A_U,A_S <= 1` under finite nonzero total variance.
2. The normalized correlation form is used only when both conditional-mean variances are positive.
3. The factorization of `Cov(m,a)` uses the correct explained-variance scales.
4. The perfect-correlation condition simplifies exactly to `A_U + A_S > 1`.
5. The symmetric divided form requires `rho_ma>-1`, and a feasible strict certificate with `0<A<=1` requires `rho_ma>0`.
6. S2.13 is sufficient, not necessary, because S2.12 uses a worst-case residual penalty.
7. High explained variance without positive conditional-mean alignment is not enough.
8. T1 additionally requires positive finite expected accessibility.
9. The core five theorem set is unchanged.
10. The Everett bridge remains separate.

## Status

**S2.13 EXPLAINED-VARIANCE ALIGNMENT CERTIFICATE PROVED. THE S2.12 RESIDUAL PENALTY IS REWRITTEN IN TERMS OF EXPLAINED-VARIANCE FRACTIONS AND CONDITIONAL-MEAN CORRELATION.**
