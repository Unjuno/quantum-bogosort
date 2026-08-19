# Recognition Time as a Stopping-Time Extension

## Motivation

The static recognition variable treats the switch from baseline policy to recognition-dependent policy as already resolved. A sequential model should instead allow recognition to occur when accumulated evidence or internal state first satisfies an activation criterion.

This note formalizes that timing variable without claiming that earlier recognition is always better.

## Filtered process

Let:

```math
(\Omega,\mathcal F,(\mathcal F_t)_{t\ge0},\mu)
```

be a filtered probability space. Let `C_t:\Omega\to\mathbb R` be an adapted recognition-confidence process, meaning that for each `t`, `C_t` is `\mathcal F_t`-measurable.

Fix an activation threshold `kappa`. Define recognition time by:

```math
\tau_{\mathrm{rec}}
=
\inf\{t\ge0:C_t\ge\kappa\}.
```

### Discrete time

In discrete time, adaptedness is sufficient. For each integer `t`:

```math
\{\tau_{\mathrm{rec}}\le t\}
=
\bigcup_{s=0}^{t}\{C_s\ge\kappa\}
\in
\mathcal F_t.
```

Hence `tau_rec` is a stopping time.

### Continuous time

In continuous time, measurability of an uncountable union should not be assumed from adaptedness alone. A standard sufficient setup is that `C` is adapted with continuous sample paths and the filtration satisfies the usual conditions. Then the first hitting time of the closed set `[kappa,\infty)` is a stopping time.

More general progressive/optional measurability hypotheses can also support hitting-time results, but this note does not need their full generality.

## Recognition-dependent policy after the stopping time

Let `pi_0` denote the baseline policy and `pi_1` the recognition-dependent policy. Define the sequential policy by:

```math
\pi_t^{(\tau)}
=
\begin{cases}
\pi_0, & t<\tau_{\mathrm{rec}},\\
\pi_1, & t\ge\tau_{\mathrm{rec}}.
\end{cases}
```

The resulting trajectory utility and accessibility are functions of the stopping rule:

```math
U_{\tau}
=
U(\pi^{(\tau)},\omega),
```

```math
S_{\tau}
=
S(\pi^{(\tau)},\omega).
```

Call a stopping rule **FP-admissible** for this value comparison when:

```math
S_{\tau}\ge0,
\qquad
0<E[S_{\tau}]<\infty,
```

```math
E[|U_{\tau}|]<\infty,
\qquad
E[|U_{\tau}|S_{\tau}]<\infty.
```

The weighted first-person value is then finite and defined by:

```math
V(\tau)
=
\frac{E[U_{\tau}S_{\tau}]}{E[S_{\tau}]}.
```

For each fixed FP-admissible stopping rule, T1 applies and gives:

```math
V(\tau)
=
E[U_{\tau}]
+
\frac{\mathrm{Cov}(U_{\tau},S_{\tau})}{E[S_{\tau}]}.
```

The separate base- and weighted-integrability conditions are both needed: positive finite expected accessibility alone does not make either `E[U_tau]` or `E[U_tau S_tau]` finite.

## Why earlier recognition is not automatically better

There is no general theorem that:

```math
\tau_1<\tau_2
\quad\Longrightarrow\quad
V(\tau_1)\ge V(\tau_2).
```

Earlier activation can have competing consequences:

- more time for an improved policy to alter trajectories;
- more time for a misspecified policy to accumulate costs;
- lower-quality evidence at early times;
- more or less aggressive accessibility weighting;
- altered future information acquisition and state visitation.

A monotone timing theorem therefore requires additional assumptions about policy advantage, information quality, selector behavior, and transition dynamics.

## Historical simulation status

Exploratory recognition-time simulations suggested that earlier activation could produce larger conditional uplift in some toy recursive models while also reducing surviving accessible measure. Those results are retained only as historical archive material until a reconstruction script and explicit timing assumptions are committed.

See:

- `experiments/archive/INDEX.md`
- the historical filenames recorded under recognition timing and recursive filtering.

## v0.2 scope decision

For the historical v0.2 scope:

- the discrete-time stopping-time definition is **FORMALIZED**;
- the continuous-time statement is **CONDITIONAL** on standard path/measurability hypotheses such as adapted continuous sample paths;
- the value functional for an FP-admissible stopping rule is **EXACT BY DEFINITION**;
- the T1 decomposition is **EXACT** under the explicit base/weighted integrability conditions above;
- a universal ordering of early versus late recognition is **NOT CLAIMED**;
- a full timing theorem and reconstructed timing experiment are **DEFERRED** to a later extension.

## Candidate future theorem

A useful future result would identify sufficient conditions under which an earlier stopping rule dominates a later one. Such conditions would likely require a pathwise or conditional advantage of the post-recognition policy, together with controlled selector changes. One possible target is to find assumptions implying:

```math
E[U_{\tau_1}-U_{\tau_2}]\ge0
```

and:

```math
Q(U_{\tau_1},S_{\tau_1})
-
Q(U_{\tau_2},S_{\tau_2})
\ge0,
```

which would imply:

```math
V(\tau_1)\ge V(\tau_2).
```

The point of the future theorem would be to make the assumptions explicit rather than infer timing monotonicity from exploratory simulations.

## ERROR CHECK

1. `C_t` is an `\mathcal F_t`-measurable random variable; it is not itself an element/event of the sigma-algebra.
2. In discrete time, adaptedness gives the stopping-time property through a finite/countable union of threshold events.
3. In continuous time, adaptedness alone is not used as a blanket hitting-time theorem; continuous sample paths plus the usual filtration conditions are one sufficient setup stated here.
4. The stopping-time definition does not itself imply optimality.
5. Earlier recognition is not treated as universally beneficial.
6. Historical timing simulations are not promoted to core evidence.
7. The FP value/decomposition requires nonnegative positive-finite accessibility plus both base and accessibility-weighted utility integrability.
8. Everett interpretation of `S_tau` remains conditional on the separate bridge assumption.

## Status

**DISCRETE-TIME STOPPING-TIME FORMALIZATION COMPLETE; CONTINUOUS-TIME HITTING CLAIM CONDITIONED ON STANDARD PATH/MEASURABILITY HYPOTHESES. FP VALUE/DECOMPOSITION DOMAIN MADE EXPLICIT. GENERAL TIMING ORDERING REMAINS DEFERRED.**
