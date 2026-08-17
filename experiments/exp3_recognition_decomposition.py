"""E3: Recognition decomposition and exact recognition null."""
import numpy as np, pandas as pd
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/"data"/"processed"; OUT.mkdir(parents=True,exist_ok=True)
rng=np.random.default_rng(20260817)
N=90000; T=18; phi=.85
ln=rng.standard_normal((N,T)); on=rng.standard_normal((N,T)); rn=rng.standard_normal((N,T)); x0=rng.standard_normal(N)

def run(rec,gain=.6):
    x=x0.copy(); b=np.zeros(N); total=np.zeros(N); sig=np.zeros(N)
    for t in range(T):
        y=x+on[:,t]; b=(1-gain)*b+gain*y
        a=(b<0).astype(float) if rec else np.zeros(N)
        total+=x+.55*a*np.maximum(-x,0)-.10*a+.15*rn[:,t]
        sig+=b; x=phi*x+.25*a+.8*ln[:,t]
    return total,sig/T

r0,y0=run(False); r1,y1=run(True)
mu=r0.mean(); sd=r0.std(); U0=(r0-mu)/sd; U1=(r1-mu)/sd
S1=np.where(y1<np.median(y1),.1,1)
policy=U1.mean()-U0.mean()
cov=np.mean(U1*S1)-U1.mean()*S1.mean()
qbs=cov/S1.mean()
total=np.mean(U1*S1)/S1.mean()-U0.mean()
pd.DataFrame([dict(policy_gain=policy,QBS_gain=qbs,total_gain=total,
                   decomposition_error=total-(policy+qbs))]).to_csv(
    OUT/"e3_recognition_decomposition_reproduction.csv",index=False)

U=rng.standard_normal(500000)
V0=U.mean(); V1=U.mean()
pd.DataFrame([dict(V0=V0,V1=V1,effect=V1-V0)]).to_csv(
    OUT/"e3_recognition_null_reproduction.csv",index=False)
print("E3 complete.")
