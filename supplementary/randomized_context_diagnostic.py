"""Finite-sample randomized-context diagnostic for shared binary selection.

This is supplementary stress code, not E6 and not evidence for an Everett bridge.
The exact preservation result is documented in randomized_context_diagnostic.md.
"""
from __future__ import annotations

from functools import lru_cache
import math

import numpy as np

SEED = 20260823
REPS = 10_000
N_SELECTED = (200, 500, 1000)
GAMMAS = (0.1, 0.2, 0.4)
ALPHA = 0.05
P_CONTEXT = 0.5

# omega = (W, L): W is observed pre-treatment; L remains latent.
STATES = np.array([(w, latent) for w in (0, 1) for latent in (0, 1)], dtype=int)
MU = np.full(4, 0.25)


def selected_joint(mode: str, gamma: float) -> np.ndarray:
    """Return Q(C, omega | selected) for one diagnostic model."""
    w = STATES[:, 0]
    latent = STATES[:, 1]

    if mode == "null_shared":
        base = np.array([0.18, 0.32, 0.48, 0.62], dtype=float)
        selector = np.vstack([base, base])
    elif mode == "rate_shift":
        base = np.array([0.18, 0.32, 0.48, 0.62], dtype=float)
        selector = np.vstack([base * np.exp(-gamma), base * np.exp(gamma)])
    elif mode == "observed_composition":
        selector = np.vstack(
            [
                np.exp(-gamma * (2 * w - 1)),
                np.exp(gamma * (2 * w - 1)),
            ]
        )
    elif mode == "latent_projection_blind":
        selector = np.vstack(
            [
                np.exp(-gamma * (2 * latent - 1)),
                np.exp(gamma * (2 * latent - 1)),
            ]
        )
    else:
        raise ValueError(f"unknown mode: {mode}")

    # Global positive scaling leaves Q(C, omega | selected) unchanged and makes
    # every selector a valid Bernoulli inclusion probability.
    selector *= 0.8 / float(selector.max())
    prior = np.array([1.0 - P_CONTEXT, P_CONTEXT])[:, None] * MU[None, :]
    selected = prior * selector
    selected /= selected.sum()
    return selected


def log_binomial_pmf_half(n: int, k: int) -> float:
    return (
        math.lgamma(n + 1)
        - math.lgamma(k + 1)
        - math.lgamma(n - k + 1)
        - n * math.log(2.0)
    )


@lru_cache(maxsize=None)
def exact_two_sided_half(n: int, k: int) -> float:
    """Conservative equal-tail exact p-value for Binomial(n, 1/2)."""
    if n <= 0:
        return 1.0
    k = min(k, n - k)
    lower = sum(math.exp(log_binomial_pmf_half(n, j)) for j in range(k + 1))
    return min(1.0, 2.0 * lower)


def reject_shared_selector(counts: np.ndarray) -> bool:
    """Bonferroni exact test over the two predeclared W strata."""
    per_stratum_alpha = ALPHA / 2.0
    for w_value in (0, 1):
        mask = STATES[:, 0] == w_value
        n_w = int(counts[:, mask].sum())
        if n_w == 0:
            continue
        k_w = int(counts[1, mask].sum())
        if exact_two_sided_half(n_w, k_w) <= per_stratum_alpha:
            return True
    return False


def observable_summary(joint: np.ndarray) -> tuple[float, float, float, float, float]:
    q_c1 = float(joint[1].sum())
    w1 = []
    latent1 = []
    for c in (0, 1):
        w1.append(float(joint[c, STATES[:, 0] == 1].sum() / joint[c].sum()))
        latent1.append(float(joint[c, STATES[:, 1] == 1].sum() / joint[c].sum()))
    return q_c1, w1[0], w1[1], latent1[0], latent1[1]


def simulate() -> list[tuple[str, float, int, float, float, float, float, float, float]]:
    rng = np.random.default_rng(SEED)
    rows: list[tuple[str, float, int, float, float, float, float, float, float]] = []

    for mode in (
        "null_shared",
        "rate_shift",
        "observed_composition",
        "latent_projection_blind",
    ):
        gammas = (0.0,) if mode == "null_shared" else GAMMAS
        for gamma in gammas:
            joint = selected_joint(mode, gamma)
            q_c1, w1_c0, w1_c1, latent1_c0, latent1_c1 = observable_summary(joint)
            for n_selected in N_SELECTED:
                rejected = 0
                for _ in range(REPS):
                    counts = rng.multinomial(n_selected, joint.ravel()).reshape(2, 4)
                    rejected += reject_shared_selector(counts)
                rows.append(
                    (
                        mode,
                        gamma,
                        n_selected,
                        rejected / REPS,
                        q_c1,
                        w1_c0,
                        w1_c1,
                        latent1_c0,
                        latent1_c1,
                    )
                )
    return rows


def validate(rows: list[tuple[str, float, int, float, float, float, float, float, float]]) -> None:
    keyed = {(mode, gamma, n): row for row in rows for mode, gamma, n, *_ in [row]}

    # Exact structural summaries.
    for n in N_SELECTED:
        null = keyed[("null_shared", 0.0, n)]
        assert abs(null[4] - 0.5) < 1e-12
        assert abs(null[5] - null[6]) < 1e-12
        blind = keyed[("latent_projection_blind", 0.4, n)]
        assert abs(blind[4] - 0.5) < 1e-12
        assert abs(blind[5] - blind[6]) < 1e-12
        assert abs(blind[7] - blind[8]) > 0.3

    # Finite-sample calibration/power sanity checks. The exact validity is analytic;
    # these Monte Carlo bounds only guard gross implementation drift.
    assert max(keyed[("null_shared", 0.0, n)][3] for n in N_SELECTED) < 0.055
    assert max(
        keyed[("latent_projection_blind", gamma, n)][3]
        for gamma in GAMMAS
        for n in N_SELECTED
    ) < 0.06
    for mode in ("rate_shift", "observed_composition"):
        assert keyed[(mode, 0.1, 1000)][3] > 0.65
        assert keyed[(mode, 0.2, 500)][3] > 0.90
        assert keyed[(mode, 0.4, 200)][3] > 0.95


def main() -> None:
    rows = simulate()
    validate(rows)

    print(f"seed={SEED} reps={REPS} alpha={ALPHA}")
    print("mode gamma n reject_rate Q_C1 Q_W1_C0 Q_W1_C1 Q_L1_C0 Q_L1_C1")
    for row in rows:
        mode, gamma, n, reject_rate, q_c1, w1_c0, w1_c1, l1_c0, l1_c1 = row
        print(
            f"{mode} {gamma:.1f} {n} {reject_rate:.4f} "
            f"{q_c1:.6f} {w1_c0:.6f} {w1_c1:.6f} {l1_c0:.6f} {l1_c1:.6f}"
        )


if __name__ == "__main__":
    main()
