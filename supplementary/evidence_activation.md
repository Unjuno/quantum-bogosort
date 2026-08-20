# Evidence-Driven Recognition Activation

## Motivation

Recognition need not be modeled as an externally fixed switch. An agent can activate or strengthen a QBS-type policy only after accumulating evidence that its evaluation signal is useful and, in a recursive extension, after updating beliefs about the observer-selection model itself.

The two evidence roles should be separated:

1. **predictive evidence** concerns whether the agent's ordinary signal predicts later outcomes;
2. **bridge evidence** concerns whether the observer-conditioned law differs from a specified null/base observer law.

Neither role gives recognition privileged causal power. Recognition matters through the policy, adoption, or accessibility rule it induces.

## Predictive recognition pipeline

A generic predictive-evidence pipeline is:

```math
\text{data}
\longrightarrow
\widehat{\rho}
\longrightarrow
\text{confidence}
\longrightarrow
q
\longrightarrow
S
\longrightarrow
\mu^{FP}.
```

Here `q` is an execution/adherence strength and the activation rule depends on estimated predictive evidence.

An earlier calibration experiment estimated score/outcome correlation and activated the QBS policy only when a one-sided Fisher-transform lower confidence bound was positive. The result was qualitative but stable: weak true correlations required much larger calibration samples than strong correlations before activation became reliable, while false activation under a true zero correlation stayed near the configured one-sided test level.

The Fisher-transform threshold is an exploratory implementation, not a privileged QBS rule.

## Recognition time

A sequential recognition rule can be written as a stopping time:

```math
\tau_{\mathrm{recognition}}
=
\inf\{t:\text{evidence criterion is satisfied at time }t\}.
```

The dedicated stopping-time treatment is in [`recognition_time.md`](recognition_time.md). It does not imply that earlier recognition is always better.

## Recursive observer-information extension

The missing feedback step in a static recognition model is that the observer's experienced history can become new information for later decisions.

Let:

```math
(\Omega,\mathcal F,(\mathcal F_t)_{t=0}^{T},\mu)
```

be a filtered base probability space. Let `H_t` denote the information available when the decision for step `t+1` is selected. A generic recursive loop is:

```math
O_t
\longrightarrow
H_t
\longrightarrow
(b_t,q_t,\pi_t)
\longrightarrow
(X_{t+1},G_{t+1})
\longrightarrow
O_{t+1},
```

where:

- `O_t` is the current observer record/state used by the model;
- `b_t` is an epistemic belief about a candidate observer-selection bridge;
- `q_t` is an adoption or execution strength chosen from current information;
- `pi_t` is the ordinary causal policy;
- `X_{t+1}` is the next outcome increment;
- `G_{t+1}` is a nonnegative incremental accessibility factor.

Define cumulative accessibility by:

```math
S_t
=
\prod_{j=1}^{t}G_j,
\qquad
S_0=1.
```

Assume the corresponding normalized measures exist and the displayed expectations below are finite.

### Sequential change-of-measure identity

For an integrable horizon-`t` quantity `Z`:

```math
E_t^{FP}[Z]
=
\frac{E_{t-1}^{FP}[ZG_t]}
{E_{t-1}^{FP}[G_t]}.
```

Therefore:

```math
E_t^{FP}[Z]
-
E_{t-1}^{FP}[Z]
=
\frac{\mathrm{Cov}_{t-1}^{FP}(Z,G_t)}
{E_{t-1}^{FP}[G_t]}.
```

This is a sequential application of the existing T1 change-of-measure identity, not a new probability theorem.

## Predictable versus innovation selection

To distinguish ordinary decision quality from outcome components that were not predictable when the decision was made, define:

```math
m_{t+1}
=
E_\mu[X_{t+1}\mid H_t],
```

and:

```math
\varepsilon_{t+1}
=
X_{t+1}-m_{t+1}.
```

Under the usual integrability conditions, the innovation sequence has zero base conditional mean:

```math
E_\mu[\varepsilon_{t+1}\mid H_t]=0.
```

Define cumulative predictable and innovation components:

```math
A_T
=
\sum_{t=0}^{T-1}m_{t+1},
\qquad
M_T
=
\sum_{t=0}^{T-1}\varepsilon_{t+1},
```

so that:

```math
U_T=A_T+M_T,
\qquad
E_\mu[M_T]=0.
```

The final first-person uplift then decomposes exactly as:

```math
E_{FP}[U_T]-E_\mu[U_T]
=
\frac{\mathrm{Cov}_\mu(A_T,S_T)}{E_\mu[S_T]}
+
\frac{\mathrm{Cov}_\mu(M_T,S_T)}{E_\mu[S_T]}.
```

The first term is **predictable selection**: reweighting of trajectory value that was predictable from the information used for the decision. The second is **innovation selection**: reweighting of a cumulative component whose increments had zero base conditional expectation at decision time.

`Innovation selection` is the preferred formal term. In informal discussion it can be related to a luck-like first-person shift, but it does not mean that objective chance or the base random generator has been causally improved.

