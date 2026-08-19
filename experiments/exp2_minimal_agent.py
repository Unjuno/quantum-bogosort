"""E2: Minimal learned agent with nonlinear world structure."""
import numpy as np
import pandas as pd
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(20260817)


def make(n, sigma):
    x1 = rng.standard_normal(n)
    x2 = rng.standard_normal(n)
    raw = x1 * x2 + sigma * rng.standard_normal(n)
    L = (raw - raw.mean()) / raw.std()
    Xlin = np.c_[np.ones(n), x1, x2]
    Xint = np.c_[np.ones(n), x1, x2, x1 * x2]
    return Xlin, Xint, L


def fit(X, y):
    return np.linalg.solve(X.T @ X + 1e-4 * np.eye(X.shape[1]), X.T @ y)


rows = []
for sigma in [.25, .5, 1, 2]:
    for rep in range(12):
        Xl0, Xi0, L0 = make(40000, sigma)
        Xl, Xi, L = make(100000, sigma)
        scores = {
            "linear_3param": Xl @ fit(Xl0, L0),
            "interaction_4param": Xi @ fit(Xi0, L0),
            "random_control": rng.standard_normal(len(L)),
        }
        for name, Y in scores.items():
            S = np.where(Y < 0, .1, 1)
            rows.append(dict(
                noise_sigma=sigma,
                replicate=rep,
                evaluator=name,
                corr=np.corrcoef(Y, L)[0, 1],
                mean_uplift=np.mean(L * S) / S.mean() - L.mean(),
                tail_gain=np.mean((L >= 1) * S) / S.mean() - np.mean(L >= 1),
            ))
result = pd.DataFrame(rows)
summary = result.groupby(["noise_sigma", "evaluator"])[["corr", "mean_uplift"]].mean()
interaction = summary.xs("interaction_4param", level="evaluator")
linear = summary.xs("linear_3param", level="evaluator")
random = summary.xs("random_control", level="evaluator")
if (interaction["corr"] <= .4).any() or (interaction["mean_uplift"] <= .2).any():
    raise RuntimeError("E2 interaction-capable evaluator lost predictive alignment")
if not np.all(np.diff(interaction["corr"].to_numpy()) < 0):
    raise RuntimeError("E2 interaction-capable correlation no longer weakens with noise")
if linear["corr"].abs().max() > .02 or random["corr"].abs().max() > .02:
    raise RuntimeError("E2 misspecified/random correlation control exceeded tolerance")
if linear["mean_uplift"].abs().max() > .01 or random["mean_uplift"].abs().max() > .01:
    raise RuntimeError("E2 misspecified/random uplift control exceeded tolerance")
result.to_csv(OUT / "e2_minimal_agent_reproduction.csv", index=False)
print("E2 complete.")
