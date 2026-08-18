# Post-v0.2 Core S2 Proof Review

**Scope:** S2, S2.11, S2.12, S2.13  
**Status:** dedicated proof-review pass after manuscript compression

This review is separate from the original theorem audits. Its purpose is to re-check the reduced main-text theorem spine for hidden integrability assumptions, boundary-case errors, and counterexample constructions before any future preprint promotion.

## H — review target

The manuscript now emphasizes the chain:

$$
\text{S2 predictive alignment}
\longrightarrow
\text{S2.11 general accessibility}
\longrightarrow
\text{S2.12 residual penalty}
\longrightarrow
\text{S2.13 explained-variance form}.
$$

The review asks whether each step remains valid under assumptions stated explicitly enough for a standalone mathematical reading.

## T — S2 review

S2 assumes:

$$
S=s(Y)\ge0,
\qquad
0<E[S]<\infty,
\qquad
E[|U|S]<\infty,
$$

with integrable `U`, and defines:

$$
m(Y)=E[U\mid Y].
$$

Because `S` is `Y`-measurable,

$$
E[US]=E[m(Y)S].
$$

Moreover conditional Jensen gives:

$$
|m(Y)|
\le
E[|U|\mid Y],
$$

so:

$$
E[|m(Y)|S]
\le
E[E[|U|\mid Y]S]
=
E[|U|S]<\infty.
$$

Thus the covariance projection identity is well-defined:

$$
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),s(Y)).
$$

The independent-copy identity used for comonotonicity is also legitimate because the required products are integrable.

**Review:** PASS. No theorem change required.

## D — S2.11 review

### Finding 1: moment assumptions were too implicit

An earlier S2.11 draft stated that the "moments required below" were finite and highlighted:

$$
E[|US|]<\infty.
$$

That wording was mathematically serviceable only if interpreted as including every moment needed by the total-covariance decomposition, but it was unnecessarily ambiguous. In particular, the theorem should not require a reader to infer separate finiteness of the covariance components.

### Correction

S2.11 now assumes explicitly:

$$
U,S\in L^2.
$$

This guarantees:

$$
E[|US|]<\infty
$$

by Cauchy--Schwarz and ensures all covariance, conditional-mean, and residual terms used in the theorem are finite.

### Finding 2: counterexample shift needed bounded residuals

The earlier counterexample said to choose centered residuals with:

$$
\xi=-\eta
$$

and add a sufficiently large constant to accessibility. For an arbitrary unbounded residual, no finite constant need make accessibility nonnegative almost surely.

### Correction

The counterexample now uses a Rademacher residual:

$$
P(\eta=1)=P(\eta=-1)=\frac12,
$$

with:

$$
U=\eta,
\qquad
S=M-\eta,
\qquad
M>1.
$$

Then:

$$
S>0
$$

almost surely and:

$$
\mathrm{Cov}(U,S)=-1.
$$

This proves the same boundary claim without any hidden boundedness assumption.

**Review:** PASS after explicit-assumption and bounded-counterexample corrections.

## C — S2.12 review

Conditional Cauchy--Schwarz gives, almost surely:

$$
\mathrm{Cov}(U,S\mid Y)
\ge
-
\sqrt{
\mathrm{Var}(U\mid Y)
\mathrm{Var}(S\mid Y)
}.
$$

Under `U,S in L^2`, the conditional variance terms have finite expectations. Therefore S2.11 yields:

$$
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(m(Y),a(Y))
-
E[\sqrt{v_U(Y)v_S(Y)}].
$$

Outer Cauchy--Schwarz gives:

$$
E[\sqrt{v_Uv_S}]
\le
\sqrt{E[v_U]E[v_S]}.
$$

The direction of the resulting lower bound is correct: replacing the residual penalty by a larger upper bound makes the covariance lower certificate weaker.

### Sharpness correction

The same boundedness issue identified for S2.11 appeared in the earlier S2.12 sharpness prose. It is now replaced by:

$$
U=\eta,
\qquad
S=M-c\eta,
$$

where `eta` is Rademacher, `c>0`, and `M>c`. Then:

$$
S>0
$$

almost surely and:

