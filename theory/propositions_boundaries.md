# Propositions, Boundaries, and Counterexamples

## Proposition 1 — Costless Recognition Has Nonnegative Option Value

Let the feasible policy set before recognition be `Pi_0` and after recognition be `Pi_1`. If knowledge can be ignored, so that:

```math
\Pi_0\subseteq\Pi_1,
```

and both sets are evaluated by the same value functional, then:

```math
\sup_{\pi\in\Pi_1}V(\pi)
\ge
\sup_{\pi\in\Pi_0}V(\pi).
```

The result follows because the supremum over a superset cannot be smaller than the supremum over a subset. This is an option-value statement and does not imply that every newly available policy is optimal.

---

## Proposition 2 — Pure Reweighting Cannot Create Support

For a fixed policy, the first-person measure is absolutely continuous with respect to the base measure:

```math
\mu^{FP}_\pi
\ll
\mu.
```

Therefore:

```math
\mu(A)=0
\Longrightarrow
\mu^{FP}_\pi(A)=0.
```

Pure accessibility reweighting cannot create outcomes that were absent from the support of the fixed-policy base measure. Recognition can still alter support indirectly by changing the policy and therefore changing the trajectory map.

---

## Boundary — Zero Accessible Measure

The normalized first-person measure requires:

```math
E[S]>0.
```

If:

```math
E[S]=0,
```

then the normalized first-person measure is undefined. This is a normalization failure, not merely a low-value first-person state.

As expected accessibility approaches zero, normalized statistics may remain finite while effective support and Monte Carlo effective sample size collapse. This is a numerical and interpretive boundary.

---

## Counterexample C1 — Independence Null

If accessibility is independent of the outcome:

```math
S\perp X,
```

then:

```math
\mathrm{Cov}(X,S)=0,
```

and therefore:

```math
E_{FP}[X]=E[X].
```

Likewise, for every tail threshold:

```math
\mathrm{Cov}(\mathbf 1_{\{X\ge c\}},S)=0.
```

Thus selection alone does not imply improved first-person outcomes; alignment to outcomes is required.

---

## Counterexample C2 — Nonmonotone Accessibility Can Break FOSD

A nonmonotone accessibility rule can favor intermediate or oscillating outcome regions. For example:

```math
S(x)
=
a+b\exp[-(x/\sigma)^2].
```

The resulting first-person and base CDFs can cross. Positive mean uplift is therefore weaker than first-order stochastic dominance, and positive Pearson correlation is not sufficient for FOSD.

---

## Counterexample C3 — Recognition-Label Null

If recognition changes neither trajectory utility nor accessibility:

```math
U_1=U_0,
```

and:

```math
S_1=S_0,
```

then:

```math
V_1-V_0=0.
```

Recognition matters only through a change in policy/trajectory, accessibility, or both.

---

## Everett-QBS Bridge Assumption

The preceding results are mathematical statements about weighted conditional measures. A physical Everett interpretation requires the additional hypothesis that observer-indexed first-person accessibility under policy `pi` can be represented by a nonnegative branch weight and normalized as:

```math
d\mu^{FP}_\pi(\omega)
=
\frac{S_\pi(\omega)}{E_\mu[S_\pi]}
\,d\mu(\omega).
```

If this bridge assumption is accepted, the theorem set applies to the corresponding Everett branch model. Rejecting the bridge assumption does not invalidate the measure-theoretic identities or the classical agent simulations.

---

## Logical boundaries

1. Mean uplift requires positive outcome-accessibility covariance; it does not follow from selection alone.
2. FOSD requires a stronger monotone-accessibility condition; positive correlation alone is insufficient.
3. Recognition has no effect unless it changes trajectory utility, accessibility, or both.
4. Policy changes can alter trajectory support; pure reweighting cannot.
5. Negative policy–QBS interaction does not imply either component has negative value.
6. Zero expected accessibility makes the normalized first-person measure undefined.
7. Everett interpretation is a bridge assumption, not a consequence of the probability identities.
