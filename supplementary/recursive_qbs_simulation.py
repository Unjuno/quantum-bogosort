"""Exploratory recursive-QBS toy simulation.

This script is supplementary research code, not part of the locked E1-E5
reproducibility suite. It separates ordinary predictable outcome from a
filtration-relative innovation term, applies cumulative accessibility weights,
and lets a path-dependent bridge belief influence later adoption.

Nothing here derives an Everettian accessibility law or changes the base RNG.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import math
import numpy as np


@dataclass(frozen=True)
class Params:
    n: int = 350_000
    steps: int = 24
    seed: int = 20260820
    signal_accuracy: float = 0.72
    gain: float = 1.15
    action_cost: float = 0.35
    k_predictable: float = 0.22
    k_innovation: float = 0.22
    assumed_k_innovation: float = 0.22
    fixed_adoption: float = 0.65
    bridge_prior: float = 0.48
    adoption_gate: float = 0.52


def sigmoid(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    pos = x >= 0
    out[pos] = 1.0 / (1.0 + np.exp(-x[pos]))
    z = np.exp(x[~pos])
    out[~pos] = z / (1.0 + z)
    return out


def weighted_mean(x: np.ndarray, logw: np.ndarray) -> float:
    shifted = logw - np.max(logw)
    w = np.exp(np.clip(shifted, -745.0, 0.0))
    return float(np.sum(w * x) / np.sum(w))


def ess_fraction(logw: np.ndarray) -> float:
    shifted = logw - np.max(logw)
    w = np.exp(np.clip(shifted, -745.0, 0.0))
    return float((w.sum() ** 2 / np.sum(w * w)) / len(w))


def simulate(model: str, p: Params) -> dict[str, float]:
    rng = np.random.default_rng(p.seed)
    n = p.n
    logw = np.zeros(n)
    total = np.zeros(n)
    predictable_sum = np.zeros(n)
    innovation_sum = np.zeros(n)
    action_sum = np.zeros(n)

    recursive = model in {"recursive_selector", "recursive_full"}
    if recursive:
        log_odds = np.full(n, math.log(p.bridge_prior / (1.0 - p.bridge_prior)))
    else:
        log_odds = None

    for _ in range(p.steps):
        state = rng.choice(np.array([-1.0, 1.0]), n)
        signal_correct = rng.random(n) < p.signal_accuracy
        signal = np.where(signal_correct, state, -state)

        if model == "base":
            adoption = np.zeros(n)
            action = np.zeros(n)
        elif model == "policy_only":
            adoption = np.ones(n)
            action = (signal > 0).astype(float)
        elif model == "fixed_qbs":
            adoption = np.full(n, p.fixed_adoption)
            action = (signal > 0).astype(float)
        elif model == "recursive_selector":
            assert log_odds is not None
            adoption = sigmoid(log_odds)
            action = (signal > 0).astype(float)
        elif model == "recursive_full":
            assert log_odds is not None
            adoption = sigmoid(log_odds)
            action = ((signal > 0) & (adoption >= p.adoption_gate)).astype(float)
        else:
            raise ValueError(f"unknown model: {model}")

        realized_policy = action * (p.gain * state - p.action_cost)
        exogenous_noise = rng.choice(np.array([-1.0, 1.0]), n)
        outcome = realized_policy + exogenous_noise

        # The action is chosen using the current signal. For the symmetric
        # binary signal model, E[state | signal=+1] = 2*accuracy-1.
        expected_state_given_positive_signal = 2.0 * p.signal_accuracy - 1.0
        predictable = action * (
            p.gain * expected_state_given_positive_signal - p.action_cost
        )
        innovation = outcome - predictable

        if model in {"fixed_qbs", "recursive_selector", "recursive_full"}:
            logw += adoption * (
                p.k_predictable * predictable + p.k_innovation * innovation
            )

        total += outcome
        predictable_sum += predictable
        innovation_sum += innovation
        action_sum += action

        if recursive:
            assert log_odds is not None
            # Bridge-belief update under the assumed innovation-tilt model.
            # The actual selector may be aligned or anti-aligned, allowing a
            # deliberate model-misspecification control.
            k_eff = adoption * p.assumed_k_innovation
            log_normalizer = np.log(np.cosh(k_eff))

            ex = expected_state_given_positive_signal
            state_mgf = (
                p.signal_accuracy * np.exp(k_eff * p.gain * (1.0 - ex))
                + (1.0 - p.signal_accuracy)
                * np.exp(k_eff * p.gain * (-1.0 - ex))
            )
            log_normalizer += action * np.log(state_mgf)
            log_odds += k_eff * innovation - log_normalizer
            log_odds = np.clip(log_odds, -30.0, 30.0)

    base_total = float(total.mean())
    base_predictable = float(predictable_sum.mean())
    base_innovation = float(innovation_sum.mean())
    base_actions = float(action_sum.mean())

    weighted = model in {"fixed_qbs", "recursive_selector", "recursive_full"}
    if weighted:
        fp_total = weighted_mean(total, logw)
        fp_predictable = weighted_mean(predictable_sum, logw)
        fp_innovation = weighted_mean(innovation_sum, logw)
        fp_actions = weighted_mean(action_sum, logw)
        ess = ess_fraction(logw)
    else:
        fp_total = base_total
        fp_predictable = base_predictable
        fp_innovation = base_innovation
        fp_actions = base_actions
        ess = 1.0

    if recursive:
        assert log_odds is not None
        final_bridge_belief = sigmoid(log_odds)
        base_belief = float(final_bridge_belief.mean())
        fp_belief = weighted_mean(final_bridge_belief, logw)
    elif model == "fixed_qbs":
        base_belief = fp_belief = p.fixed_adoption
    elif model == "policy_only":
        base_belief = fp_belief = 1.0
    else:
        base_belief = fp_belief = 0.0

    predictable_shift = fp_predictable - base_predictable
    innovation_shift = fp_innovation - base_innovation
    uplift = fp_total - base_total
    decomposition_error = uplift - (predictable_shift + innovation_shift)

    return {
        "base_total": base_total,
        "fp_total": fp_total,
        "uplift": uplift,
        "predictable_shift": predictable_shift,
        "innovation_shift": innovation_shift,
        "base_actions": base_actions,
        "fp_actions": fp_actions,
        "base_bridge_belief": base_belief,
        "fp_bridge_belief": fp_belief,
        "ess_fraction": ess,
        "decomposition_error": decomposition_error,
    }


def print_result(label: str, result: dict[str, float]) -> None:
    print(label)
    for key, value in result.items():
        print(f"  {key:24s} {value: .8f}")


def main() -> None:
    p = Params()
    aligned = simulate("recursive_full", p)
    anti_aligned = simulate(
        "recursive_full",
        replace(
            p,
            k_predictable=0.70,
            k_innovation=-0.08,
            assumed_k_innovation=0.22,
        ),
    )
    null = simulate("policy_only", p)

    # Mechanism checks. Magnitudes are not treated as universal constants.
    assert abs(null["uplift"]) < 1e-12
    assert abs(aligned["decomposition_error"]) < 1e-10
    assert abs(anti_aligned["decomposition_error"]) < 1e-10
    assert aligned["innovation_shift"] > 0
    assert anti_aligned["predictable_shift"] > 0
    assert anti_aligned["innovation_shift"] < 0
    assert anti_aligned["uplift"] < 0

    print_result("aligned recursive model", aligned)
    print()
    print_result("anti-aligned innovation control", anti_aligned)
    print()
    print_result("ordinary policy-only null", null)


if __name__ == "__main__":
    main()
