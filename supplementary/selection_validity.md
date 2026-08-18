# S2.6–S2.7 Selection-Safe Certification

## H — problem

S2.5 certifies positive population outcome/accessibility covariance for a predictor and accessibility rule that are fixed independently of the held-out certification sample.

In practice, a learned agent may be produced by an arbitrary training algorithm, and a researcher may compare several candidate predictors or accessibility rules. The relevant question is whether the finite-sample certificate remains valid after these forms of selection.

The answer separates into two cases:

1. arbitrary training or model construction performed on data independent of the certification sample;
2. finite candidate selection performed on the certification sample itself, with explicit multiplicity correction.

## T — Corollary S2.6: conditional validity after arbitrary independent training

Let `T` denote an arbitrary training random element. Conditional on `T`, suppose a learning procedure outputs a predictor/accessibility rule:

```math
Y_T=f_T(X),
\qquad
S_T=s_T(Y_T),
```

and certification bounds:

```math
|Y_T|\le B_Y(T),
\qquad
0\le S_T\le B_S(T),
\qquad
|U-Y_T|\le B_R(T)
```

for fresh population draws, almost surely.

Let the certification sample:

```math
(U_i,X_i)_{i=1}^n
```

be i.i.d. from the target population and independent of `T`. Evaluate `Y_{T,i}` and `S_{T,i}` on this sample and construct the S2.5 lower certificate:

```math
D_L(T)
```

using confidence level `delta` and the realized training-dependent but certification-sample-independent bounds.

For the population covariance of the trained rule, define:

```math
C(T)
=
\mathrm{Cov}(U,S_T\mid T),
```

where the covariance is over a fresh population draw conditional on the trained rule.

Then:

```math
\boxed{
P\!\left(
C(T)\ge D_L(T)
\mid T
\right)
\ge
1-\delta
}
```

almost surely in `T`.

Consequently, by taking expectations over training randomness:

```math
\boxed{
P\!\left(
C(T)\ge D_L(T)
\right)
\ge
1-\delta
}.
```

Therefore arbitrary optimization, hyperparameter search, representation learning, or policy construction performed entirely before and independently of the certification sample does not invalidate S2.5.

If:

```math
D_L(T)>0,
```

then the trained rule has positive population outcome/accessibility covariance with confidence at least `1-delta` under the stated assumptions.

### Proof

Fix any realized training state `T=t` for which the stated bounds hold. Conditional on `T=t`, the predictor, accessibility map, and bounds are fixed before the independent certification observations are evaluated.

Therefore all assumptions of S2.5 hold conditionally, and:

```math
P\!\left(
C(t)\ge D_L(t)
\mid T=t
\right)
\ge
1-\delta.
```

Since this holds for almost every training realization, the conditional statement follows. The unconditional statement follows from the law of total probability:

```math
P(C(T)\ge D_L(T))
=
E\!\left[
P(C(T)\ge D_L(T)\mid T)
\right]
\ge
1-\delta.
```

No restriction is imposed on the complexity of the training procedure itself beyond independence of the certification sample and validity of the post-training bounds for fresh population draws.

## T — Corollary S2.7: finite candidate selection on the same held-out sample

Now suppose a training stage, independent of the held-out certification sample, produces `K` candidate predictor/accessibility rules:

```math
(Y^{(k)},S^{(k)})
\qquad
k=1,\ldots,K.
```

The candidate set, all rule definitions, and valid population bounds:

```math
B_{Y,k},
\qquad
B_{S,k},
\qquad
B_{R,k}
```

must be fixed before inspecting the certification sample.

For each candidate `k`, construct the S2.5 certificate using per-candidate confidence level:

```math
\delta_k=\frac{\delta}{K}.
```

Equivalently, the Hoeffding radius for candidate `k` is:

```math
\tau_{n,\delta,K}
=
\sqrt{
\frac{\log(10K/\delta)}{2n}
}.
```

Let:

```math
D_{L,k}
```

denote the resulting lower certificate and let:

```math
C_k
=
\mathrm{Cov}(U,S^{(k)})
```

be the corresponding population covariance.

Then:

```math
\boxed{
P\!\left(
C_k\ge D_{L,k}
\text{ for every }k=1,\ldots,K
\right)
\ge
1-\delta
}.
```

Therefore, for **any** data-dependent selection rule:

```math
\widehat k
=\widehat k(\text{held-out sample})
\in\{1,\ldots,K\},
```

including selection of the candidate with the largest observed certificate,

```math
\boxed{
P\!\left(
C_{\widehat k}\ge D_{L,\widehat k}
\right)
\ge
1-\delta
}.
```

