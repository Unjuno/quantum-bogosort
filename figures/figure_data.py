"""Canonical numerical data contract shared by QBS SVG and manuscript PDF figures.

The public SVGs and manuscript PDFs intentionally use different rendering backends and
layouts. Figures 2--6 must nevertheless plot the same numerical series. Keep those series
here so one renderer cannot silently drift from the other while both still build.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"


def fosd_curves() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return x, base CDF, monotone-accessibility FP CDF, and nonmonotone FP CDF."""
    x = np.linspace(-4, 4, 801)
    phi = np.exp(-x * x / 2) / np.sqrt(2 * np.pi)

    def weighted_cdf(weight: np.ndarray) -> np.ndarray:
        z = phi * weight
        cumulative = np.cumsum(z) * (x[1] - x[0])
        return cumulative / cumulative[-1]

    base = weighted_cdf(np.ones_like(x))
    monotone = weighted_cdf(0.1 + 0.9 / (1 + np.exp(-2 * x)))
    nonmonotone = weighted_cdf(0.1 + 0.9 * np.exp(-(x / 0.9) ** 2))
    return x, base, monotone, nonmonotone


def recognition_bar_data() -> tuple[list[str], list[float]]:
    row = pd.read_csv(DATA / "e3_recognition_decomposition_reproduction.csv").iloc[0]
    return ["Policy", "QBS", "Total"], [
        row["policy_gain"],
        row["QBS_gain"],
        row["total_gain"],
    ]


def interaction_bar_data() -> tuple[list[str], list[float]]:
    data = pd.read_csv(DATA / "e4_fixed_selector_sign_reproduction.csv")
    return list(data["policy"]), list(data["interaction"])


def adaptation_line_data() -> tuple[np.ndarray, list[tuple[str, np.ndarray]]]:
    data = pd.read_csv(DATA / "qbs_adaptation_total_effect_summary.csv")
    x = data["adaptation_accuracy_p"].to_numpy()
    series = [
        ("Policy effect", data["policy_effect"].to_numpy()),
        ("QBS after policy", data["QBS_after"].to_numpy()),
        ("Interaction", data["interaction"].to_numpy()),
        ("Total FP effect", data["total_FP_effect"].to_numpy()),
    ]
    return x, series


def branch_line_data() -> tuple[np.ndarray, list[tuple[str, np.ndarray]]]:
    data = pd.read_csv(DATA / "e5_rho_paired_reproduction.csv")
    x = data["rho_env"].to_numpy()
    series = [
        ("Action-correlation increment", data["action_corr_increment"].to_numpy()),
        ("Total FP gain", data["total_FP_gain"].to_numpy()),
    ]
    return x, series
