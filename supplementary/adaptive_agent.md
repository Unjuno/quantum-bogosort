# Adaptive-Agent Predictive Alignment

## H — theorem target

The adaptive-agent mechanism should not rely on an externally inserted score/outcome correlation. Let:

- `X_t` be the environment state,
- `B_t` be the agent's internal belief or world-model state,
- `Y_t=h(B_t)` be a scalar evaluation signal available at time `t`,
- `U_T` be a later outcome,
- `S_t=s(Y_t)` be nonnegative observer-indexed accessibility.

The exact question is: under what conditions does a predictive internal signal imply

$$
\operatorname{Cov}(U_T,S_t)\ge 0?
$$

The relevant notion of prediction is **conditional-mean prediction**, not mutual information by itself.

## T — Supplementary Theorem S2: Predictive-Calibration Alignment

Let `U` be integrable, let `Y` be a scalar signal, and let:

$$
m(Y)=E[U\mid Y].
$$

Let accessibility be score-measurable:

$$
S=s(Y)\ge 0,
$$

with:

$$
0<E[S]<\infty,
\qquad
E[|U|S]<\infty.
$$

Then the following projection identity is exact:

$$
\boxed{
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(m(Y),s(Y))
}.
$$

If versions of `m(y)` and `s(y)` are both nondecreasing on the support of `Y`, then:

$$
\boxed{
\operatorname{Cov}(U,S)\ge 0
}.
$$

Let `Y'` be an independent copy of `Y`. The inequality is strict whenever:

$$
P\!\left(
[m(Y)-m(Y')][s(Y)-s(Y')]>0
\right)>0.
$$

Therefore, under the weighted first-person value model:

$$
E_{FP}[U]-E[U]
=
\frac{\operatorname{Cov}(U,S)}{E[S]}
\ge 0,
$$

with strict uplift under the strictness condition above.

### Equivalent comonotonic formulation

The scalar-score monotonicity assumption can be replaced by the more general pairwise condition:

$$
[m(Y)-m(Y')][s(Y)-s(Y')]\ge0
\quad\text{almost surely}.
$$

Thus the theorem is fundamentally a comonotonicity result between conditional expected outcome and accessibility.

### Corollary S2.1: accessibility as a monotone function of predicted value

If:

$$
S=r(m(Y))
$$

for a nondecreasing measurable function `r`, then:

$$
\operatorname{Cov}(U,S)\ge0.
$$

If `m(Y)` is nonconstant with positive probability and `r` is strictly increasing on its essential range, then:

$$
\operatorname{Cov}(U,S)>0.
$$

This form does not require the raw score `Y` itself to have a globally meaningful scale; only the predicted conditional value must be ordered consistently with accessibility.

### Corollary S2.2: posterior-mean self-calibration

Let `B` denote an internal information state and suppose the evaluation score is the posterior-mean forecast:

$$
Y=E[U\mid B].
$$

Because `Y` is measurable with respect to `B`, the tower property gives:

$$
E[U\mid Y]
=
E[E[U\mid B]\mid Y]
=
E[Y\mid Y]
=Y.
$$

Therefore the conditional-mean calibration premise of S2 holds **exactly**:

$$
m(Y)=Y.
$$

Hence, for every nondecreasing score-measurable accessibility map `S=s(Y)`:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(Y,s(Y))
\ge0.
$$

If `Y` is nonconstant and `s` is strictly increasing on the essential range of `Y`, then:

$$
\operatorname{Cov}(U,S)>0.
$$

This corollary converts a standard posterior-mean prediction target into the directional calibration condition required by S2. It still does not prove that a learned finite model exactly equals the true posterior mean.

### Corollary S2.3: approximate-calibration robustness

Assume `U`, `Y`, and `S=s(Y)` are square-integrable and define calibration error:

$$
e(Y)=E[U\mid Y]-Y.
$$

Then:

$$
\operatorname{Cov}(U,S)
=
\operatorname{Cov}(Y,S)
+
\operatorname{Cov}(e(Y),S).
$$

By Cauchy--Schwarz:

$$
|\operatorname{Cov}(e(Y),S)|
\le
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)}.
$$

Therefore:

$$
\boxed{
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)}
}.
$$

A sufficient robustness condition for positive covariance is:

$$
\operatorname{Cov}(Y,S)
>
\sqrt{\operatorname{Var}(e(Y))\operatorname{Var}(S)}.
$$

This gives a direct quantitative target for learned agents: a positively ordered score can tolerate calibration error up to the point where the worst-case covariance perturbation exceeds the score/accessibility alignment margin.

## D — derivation

Because `S=s(Y)` is measurable with respect to `Y`, the tower property gives:

$$
E[US]
=
E\!\left[E[U\mid Y]S\right]
=
E[m(Y)s(Y)].
$$

Also:

$$
E[U]
=
E[m(Y)].
$$

