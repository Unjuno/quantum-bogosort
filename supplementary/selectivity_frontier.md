# Selectivity Frontier

## Motivation

Positive predictor/outcome alignment does not imply that maximal selectivity is optimal when the predictor is imperfect.

## Setup

Consider a family of accessibility maps indexed by a selectivity parameter. More aggressive rules downweight a larger or more strongly adverse-scored region.

The first-person value depends on both the quality of ranking and the accessibility retained under the selected rule.

## Exploratory result

In positive-correlation toy models, increasing selectivity initially improved first-person mean and upper-tail probabilities, but sufficiently aggressive thresholds produced an interior optimum rather than monotone improvement.

This is compatible with the FOSD theorem. The theorem compares the base measure to the weighted measure for a fixed monotone accessibility function; the selectivity frontier compares different accessibility functions against one another.

## Measure constraint

A useful constrained formulation is:

$$
\max_{S\in\mathcal S}
V_{FP}(S)
$$

subject to:

$$
E[S]\ge m_{min},
$$

where `m_min` is a minimum accessible-measure requirement.

## Interpretation

Under imperfect prediction, selectivity and ordinary adaptation can trade off:

- more aggressive selection can improve conditional outcomes;
- but prediction errors can downweight branches that later turn out well;
- ordinary adaptive policy can reduce the need for extreme selection by rescuing poor states.

## Limitations

The location of the interior optimum is toy-model dependent and should not be universalized. It depends on the base distribution, predictor quality, accessibility family, and any measure constraint.

## Status

**SIMULATION-SUPPORTED toy-model frontier. General optimization theorem OPEN.**
