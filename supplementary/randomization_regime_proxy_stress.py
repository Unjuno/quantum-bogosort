from __future__ import annotations

from functools import lru_cache
import math

import numpy as np

SEED = 20260823
REPS = 5000
ALPHA = 0.05
P_REGIMES = np.array([0.2, 0.5, 0.8], dtype=float)


def logistic(x: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.exp(-x))


def logit(p: np.ndarray) -> np.ndarray:
    return np.log(p / (1.0 - p))


def log_binomial_pmf(n: int, k: int, p: float) -> float:
    return (
        math.lgamma(n + 1)
        - math.lgamma(k + 1)
        - math.lgamma(n - k + 1)
        + k * math.log(p)
        + (n - k) * math.log1p(-p)
    )


@lru_cache(maxsize=None)
def exact_two_sided_binomial(n: int, k: int, p_million: int) -> float:
    p = p_million / 1_000_000.0
    target = math.exp(log_binomial_pmf(n, k, p))
    total = 0.0
    for j in range(n + 1):
        probability = math.exp(log_binomial_pmf(n, j, p))
        if probability <= target * (1.0 + 1e-12):
            total += probability
    return min(1.0, total)


def exact_pvalue(n: int, k: int, p: float) -> float:
    return exact_two_sided_binomial(n, k, int(round(p * 1_000_000)))


def common_offset_mle(k: np.ndarray, n: np.ndarray, p: np.ndarray) -> float:
    delta = 0.0
    for _ in range(60):
        q = logistic(logit(p) + delta)
        score = float(np.sum(k - n * q))
        hessian = -float(np.sum(n * q * (1.0 - q)))
        updated = delta - score / hessian
        if abs(updated - delta) < 1e-12:
            return updated
        delta = updated
    return delta


def binomial_loglik(k: np.ndarray, n: np.ndarray, q: np.ndarray) -> float:
    total = 0.0
    for ki, ni, qi in zip(k, n, q):
        if ki > 0:
            total += float(ki) * math.log(float(qi))
        if ni - ki > 0:
            total += float(ni - ki) * math.log1p(-float(qi))
    return total


def regime_homogeneity_pvalue(k: np.ndarray, n: np.ndarray) -> float:
    mask = n > 0
    k = k[mask].astype(float)
    n = n[mask].astype(float)
    p = P_REGIMES[mask]
    if len(n) <= 1:
        return 1.0
    delta = common_offset_mle(k, n, p)
    q = logistic(logit(p) + delta)
    restricted = binomial_loglik(k, n, q)
    saturated_q = np.clip(k / n, 1e-15, 1.0 - 1e-15)
    saturated = binomial_loglik(k, n, saturated_q)
    deviance = max(0.0, 2.0 * (saturated - restricted))
    df = len(n) - 1
    if df == 2:
        return math.exp(-deviance / 2.0)
    if df == 1:
        return math.erfc(math.sqrt(deviance / 2.0))
    raise AssertionError("diagnostic is specified for three regimes")


def selected_joint(mode: str, gamma: float, proxy_accuracy: float) -> np.ndarray:
    """Return Q(C,Z,L | selected,R) for each randomization regime R."""
    out = np.zeros((3, 2, 2, 2), dtype=float)
    for regime, p_context in enumerate(P_REGIMES):
        latent_probability = (
            (0.2, 0.5, 0.8)[regime] if mode == "composition_shift" else 0.5
        )
        for context in (0, 1):
            context_probability = p_context if context == 1 else 1.0 - p_context
            for latent in (0, 1):
                latent_mass = (
                    latent_probability if latent == 1 else 1.0 - latent_probability
                )
                for proxy in (0, 1):
                    proxy_probability = (
                        proxy_accuracy if proxy == latent else 1.0 - proxy_accuracy
                    )
                    if mode == "shared_null":
                        selector = (0.25, 0.75)[latent]
                    elif mode == "stable_context":
                        selector = float(logistic((2 * context - 1) * gamma))
                    elif mode == "regime_retuned":
                        shift = (-gamma, gamma, 2.0 * gamma)[regime]
                        selector = float(logistic((2 * context - 1) * shift))
                    elif mode == "projection_blind":
                        selector = ((0.8, 0.2), (0.2, 0.8))[context][latent]
                    elif mode == "composition_shift":
                        selector = ((0.8, 0.2), (0.3, 0.7))[context][latent]
                    else:
                        raise ValueError(f"unknown mode: {mode}")
                    out[regime, context, proxy, latent] = (
                        context_probability * latent_mass * proxy_probability * selector
                    )
        out[regime] /= out[regime].sum()
    return out


