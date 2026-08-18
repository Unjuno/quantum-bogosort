# S2.13 Explained-Variance Certificate — Theorem Audit

**Status:** post-v0.2 stacked theorem candidate; symmetric-threshold domain tightened in proof review

## H — claim under review

S2.13 should rewrite the coarser S2.12 residual-variance certificate using explained-variance fractions and conditional-mean correlation, without changing the underlying inequality.

Assume `U,S` are square-integrable with positive total variances.

## T — total-variance audit

Define:

```math
A_U
=
\frac{\mathrm{Var}(E[U\mid Y])}{\mathrm{Var}(U)},
```

```math
A_S
=
\frac{\mathrm{Var}(E[S\mid Y])}{\mathrm{Var}(S)}.
```

The law of total variance gives:

```math
E[\mathrm{Var}(U\mid Y)]
=
\mathrm{Var}(U)(1-A_U),
```

and:

```math
E[\mathrm{Var}(S\mid Y)]
=
\mathrm{Var}(S)(1-A_S).
```

Therefore substitution into S2.12 gives:

```math
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
\sqrt{
\mathrm{Var}(U)
\mathrm{Var}(S)
(1-A_U)(1-A_S)
}.
```

**Audit:** PASS.

## D — normalized correlation audit

When:

```math
A_UA_S>0,
```

define:

```math
\rho_{ma}
=
\mathrm{Corr}(m(Y),a(Y)).
```

Then:

```math
\mathrm{Cov}(m(Y),a(Y))
=
\rho_{ma}
\sqrt{
A_UA_S
\mathrm{Var}(U)
\mathrm{Var}(S)
}.
```

Factoring out the positive total standard-deviation product yields:

```math
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
\right].
```

**Audit:** PASS.

## Corollary algebra audit

### Perfect conditional-mean alignment

With:

```math
\rho_{ma}=1,
```

the positive-certificate condition is:

```math
A_UA_S>(1-A_U)(1-A_S).
```

Expanding and canceling gives:

```math
A_U+A_S>1.
```

**Audit:** PASS.

### Symmetric explained variance

With:

```math
A_U=A_S=A>0,
```

the condition is:

```math
\rho_{ma}A>1-A.
```

If:

```math
\rho_{ma}>-1,
```

then division by `1+rho_ma` is valid and gives:

```math
A>
\frac{1}{1+\rho_{ma}}.
```

Because:

```math
0<A\le1,
```

a strict certificate is feasible only for:

```math
\rho_{ma}>0.
```

At `rho_ma=0`, the threshold is `A>1`; for negative `rho_ma` it exceeds one; at `rho_ma=-1` the divided form is undefined.

**Audit:** PASS after explicit domain clarification.

## C — boundary audit

If either:

```math
A_U=0
```

or:

```math
A_S=0,
```

one conditional mean is constant and `rho_ma` may be undefined. The unnormalized S2.13 inequality remains valid.

The general normalized sufficient condition itself requires positive conditional-mean alignment because its right-hand side is nonnegative.

S2.13 remains sufficient, not necessary, because the S2.12 residual penalty is a worst-case lower bound.

High explained variance alone is not enough when conditional means are nonpositively aligned.

## U — interpretation

The quantities `A_U` and `A_S` are correlation-ratio / explained-variance objects. S2.13 makes the tradeoff between explained signal and residual uncertainty explicit but introduces no new physical assumption.

## ERROR CHECK

1. `A_U` and `A_S` lie in `[0,1]` by total variance.
2. The normalized form is used only when both conditional-mean variances are positive.
3. The perfect-alignment simplification to `A_U+A_S>1` is exact.
4. The symmetric divided form requires `rho_ma>-1`.
5. Feasibility of the strict symmetric worst-case certificate under `A<=1` requires `rho_ma>0`.
6. The result remains a worst-case sufficient certificate inherited from S2.12.
7. Everett interpretation remains separate.

## Audit conclusion

**S2.13 IS MATHEMATICALLY SOUND. THE PROOF-REVIEW REVISION MAKES THE DOMAIN OF THE SYMMETRIC THRESHOLD EXPLICIT AND PREVENTS NONPOSITIVE CONDITIONAL-MEAN CORRELATION FROM BEING MISREAD AS CERTIFIABLE BY EXPLAINED VARIANCE ALONE.**
