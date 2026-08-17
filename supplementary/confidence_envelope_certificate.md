# S2.8 Confidence-Envelope Certificate

## H — objective

S2.5 derives a finite-sample certificate by one specific route: bounded observations plus simultaneous Hoeffding inequalities.

The QBS covariance step itself does not depend on Hoeffding. What is actually needed is a simultaneous confidence envelope for five population moments:

$$
E[Y],
\qquad
E[S],
\qquad
E[YS],
\qquad
E[S^2],
\qquad
E[(U-Y)^2].
$$

S2.8 separates the **statistical concentration layer** from the **QBS certificate-composition layer**.

## T — Corollary S2.8: generic confidence-envelope certificate

Assume:

$$
S\ge0,
\qquad
0<E[S]<\infty,
$$

and the moments below are finite.

Suppose a statistical procedure outputs random bounds:

$$
L_Y\le U_Y,
\qquad
L_S\le U_S,
\qquad
L_{YS},
\qquad
U_{S^2},
\qquad
U_M,
$$

such that the simultaneous event:

$$
\mathcal E
=
\left\{
L_Y\le E[Y]\le U_Y
\right\}
\cap
\left\{
L_S\le E[S]\le U_S
\right\}
$$

$$
\cap
\left\{
E[YS]\ge L_{YS}
\right\}
\cap
\left\{
E[S^2]\le U_{S^2}
\right\}
\cap
\left\{
E[(U-Y)^2]\le U_M
\right\}
$$

satisfies:

$$
P(\mathcal E)\ge1-\delta.
$$

Because accessibility is nonnegative, define the effective lower bound:

$$
L_S^+
=
\max\{0,L_S\}.
$$

Define the largest possible product of the two mean intervals:

$$
P_U
=
\max\left\{
L_YL_S^+,
L_YU_S,
U_YL_S^+,
U_YU_S
\right\}.
$$

Define:

$$
C_L
=
L_{YS}-P_U.
$$

Define the variance upper envelope:

$$
V_U
=
\max\left\{
0,
U_{S^2}-(L_S^+)^2
\right\}.
$$

Finally define:

$$
\boxed{
D_{\mathrm{env}}
=
C_L-\sqrt{U_MV_U}
}.
$$

Then:

$$
\boxed{
P\!\left(
\operatorname{Cov}(U,S)
\ge
D_{\mathrm{env}}
\right)
\ge1-\delta
}.
$$

Therefore, whenever the realized confidence envelopes satisfy:

$$
\boxed{
D_{\mathrm{env}}>0,
}
$$

positive population outcome/accessibility covariance is certified at confidence at least `1-delta`.

If additionally:

$$
0<U_S<\infty,
$$

then T1 gives the first-person lower bound:

$$
\boxed{
E_{FP}[U]-E[U]
\ge
\frac{D_{\mathrm{env}}}{U_S}
>0
}
$$

on the same simultaneous event.

## D — proof

All statements below are on the simultaneous event `E`.

### Step 1: covariance lower envelope

Write:

$$
\operatorname{Cov}(Y,S)
=
E[YS]-E[Y]E[S].
$$

The event gives:

$$
E[YS]\ge L_{YS}.
$$

Also:

$$
E[Y]\in[L_Y,U_Y],
$$

and because `S>=0`:

$$
E[S]\in[L_S^+,U_S].
$$

The bilinear map:

$$
(a,b)\mapsto ab
$$

attains its maximum on a compact rectangle at a corner. Therefore:

$$
E[Y]E[S]
\le
P_U.
$$

Hence:

$$
\operatorname{Cov}(Y,S)
\ge
L_{YS}-P_U
=
C_L.
$$

### Step 2: variance upper envelope

Because:

$$
\operatorname{Var}(S)
=
E[S^2]-E[S]^2,
$$

and on `E`:

$$
E[S^2]\le U_{S^2},
\qquad
E[S]\ge L_S^+,
$$

we obtain:

$$
\operatorname{Var}(S)
\le
U_{S^2}-(L_S^+)^2.
$$

On the simultaneous-validity event this right-hand side is nonnegative. The explicit outer `max` merely keeps the reported numerical envelope nonnegative even on samples outside the confidence event. Thus:

$$
\operatorname{Var}(S)
\le
V_U.
$$

### Step 3: prediction-MSE upper envelope

The event directly gives:

$$
E[(U-Y)^2]
\le
U_M.
$$

### Step 4: compose with S2.4

S2.4 states:

$$
\operatorname{Cov}(U,S)
\ge
\operatorname{Cov}(Y,S)
-
\sqrt{
E[(U-Y)^2]\operatorname{Var}(S)
}.
$$

Substituting the simultaneous lower and upper envelopes gives:

