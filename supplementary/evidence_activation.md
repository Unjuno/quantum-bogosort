# Evidence-Driven Recognition Activation

## Motivation

Recognition need not be modeled as an externally fixed switch. An agent can activate a QBS-type policy only after accumulating enough evidence that its evaluation signal is positively related to later outcomes.

## Recognition pipeline

A generic pipeline is:

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

## Exploratory experiment

A calibration experiment estimated score/outcome correlation and activated the QBS policy only when a one-sided Fisher-transform lower confidence bound was positive.

The exploratory result was qualitative but stable: weak true correlations required much larger calibration samples than strong correlations before activation became reliable. False activation under a true zero correlation stayed near the configured one-sided test level.

## Recognition time

A sequential extension defines recognition time as a stopping time:

```math
\tau_{recognition}
=
\inf\{t:\text{evidence criterion is satisfied at time }t\}.
```

This would allow explicit separation of:

- how much branch history is affected by early versus late recognition,
- how policy trajectories diverge after recognition,
- how accessibility changes after recognition,
- how cross-branch recognition correlation depends on shared evidence history.

## Limitations

The Fisher-transform threshold is an exploratory implementation, not a privileged QBS rule. A full treatment should account for sequential testing, model misspecification, dependence, calibration cost, and changing environments.

## Status

**SIMULATION-SUPPORTED modeling direction. Sequential recognition theorem OPEN.**
