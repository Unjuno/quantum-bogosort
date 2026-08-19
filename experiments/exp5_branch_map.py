"""E5: Cross-branch recognition, paired q sweeps, and shared recognition.

All q values reuse the same primitive random arrays. This makes the q sweep a
paired counterfactual experiment rather than an unpaired seed sweep.

Outputs:
- e5_q_paired_reproduction.csv
- e5_rho_paired_reproduction.csv
- e5_shared_vs_independent_recognition.csv
- e5_shared_recognition_contrasts.csv
"""
from pathlib import Path
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)
SEED = 20260817
K = 18_000
M = 12
ALPHA = 0.10


def sigmoid(x):
    x = np.clip(x, -40, 40)
    return 1.0 / (1.0 + np.exp(-x))


def avg_pair_corr(a):
    c = np.corrcoef(a, rowvar=False)
    iu = np.triu_indices_from(c, k=1)
    return float(np.nanmean(c[iu]))


def qbs_term(u, s):
    es = np.mean(s)
    return (np.mean(u * s) - np.mean(u) * es) / es


rng = np.random.default_rng(SEED)
common_factor = rng.standard_normal((K, 1))
local_factor = rng.standard_normal((K, M))
obs_noise = rng.standard_normal((K, M))
future_noise = rng.standard_normal((K, M))
baseline_action_u = rng.random((K, M))
execution_u = rng.random((K, M))
recognition_shared_u = rng.random((K, 1))
recognition_ind_u = rng.random((K, M))


def state_from_rho(rho):
    return np.sqrt(rho) * common_factor + np.sqrt(max(0.0, 1.0 - rho)) * local_factor


def components(rho):
    B = state_from_rho(rho)
    O = B + 0.65 * obs_noise
    Ubase = -B + 0.55 * future_noise
    A0 = (baseline_action_u < 0.5).astype(float)
    Aad = (O > 0).astype(float)
    return B, O, Ubase, A0, Aad


def utility(Ubase, B, A):
    return Ubase + 0.85 * A * np.maximum(B, 0) - 0.08 * A


B, O, Ubase, A0, Aad = components(0.60)
U0 = utility(Ubase, B, A0)
u0 = U0.ravel()
base_corr = avg_pair_corr(A0)

q_rows = []
for q in np.linspace(0, 1, 11):
    execute = execution_u < q
    A1 = np.where(execute, Aad, A0)
    U1 = utility(Ubase, B, A1)
    Y1 = -O + 0.85 * A1 * np.maximum(O, 0) - 0.08 * A1
    Sfull = ALPHA + (1 - ALPHA) * sigmoid(2.2 * Y1)
    S1 = 1 - q * (1 - Sfull)
    u1 = U1.ravel()
    s1 = S1.ravel()
    policy_gain = u1.mean() - u0.mean()
    qbs_gain = qbs_term(u1, s1)
    total_gain = np.mean(u1 * s1) / np.mean(s1) - u0.mean()
    q_rows.append({
        "q": q,
        "decision_corr_increment": avg_pair_corr(A1) - base_corr,
        "fraction_policy_changed": np.mean(A1 != A0),
        "policy_gain": policy_gain,
        "QBS_gain": qbs_gain,
        "total_FP_gain": total_gain,
        "decomposition_error": total_gain - (policy_gain + qbs_gain),
        "E[S]": np.mean(s1),
    })

q_df = pd.DataFrame(q_rows)
if q_df["decomposition_error"].abs().max() > 1e-12:
    raise RuntimeError("E5 q-sweep decomposition failed")
q0 = q_df.loc[np.isclose(q_df["q"], 0)].iloc[0]
for field in ["decision_corr_increment", "fraction_policy_changed", "policy_gain", "QBS_gain", "total_FP_gain"]:
    if abs(q0[field]) > 1e-12:
        raise RuntimeError(f"E5 q=0 null failed for {field}")
if abs(q0["E[S]"] - 1.0) > 1e-12:
    raise RuntimeError("E5 q=0 accessibility baseline failed")
q_df.to_csv(OUT / "e5_q_paired_reproduction.csv", index=False)

