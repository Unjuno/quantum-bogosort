"""E4: Policy–QBS interaction theorem and adaptive rescue sign."""
import numpy as np, pandas as pd
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/"data"/"processed"; OUT.mkdir(parents=True,exist_ok=True)
rng=np.random.default_rng(20260817); N=400000
x=rng.standard_normal(N); fn=rng.standard_normal(N)
U0=.8*x+.6*fn; U0=(U0-U0.mean())/U0.std()
Y=x+.8*rng.standard_normal(N); S=np.where(Y<np.median(Y),.1,1)
bad=np.maximum(-Y,0); bad/=bad.std()
good=np.maximum(Y,0); good/=good.std()
eps=.15*rng.standard_normal(N)
Ds={"rescue_bad":.45*bad+eps,
    "neutral":.45*rng.standard_normal(N),
    "amplify_good":.45*good+eps}
rows=[]
for name,D in Ds.items():
    U1=U0+D
    q0=(np.mean(U0*S)-U0.mean()*S.mean())/S.mean()
    q1=(np.mean(U1*S)-U1.mean()*S.mean())/S.mean()
    I=q1-q0
    pred=(np.mean(D*S)-D.mean()*S.mean())/S.mean()
    rows.append(dict(policy=name,corr_DS=np.corrcoef(D,S)[0,1],
                     interaction=I,predicted=pred,error=I-pred))
pd.DataFrame(rows).to_csv(OUT/"e4_interaction_reproduction.csv",index=False)
print("E4 complete.")