Hence an observed selected-candidate result:

```math
D_{L,\widehat k}>0
```

certifies positive population covariance for the selected candidate while preserving family-wise confidence at least `1-delta`.

### Proof

For each fixed candidate `k`, S2.5 at confidence level `delta/K` gives:

```math
P(C_k<D_{L,k})
\le
\frac{\delta}{K}.
```

By the union bound:

```math
P\!\left(
\exists k:\ C_k<D_{L,k}
\right)
\le
\sum_{k=1}^K\frac{\delta}{K}
=
\delta.
```

Thus with probability at least `1-delta`, all `K` lower bounds are simultaneously valid.

On that simultaneous-validity event, whichever candidate is selected from the held-out sample satisfies:

```math
C_{\widehat k}
\ge
D_{L,\widehat k}.
```

The selection rule may depend arbitrarily on the certification observations because simultaneous validity is established before selecting the index.

## Corollary S2.7.1 — unequal confidence allocation

Equal Bonferroni allocation is not required. Let positive weights:

```math
w_1,\ldots,w_K
```

satisfy:

```math
\sum_{k=1}^K w_k\le1.
```

Applying S2.5 to candidate `k` with:

```math
\delta_k=\delta w_k
```

again gives simultaneous family-wise coverage at least `1-delta`.

This permits prior emphasis on preferred candidates while maintaining valid post-selection inference.

## D — what these results add

S2.6 and S2.7 remove two ambiguities from S2.5.

### Arbitrary upstream learning is allowed

A model may be extremely complex and may have been selected through extensive training-time search. If that entire process is independent of the final certification sample, the S2.5 guarantee can be conditioned on the realized trained model.

The theorem therefore does not require a simple learner.

### Same-holdout candidate selection is possible with correction

The held-out sample may be used to choose among a finite predeclared collection of candidates if all candidate-specific certificates are made simultaneously valid. The cost is the expected multiplicity penalty:

```math
\log(10/\delta)
\longrightarrow
\log(10K/\delta)
```

inside the Hoeffding radius for equal allocation.

## C — invalid selection patterns

### Uncorrected best-of-K search

Computing `K` certificates each at nominal confidence `1-delta` and then reporting only the largest positive one does **not** preserve `1-delta` coverage in general.

The family-wise false-certificate probability can increase with `K`.

### Candidate invention after inspecting the certification data

S2.7 assumes a finite candidate family fixed independently of the held-out sample. If new predictor forms, accessibility rules, transformations, clipping bounds, or candidate definitions are invented after inspecting the certification sample, the finite-family guarantee no longer applies automatically.

Such adaptive search requires another independent sample, explicit data reuse accounting, or a more general selective-inference/uniform-convergence argument.

### Random number of candidates

A random `K` is allowed only when the candidate family and allocation rule are determined independently of the certification sample, or when a valid conditional argument is supplied. Choosing how many hypotheses to test in response to held-out outcomes is not covered by the simple statement.

## U — interpretation boundary

S2.6–S2.7 are statistical-validity results. They make the adaptive-agent certificate compatible with realistic training and finite candidate comparison while preserving the separation between:

- learning/training;
- statistical certification;
- the abstract QBS covariance implication;
- the unresolved Everett accessibility bridge.

Passing a selection-safe certificate does not make accessibility physical. It only certifies the relevant population covariance for the selected abstract rule under the declared sampling and boundedness assumptions.

## ERROR CHECK

1. S2.6 conditions on the entire training procedure; the certification observations must remain independent of it.
2. Training-dependent bounds are allowed only when they are fixed before certification and valid for fresh population draws.
3. S2.7 uses family-wise simultaneous coverage, so post-holdout selection among the fixed finite candidates is valid.
4. The equal-allocation radius uses `log(10 K / delta)` because each S2.5 certificate already contains a five-event union bound and receives error budget `delta/K`.
5. Candidate-specific bounds may differ; the equal-allocation formula only simplifies the confidence radius.
6. Failure of a selected certificate remains inconclusive.
7. Uncorrected best-of-K selection is not licensed.
8. Post-hoc creation of new candidates from the certification data is not covered.
9. These results do not relax S2.5 boundedness assumptions.
10. These results do not derive an Everettian accessibility map.

## Status

**S2.6 SAMPLE-SPLIT SELECTION VALIDITY AND S2.7 FINITE-CANDIDATE MULTIPLICITY-CORRECTED SELECTION ARE PROVED UNDER THE STATED INDEPENDENCE, FIXED-FAMILY, AND S2.5 BOUNDEDNESS ASSUMPTIONS.**