rho_rows = []
for rho in [0.0, 0.15, 0.35, 0.60, 0.80, 0.95]:
    B, O, Ubase, A0, Aad = components(rho)
    U0 = utility(Ubase, B, A0)
    U1 = utility(Ubase, B, Aad)
    Y1 = -O + 0.85 * Aad * np.maximum(O, 0) - 0.08 * Aad
    S1 = ALPHA + (1 - ALPHA) * sigmoid(2.2 * Y1)
    u0 = U0.ravel()
    u1 = U1.ravel()
    s1 = S1.ravel()
    policy_gain = u1.mean() - u0.mean()
    qbs_gain = qbs_term(u1, s1)
    rho_rows.append({
        "rho_env": rho,
        "action_corr_baseline": avg_pair_corr(A0),
        "action_corr_recognition": avg_pair_corr(Aad),
        "action_corr_increment": avg_pair_corr(Aad) - avg_pair_corr(A0),
        "policy_gain": policy_gain,
        "QBS_gain": qbs_gain,
        "total_FP_gain": policy_gain + qbs_gain,
    })

rho_df = pd.DataFrame(rho_rows)
if not np.all(np.diff(rho_df["action_corr_increment"].to_numpy()) > 0):
    raise RuntimeError("E5 action-correlation increment no longer rises with environmental correlation")
if rho_df["action_corr_increment"].iloc[-1] < .4:
    raise RuntimeError("E5 high-correlation action-coherence control weakened unexpectedly")
if np.ptp(rho_df["total_FP_gain"].to_numpy()) > .01:
    raise RuntimeError("E5 marginal FP gain is no longer approximately flat across rho sweep")
rho_df.to_csv(OUT / "e5_rho_paired_reproduction.csv", index=False)

B, O, Ubase, A0, Aad = components(0.60)
shared_rows = []
for p in [0.10, 0.25, 0.50, 0.75, 0.90]:
    R_shared = np.repeat(recognition_shared_u < p, M, axis=1)
    R_ind = recognition_ind_u < p
    for mode, Rmap in [
        ("shared_recognition", R_shared),
        ("independent_recognition", R_ind),
    ]:
        A = np.where(Rmap, Aad, A0)
        U = utility(Ubase, B, A)
        Y = -O + 0.85 * A * np.maximum(O, 0) - 0.08 * A
        Sfull = ALPHA + (1 - ALPHA) * sigmoid(2.2 * Y)
        S = np.where(Rmap, Sfull, 1.0)
        u = U.ravel()
        s = S.ravel()
        shared_rows.append({
            "recognition_probability_target": p,
            "mode": mode,
            "fraction_recognized": np.mean(Rmap),
            "action_pair_corr": avg_pair_corr(A),
            "recognition_pair_corr": avg_pair_corr(Rmap.astype(float)),
            "global_mean_U": np.mean(u),
            "FP_mean_U": np.mean(u * s) / np.mean(s),
            "QBS_conditional_uplift": qbs_term(u, s),
        })

shared_df = pd.DataFrame(shared_rows)
if shared_df.groupby("recognition_probability_target")["fraction_recognized"].apply(lambda x: x.max() - x.min()).max() > .01:
    raise RuntimeError("E5 shared/independent recognition prevalence is no longer matched")
shared_df.to_csv(OUT / "e5_shared_vs_independent_recognition.csv", index=False)

contrasts = []
for p, g in shared_df.groupby("recognition_probability_target"):
    sh = g[g["mode"] == "shared_recognition"].iloc[0]
    ind = g[g["mode"] == "independent_recognition"].iloc[0]
    contrasts.append({
        "recognition_probability_target": p,
        "delta_action_pair_corr_shared_minus_ind": sh["action_pair_corr"] - ind["action_pair_corr"],
        "delta_recognition_pair_corr": sh["recognition_pair_corr"] - ind["recognition_pair_corr"],
        "delta_QBS_uplift": sh["QBS_conditional_uplift"] - ind["QBS_conditional_uplift"],
        "delta_FP_mean": sh["FP_mean_U"] - ind["FP_mean_U"],
    })

contrast_df = pd.DataFrame(contrasts)
if (contrast_df["delta_action_pair_corr_shared_minus_ind"] <= 0).any():
    raise RuntimeError("E5 shared recognition no longer raises cross-copy action correlation")
if (contrast_df["delta_recognition_pair_corr"] < .95).any():
    raise RuntimeError("E5 recognition-correlation contrast weakened unexpectedly")
if contrast_df["delta_FP_mean"].abs().max() > .01:
    raise RuntimeError("E5 matched-marginal FP contrast exceeded tolerance")
contrast_df.to_csv(OUT / "e5_shared_recognition_contrasts.csv", index=False)
print("E5 complete.")
