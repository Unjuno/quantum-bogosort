# Recognition Time as a Stopping-Time Extension

## Motivation

The static recognition variable treats the switch from baseline policy to recognition-dependent policy as already resolved. A sequential model should instead allow recognition to occur when accumulated evidence or internal state first satisfies an activation criterion.

This note formalizes that timing variable without claiming that earlier recognition is always better.

## Filtered process

Let:

$$
(\Omega,\mathcal F,(\mathcal F_t)_{t\ge0},\mu)
$$

be a filtered probability space. Let `C_t` be an adapted recognition-confidence process:

$$
C_t
\in
\mathcal F_t.
$$

Fix an activation threshold `kappa`. Define recognition time by:

$$
\tau_{\mathrm{rec}}
=
\inf\{t\ge0:C_t\ge\kappa\}.
$$

If for each `t` the event:

$$
\{C_t\ge\kappa\}
$$

is measurable with respect to:

$$
\mathcal F_t,
$$

then `tau_rec` is a stopping time because:

$$
\{\tau_{\mathrm{rec}}\le t\}
=
\bigcup_{s\le t}\{C_s\ge\kappa\}
\in
\mathcal F_t
$$

in discrete time, with the usual right-continuity/measurability qualifications in continuous time.

## Recognition-dependent policy after the stopping time

Let `pi_0` denote the baseline policy and `pi_1` the recognition-dependent policy. Define the sequential policy by:

$$
\pi_t^{(\tau)}
=
\begin{cases}
\pi_0, & t<\tau_{\mathrm{rec}},\\
\pi_1, & t\ge\tau_{\mathrm{rec}}.
\end{cases}
$$

The resulting trajectory utility and accessibility are functions of the stopping rule:

$$
U_{\tau}
=
U(\pi^{(\tau)},\omega),
$$

$$
S_{\tau}
=
S(\pi^{(\tau)},\omega).
$$

The first-person value of a recognition-time rule is therefore:

$$
V(\tau)
=
\frac{E[U_{\tau}S_{\tau}]}{E[S_{\tau}]},
$$

whenever:

$$
0<E[S_{\tau}]<\infty.
$$

The covariance decomposition applies to each fixed admissible stopping rule:

$$
V(\tau)
=
E[U_{\tau}]
+
\frac{\operatorname{Cov}(U_{\tau},S_{\tau})}{E[S_{\tau}]}.
$$

## Why earlier recognition is not automatically better

There is no general theorem that:

$$
\tau_1<\tau_2
\quad\Longrightarrow\quad
V(\tau_1)\ge V(\tau_2).
$$

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

For v0.2:

- the stopping-time definition is **FORMALIZED**;
- the value functional for a stopping rule is **EXACT BY DEFINITION**;
- a universal ordering of early versus late recognition is **NOT CLAIMED**;
- a full timing theorem and reconstructed timing experiment are **DEFERRED** to a later extension.

## Candidate future theorem

A useful future result would identify sufficient conditions under which an earlier stopping rule dominates a later one. Such conditions would likely require a pathwise or conditional advantage of the post-recognition policy, together with controlled selector changes. One possible target is to find assumptions implying:

$$
E[U_{\tau_1}-U_{\tau_2}]\ge0
$$

and:

$$
Q(U_{\tau_1},S_{\tau_1})
-
Q(U_{\tau_2},S_{\tau_2})
\ge0,
$$

which would imply:

$$
V(\tau_1)\ge V(\tau_2).
$$

The point of the future theorem would be to make the assumptions explicit rather than infer timing monotonicity from exploratory simulations.

## ERROR CHECK

1. The stopping-time definition does not itself imply optimality.
2. Earlier recognition is not treated as universally beneficial.
3. Historical timing simulations are not promoted to core evidence.
4. The first-person normalization still requires positive expected accessibility.
5. Everett interpretation of `S_tau` remains conditional on the separate bridge assumption.

## Status

**STOPPING-TIME FORMALIZATION COMPLETE. GENERAL TIMING ORDERING DEFERRED BEYOND v0.2.**
