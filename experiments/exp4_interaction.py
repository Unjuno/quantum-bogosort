"""E4: Policy-QBS interaction identities and adaptive-rescue sign tests.

Outputs:
- e4_fixed_selector_sign_reproduction.csv
- e4_general_interaction_reproduction.csv

The first output verifies the fixed-selector identity
    I = Cov(D,S)/E[S]
for rescue-bad, neutral, and amplify-good policy increments.

The second output verifies the general S0 != S1 decomposition
    I = Cov(D,S0)/E[S0] + [Q(U1,S1) - Q(U1,S0)].
"""
from pathlib import Path
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)
SEED = 20260817
N = 400_000
ALPHA = 0.10


def sigmoid(x):
    x = np.clip(x, -40, 40)
    return 1.0 / (1.0 + np.exp(-x))


def qbs_term(u, s):
    es = np.mean(s)
    return (np.mean(u * s) - np.mean(u) * es) / es


rng = np.random.default_rng(SEED)
x = rng.standard_normal(N)
future_noise = rng.standard_normal(N)
selector_noise = rng.standard_normal(N)

U0 = 0.8 * x + 0.6 * future_noise
U0 = (U0 - U0.mean()) / U0.std()
Y0 = U0 + 0.70 * selector_noise
S0 = ALPHA + (1 - ALPHA) * sigmoid(1.8 * Y0)

badness = np.maximum(-Y0, 0.0)
goodness = np.maximum(Y0, 0.0)
badness /= badness.std() + 1e-12
goodness /= goodness.std() + 1e-12
common_noise = 0.15 * rng.standard_normal(N)

increments = {
    "rescue_bad": 0.45 * badness + common_noise,
    "neutral": 0.45 * rng.standard_normal(N),
    "amplify_good": 0.45 * goodness + common_noise,
}

fixed_rows = []
for name, D in increments.items():
    U1 = U0 + D
    interaction = qbs_term(U1, S0) - qbs_term(U0, S0)
    predicted = (np.mean(D * S0) - np.mean(D) * np.mean(S0)) / np.mean(S0)
    fixed_rows.append({
        "policy": name,
        "Corr(D,S)": np.corrcoef(D, S0)[0, 1],
        "interaction": interaction,
        "predicted_Cov_over_ES": predicted,
        "identity_error": interaction - predicted,
    })

fixed_df = pd.DataFrame(fixed_rows).set_index("policy")
if fixed_df["identity_error"].abs().max() > 1e-12:
    raise RuntimeError("E4 fixed-selector identity failed")
if fixed_df.loc["rescue_bad", "interaction"] >= 0:
    raise RuntimeError("E4 rescue-bad interaction lost its negative sign")
if abs(fixed_df.loc["neutral", "interaction"]) > .01:
    raise RuntimeError("E4 neutral interaction exceeded tolerance")
if fixed_df.loc["amplify_good", "interaction"] <= 0:
    raise RuntimeError("E4 amplify-good interaction lost its positive sign")
fixed_df.reset_index().to_csv(
    OUT / "e4_fixed_selector_sign_reproduction.csv", index=False
)

D = 0.52 * badness + 0.10 * rng.standard_normal(N)
U1 = U0 + D
Y1 = Y0 + 0.75 * D + 0.10 * rng.standard_normal(N)
S1 = ALPHA + (1 - ALPHA) * sigmoid(1.8 * Y1)

Q0S0 = qbs_term(U0, S0)
Q1S0 = qbs_term(U1, S0)
Q1S1 = qbs_term(U1, S1)
interaction = Q1S1 - Q0S0
targeting = (np.mean(D * S0) - np.mean(D) * np.mean(S0)) / np.mean(S0)
selector_map_shift = Q1S1 - Q1S0

general_df = pd.DataFrame([{
    "Corr(D,S0)": np.corrcoef(D, S0)[0, 1],
    "Q(U0,S0)": Q0S0,
    "Q(U1,S0)": Q1S0,
    "Q(U1,S1)": Q1S1,
    "interaction": interaction,
    "targeting_term": targeting,
    "selector_map_shift": selector_map_shift,
    "selector_changed_fraction_gt_1e-6": np.mean(np.abs(S1 - S0) > 1e-6),
    "decomposition_error": interaction - (targeting + selector_map_shift),
}])
if general_df["decomposition_error"].abs().max() > 1e-12:
    raise RuntimeError("E4 changing-selector decomposition failed")
if general_df.loc[0, "selector_changed_fraction_gt_1e-6"] < .9:
    raise RuntimeError("E4 changing-selector control no longer changes the selector map")
general_df.to_csv(OUT / "e4_general_interaction_reproduction.csv", index=False)

print("E4 complete.")
