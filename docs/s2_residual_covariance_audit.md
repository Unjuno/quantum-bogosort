# S2.11 Residual Conditional-Covariance Extension — Theorem Audit

**Status:** post-v0.2 stacked theorem candidate; proof-review assumptions tightened

## H — claim under review

S2.11 should remove the strong assumption:

```math
S=s(Y)
```

without discarding residual accessibility/outcome dependence that remains after conditioning on `Y`.

For the theorem statement used in the repository, assume:

```math
U,S\in L^2,
\qquad
S\ge0,
\qquad
0<E[S]<\infty.
```

Square integrability is a simple sufficient condition ensuring every covariance and residual product below is finite.

## T — identity audit

Let:

```math
m(Y)=E[U\mid Y],
\qquad
a(Y)=E[S\mid Y].
```

The law of total covariance gives:

```math
\boxed{
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),a(Y))
+
E[\mathrm{Cov}(U,S\mid Y)]
}.
```

**Audit:** PASS.

### Conditional-mean sign

For an independent copy `Y'`:

```math
2\mathrm{Cov}(m(Y),a(Y))
=
E[(m(Y)-m(Y'))(a(Y)-a(Y'))].
```

If `m` and `a` are comonotone, the integrand is nonnegative almost surely.

**Audit:** PASS.

### Residual tolerance

If:

```math
E[\mathrm{Cov}(U,S\mid Y)]
\ge-\varepsilon,
```

then:

```math
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))-\varepsilon.
```

Thus:

```math
\mathrm{Cov}(m(Y),a(Y))>\varepsilon
```

is sufficient for positive total covariance.

**Audit:** PASS.

## D — residual representation audit

Define:

```math
\eta=U-m(Y),
\qquad
\xi=S-a(Y).
```

Then:

```math
E[\eta\mid Y]=E[\xi\mid Y]=0,
```

and:

```math
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),a(Y))+E[\eta\xi].
```

Conditioning on `Y` gives:

```math
E[\eta\xi\mid Y]
=
\mathrm{Cov}(U,S\mid Y).
```

**Audit:** PASS.

## C — bounded counterexample boundary

A previous draft described arbitrary centered residuals and then said a sufficiently large constant could be added to accessibility. That statement requires a bounded-below accessibility residual. The proof-review version uses a bounded construction explicitly.

Let `Y` be constant and let `eta` be Rademacher:

```math
P(\eta=1)=P(\eta=-1)=\frac12.
```

Set:

```math
U=\eta,
\qquad
S=M-\eta,
\qquad
M>1.
```

Then `S>0` almost surely, the conditional means are constant, and the centered accessibility residual is:

```math
\xi=-\eta.
```

Hence:

```math
\mathrm{Cov}(m(Y),a(Y))=0,
```

but:

```math
E[\eta\xi]=-1<0.
```

**Audit:** PASS. This establishes the required counterexample without any hidden boundedness assumption.

## U — relation to S2

S2 is recovered when:

```math
S=s(Y),
```

because then:

```math
a(Y)=S
```

and:

```math
\mathrm{Cov}(U,S\mid Y)=0
```

almost surely.

S2.11 therefore broadens the abstract model while keeping residual dependence explicit.

## ERROR CHECK

1. `U,S in L^2` is sufficient for all displayed covariance terms.
2. No conditional independence assumption is used.
3. Comonotonicity controls only the conditional-mean term.
4. The residual term may have either sign.
5. The epsilon condition is sufficient, not necessary.
6. `S=s(Y)` is correctly recovered as a zero-residual special case.
7. The counterexample uses bounded residuals and strictly positive accessibility.
8. The Everett bridge remains separate.

## Audit conclusion

**S2.11 IS MATHEMATICALLY SOUND UNDER THE EXPLICIT SQUARE-INTEGRABILITY ASSUMPTION. THE PROOF-REVIEW REVISION REMOVES AN AMBIGUOUS MOMENT CONDITION AND MAKES THE NEGATIVE-RESIDUAL COUNTEREXAMPLE FULLY BOUNDED.**