def reject_shared_selector(counts: np.ndarray) -> bool:
    """Exact Bonferroni test of preserved randomization probabilities."""
    observed = counts.sum(axis=3)
    pvalues: list[float] = []
    for regime, p_context in enumerate(P_REGIMES):
        for proxy in (0, 1):
            n_cell = int(observed[regime, :, proxy].sum())
            if n_cell == 0:
                continue
            k_cell = int(observed[regime, 1, proxy])
            pvalues.append(exact_pvalue(n_cell, k_cell, float(p_context)))
    return bool(pvalues) and min(pvalues) * len(pvalues) <= ALPHA


def reject_regime_invariance(counts: np.ndarray) -> bool:
    """Asymptotic diagnostic for one common selected log-odds offset."""
    observed = counts.sum(axis=3)
    pvalues: list[float] = []
    for proxy in (0, 1):
        k = np.array([observed[r, 1, proxy] for r in range(3)], dtype=int)
        n = np.array([observed[r, :, proxy].sum() for r in range(3)], dtype=int)
        pvalues.append(regime_homogeneity_pvalue(k, n))
    return min(pvalues) * len(pvalues) <= ALPHA


def run_case(
    rng: np.random.Generator,
    mode: str,
    gamma: float,
    proxy_accuracy: float,
    n_selected_per_regime: int,
) -> tuple[float, float]:
    joint = selected_joint(mode, gamma, proxy_accuracy)
    shared_rejections = 0
    homogeneity_rejections = 0
    for _ in range(REPS):
        counts = np.zeros((3, 2, 2, 2), dtype=int)
        for regime in range(3):
            counts[regime] = rng.multinomial(
                n_selected_per_regime, joint[regime].ravel()
            ).reshape(2, 2, 2)
        shared_rejections += reject_shared_selector(counts)
        homogeneity_rejections += reject_regime_invariance(counts)
    return shared_rejections / REPS, homogeneity_rejections / REPS


def main() -> None:
    rng = np.random.default_rng(SEED)
    cases = [
        ("shared_null", 0.0, 0.8, 500),
        ("stable_context", 0.4, 0.8, 500),
        ("regime_retuned", 0.4, 0.8, 500),
        ("projection_blind", 0.4, 0.50, 500),
        ("projection_blind", 0.4, 0.55, 500),
        ("projection_blind", 0.4, 0.60, 200),
        ("projection_blind", 0.4, 0.60, 500),
        ("projection_blind", 0.4, 0.60, 1000),
        ("projection_blind", 0.4, 0.65, 500),
        ("projection_blind", 0.4, 0.70, 500),
        ("composition_shift", 0.4, 0.80, 500),
    ]
    rows = []
    for case in cases:
        shared, homogeneous = run_case(rng, *case)
        rows.append((*case, shared, homogeneous))

    keyed = {(m, g, q, n): (s, h) for m, g, q, n, s, h in rows}
    assert keyed[("shared_null", 0.0, 0.8, 500)][0] < 0.06
    assert keyed[("shared_null", 0.0, 0.8, 500)][1] < 0.07
    assert keyed[("stable_context", 0.4, 0.8, 500)][0] > 0.97
    assert keyed[("stable_context", 0.4, 0.8, 500)][1] < 0.07
    assert keyed[("regime_retuned", 0.4, 0.8, 500)][0] > 0.99
    assert keyed[("regime_retuned", 0.4, 0.8, 500)][1] > 0.99
    assert keyed[("projection_blind", 0.4, 0.50, 500)][0] < 0.06
    assert keyed[("projection_blind", 0.4, 0.50, 500)][1] < 0.07
    assert keyed[("projection_blind", 0.4, 0.60, 200)][0] < keyed[
        ("projection_blind", 0.4, 0.60, 500)
    ][0] < keyed[("projection_blind", 0.4, 0.60, 1000)][0]
    assert keyed[("projection_blind", 0.4, 0.65, 500)][0] > 0.90
    assert keyed[("projection_blind", 0.4, 0.70, 500)][0] > 0.99
    assert max(
        keyed[("projection_blind", 0.4, q, 500)][1]
        for q in (0.50, 0.55, 0.60, 0.65, 0.70)
    ) < 0.07
    assert keyed[("composition_shift", 0.4, 0.80, 500)][0] > 0.99
    assert keyed[("composition_shift", 0.4, 0.80, 500)][1] > 0.95

    print(f"seed={SEED} reps={REPS} alpha={ALPHA} regimes=0.2,0.5,0.8")
    print("mode gamma proxy_accuracy n_per_regime shared_reject common_offset_reject")
    for row in rows:
        mode, gamma, q, n, shared, hom = row
        print(f"{mode} {gamma:.2f} {q:.2f} {n} {shared:.4f} {hom:.4f}")


if __name__ == "__main__":
    main()
