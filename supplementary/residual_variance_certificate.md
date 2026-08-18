# S2.12 Residual-Variance Certificate

## H — objective

S2.11 gives the exact general-accessibility decomposition:

```math
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(E[U\mid Y],E[S\mid Y])
+
E[\mathrm{Cov}(U,S\mid Y)].
```

Its residual-tolerance form assumes a lower bound on the average conditional covariance itself. S2.12 replaces that unknown residual covariance by a universal lower bound based on conditional variances.

## T — Supplementary Theorem S2.12: residual-variance lower certificate

Assume `U` and `S` are square-integrable, with:

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
a(Y)=E[S\mid Y],
```

```math
v_U(Y)=\mathrm{Var}(U\mid Y),
```

and:

```math
v_S(Y)=\mathrm{Var}(S\mid Y).
```

Then:

```math
\boxed{
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
E\!\left[
\sqrt{v_U(Y)v_S(Y)}
\right]
}.
```

By Cauchy--Schwarz across the conditioning variable:

```math
E\!\left[
\sqrt{v_U(Y)v_S(Y)}
\right]
\le
\sqrt{
E[v_U(Y)]
E[v_S(Y)]
}.
```

Therefore the coarser but simpler certificate is:

```math
\boxed{
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
\sqrt{
E[v_U(Y)]
E[v_S(Y)]
}
}.
```

Consequently, either of the sufficient conditions:

```math
\mathrm{Cov}(m(Y),a(Y))
>
E\!\left[
\sqrt{v_U(Y)v_S(Y)}
\right]
```

or the stronger but simpler condition:

```math
\mathrm{Cov}(m(Y),a(Y))
>
\sqrt{
E[v_U(Y)]
E[v_S(Y)]
}
```

implies:

```math
\mathrm{Cov}(U,S)>0.
```

Under T1, positive total covariance implies positive first-person mean uplift.

## Corollary S2.12.1 — residual-energy form

Define:

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
E[v_U(Y)]
=
E[\eta^2],
```

and:

```math
E[v_S(Y)]
=
E[\xi^2].
```

Hence:

```math
\boxed{
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
\sqrt{E[\eta^2]E[\xi^2]}
}.
```

This expresses the worst-case residual penalty using the unexplained mean-square variation in outcome and accessibility after conditioning on `Y`.

## Corollary S2.12.2 — bounded conditional anti-correlation

Suppose conditional standard deviations are:

```math
\sigma_U(Y)=\sqrt{v_U(Y)},
```

```math
\sigma_S(Y)=\sqrt{v_S(Y)}.
```

If the conditional covariance satisfies the stronger model-specific lower bound:

```math
\mathrm{Cov}(U,S\mid Y)
\ge
-\rho(Y)
\sigma_U(Y)\sigma_S(Y)
```

almost surely, where:

```math
0\le\rho(Y)\le1,
```

then:

```math
\boxed{
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
E[\rho(Y)\sigma_U(Y)\sigma_S(Y)]
}.
```

Thus any substantive model restriction preventing perfect residual anti-alignment directly tightens the S2.12 certificate.

## D — proof

S2.11 gives:

```math
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),a(Y))
+
E[\mathrm{Cov}(U,S\mid Y)].
```

For each realized `Y`, conditional Cauchy--Schwarz gives:

```math
|\mathrm{Cov}(U,S\mid Y)|
\le
\sqrt{
\mathrm{Var}(U\mid Y)
\mathrm{Var}(S\mid Y)
}.
```

Therefore:

```math
\mathrm{Cov}(U,S\mid Y)
\ge
-
\sqrt{v_U(Y)v_S(Y)}
```

almost surely. Taking expectations and substituting into S2.11 yields:

```math
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
E[\sqrt{v_U(Y)v_S(Y)}].
```

For the coarser form, apply ordinary Cauchy--Schwarz to the nonnegative random variables:

```math
\sqrt{v_U(Y)}
```

and:

```math
\sqrt{v_S(Y)}.
```

This gives:

```math
E[\sqrt{v_U(Y)v_S(Y)}]
\le
\sqrt{E[v_U(Y)]E[v_S(Y)]}.
```

The residual-energy identities follow from the law of total variance:

```math
E[(U-m(Y))^2]
=
E[\mathrm{Var}(U\mid Y)],
```

and analogously for `S`.

The bounded conditional anti-correlation corollary follows by inserting its stronger pointwise residual covariance lower bound into S2.11.

## C — sharpness boundary

The basic conditional Cauchy--Schwarz penalty is sharp, and the sharpness is compatible with nonnegative accessibility.

Let `Y` be constant and let `eta` be a Rademacher variable:

```math
P(\eta=1)=P(\eta=-1)=\frac12.
```

For any:

```math
c>0,
```

set:

```math
U=\eta,
```

and:

```math
S=M-c\eta
```

with:

```math
M>c.
```

Then `S>0` almost surely and the centered accessibility residual is:

```math
\xi=-c\eta.
```

Therefore:

```math
\mathrm{Cov}(U,S\mid Y)
=-cE[\eta^2]
=-c,
```

while:

```math
\sqrt{
\mathrm{Var}(U\mid Y)
\mathrm{Var}(S\mid Y)
}
=c.
```

Thus equality holds in the negative conditional Cauchy--Schwarz bound while accessibility remains strictly positive.

Therefore no uniformly tighter residual lower bound is possible from conditional variances alone.

## U — interpretation boundary

S2.12 turns the abstract `epsilon` in S2.11 into a conservative variance-based penalty. It is useful when a model can estimate or bound unexplained conditional variation more readily than residual conditional covariance itself.

The result does not imply that residual anti-correlation is physically likely. It only quantifies the worst-case penalty compatible with the conditional variances.

In an Everett interpretation, a physical model would still be needed to justify the relevant conditioning signal, accessibility variable, and residual dependence structure.

## ERROR CHECK

1. Conditional Cauchy--Schwarz is applied pointwise in `Y`.
2. The outer Cauchy--Schwarz step makes the second certificate weaker, not stronger.
3. Square integrability is sufficient for all displayed variance and covariance terms.
4. The residual-energy identities are exact conditional-variance identities.
5. The Cauchy--Schwarz residual penalty is sharp under perfect conditional anti-correlation.
6. The bounded Rademacher construction proves sharpness while maintaining `S>0` with a finite constant.
7. The bounded conditional anti-correlation result is a model-specific tightening, not a universal assumption.
8. S2.11 remains the exact decomposition; S2.12 is a conservative lower certificate built on it.
9. T1 additionally requires positive finite `E[S]`, already included here.
10. The Everett bridge remains separate.

## Status

**S2.12 RESIDUAL-VARIANCE CERTIFICATE PROVED. THE UNKNOWN S2.11 RESIDUAL TERM IS LOWER-BOUNDED BY CONDITIONAL VARIANCE PRODUCTS, WITH A SHARP WORST-CASE Cauchy--Schwarz PENALTY.**
