# Theorems 4–5

## Theorem 4 — Recognition Decomposition

Let recognition status take two values, with recognition allowed to change policy, trajectory utility, and accessibility:

$$
R
\longrightarrow
\pi_R
\longrightarrow
(U_R,S_R).
$$

Define the first-person value under recognition state `R` by:

$$
V_R
=
\frac{E[U_RS_R]}{E[S_R]}.
$$

Define the QBS conditioning contribution:

$$
Q(U,S)
=
\frac{\operatorname{Cov}(U,S)}{E[S]}.
$$

Then:

$$
V_1-V_0
=
E[U_1-U_0]
+
Q(U_1,S_1)-Q(U_0,S_0).
$$

### Proof

By Theorem 1, each recognition state satisfies:

$$
V_R
=
E[U_R]
+
Q(U_R,S_R).
$$

Subtracting the recognition-off expression from the recognition-on expression gives:

$$
V_1-V_0
=
(E[U_1]-E[U_0])
+
(Q(U_1,S_1)-Q(U_0,S_0)).
$$

This is the stated decomposition.

### Corollary 4.1 — No pre-recognition selector

If recognition-off uses no special QBS accessibility weighting:

$$
S_0\equiv 1,
$$

then:

$$
Q(U_0,S_0)=0,
$$

and therefore:

$$
V_1-V_0
=
E[U_1-U_0]
+
\frac{\operatorname{Cov}(U_1,S_1)}{E[S_1]}.
$$

The first term is the ordinary causal policy/trajectory effect. The second term is the first-person conditioning contribution.

### Corollary 4.2 — Recognition-label null

If recognition changes neither trajectories nor accessibility:

$$
U_1=U_0,
$$

and:

$$
S_1=S_0,
$$

almost surely, then:

$$
V_1-V_0=0.
$$

Recognition has no effect merely by being a label; it must alter the policy/trajectory map, the accessibility map, or both.

---

## Theorem 5 — Policy–QBS Interaction Decomposition

Define the ordinary policy increment:

$$
D
=
U_1-U_0.
$$

Define the change in the QBS conditioning contribution:

$$
I
=
Q(U_1,S_1)-Q(U_0,S_0).
$$

Then:

$$
I
=
\frac{\operatorname{Cov}(D,S_0)}{E[S_0]}
+
\left[
Q(U_1,S_1)-Q(U_1,S_0)
\right].
$$

### Proof

Add and subtract the intermediate term:

$$
Q(U_1,S_0).
$$

This gives:

$$
I
=
[Q(U_1,S_0)-Q(U_0,S_0)]
+
[Q(U_1,S_1)-Q(U_1,S_0)].
$$

Using:

$$
U_1=U_0+D,
$$

and linearity of covariance in its first argument:

$$
Q(U_1,S_0)-Q(U_0,S_0)
=
\frac{\operatorname{Cov}(D,S_0)}{E[S_0]}.
$$

Substitution proves the result.

### Interpretation

The first term is the **targeting term**:

$$
I_{\mathrm{target}}
=
\frac{\operatorname{Cov}(D,S_0)}{E[S_0]}.
$$

It measures whether ordinary policy improvement is concentrated in branches that the baseline selector would upweight or downweight.

The second term is the **selector-map-shift term**:

$$
I_{\mathrm{map}}
=
Q(U_1,S_1)-Q(U_1,S_0).
$$

It captures the fact that changed trajectories or beliefs can alter the accessibility map itself.

Hence:

$$
I
=
I_{\mathrm{target}}
+
I_{\mathrm{map}}.
$$

### Fixed-selector corollary

If the selector does not change under the policy intervention:

$$
S_1=S_0=S,
$$

then:

$$
I
=
\frac{\operatorname{Cov}(D,S)}{E[S]}.
$$

Therefore:

$$
\operatorname{sign}(I)
=
\operatorname{sign}(\operatorname{Cov}(D,S)).
$$

---

## Corollary 5.1 — Adaptive Rescue Gives Nonpositive Interaction

Let `B` represent branch badness. Suppose policy improvement is nondecreasing in badness:

$$
D=d(B),
$$

while accessibility is nonincreasing in badness:

$$
S=s(B).
$$

Then:

$$
\operatorname{Cov}(D,S)
\le
0.
$$

Under a fixed selector:

$$
I\le0.
$$

### Proof

Let `B'` be an independent copy of `B`. Then:

$$
2\operatorname{Cov}(d(B),s(B))
=
E[(d(B)-d(B'))(s(B)-s(B'))].
$$

Because the two functions have opposite monotonicity, the product inside the expectation is nonpositive almost surely. Therefore the covariance is nonpositive.

### Strict condition

If both functions vary nontrivially and there is positive probability of ordered pairs for which improvement strictly rises while accessibility strictly falls, then:

$$
\operatorname{Cov}(D,S)<0,
$$

and therefore:

$$
I<0.
$$

A negative interaction does not imply that either the ordinary policy effect or the QBS contribution is negative. Both can be positive while partially substituting for each other by targeting overlapping low-value branches.
