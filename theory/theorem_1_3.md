# Theorems 1–3

## Theorem 1 — QBS Covariance Identity

Let `X` be an integrable outcome, and let `S` be a nonnegative accessibility weight satisfying positive finite expectation. Define:

$$
E_{FP}[X]
=
\frac{E[XS]}{E[S]}.
$$

Then:

$$
E_{FP}[X]-E[X]
=
\frac{\mathrm{Cov}(X,S)}{E[S]}.
$$

### Proof

By definition:

$$
E_{FP}[X]
=
\frac{E[XS]}{E[S]}.
$$

Using:

$$
E[XS]
=
E[X]E[S]
+
\mathrm{Cov}(X,S),
$$

we get:

$$
E_{FP}[X]
=
E[X]
+
\frac{\mathrm{Cov}(X,S)}{E[S]}.
$$

Subtracting the base expectation proves the identity.

### Exact sign criterion

Because the denominator is positive:

$$
E_{FP}[X]>E[X]
\iff
\mathrm{Cov}(X,S)>0.
$$

Equality holds exactly when:

$$
\mathrm{Cov}(X,S)=0.
$$

In particular, outcome-independent accessibility implies zero mean uplift in expectation.

---

## Theorem 2 — Tail Probability Identity

For any threshold `c`:

$$
P_{FP}(X\ge c)-P(X\ge c)
=
\frac{
\mathrm{Cov}(\mathbf 1_{\{X\ge c\}},S)
}{E[S]}.
$$

### Proof

Apply Theorem 1 to the indicator outcome:

$$
Z
=
\mathbf 1_{\{X\ge c\}}.
$$

Then:

$$
E[Z]
=
P(X\ge c),
$$

and:

$$
E_{FP}[Z]
=
P_{FP}(X\ge c).
$$

Theorem 1 immediately gives the result.

### Exact tail criterion

$$
P_{FP}(X\ge c)>P(X\ge c)
\iff
\mathrm{Cov}(\mathbf 1_{\{X\ge c\}},S)>0.
$$

---

## Theorem 3 — Monotone Accessibility Implies FOSD

Define the conditional mean accessibility profile:

$$
g(x)
=
E[S\mid X=x].
$$

Assume this profile is nondecreasing on the support of the outcome variable. Then the first-person distribution first-order stochastically dominates the base distribution:

$$
F_{FP}(c)
\le
F(c)
\qquad
\text{for every }c.
$$

Equivalently:

$$
X_{FP}
\succeq_{\mathrm{FOSD}}
X.
$$

### Proof

For fixed threshold `c`, define:

$$
f_c(x)
=
\mathbf 1_{\{x\le c\}}.
$$

By Theorem 1:

$$
F_{FP}(c)-F(c)
=
\frac{
\mathrm{Cov}(f_c(X),S)
}{E[S]}.
$$

Because `f_c(X)` is measurable with respect to `X`:

$$
\mathrm{Cov}(f_c(X),S)
=
\mathrm{Cov}(f_c(X),E[S\mid X])
=
\mathrm{Cov}(f_c(X),g(X)).
$$

Let `X'` be an independent copy of `X`. For integrable functions `a` and `b`:

$$
2\mathrm{Cov}(a(X),b(X))
=
E[(a(X)-a(X'))(b(X)-b(X'))].
$$

Here `f_c` is nonincreasing while `g` is nondecreasing, so:

$$
(f_c(X)-f_c(X'))(g(X)-g(X'))
\le
0
$$

almost surely. Therefore:

$$
\mathrm{Cov}(f_c(X),g(X))
\le
0.
$$

Since the accessibility expectation is positive:

$$
F_{FP}(c)-F(c)
\le
0.
$$

Thus:

$$
F_{FP}(c)
\le
F(c)
$$

for all thresholds.

### Equality and strictness

At a fixed threshold, equality holds exactly when:

$$
\mathrm{Cov}(\mathbf 1_{\{X\le c\}},g(X))
=
0.
$$

A sufficient condition for equality at every threshold is that the conditional accessibility profile is almost surely constant.

Strict dominance at threshold `c` follows when there is positive probability of two independent draws satisfying both:

$$
X\le c<X',
$$

and:

$$
g(X)<g(X').
$$

### Important limitation

Positive Pearson correlation by itself does not imply FOSD. A nonmonotone accessibility profile can have positive outcome-accessibility correlation while the first-person and base CDFs cross. The nonmonotone counterexample is included in E1.
