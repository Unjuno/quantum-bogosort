# S2.13 Explained-Variance Certificate — Theorem Audit

**Status:** post-v0.2 stacked theorem candidate

## H — claim under review

S2.13 should rewrite the coarser S2.12 residual-variance certificate using explained-variance fractions and conditional-mean correlation, without changing the underlying inequality.

## T — total-variance audit

Define:

$$
A_U
=
\frac{\operatorname{Var}(E[U\mid Y])}{\operatorname{Var}(U)},
$$

$$
A_S
=
\frac{\operatorname{Var}(E[S\mid Y])}{\operatorname{Var}(S)}.
$$

The law of total variance gives:

$$
E[\operatorname{Var}(U\mid Y)]
=
\operatorname{Var}(U)(1-A_U),
$$

and:

$$
E[\operatorname{Var}(S\mid Y)]
=
\operatorname{Var}(S)(1-A_S).
$$

Therefore substitution into S2.12 gives:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(m(Y),a(Y))
-
\sqrt{
\operatorname{Var}(U)
\operatorname{Var}(S)
(1-A_U)(1-A_S)
}.
$$

**Audit:** PASS.

## D — normalized correlation audit

When:

$$
A_UA_S>0,
$$

define:

$$
\rho_{ma}
=
\operatorname{Corr}(m(Y),a(Y)).
$$

Then:

$$
\operatorname{Cov}(m(Y),a(Y))
=
\rho_{ma}
\sqrt{
A_UA_S
\operatorname{Var}(U)
\operatorname{Var}(S)
}.
$$

Factoring out the positive total standard-deviation product yields:

$$
\operatorname{Cov}(U,S)
\ge
\sqrt{
\operatorname{Var}(U)
\operatorname{Var}(S)
}
\left[
\rho_{ma}\sqrt{A_UA_S}
-
\sqrt{(1-A_U)(1-A_S)}
\right].
$$

**Audit:** PASS.

## Corollary algebra audit

### Perfect conditional-mean alignment

With:

$$
\rho_{ma}=1,
$$

the positive-certificate condition is:

$$
A_UA_S
>
(1-A_U)(1-A_S).
$$

Expanding the right side gives:

$$
1-A_U-A_S+A_UA_S.
$$

Canceling `A_U A_S` gives:

$$
A_U+A_S>1.
$$

**Audit:** PASS.

### Symmetric explained variance

With:

$$
A_U=A_S=A,
$$

the condition is:

$$
\rho_{ma}A>1-A,
$$

so:

$$
A>
\frac{1}{1+\rho_{ma}}
$$

when the denominator is positive. The theorem presents this corollary for the positive-alignment regime.

**Audit:** PASS.

## C — boundary audit

If either:

$$
A_U=0
$$

or:

$$
A_S=0,
$$

one conditional mean is constant and `rho_ma` may be undefined. The unnormalized S2.13 inequality remains valid.

S2.13 remains sufficient, not necessary, because the S2.12 residual penalty is a worst-case lower bound.

High explained variance alone is not enough when conditional means are nonpositively aligned.

## U — interpretation

The quantities `A_U` and `A_S` are correlation-ratio / explained-variance objects. S2.13 makes the tradeoff between explained signal and residual uncertainty explicit but introduces no new physical assumption.

## ERROR CHECK

1. `A_U` and `A_S` lie in `[0,1]` by total variance.
2. The normalized form is used only when both conditional-mean variances are positive.
3. The perfect-alignment simplification to `A_U+A_S>1` is exact.
4. The symmetric threshold is algebraically correct in the positive-alignment regime.
5. The result remains a worst-case sufficient certificate inherited from S2.12.
6. Everett interpretation remains separate.

## Audit conclusion

**S2.13 IS MATHEMATICALLY SOUND. IT IS AN EXACT REPARAMETERIZATION OF THE S2.12 COARSER BOUND INTO EXPLAINED-VARIANCE FRACTIONS AND CONDITIONAL-MEAN CORRELATION.**
