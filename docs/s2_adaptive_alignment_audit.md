# S2 Predictive-Calibration Alignment — Theorem Audit

**Date:** 2026-08-17  
**Status:** post-v0.2 theorem candidate

## H — hypothesis being formalized

The adaptive-agent mechanism needs a rigorous step from an internally generated predictive score to positive outcome/accessibility covariance.

Let:

$$
m(Y)=E[U\mid Y],
\qquad
S=s(Y)\ge0.
$$

The intended implication is:

$$
\text{ordered conditional-mean prediction}
+
\text{ordered accessibility}
\Longrightarrow
\operatorname{Cov}(U,S)\ge0.
$$

## T — theorem audit

### Projection identity

Because `S=s(Y)` is measurable with respect to `Y`:

$$
E[US]
=
E[E[U\mid Y]S].
$$

Therefore:

$$
\boxed{
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(E[U\mid Y],s(Y))
}.
$$

**Audit:** PASS.

### Monotone/comonotone sign condition

For an independent copy `Y'`:

$$
2\operatorname{Cov}(m(Y),s(Y))
=
E[(m(Y)-m(Y'))(s(Y)-s(Y'))].
$$

If the two factors always have the same sign, the integrand is nonnegative almost surely.

**Audit:** PASS.

### Strictness

If:

$$
P((m(Y)-m(Y'))(s(Y)-s(Y'))>0)>0,
$$

then the nonnegative integrand is strictly positive on a positive-probability set, hence:

$$
\operatorname{Cov}(U,S)>0.
$$

**Audit:** PASS.

### First-person implication

Given:

$$
0<E[S]<\infty,
$$

T1 gives:

$$
E_{FP}[U]-E[U]
=
\frac{\operatorname{Cov}(U,S)}{E[S]}.
$$

Thus S2 supplies a sufficient condition for nonnegative or strict first-person mean uplift.

**Audit:** PASS conditional on the existing weighted-measure model.

## D — assumptions checked

The theorem uses:

1. `U` integrable;
2. `S=s(Y)` nonnegative and score-measurable;
3. `0<E[S]<∞`;
4. `E[|U|S]<∞`;
5. comonotonicity of `m(Y)` and `s(Y)` for the sign result;
6. a positive-probability strict-order event for strict positivity.

The projection identity does **not** require scalar monotonicity; scalar monotonicity is only one easy sufficient condition for comonotonicity.

## C — counterexample boundary

### Mutual information alone

Take `Y` equally likely to be `0` or `1`.

If `Y=0`, let `U` be `+1` or `-1` equally likely. If `Y=1`, let `U` be `+2` or `-2` equally likely.

Then `|U|` determines `Y`, so:

$$
I(U;Y)>0.
$$

But:

$$
E[U\mid Y]=0
$$

almost surely. Therefore, for every `S=s(Y)`:

$$
\operatorname{Cov}(U,S)=0.
$$

Hence:

$$
I(U;Y)>0
\not\Rightarrow
\operatorname{Cov}(U,S)>0.
$$

**Audit:** PASS; this blocks an overstrong information-theoretic claim.

### Accessibility with residual randomness

For general `S` not measurable with respect to `Y`:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(E[U\mid Y],E[S\mid Y])
+
E[\operatorname{Cov}(U,S\mid Y)].
$$

S2 controls only the first term unless score-measurability sets the second term to zero.

**Audit:** PASS; residual conditional covariance is an explicit extension problem.

## U — interpretation and novelty boundary

S2 strengthens the adaptive-agent layer in a narrow way:

- **before S2:** E2/E3 showed that toy learned agents can generate outcome/accessibility alignment;
- **after S2:** once a learned score orders conditional expected outcome and accessibility respects that ordering, the covariance implication is exact.

S2 does not establish:

- that adaptation automatically gives calibration;
- that mutual information is sufficient;
- that accessibility should be a function of the learned score;
- that the accessibility map has an Everettian physical interpretation.

The remaining agent-learning question is upstream of S2:

$$
\text{learning dynamics}
\Longrightarrow
E[U_T\mid Y_t=y]\text{ monotone in }y.
$$

## ERROR CHECK

1. No appeal to Pearson correlation is required.
2. No appeal to mutual information is used in the proof.
3. The sign proof uses the same independent-copy covariance identity already used in T3 and C5.1.
4. Strictness is not inferred merely from nonconstant `Y`; the ordered quantities themselves must vary together.
5. The theorem is supplementary and does not alter the locked core five.
6. No new simulation is needed to establish the theorem; E2/E3 only illustrate premise generation.
7. The Everett bridge remains logically separate.

## Audit conclusion

**S2 IS MATHEMATICALLY SOUND UNDER THE STATED SCORE-MEASURABILITY, INTEGRABILITY, AND COMONOTONICITY ASSUMPTIONS.**
