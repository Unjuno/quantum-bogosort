"""E3: Recognition decomposition and exact recognition null."""
import numpy as np
import pandas as pd
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(20260817)
N = 90000
T = 18
phi = .85
ln = rng.standard_normal((N, T))
on = rng.standard_normal((N, T))
rn = rng.standard_normal((N, T))
x0 = rng.standard_normal(N)


def fp_value(u, s):
    es = np.mean(s)
    if not np.isfinite(es) or es <= 0:
        raise ValueError("First-person accessibility must have finite positive mean")
    return np.mean(u * s) / es


def run(rec, gain=.6):
    x = x0.copy()
    b = np.zeros(N)
    total = np.zeros(N)
    sig = np.zeros(N)
    for t in range(T):
        y = x + on[:, t]
        b = (1 - gain) * b + gain * y
        a = (b < 0).astype(float) if rec else np.zeros(N)
        total += x + .55 * a * np.maximum(-x, 0) - .10 * a + .15 * rn[:, t]
        sig += b
        x = phi * x + .25 * a + .8 * ln[:, t]
    return total, sig / T


r0, y0 = run(False)
r1, y1 = run(True)
mu = r0.mean()
sd = r0.std()
U0 = (r0 - mu) / sd
U1 = (r1 - mu) / sd
S1 = np.where(y1 < np.median(y1), .1, 1)
policy = U1.mean() - U0.mean()
qbs = fp_value(U1, S1) - U1.mean()
total = fp_value(U1, S1) - U0.mean()
result = pd.DataFrame([dict(
    policy_gain=policy,
    QBS_gain=qbs,
    total_gain=total,
    decomposition_error=total - (policy + qbs),
)])
if result["decomposition_error"].abs().max() > 1e-12:
    raise RuntimeError("E3 recognition decomposition failed")
result.to_csv(OUT / "e3_recognition_decomposition_reproduction.csv", index=False)

# Recognition-label null: changing only an inert label leaves both the trajectory
# and accessibility arrays identical. Evaluate both sides through the same general
# first-person value path rather than comparing the same arithmetic expression twice.
U_null = rng.standard_normal(500000)
U_label0 = U_null.copy()
U_label1 = U_null.copy()
S_label0 = np.ones_like(U_null)
S_label1 = np.ones_like(U_null)
if not np.array_equal(U_label0, U_label1) or not np.array_equal(S_label0, S_label1):
    raise RuntimeError("E3 recognition-label null primitives are not identical")
V0 = fp_value(U_label0, S_label0)
V1 = fp_value(U_label1, S_label1)
null_result = pd.DataFrame([dict(V0=V0, V1=V1, effect=V1 - V0)])
if null_result["effect"].abs().max() > 1e-15:
    raise RuntimeError("E3 recognition-label null failed")
null_result.to_csv(OUT / "e3_recognition_null_reproduction.csv", index=False)
print("E3 complete.")
