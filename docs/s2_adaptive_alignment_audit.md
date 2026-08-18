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
\mathrm{Cov}(U,S)\ge0.
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
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(E[U\mid Y],s(Y))
}.
$$

**Audit:** PASS.

### Monotone/comonotone sign condition

For an independent copy `Y'`:

$$
2\mathrm{Cov}(m(Y),s(Y))
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
\mathrm{Cov}(U,S)>0.
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
\frac{\mathrm{Cov}(U,S)}{E[S]}.
$$

Thus S2 supplies a sufficient condition for nonnegative or strict first-person mean uplift.

**Audit:** PASS conditional on the existing weighted-measure model.

### Corollary S2.2 — posterior-mean self-calibration

If an internal information state `B` generates the score:

$$
Y=E[U\mid B],
$$

then `Y` is `B`-measurable and the tower property gives:

$$
E[U\mid Y]
=
E[E[U\mid B]\mid Y]
=E[Y\mid Y]
=Y.
$$

Hence a true posterior-mean score satisfies the S2 conditional-mean calibration premise exactly.

**Audit:** PASS.

### Corollary S2.3 — approximate-calibration robustness

Define:

$$
e(Y)=E[U\mid Y]-Y.
$$

Then:

$$
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(Y,S)+\mathrm{Cov}(e(Y),S).
$$

Cauchy--Schwarz gives:

$$
|\mathrm{Cov}(e(Y),S)|
\le
\sqrt{\mathrm{Var}(e(Y))\mathrm{Var}(S)}.
$$

Therefore:

$$
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(Y,S)
-
\sqrt{\mathrm{Var}(e(Y))\mathrm{Var}(S)}.
$$

The strict inequality:

$$
\mathrm{Cov}(Y,S)
>
\sqrt{\mathrm{Var}(e(Y))\mathrm{Var}(S)}
$$

is sufficient for positive outcome/accessibility covariance.

**Audit:** PASS under square integrability.

### Corollary S2.4 — prediction-MSE certificate

The S2.3 calibration variance may be difficult to estimate directly. Since:

$$
e(Y)=E[U-Y\mid Y],
$$

conditional Jensen gives:

$$
E[e(Y)^2]
\le
E[(U-Y)^2].
$$

Also:

$$
\mathrm{Var}(e(Y))
\le
E[e(Y)^2].
$$

Substituting into S2.3 yields:

$$
\boxed{
\mathrm{Cov}(U,S)
\ge
\mathrm{Cov}(Y,S)
-
\sqrt{E[(U-Y)^2]\mathrm{Var}(S)}
}.
$$

Therefore:

$$
\mathrm{Cov}(Y,S)
>
\sqrt{E[(U-Y)^2]\mathrm{Var}(S)}
$$

is sufficient for strict positive outcome/accessibility covariance.

**Audit:** PASS under square integrability.

The prediction MSE decomposes exactly as:

$$
E[(U-Y)^2]
=
E[\mathrm{Var}(U\mid Y)]
+
E[e(Y)^2].
$$

To verify this, write:

$$
U-Y
=
(U-E[U\mid Y])+e(Y).
$$

The cross term has conditional expectation zero given `Y`, so the squared-error expectation separates into conditional variance plus squared calibration error.

**Audit:** PASS.

This decomposition establishes the key boundary: S2.4 is conservative relative to S2.3 because standard prediction MSE includes irreducible conditional outcome variance.

## D — assumptions checked

The base theorem uses:

1. `U` integrable;
2. `S=s(Y)` nonnegative and score-measurable;
3. `0<E[S]<∞`;
4. `E[|U|S]<∞`;
5. comonotonicity of `m(Y)` and `s(Y)` for the sign result;
6. a positive-probability strict-order event for strict positivity.

The posterior-mean corollary additionally assumes the displayed score really is the conditional expectation under the analyzed probability model. S2.3 and S2.4 assume square integrability of the relevant quantities.

The projection identity does **not** require scalar monotonicity; scalar monotonicity is only one easy sufficient condition for comonotonicity.

## C — counterexample and certificate boundaries

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
\mathrm{Cov}(U,S)=0.
$$

Hence:

$$
I(U;Y)>0
\not\Rightarrow
\mathrm{Cov}(U,S)>0.
$$

**Audit:** PASS; this blocks an overstrong information-theoretic claim.

### S2.4 can fail to certify a true positive covariance

Suppose the score is perfectly calibrated, so:

$$
e(Y)=0,
$$

but the future outcome has large irreducible conditional variance. Then S2.2/S2.3 may certify positive covariance from score ordering while:

$$
E[(U-Y)^2]
=
E[\mathrm{Var}(U\mid Y)]
$$

is large enough that the S2.4 inequality does not certify positivity.

Therefore failure of the MSE certificate means only that this **sufficient lower bound is inconclusive**; it does not imply zero or negative covariance.

**Audit:** PASS.

### Accessibility with residual randomness

For general `S` not measurable with respect to `Y`:

$$
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(E[U\mid Y],E[S\mid Y])
+
E[\mathrm{Cov}(U,S\mid Y)].
$$

S2 controls only the first term unless score-measurability sets the second term to zero.

**Audit:** PASS; residual conditional covariance is an explicit extension problem.

## U — interpretation and novelty boundary

S2 strengthens the adaptive-agent layer in a narrow way:

- **before S2:** E2/E3 showed that toy learned agents can generate outcome/accessibility alignment;
- **S2:** once a learned score orders conditional expected outcome and accessibility respects that ordering, the covariance implication is exact;
- **S2.2:** a true posterior-mean score is exactly conditionally mean-calibrated;
- **S2.3:** approximate calibration admits a quantitative worst-case covariance-error bound;
- **S2.4:** ordinary prediction MSE gives a weaker but directly estimable sufficient certificate.

These results do not establish:

- that adaptation automatically learns the true posterior mean;
- that a finite trained model has sufficiently small calibration error;
- that low prediction MSE is necessary for positive covariance;
- that mutual information is sufficient;
- that accessibility should be a function of the learned score;
- that the accessibility map has an Everettian physical interpretation.

The remaining finite-agent question is directly testable: estimate either the sharp conditional-mean calibration term or the conservative prediction-MSE term and compare it with the score/accessibility alignment margin.

## ERROR CHECK

1. No appeal to Pearson correlation is required.
2. No appeal to mutual information is used in the proof.
3. The sign proof uses the same independent-copy covariance identity already used in T3 and C5.1.
4. Strictness is not inferred merely from nonconstant `Y`; the ordered quantities themselves must vary together.
5. Posterior-mean self-calibration is exact only for `Y=E[U|B]` under the same analyzed probability model.
6. The S2.3 calibration-error inequality is a sufficient lower bound obtained by worst-case sign; it is not necessary for positivity.
7. S2.4 uses conditional Jensen and is weaker than S2.3 because prediction MSE includes irreducible conditional variance.
8. Failure of the S2.4 certificate is inconclusive and must not be interpreted as evidence of negative covariance.
9. S2.3 and S2.4 require square integrability.
10. The theorem is supplementary and does not alter the locked core five.
11. No new simulation is needed to establish the theorem; E2/E3 only illustrate premise generation.
12. The Everett bridge remains logically separate.

## Audit conclusion

**S2 AND COROLLARIES S2.1–S2.4 ARE MATHEMATICALLY SOUND UNDER THEIR STATED MEASURABILITY, INTEGRABILITY, CALIBRATION, AND COMONOTONICITY ASSUMPTIONS. S2.4 IS A CONSERVATIVE SUFFICIENT CERTIFICATE, NOT A NECESSARY CONDITION.**
