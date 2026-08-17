"""E2: Minimal learned agent with nonlinear world structure."""
import numpy as np, pandas as pd
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/"data"/"processed"; OUT.mkdir(parents=True,exist_ok=True)
rng=np.random.default_rng(20260817)

def make(n,sigma):
    x1=rng.standard_normal(n); x2=rng.standard_normal(n)
    raw=x1*x2+sigma*rng.standard_normal(n)
    L=(raw-raw.mean())/raw.std()
    Xlin=np.c_[np.ones(n),x1,x2]
    Xint=np.c_[np.ones(n),x1,x2,x1*x2]
    return Xlin,Xint,L

def fit(X,y):
    return np.linalg.solve(X.T@X+1e-4*np.eye(X.shape[1]),X.T@y)

rows=[]
for sigma in [.25,.5,1,2]:
    for rep in range(12):
        Xl0,Xi0,L0=make(40000,sigma); Xl,Xi,L=make(100000,sigma)
        scores={
            "linear_3param":Xl@fit(Xl0,L0),
            "interaction_4param":Xi@fit(Xi0,L0),
            "random_control":rng.standard_normal(len(L))
        }
        for name,Y in scores.items():
            S=np.where(Y<0,.1,1)
            rows.append(dict(
                noise_sigma=sigma,replicate=rep,evaluator=name,
                corr=np.corrcoef(Y,L)[0,1],
                mean_uplift=np.mean(L*S)/S.mean()-L.mean(),
                tail_gain=np.mean((L>=1)*S)/S.mean()-np.mean(L>=1)
            ))
pd.DataFrame(rows).to_csv(OUT/"e2_minimal_agent_reproduction.csv",index=False)
print("E2 complete.")
