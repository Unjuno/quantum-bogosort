"""E5: Cross-branch recognition map and probabilistic QBS execution."""
import numpy as np, pandas as pd
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/"data"/"processed"; OUT.mkdir(parents=True,exist_ok=True)
K=18000; M=12; alpha=.1

def sigmoid(x):
    x=np.clip(x,-40,40); return 1/(1+np.exp(-x))

def avgcorr(A):
    C=np.corrcoef(A,rowvar=False); i=np.triu_indices_from(C,1)
    return np.nanmean(C[i])

def run(q,seed=20260817,rho=.6):
    rng=np.random.default_rng(seed)
    C=rng.standard_normal((K,1)); E=rng.standard_normal((K,M))
    B=np.sqrt(rho)*C+np.sqrt(1-rho)*E
    O=B+.65*rng.standard_normal((K,M))
    Ubase=-B+.55*rng.standard_normal((K,M))
    A0=(rng.random((K,M))<.5).astype(float); Aad=(O>0).astype(float)
    ex=rng.random((K,M))<q; A1=np.where(ex,Aad,A0)
    U0=Ubase+.85*A0*np.maximum(B,0)-.08*A0
    U1=Ubase+.85*A1*np.maximum(B,0)-.08*A1
    Y=-O+.85*A1*np.maximum(O,0)-.08*A1
    Sfull=alpha+(1-alpha)*sigmoid(2.2*Y)
    S=1-q*(1-Sfull)
    u0=U0.ravel(); u1=U1.ravel(); s=S.ravel()
    pg=u1.mean()-u0.mean()
    qg=(np.mean(u1*s)-u1.mean()*s.mean())/s.mean()
    return dict(q=q,decision_corr_increment=avgcorr(A1)-avgcorr(A0),
                policy_gain=pg,QBS_gain=qg,total_gain=pg+qg)
rows=[run(float(q),20260817+i) for i,q in enumerate(np.linspace(0,1,11))]
pd.DataFrame(rows).to_csv(OUT/"e5_branch_map_reproduction.csv",index=False)
print("E5 complete.")