### Dynamic refinement of recognition decomposition

For recognition conditions `r` in `{0,1}`, write:

```math
U_{r,T}=A_{r,T}+M_{r,T}.
```

Then the existing T4 recognition decomposition refines to:

```math
V_{1,T}-V_{0,T}
=
E_\mu[A_{1,T}-A_{0,T}]
```

```math
+
\left[
Q(A_{1,T},S_{1,T})
-
Q(A_{0,T},S_{0,T})
\right]
```

```math
+
\left[
Q(M_{1,T},S_{1,T})
-
Q(M_{0,T},S_{0,T})
\right].
```

This separates:

1. ordinary causal/predictable policy improvement;
2. first-person selection among predictably favorable or unfavorable trajectories;
3. first-person selection among filtration-relative innovations.

The identity is an exact refinement of T4 plus the standard predictable/innovation decomposition. It is not labeled as a new numbered `S2` theorem.

## Recursive bridge-belief update

Let `H_0` denote a specified null/base observer model and `H_1` a specified QBS first-person observer model. Conditional on current information `H_t`, let `P_{0,t}` and `P_{1,t}` denote their candidate laws for the next observer record `O_{t+1}`.

When the needed absolute-continuity conditions hold, define the one-step log likelihood ratio:

```math
\ell_{t+1}
=
\log
\frac{dP_{1,t}}
{dP_{0,t}}(O_{t+1}).
```

Posterior log odds can be updated by:

```math
L_{t+1}=L_t+\ell_{t+1}.
```

The corresponding bridge belief `b_t` may then enter the next adoption rule `q_t` or policy-selection rule.

Under correctly specified conditional models:

```math
E_{H_1}[\ell_{t+1}\mid H_t]
=
D_{\mathrm{KL}}(P_{1,t}\|P_{0,t})
\ge0,
```

while, when the reverse likelihood ratio is also defined:

```math
E_{H_0}[\ell_{t+1}\mid H_t]
=
-D_{\mathrm{KL}}(P_{0,t}\|P_{1,t})
\le0.
```

Thus the recursive epistemic loop can be written without assigning recognition a special physical force:

```math
\text{experienced observer history}
\longrightarrow
\text{bridge evidence}
\longrightarrow
b_t
\longrightarrow
(q_t,\pi_t,S_t)
\longrightarrow
\text{future observer history}.
```

These KL identities are standard likelihood-ratio facts. Their role here is to close the previously open QBS feedback arrow from first-person observation to later recognition/adoption.

## Exploratory recursive simulation

[`recursive_qbs_simulation.py`](recursive_qbs_simulation.py) implements a deterministic classical toy model with:

- a noisy predictive signal;
- signal-gated ordinary policy action;
- filtration-relative predictable and innovation components;
- path-dependent bridge belief;
- belief-dependent adoption;
- cumulative first-person weighting;
- aligned and anti-aligned innovation controls.

Under its default aligned 24-step configuration with 350,000 base trajectories, the combined recursive condition gives approximately:

```text
base cumulative outcome            0.39314
first-person cumulative outcome    4.86658
predictable-selection shift        0.36097
innovation-selection shift         4.11248
base mean action count             2.42621
first-person mean action count     4.74010
base final bridge belief           0.44423
first-person final bridge belief   0.54279
```

The decomposition error is at floating-point noise level in the implementation. An anti-aligned selector provides a counterexample in which innovation selection is negative even though ordinary/predictable effects can remain favorable.

These numbers demonstrate only that the proposed mechanism can be separated and recursively instantiated in a classical toy model. They are not evidence that an Everettian or multiverse accessibility law exists in nature.

## Boundaries and failure modes

- The innovation decomposition is relative to the chosen information filtration. Enlarging the information state can move variation from the innovation term into the predictable term.
- Positive total first-person uplift does not imply positive innovation selection.
- A negative innovation term can outweigh positive ordinary/predictable effects.
- Correctly specified Bayes-factor drift does not imply monotone pathwise belief growth.
- A misspecified bridge model can produce misleading belief dynamics; model comparison must include null and misspecification controls.
- If `P_{1,t}=P_{0,t}`, the KL evidence drift is zero and the observer history supplies no discriminating bridge evidence at that step.
- The recursive model does not establish quantum immortality, guaranteed survival, backward causation, or objective RNG bias.
- The physical source of `G_t` or `S_t` remains the separate Everett/multiverse bridge problem.

## Status

**DYNAMIC RECOGNITION/SELF-LOCATION LOOP FORMALIZED AS AN UNNUMBERED SUPPLEMENTARY EXTENSION. SEQUENTIAL WEIGHTING, PREDICTABLE/INNOVATION DECOMPOSITION, AND CONDITIONAL KL EVIDENCE DRIFT ARE EXACT UNDER THEIR STATED CONDITIONS. THE RECURSIVE CLASSICAL SIMULATION IS EXPLORATORY. THE PHYSICAL ACCESSIBILITY BRIDGE REMAINS OPEN.**
