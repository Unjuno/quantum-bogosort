"""Deterministic sanity checks for the unnumbered context-identifiability boundary.

This script is supplementary audit code, not E6 and not evidence for an Everett bridge.
The exact claims are proved in supplementary/selection_equivalence.md.
"""
from __future__ import annotations

import numpy as np

SEED = 20260823
TRIALS = 20_000
ATOL = 1e-12
FIT_ATOL = 1e-10


def normalized_positive(rng: np.random.Generator, n: int) -> np.ndarray:
    values = rng.random(n) + 0.05
    return values / values.sum()


def run_property_tests() -> tuple[float, float, int, int]:
    rng = np.random.default_rng(SEED)
    max_representation_error = 0.0
    max_shared_ratio_deviation = 0.0
    false_shared_null_fits = 0
    nonconstant_pairs = 0

    for _ in range(TRIALS):
        n = int(rng.integers(2, 12))

        mu0 = normalized_positive(rng, n)
        q0 = normalized_positive(rng, n)
        r0 = q0 / mu0

        reconstructed_q0 = mu0 * r0
        reconstructed_q0 /= reconstructed_q0.sum()
        max_representation_error = max(
            max_representation_error,
            float(np.max(np.abs(reconstructed_q0 - q0))),
        )

        mu1 = normalized_positive(rng, n)
        q1 = normalized_positive(rng, n)
        r1 = q1 / mu1

        arbitrary_ratio = r0 / r1
        if float(np.max(arbitrary_ratio) - np.min(arbitrary_ratio)) > FIT_ATOL:
            nonconstant_pairs += 1
            candidate_shared_a = r0
            reconstructed_q1 = mu1 * candidate_shared_a
            reconstructed_q1 /= reconstructed_q1.sum()
            if float(np.max(np.abs(reconstructed_q1 - q1))) < FIT_ATOL:
                false_shared_null_fits += 1

        shared_a = rng.random(n) + 0.05
        z0 = float(np.dot(mu0, shared_a))
        z1 = float(np.dot(mu1, shared_a))
        shared_r0 = shared_a / z0
        shared_r1 = shared_a / z1
        shared_ratio = shared_r0 / shared_r1
        max_shared_ratio_deviation = max(
            max_shared_ratio_deviation,
            float(np.max(np.abs(shared_ratio - shared_ratio[0]))),
        )

    return (
        max_representation_error,
        max_shared_ratio_deviation,
        false_shared_null_fits,
        nonconstant_pairs,
    )


def run_projection_checks() -> None:
    # Shared latent selector, different observation maps.
    mu = np.array([0.5, 0.5])
    shared_a = np.array([1.0, 3.0])
    latent_selected = mu * shared_a
    latent_selected /= latent_selected.sum()
    np.testing.assert_allclose(latent_selected, np.array([0.25, 0.75]), atol=ATOL, rtol=0)
    flipped_observation = latent_selected[::-1]
    np.testing.assert_allclose(flipped_observation, np.array([0.75, 0.25]), atol=ATOL, rtol=0)

    # Latent shared-null violation hidden by a coarse projection.
    q0 = np.array([4.0, 2.0, 1.0, 1.0])
    q0 /= q0.sum()
    q1 = np.array([2.0, 4.0, 1.0, 1.0])
    q1 /= q1.sum()
    latent_ratio = q0 / q1
    assert float(np.max(latent_ratio) - np.min(latent_ratio)) > 1.0

    projected_q0 = np.array([q0[:2].sum(), q0[2:].sum()])
    projected_q1 = np.array([q1[:2].sum(), q1[2:].sum()])
    np.testing.assert_allclose(projected_q0, np.array([0.75, 0.25]), atol=ATOL, rtol=0)
    np.testing.assert_allclose(projected_q1, projected_q0, atol=ATOL, rtol=0)


def main() -> None:
    (
        max_representation_error,
        max_shared_ratio_deviation,
        false_shared_null_fits,
        nonconstant_pairs,
    ) = run_property_tests()
    run_projection_checks()

    assert max_representation_error < ATOL
    assert max_shared_ratio_deviation < ATOL
    assert nonconstant_pairs == TRIALS
    assert false_shared_null_fits == 0

    print(f"seed={SEED} trials={TRIALS}")
    print(f"max representation error={max_representation_error:.17g}")
    print(f"max shared-ratio deviation={max_shared_ratio_deviation:.17g}")
    print(f"nonconstant arbitrary pairs={nonconstant_pairs}")
    print(f"false shared-null fits={false_shared_null_fits}")
    print("projection checks=pass")


if __name__ == "__main__":
    main()
