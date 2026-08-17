# Quantum Bogosort — Core Theorem Set v0.1

## 0. Setup

Let \((\Omega,\mathcal F,\mu)\) be a probability space.  
For a policy \(\pi\), let:

- \(U_\pi:\Omega\to\mathbb R\) be the trajectory utility/outcome;
- \(S_\pi:\Omega\to[0,\infty)\) be the observer-indexed accessibility weight.

Assume

\[
0<E_\mu[S_\pi]<\infty,\qquad E_\mu[|U_\pi|S_\pi]<\infty.
\]

Define the first-person (FP) measure by

\[
\mu^{FP}_\pi(A)
=
\frac{E_\mu[\mathbf 1_A S_\pi]}{E_\mu[S_\pi]},
\qquad A\in\mathcal F.
\]

For any integrable outcome \(X\), define

\[
E_{FP}[X]
=
\frac{E_\mu[XS]}{E_\mu[S]}.
\]

Throughout, the mathematical results are measure-theoretic statements.  
Any Everett interpretation requires a separate bridge assumption identifying \(S_\pi\) with an observer-indexed accessibility/weighting rule.

---

## Theorem 1 — QBS Covariance Identity

Let \(X\) satisfy \(E[|X|S]<\infty\), with \(S\ge0\) and \(0<E[S]<\infty\). Then

\[
\boxed{
E_{FP}[X]-E[X]
=
\frac{\operatorname{Cov}(X,S)}{E[S]}.
}
\]

### Proof

By definition,

\[
E_{FP}[X]=\frac{E[XS]}{E[S]}.
\]

Using

\[
E[XS]=E[X]E[S]+\operatorname{Cov}(X,S),
\]

we obtain

\[
E_{FP}[X]
=
E[X]
+
\frac{\operatorname{Cov}(X,S)}{E[S]}.
\]

Subtracting \(E[X]\) proves the identity. \(\square\)

### Exact sign criterion

Because \(E[S]>0\),

\[
E_{FP}[X]>E[X]
\iff
\operatorname{Cov}(X,S)>0,
\]

with equality iff \(\operatorname{Cov}(X,S)=0\).

### Null implication

If \(X\) and \(S\) are independent, then \(\operatorname{Cov}(X,S)=0\), hence

\[
E_{FP}[X]=E[X].
\]

---

## Theorem 2 — Tail Probability Identity

For any threshold \(c\in\mathbb R\),

\[
\boxed{
P_{FP}(X\ge c)-P(X\ge c)
=
\frac{
\operatorname{Cov}(\mathbf 1_{\{X\ge c\}},S)
}{
E[S]
}.
}
\]

### Proof

Apply Theorem 1 to the bounded random variable

\[
Z=\mathbf 1_{\{X\ge c\}}.
\]

Then \(E[Z]=P(X\ge c)\) and \(E_{FP}[Z]=P_{FP}(X\ge c)\). \(\square\)

### Exact tail criterion

\[
P_{FP}(X\ge c)>P(X\ge c)
\iff
\operatorname{Cov}(\mathbf 1_{\{X\ge c\}},S)>0.
\]

---

## Theorem 3 — Monotone Accessibility Implies First-Order Stochastic Dominance

Define

\[
g(x)=E[S\mid X=x]
\]

using any version of the conditional expectation as a measurable function of \(X\).

Assume \(g\) is nondecreasing on the support of \(X\). Then

\[
\boxed{
F_{FP}(c)\le F(c)
\quad\text{for every }c\in\mathbb R,
}
\]

where

\[
F(c)=P(X\le c),
\qquad
F_{FP}(c)=P_{FP}(X\le c).
\]

Equivalently,

\[
\boxed{
X_{FP}\succeq_{\mathrm{FOSD}} X.
}
\]

### Proof

For fixed \(c\), let

\[
f_c(x)=\mathbf 1_{\{x\le c\}}.
\]

By Theorem 1,

\[
F_{FP}(c)-F(c)
=
\frac{\operatorname{Cov}(f_c(X),S)}{E[S]}.
\]

Since \(f_c(X)\) is \(\sigma(X)\)-measurable,

\[
\operatorname{Cov}(f_c(X),S)
=
\operatorname{Cov}(f_c(X),E[S\mid X])
=
\operatorname{Cov}(f_c(X),g(X)).
\]

