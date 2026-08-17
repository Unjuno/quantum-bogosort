# S2.11 Residual Conditional-Covariance Extension — Theorem Audit

**Status:** post-v0.2 stacked theorem candidate

## H — claim under review

S2.11 should remove the strong assumption:

$$
S=s(Y)
$$

without discarding residual accessibility/outcome dependence that remains after conditioning on `Y`.

## T — identity audit

Let:

$$
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
$$

The law of total covariance gives:

$$
\boxed{
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),a(Y))
+
E[\operatorname{Cov}(U,S\mid Y)]
}.
$$

**Audit:** PASS.

### Conditional-mean sign

For an independent copy `Y'`:

$$
2\operatorname{Cov}(m(Y),a(Y))
=
E[(m(Y)-m(Y'))(a(Y)-a(Y'))].
$$

If `m` and `a` are comonotone, the integrand is nonnegative almost surely.

**Audit:** PASS.

### Residual tolerance

If:

$$
E[\operatorname{Cov}(U,S\mid Y)]
\ge-\varepsilon,
$$

then:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))-
\varepsilon.
$$

Thus:

$$
\operatorname{Cov}(m(Y),a(Y))>\varepsilon
$$

is sufficient for positive total covariance.

**Audit:** PASS.

## D — residual representation audit

Define:

$$
\eta=U-m(Y),
\qquad
\xi=S-a(Y).
$$

Then:

$$
E[\eta\mid Y]=E[\xi\mid Y]=0.
$$

Expanding the covariance removes cross terms because the residuals have zero conditional mean, leaving:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),a(Y))+E[\eta\xi].
$$

Conditioning on `Y` gives:

$$
E[\eta\xi\mid Y]
=
\operatorname{Cov}(U,S\mid Y).
$$

**Audit:** PASS.

## C — counterexample boundary

Let `Y` be constant. Then:

$$
\operatorname{Cov}(m(Y),a(Y))=0.
$$

Let centered residuals satisfy:

$$
\xi=-\eta
$$

and add a sufficiently large positive constant to accessibility so that `S>=0`. Then:

$$
E[\eta\xi]
=-E[\eta^2]<0.
$$

Therefore:

$$
\operatorname{Cov}(U,S)<0.
$$

This proves that comonotone or constant conditional means do not control the total covariance after score-measurability is removed unless the residual term is also bounded or signed.

**Audit:** PASS.

## U — relation to S2

S2 is recovered when:

$$
S=s(Y),
$$

because then:

$$
a(Y)=S
$$

and:

$$
\operatorname{Cov}(U,S\mid Y)=0
$$

almost surely.

S2.11 therefore strictly broadens the abstract probability model, while making the additional residual-dependence requirement explicit rather than silently dropping it.

## ERROR CHECK

1. No conditional independence assumption is used.
2. The law of total covariance is exact under the stated moment conditions.
3. Comonotonicity controls only the first term.
4. The residual term may have either sign.
5. The epsilon condition is sufficient, not necessary.
6. `S=s(Y)` is correctly recovered as a zero-residual special case.
7. The counterexample preserves accessibility nonnegativity by adding a constant, which does not change covariance.
8. The Everett bridge remains separate.

## Audit conclusion

**S2.11 IS MATHEMATICALLY SOUND UNDER THE STATED INTEGRABILITY CONDITIONS. THE EXTENSION CORRECTLY REPLACES SCORE-MEASURABILITY WITH AN EXACT TOTAL-COVARIANCE DECOMPOSITION AND AN EXPLICIT RESIDUAL CONDITION.**
