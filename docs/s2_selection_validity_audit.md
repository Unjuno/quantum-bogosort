# S2.6–S2.7 Selection-Validity Audit

**Date:** 2026-08-17  
**Status:** post-v0.2 stacked theorem candidate

## H — target

S2.5 is a fixed-rule held-out certificate. The extension must answer two common reuse questions without weakening nominal coverage:

1. may the predictor/accessibility rule be produced by arbitrary training before the hold-out sample is evaluated?
2. may the same hold-out sample be used to choose among several predeclared candidate rules?

## T — S2.6 conditional-on-training validity

Let `T` denote the entire random training history. For a fresh population draw, the trained rule defines:

```math
Y_T=f_T(X),
\qquad
S_T=s_T(Y_T).
```

The final certification sample is independent of `T`.

Conditional on `T=t`, the rule and its valid population bounds are fixed, so S2.5 gives:

```math
P\!\left(
C(t)\ge D_L(t)
\mid T=t
\right)
\ge1-\delta,
```

where:

```math
C(t)=\mathrm{Cov}(U,S_t).
```

Therefore:

```math
P\!\left(
C(T)\ge D_L(T)
\right)
=
E\!\left[
P(C(T)\ge D_L(T)\mid T)
\right]
\ge1-\delta.
```

**Audit:** PASS.

### Important interpretation

The target covariance is the population covariance of the **random trained rule**. The theorem does not claim that all possible training outcomes share one deterministic covariance value. It says that after arbitrary independent training, the certificate covers the covariance associated with the realized trained rule.

**Audit:** PASS.

## T — S2.7 finite candidate simultaneous validity

Suppose `K` candidate rules are fixed before the certification sample is inspected. Apply S2.5 to each candidate with:

```math
\delta_k=\frac{\delta}{K}.
```

For each candidate:

```math
P(C_k<D_{L,k})
\le
\frac{\delta}{K}.
```

The union bound gives:

```math
P\!\left(
\exists k:\ C_k<D_{L,k}
\right)
\le
\delta.
```

Hence:

```math
P\!\left(
C_k\ge D_{L,k}
\text{ for all }k
\right)
\ge1-\delta.
```

**Audit:** PASS.

## T — post-selection validity on the same hold-out sample

Let the selected index be any measurable function of the certification data:

```math
\widehat k
=\widehat k(\text{hold-out sample}).
```

On the simultaneous-validity event:

```math
C_k\ge D_{L,k}
```

for every candidate, so in particular:

```math
C_{\widehat k}
\ge
D_{L,\widehat k}.
```

No independence between `widehat k` and the certification sample is required after simultaneous coverage has been established.

**Audit:** PASS.

## D — multiplicity constant

S2.5 uses:

```math
\tau_{n,\delta}
=
\sqrt{\frac{\log(10/\delta)}{2n}}
```

because each candidate certificate internally uses five simultaneous two-sided Hoeffding events.

Replacing the per-candidate error probability by:

```math
\frac{\delta}{K}
```

gives:

```math
\tau_{n,\delta,K}
=
\sqrt{\frac{\log(10K/\delta)}{2n}}.
```

**Audit:** PASS.

## D — unequal allocation

For positive weights satisfying:

```math
\sum_{k=1}^K w_k\le1,
```

using:

```math
\delta_k=\delta w_k
```

gives:

```math
\sum_{k=1}^K\delta_k\le\delta.
```

The same union-bound proof gives family-wise coverage at least `1-delta`.

**Audit:** PASS.

## C — invalid patterns

### Uncorrected best-of-K

If every candidate is evaluated at nominal error level `delta` and the largest positive certificate is selected, the family-wise failure probability may exceed `delta`.

**Audit:** correctly excluded.

### Post-hoc candidate construction

If candidate definitions, accessibility maps, transformations, or clipping bounds are created after examining the certification observations, the finite predeclared-family proof no longer applies.

**Audit:** correctly excluded.

### Training-dependent bounds

S2.6 permits bounds depending on the training state only if they are fixed before certification and are genuinely valid for fresh draws under the realized trained rule.

Data-dependent bounds estimated from the certification sample require their own concentration argument.

**Audit:** correctly restricted.

### Random K

A random number of candidates is safe under the stated conditional argument only if the candidate family and confidence-allocation rule are determined independently of the final certification sample. Choosing `K` in response to certificate outcomes is not covered by the simple theorem.

**Audit:** correctly restricted.

## U — relation to adaptive agents

S2.6 closes a practical gap between learning and certification:

```math
\text{arbitrary independent training}
\longrightarrow
\text{fixed realized rule}
\longrightarrow
\text{valid S2.5 certificate}.
```

S2.7 adds:

```math
\text{finite predeclared candidate family}
\longrightarrow
\text{simultaneous certificate family}
\longrightarrow
\text{valid same-holdout candidate selection}.
```

These are statistical selection results. They do not show that the selected rule has a physical Everettian accessibility interpretation.

## ERROR CHECK

1. S2.6 conditions on the entire training random element, not merely a chosen hyperparameter.
2. The certification sample must remain independent of training for the simple conditional proof.
3. The theorem targets the covariance of the realized trained rule, which may itself depend on training randomness.
4. S2.7 relies on simultaneous family-wise validity before selecting the candidate index.
5. Same-holdout selection is valid only within the finite family whose certificates were multiplicity-corrected.
6. The factor `K` enters through the outer candidate union bound, while the factor `10` remains from the five two-sided S2.5 moment bounds.
7. Bonferroni is sufficient and conservative; no claim of optimality is made.
8. Post-hoc candidate invention and uncorrected best-of-K selection are excluded.
9. Failure to certify remains inconclusive.
10. The results remain abstract statistical statements and do not derive the Everett bridge.

## Audit conclusion

**S2.6 AND S2.7 ARE MATHEMATICALLY SOUND UNDER THE STATED INDEPENDENT-CERTIFICATION, VALID-BOUND, FIXED-FAMILY, AND MULTIPLICITY-ACCOUNTING ASSUMPTIONS.**