$$
\operatorname{Cov}(U,S)
\ge
C_L-\sqrt{U_MV_U}
=
D_{\mathrm{env}}.
$$

Because `P(E)>=1-delta`, the claimed coverage follows.

If `D_env>0`, then on `E`:

$$
\operatorname{Cov}(U,S)>0.
$$

Finally, when `E[S]<=U_S` and `D_env>0`:

$$
E_{FP}[U]-E[U]
=
\frac{\operatorname{Cov}(U,S)}{E[S]}
\ge
\frac{D_{\mathrm{env}}}{U_S}.
$$

## Corollary S2.8.1 — S2.5 is an instantiation

The bounded Hoeffding construction in S2.5 supplies one valid simultaneous envelope for exactly the moments required by S2.8.

Therefore S2.5 can be viewed as:

$$
\text{Hoeffding moment bounds}
\longrightarrow
\text{S2.8 envelope composition}.
$$

The constants in S2.5 are specialized and can be tighter than a naive generic-envelope substitution because S2.5 directly exploits the bounded structure when forming its covariance and variance bounds.

## Corollary S2.8.2 — concentration method modularity

Any method that supplies a valid simultaneous event of the S2.8 form can replace Hoeffding without changing the covariance-composition proof.

Candidate methods include, subject to their own assumptions:

- sub-Gaussian or sub-exponential concentration;
- empirical Bernstein bounds;
- bounded-difference refinements;
- robust mean estimators such as median-of-means under finite-moment assumptions;
- confidence sequences for sequentially monitored moments;
- bootstrap or asymptotic intervals only when their claimed coverage is independently justified for the application.

S2.8 does **not** assert that every method in this list automatically yields valid finite-sample coverage. The statistical procedure must independently establish the stated simultaneous event.

## Corollary S2.8.3 — modular multiplicity correction

Suppose there are `K` predeclared candidate rules. If candidate `k` receives a simultaneous envelope with failure probability at most:

$$
\delta_k,
$$

where:

$$
\sum_{k=1}^K\delta_k\le\delta,
$$

then the S2.8 certificate is simultaneously valid for every candidate with probability at least `1-delta`.

Thus S2.7 extends immediately to any concentration method that can produce candidate-level S2.8 envelopes.

## C — failure boundaries

### Marginal intervals are not enough without joint accounting

Five separately reported `95%` intervals do not automatically form a `95%` simultaneous event. Their joint failure probability must be controlled explicitly.

S2.8 takes the simultaneous event as an assumption precisely to avoid silently multiplying marginal confidence claims.

### Invalid moment intervals invalidate the certificate

If a sub-Gaussian, asymptotic, bootstrap, or robust interval is used outside its assumptions, S2.8 does not rescue its coverage. The theorem composes valid envelopes; it cannot repair invalid input intervals.

### Random interval selection can reintroduce selection bias

Choosing among several interval constructions after viewing the certification data requires the same selection accounting principles as S2.6–S2.7.

### Negative or zero certificate is inconclusive

If:

$$
D_{\mathrm{env}}\le0,
$$

then the envelope does not certify positive covariance. This does not imply that the true covariance is nonpositive.

## U — interpretation boundary

S2.8 modularizes the statistical layer of the adaptive-agent theorem stack. The QBS-specific content is reduced to a deterministic transformation from valid moment envelopes to a covariance lower bound.

This is useful because improvements in statistical methodology can be imported without changing the measure-theoretic QBS results.

The theorem remains interpretation-neutral. A valid sub-Gaussian, robust, or sequential certificate for positive covariance does not establish that the accessibility function is physically correct in Everettian quantum mechanics.

## ERROR CHECK

1. The covariance product bound uses all four corners because `E[Y]` may be negative.
2. Nonnegativity of `S` permits replacing the lower mean bound by `L_S^+=max(0,L_S)`.
3. The variance upper bound uses a lower bound on `E[S]`; using an upper bound there would have the wrong direction.
4. `D_env` is valid only on the stated simultaneous confidence event.
5. Marginal confidence intervals must be combined into a justified simultaneous event.
6. The theorem makes no distributional assumption beyond whatever is required to produce the input confidence envelopes.
7. S2.8 does not claim that bootstrap or asymptotic intervals are finite-sample exact.
8. The FP lower bound uses the upper confidence bound `U_S` on the positive denominator.
9. `D_env<=0` is inconclusive.
10. The Everett bridge remains logically separate.

## Status

**S2.8 GENERIC CONFIDENCE-ENVELOPE CERTIFICATE PROVED. HOEFFDING, SUB-GAUSSIAN, EMPIRICAL-BERNSTEIN, ROBUST, OR SEQUENTIAL METHODS ENTER ONLY THROUGH THEIR INDEPENDENTLY VALID MOMENT ENVELOPES.**