Let \(X'\) be an independent copy of \(X\). The covariance identity

\[
2\operatorname{Cov}(a(X),b(X))
=
E[(a(X)-a(X'))(b(X)-b(X'))]
\]

holds for integrable \(a(X),b(X)\).

Here \(f_c\) is nonincreasing and \(g\) is nondecreasing. Therefore

\[
(f_c(X)-f_c(X'))(g(X)-g(X'))\le0
\]

almost surely. Hence

\[
\operatorname{Cov}(f_c(X),g(X))\le0.
\]

Since \(E[S]>0\),

\[
F_{FP}(c)-F(c)\le0.
\]

Thus \(F_{FP}(c)\le F(c)\) for every \(c\). \(\square\)

### Equality condition

At a given threshold \(c\),

\[
F_{FP}(c)=F(c)
\iff
\operatorname{Cov}(\mathbf 1_{\{X\le c\}},g(X))=0.
\]

A sufficient condition for equality at every threshold is that \(g(X)\) is almost surely constant.

### Strict condition

For a fixed \(c\), strict dominance

\[
F_{FP}(c)<F(c)
\]

holds whenever there is positive probability of two independent draws \(X,X'\) satisfying

\[
X\le c<X'
\quad\text{and}\quad
g(X)<g(X').
\]

Thus a nonconstant increasing accessibility profile gives strict improvement at thresholds that separate regions on which accessibility differs.

### Important limitation

Positive Pearson correlation alone does **not** imply FOSD.  
A nonmonotone \(g(x)\) can have \(\operatorname{Corr}(X,S)>0\) while the FP and base CDFs cross.

---

## Theorem 4 — Recognition Decomposition

Let recognition status be \(R\in\{0,1\}\). Recognition may change policy, trajectory utility, and accessibility:

\[
R
\longrightarrow
\pi_R
\longrightarrow
(U_R,S_R).
\]

Define

\[
V_R
=
\frac{E[U_RS_R]}{E[S_R]},
\]

and

\[
Q(U,S)
=
\frac{\operatorname{Cov}(U,S)}{E[S]}.
\]

Then

\[
\boxed{
V_1-V_0
=
E[U_1-U_0]
+
Q(U_1,S_1)-Q(U_0,S_0).
}
\]

### Proof

By Theorem 1,

\[
V_R=E[U_R]+Q(U_R,S_R).
\]

Therefore

\[
V_1-V_0
=
(E[U_1]-E[U_0])
+
(Q(U_1,S_1)-Q(U_0,S_0)).
\]

This is the stated decomposition. \(\square\)

### Corollary 4.1 — No pre-recognition selector

If

\[
S_0\equiv1,
\]

then \(Q(U_0,S_0)=0\), so

\[
\boxed{
V_1-V_0
=
E[U_1-U_0]
+
\frac{\operatorname{Cov}(U_1,S_1)}{E[S_1]}.
}
\]

The first term is the causal trajectory/policy effect.  
The second term is the QBS first-person conditioning effect.

### Corollary 4.2 — Recognition-label null

If recognition changes neither trajectory nor accessibility,

\[
U_1=U_0,\qquad S_1=S_0
\]

almost surely, then

\[
\boxed{V_1-V_0=0.}
\]

Thus the label "recognition" has no effect unless it changes policy/trajectory, accessibility, or both.

---

## Theorem 5 — Policy–QBS Interaction Decomposition

Let

\[
D=U_1-U_0.
\]

Define the change in the QBS contribution by

\[
I
=
Q(U_1,S_1)-Q(U_0,S_0).
\]

Then

\[
\boxed{
I
=
\frac{\operatorname{Cov}(D,S_0)}{E[S_0]}
+
\left[
Q(U_1,S_1)-Q(U_1,S_0)
\right].
}
\]

### Proof

Add and subtract \(Q(U_1,S_0)\):

\[
I
=
[Q(U_1,S_0)-Q(U_0,S_0)]
+
[Q(U_1,S_1)-Q(U_1,S_0)].
\]

Since \(U_1=U_0+D\),

\[
Q(U_1,S_0)-Q(U_0,S_0)
=
\frac{
\operatorname{Cov}(U_0+D,S_0)-\operatorname{Cov}(U_0,S_0)
}{
E[S_0]
}
=
\frac{\operatorname{Cov}(D,S_0)}{E[S_0]}.
\]

Substitution proves the identity. \(\square\)

### Fixed-selector corollary

If

\[
S_1=S_0=S,
\]

then the selector-map term vanishes:

\[
\boxed{
I
=
\frac{\operatorname{Cov}(D,S)}{E[S]}.
}
\]

Hence

\[
\operatorname{sign}(I)
=
\operatorname{sign}(\operatorname{Cov}(D,S)).
\]

---

## Corollary 5.1 — Adaptive Rescue Gives Nonpositive Interaction

Let \(B\) denote branch badness. Suppose

\[
D=d(B)
\]

with \(d\) nondecreasing, while

\[
S=s(B)
\]

with \(s\) nonincreasing.

Then

\[
\boxed{
\operatorname{Cov}(D,S)\le0,
}
\]

and under a fixed selector,

\[
\boxed{I\le0.}
\]

### Proof

Let \(B'\) be an independent copy of \(B\). Then

\[
2\operatorname{Cov}(d(B),s(B))
=
E[(d(B)-d(B'))(s(B)-s(B'))].
\]

Because \(d\) and \(s\) have opposite monotonicity, the product in the expectation is nonpositive almost surely. Therefore the covariance is nonpositive. \(\square\)

### Strict condition

If \(d(B)\) and \(s(B)\) are both nonconstant on a set of positive probability and there is positive probability of \(B<B'\) for which

\[
d(B)<d(B'),
\qquad
s(B)>s(B'),
\]

then

\[
\operatorname{Cov}(D,S)<0,
\]

so \(I<0\).

This does **not** mean that the ordinary policy effect or the QBS effect is negative. Both can be positive while the interaction is negative because they partially target the same low-value branches.

---

## Proposition 1 — Costless Recognition Has Nonnegative Option Value

Let \(\Pi_0\) be the feasible policy set before recognition and \(\Pi_1\) the feasible policy set after recognition. If knowledge can be ignored, so that

\[
\Pi_0\subseteq\Pi_1,
\]

and both are evaluated by the same value functional \(V\), then

\[
\boxed{
\sup_{\pi\in\Pi_1}V(\pi)
\ge
\sup_{\pi\in\Pi_0}V(\pi).
}
\]

### Proof

The supremum over a superset cannot be smaller than the supremum over a subset. \(\square\)

This proposition concerns the value of having an additional option. It does not imply that every newly available policy is optimal.

---

## Proposition 2 — Support Cannot Be Created by Pure Reweighting

For a fixed policy \(\pi\), the FP measure is absolutely continuous with respect to the base measure:

\[
\mu^{FP}_\pi\ll\mu.
\]

Therefore if an event \(A\) has

\[
\mu(A)=0,
\]

then

\[
\mu^{FP}_\pi(A)=0.
\]

Thus pure QBS reweighting cannot create outcomes outside the support of the base branch space for that fixed policy.

However, recognition may change the policy \(\pi\), and therefore may change the trajectory map \(U_\pi\) and its induced support. Policy effects and conditioning effects must therefore be distinguished.

---

## Boundary Condition — Extinction / Zero Accessible Measure

The FP measure requires

\[
E[S]>0.
\]

If

\[
E[S]=0,
\]

then

\[
\mu^{FP}(A)
=
\frac{E[\mathbf1_A S]}{E[S]}
\]

is undefined.

This is not a low-value FP state; it is a failure of the normalized FP measure to exist.

If \(E[S]\to0^+\), normalized quantities may remain finite while effective support and Monte Carlo effective sample size collapse. This is an important numerical and interpretive boundary.

---

# Counterexamples / Stress Tests

## C1 — Independence null

If

\[
S\perp X,
\]

then

\[
\operatorname{Cov}(X,S)=0
\]

and all mean uplift vanishes in expectation. Likewise, for every threshold \(c\),

\[
\operatorname{Cov}(\mathbf1_{\{X\ge c\}},S)=0.
\]

This falsifies any claim that accessibility weighting alone, without alignment to outcomes, necessarily improves FP outcomes.

## C2 — Nonmonotone accessibility can break FOSD

Let \(X\sim N(0,1)\), and choose an accessibility rule that favors intermediate outcomes, e.g.

\[
S(x)=a+b\exp[-(x/\sigma)^2].
\]

Then \(E[S\mid X=x]=S(x)\) is nonmonotone. The FP CDF may cross the base CDF, so neither distribution first-order stochastically dominates the other.

Positive mean uplift also does not by itself imply FOSD; an oscillatory nonmonotone \(S(x)\) can produce

\[
E_{FP}[X]>E[X]
\]

while the CDFs cross.

## C3 — Recognition-label null

If

\[
U_1=U_0
\quad\text{and}\quad
S_1=S_0,
\]

then recognition has exactly zero effect:

\[
V_1-V_0=0.
\]

Recognition matters only through a change in the branch-wise policy/trajectory map, the accessibility map, or both.

---

# Everett-QBS Bridge Assumption

The preceding results are mathematical statements about weighted conditional measures.

To interpret them physically in an Everett framework, introduce the separate hypothesis:

> **Everett-QBS Bridge Assumption.**  
> Observer-indexed first-person accessibility under policy \(\pi\) is represented by a nonnegative branch weight \(S_\pi(\omega)\), and self-location is described by
>
> \[
> d\mu^{FP}_\pi(\omega)
> =
> \frac{S_\pi(\omega)}{E_\mu[S_\pi]}
> d\mu(\omega).
> \]

If this bridge assumption is accepted, Theorems 1–5 apply to the corresponding Everett branch model. Rejecting the bridge assumption does not invalidate the measure-theoretic theorems or the classical agent simulations.

---

# Error Check / Logical Boundaries

1. Mean uplift requires positive covariance; it does not follow from "selection" alone.
2. FOSD requires a stronger monotone-accessibility condition; positive correlation alone is insufficient.
3. Recognition has no effect unless it changes \(U\), \(S\), or both.
4. Policy effects can change the trajectory support; pure reweighting cannot.
5. A negative policy–QBS interaction does not imply either component has negative value.
6. \(E[S]=0\) makes the normalized FP measure undefined.
7. The Everett physical interpretation is a bridge assumption, not a consequence of the probability identities.