$$
\mathrm{Cov}(U,S\mid Y)=-c
$$

while:

$$
\sqrt{
\mathrm{Var}(U\mid Y)
\mathrm{Var}(S\mid Y)
}=c.
$$

Thus the universal negative conditional Cauchy--Schwarz penalty is genuinely sharp within the nonnegative-accessibility model.

**Review:** PASS after bounded sharpness correction.

## U — S2.13 review

Assume:

$$
\mathrm{Var}(U)>0,
\qquad
\mathrm{Var}(S)>0.
$$

Define:

$$
A_U
=
\frac{\mathrm{Var}(E[U\mid Y])}{\mathrm{Var}(U)},
\qquad
A_S
=
\frac{\mathrm{Var}(E[S\mid Y])}{\mathrm{Var}(S)}.
$$

Total variance gives:

$$
0\le A_U,A_S\le1.
$$

When `A_U A_S>0`, the conditional-mean correlation is well-defined and:

$$
\mathrm{Cov}(m,a)
=
\rho_{ma}
\sqrt{
A_UA_S
\mathrm{Var}(U)
\mathrm{Var}(S)
}.
$$

Substitution into S2.12 gives the stated normalized lower bound.

### Finding: symmetric threshold needed an explicit domain

For:

$$
A_U=A_S=A>0,
$$

the sufficient condition is:

$$
\rho_{ma}A>1-A.
$$

The divided form:

$$
A>
\frac{1}{1+\rho_{ma}}
$$

requires:

$$
\rho_{ma}>-1.
$$

Because:

$$
A\le1,
$$

the strict worst-case certificate is feasible only if:

$$
\rho_{ma}>0.
$$

At zero correlation it would require `A>1`; for negative correlation it is impossible under `A<=1`; at `rho_ma=-1` the divided form is undefined.

### Correction

The theorem source, Appendix, and audit now state this domain explicitly. The primary normalized S2.13 inequality itself was already correct.

**Review:** PASS after boundary-domain clarification.

## Cross-theorem consistency

### S2 to S2.11

When:

$$
S=s(Y),
$$

the residual accessibility term vanishes and:

$$
\mathrm{Cov}(U,S\mid Y)=0.
$$

Therefore S2 is exactly recovered from S2.11.

**Check:** PASS.

### S2.11 to S2.12

S2.12 does not replace the exact residual term by an equality. It supplies only a lower bound based on conditional variances.

**Check:** PASS.

### S2.12 to S2.13

S2.13 is a reparameterization of the coarser S2.12 bound using total-variance fractions and conditional-mean correlation.

**Check:** PASS.

### T1 bridge

Positive covariance implies positive first-person mean shift only after:

$$
0<E[S]<\infty.
$$

This condition is retained in the main S2.11–S2.13 presentation.

**Check:** PASS.

## ERROR CHECK

1. No new theorem was introduced by this review.
2. S2's projection identity remains valid under its original integrability assumptions.
3. S2.11 now uses explicit square integrability rather than an ambiguous moment catch-all.
4. S2.11 and S2.12 counterexamples now use bounded Rademacher residuals, so finite accessibility shifts are rigorous.
5. S2.12's outer Cauchy--Schwarz inequality direction is correct.
6. S2.12 sharpness is compatible with strictly positive accessibility.
7. S2.13's primary normalized inequality is unchanged.
8. The S2.13 symmetric divided threshold now states its denominator and feasibility conditions.
9. Failure of S2.12/S2.13 remains inconclusive because both are sufficient worst-case certificates.
10. The Everett bridge remains independent of all proof corrections.
11. T1–T5 and E1–E5 remain unchanged.

## Review conclusion

**PASS WITH THREE CORRECTIONS. THE CORE S2 SPINE IS MATHEMATICALLY SOUND. THE REVIEW TIGHTENED S2.11 MOMENT ASSUMPTIONS, MADE S2.11/S2.12 COUNTEREXAMPLES FULLY BOUNDED, AND CLARIFIED THE DOMAIN OF THE S2.13 SYMMETRIC THRESHOLD. NONE OF THESE CHANGES ALTER THE CENTRAL THEOREM IDENTITIES OR THE QBS CLAIM BOUNDARY.**