Hence:

$$
\operatorname{Cov}(U,S)
=
E[m(Y)s(Y)]-E[m(Y)]E[s(Y)]
=
\operatorname{Cov}(m(Y),s(Y)).
$$

Now let `Y'` be an independent copy of `Y`. For integrable random variables of the required products:

$$
2\operatorname{Cov}(m(Y),s(Y))
=
E\!\left[
(m(Y)-m(Y'))(s(Y)-s(Y'))
\right].
$$

If `m` and `s` are both nondecreasing, every integrand is nonnegative. Therefore:

$$
\operatorname{Cov}(U,S)\ge0.
$$

If the pairwise product is strictly positive on a positive-probability event, the expectation is strictly positive.

## Mean-predictive strength

For `U` in `L^2`, define:

$$
M(U;Y)
=
\operatorname{Var}(E[U\mid Y]).
$$

This quantity is zero exactly when the signal does not change the conditional mean of `U` almost surely. When `\operatorname{Var}(U)>0`, the normalized correlation-ratio form is:

$$
\eta^2(U\mid Y)
=
\frac{\operatorname{Var}(E[U\mid Y])}{\operatorname{Var}(U)}.
$$

A positive value of `M(U;Y)` or `\eta^2(U\mid Y)` supplies the nondegeneracy needed for strict uplift when accessibility is a strictly increasing function of predicted value.

This is the appropriate information-like quantity for the present mean-uplift theorem. Mutual information measures general statistical dependence and is strictly weaker for this purpose.

## C — mutual information is not sufficient

Positive mutual information alone does **not** imply positive outcome/accessibility covariance.

Let:

$$
P(Y=0)=P(Y=1)=\frac12.
$$

Conditional on `Y=0`, let `U` be `+1` or `-1` with equal probability. Conditional on `Y=1`, let `U` be `+2` or `-2` with equal probability. Then `|U|` identifies `Y`, so:

$$
I(U;Y)>0.
$$

But:

$$
E[U\mid Y=0]=E[U\mid Y=1]=0.
$$

Therefore:

$$
m(Y)=0
$$

almost surely, and for **every** accessibility map of the form `S=s(Y)`:

$$
\operatorname{Cov}(U,S)=0.
$$

Thus the chain

$$
I(Y;U)>0
\Longrightarrow
\operatorname{Cov}(U,S)>0
$$

is false without an additional directional conditional-mean calibration assumption.

## Connection to adaptation

The cleanest sufficient chain is now:

$$
\text{internal information }B_t
\longrightarrow
Y_t=E[U_T\mid B_t]
\longrightarrow
E[U_T\mid Y_t]=Y_t
\longrightarrow
S_t=s(Y_t)\text{ monotone}
\longrightarrow
\operatorname{Cov}(U_T,S_t)\ge0.
$$

For an approximate learned predictor, Corollary S2.3 quantifies how much conditional-mean calibration error can be tolerated while preserving positive covariance.

E2 provides a classical nonlinear example in which a representationally adequate model learns predictive alignment while a misspecified linear model and random control do not. E3 provides a paired endogenous-policy example in which a learned internal signal remains positively associated with post-policy outcomes.

## U — interpretation boundary

S2 is a probability theorem about a score-measurable accessibility function. It strengthens the adaptive-agent part of QBS from a purely simulation-supported covariance mechanism to an exact sufficient condition, and S2.2 gives an exact self-calibration result for posterior-mean forecasts.

It does **not** establish:

- that adaptation always learns the true posterior mean;
- that finite learned models have negligible calibration error;
- that mutual information alone is enough;
- that accessibility is physically determined by the score;
- that Everettian branch self-location obeys this accessibility map.

The remaining adaptive-learning problem is narrower and empirically meaningful: measure or bound the calibration error of the learned score and compare it with the alignment margin in S2.3.

## ERROR CHECK

1. `S=s(Y)` is essential for the projection identity as stated; if accessibility contains additional randomness conditionally correlated with `U`, an extra conditional-covariance term appears.
2. Monotonicity gives a sufficient condition, not a necessary condition. Positive covariance can occur without global monotonicity.
3. Strict positivity requires nondegeneracy; two constant functions give equality.
4. Positive mutual information is deliberately not used as a sufficient condition.
5. Posterior-mean self-calibration uses only the tower property and the fact that `Y=E[U|B]` is `B`-measurable.
6. The approximate-calibration bound is one-sided after applying the absolute Cauchy--Schwarz bound; it is sufficient, not necessary, for positivity.
7. The first-person uplift conclusion additionally requires `0<E[S]<\infty`.
8. The theorem is interpretation-neutral and does not derive the Everett bridge.

## Status

**Supplementary Theorem S2 and Corollaries S2.1–S2.3 PROVED. E2/E3 remain classical mechanism demonstrations. Physical accessibility mapping remains OPEN.**
