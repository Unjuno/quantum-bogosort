"""E1: Pure QBS weighting, FOSD, and falsification stress tests."""
import numpy as np
import pandas as pd
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(20260817)

def sigmoid(x):
    x = np.clip(x, -40, 40)
    return 1/(1+np.exp(-x))

def z(x):
    return (x-x.mean())/x.std()

def sample_luck(kind, n):
    if kind=="Gaussian": x=rng.standard_normal(n)
    elif kind=="Student_t_df3": x=rng.standard_t(3,n)
    elif kind=="Bimodal":
        c=rng.random(n)<0.5
        x=np.where(c,rng.normal(-1.2,.7,n),rng.normal(1.2,.7,n))
    elif kind=="Skewed_log":
        r=np.exp(rng.normal(0,.8,n))
        x=np.log(r)+.35*(r-r.mean())/r.std()
    return z(x)

def wcdf(v,w,g):
    o=np.argsort(v); v=v[o]; w=w[o]
    c=np.cumsum(w)/w.sum()
    i=np.searchsorted(v,g,side="right")-1
    out=np.zeros(len(g)); ok=i>=0; out[ok]=c[i[ok]]
    return out

rows=[]
for kind in ["Gaussian","Student_t_df3","Bimodal","Skewed_log"]:
    for rep in range(6):
        L=sample_luck(kind,60000)
        Y=z(L+rng.standard_normal(len(L)))
        grid=np.linspace(*np.quantile(L,[.002,.998]),500)
        F0=wcdf(L,np.ones(len(L)),grid)
        for k in [.5,1,2,4]:
            S=.1+.9*sigmoid(k*(Y-np.median(Y)))
            F1=wcdf(L,S,grid)
            rows.append(dict(
                distribution=kind,replicate=rep,k=k,
                rho=np.corrcoef(Y,L)[0,1],
                mean_uplift=np.mean(L*S)/S.mean()-L.mean(),
                max_FOSD_violation=np.max(F1-F0)
            ))
pd.DataFrame(rows).to_csv(OUT/"e1_fosd_reproduction.csv",index=False)

U=rng.standard_normal(500000)
rows=[]
for strength in [0,.25,.5,.75,1]:
    Z=rng.standard_normal(len(U))
    S=.1+.9*sigmoid(strength*Z)
    rows.append(dict(
        selector_strength=strength,
        mean_uplift=np.mean(U*S)/S.mean()-U.mean(),
        corr=np.corrcoef(U,S)[0,1] if np.std(S)>0 else np.nan
    ))
pd.DataFrame(rows).to_csv(OUT/"e1_independence_null_reproduction.csv",index=False)

U=rng.standard_normal(500000)
grid=np.linspace(-3,3,1201)
F0=wcdf(U,np.ones(len(U)),grid)
selectors={
    "monotone":.1+.9*sigmoid(2*U),
    "middle":.1+.9*np.exp(-(U/.9)**2),
    "oscillatory":np.clip(.55+.35*np.sin(2.5*U),.05,1),
}
rows=[]
for name,S in selectors.items():
    F1=wcdf(U,S,grid)
    rows.append(dict(
        selector=name,
        mean_uplift=np.mean(U*S)/S.mean()-U.mean(),
        max_FOSD_violation=np.max(F1-F0),
        cdf_crosses=bool(np.any(F1-F0>.002) and np.any(F1-F0<-.002))
    ))
pd.DataFrame(rows).to_csv(OUT/"e1_nonmonotone_counterexample_reproduction.csv",index=False)
print("E1 complete.")
