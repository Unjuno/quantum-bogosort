# S2.12 Residual-Variance Certificate

## H — objective

S2.11 gives the exact general-accessibility decomposition:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(E[U\mid Y],E[S\mid Y])
+
E[\operatorname{Cov}(U,S\mid Y)].
$$

Its residual-tolerance form assumes a lower bound on the average conditional covariance itself. S2.12 replaces that unknown residual covariance by a universal lower bound based on conditional variances.

## T — Supplementary Theorem S2.12: residual-variance lower certificate

Assume `U` and `S` are square-integrable, with:

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
a(Y)=E[S\mid Y],
$$

$$
v_U(Y)=\operatorname{Var}(U\mid Y),
$$

and:

$$
v_S(Y)=\operatorname{Var}(S\mid Y).
$$

Then:

$$
\boxed{
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
E\!\left[
\sqrt{v_U(Y)v_S(Y)}
\right]
}.
$$

By Cauchy--Schwarz across the conditioning variable:

$$
E\!\left[
\sqrt{v_U(Y)v_S(Y)}
\right]
\le
\sqrt{
E[v_U(Y)]
E[v_S(Y)]
}.
$$

Therefore the coarser but simpler certificate is:

$$
\boxed{
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
\sqrt{
E[v_U(Y)]
E[v_S(Y)]
}
}.
$$

Consequently, either of the sufficient conditions:

$$
\operatorname{Cov}(m(Y),a(Y))
>
E\!\left[
\sqrt{v_U(Y)v_S(Y)}
\right]
$$

or the stronger but simpler condition:

$$
\operatorname{Cov}(m(Y),a(Y))
>
\sqrt{
E[v_U(Y)]
E[v_S(Y)]
}
$$

implies:

$$
\operatorname{Cov}(U,S)>0.
$$

Under T1, positive total covariance implies positive first-person mean uplift.

## Corollary S2.12.1 — residual-energy form

Define:

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
E[v_U(Y)]
=
E[\eta^2],
$$

and:

$$
E[v_S(Y)]
=
E[\xi^2].
$$

Hence:

$$
\boxed{
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
\sqrt{E[\eta^2]E[\xi^2]}
}.
$$

This expresses the worst-case residual penalty using the unexplained mean-square variation in outcome and accessibility after conditioning on `Y`.

## Corollary S2.12.2 — bounded conditional anti-correlation

Suppose conditional standard deviations are:

$$
\sigma_U(Y)=\sqrt{v_U(Y)},
$$

$$
\sigma_S(Y)=\sqrt{v_S(Y)}.
$$

If the conditional covariance satisfies the stronger model-specific lower bound:

$$
\operatorname{Cov}(U,S\mid Y)
\ge
-\rho(Y)
\sigma_U(Y)\sigma_S(Y)
$$

almost surely, where:

$$
0\le\rho(Y)\le1,
$$

then:

$$
\boxed{
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
E[\rho(Y)\sigma_U(Y)\sigma_S(Y)]
}.
$$

Thus any substantive model restriction preventing perfect residual anti-alignment directly tightens the S2.12 certificate.

## D — proof

S2.11 gives:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),a(Y))
+
E[\operatorname{Cov}(U,S\mid Y)].
$$

For each realized `Y`, conditional Cauchy--Schwarz gives:

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
\sqrt{v_U(Y)v_S(Y)}
$$

almost surely. Taking expectations and substituting into S2.11 yields:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
E[\sqrt{v_U(Y)v_S(Y)}].
$$

For the coarser form, apply ordinary Cauchy--Schwarz to the nonnegative random variables:

$$
\sqrt{v_U(Y)}
$$

and:

$$
\sqrt{v_S(Y)}.
$$

This gives:

$$
E[\sqrt{v_U(Y)v_S(Y)}]
\le
\sqrt{E[v_U(Y)]E[v_S(Y)]}.
$$

The residual-energy identities follow from the law of total variance:

$$
E[(U-m(Y))^2]
=
E[\operatorname{Var}(U\mid Y)],
$$

and analogously for `S`.

The bounded conditional anti-correlation corollary follows by inserting its stronger pointwise residual covariance lower bound into S2.11.

## C — sharpness boundary

The basic conditional Cauchy--Schwarz penalty is sharp, and the sharpness is compatible with nonnegative accessibility.

Let `Y` be constant and let `eta` be a Rademacher variable:

$$
P(\eta=1)=P(\eta=-1)=\frac12.
$$

For any:

$$
c>0,
$$

set:

$$
U=\eta,
$$

and:

$$
S=M-c\eta
$$

with:

$$
M>c.
$$

Then `S>0` almost surely and the centered accessibility residual is:

$$
\xi=-c\eta.
$$

Therefore:

$$
\operatorname{Cov}(U,S\mid Y)
=-cE[\eta^2]
=-c,
$$

while:

$$
\sqrt{
\operatorname{Var}(U\mid Y)
\operatorname{Var}(S\mid Y)
}
=c.
$$

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
