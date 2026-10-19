"""Blind tide test (Amendment 1 method). Run: python3 experiments/tides/tide_test.py"""
import numpy as np, glob, math, os
HERE=os.path.dirname(os.path.abspath(__file__))
from scipy.optimize import least_squares
pred={'M2':28.9841042,'S2':30.0,'N2':28.4397295,'K1':15.0410686,'O1':13.9430356}
y=[]
_csv=os.path.join(HERE,'noaa_9414290_sanfrancisco_2023_hourly.csv')
if not os.path.exists(_csv): raise SystemExit('data missing: run  python3 experiments/tides/fetch_data.py  first')
for f in [_csv]:
    for line in open(f).read().splitlines()[1:]: y.append(float(line.split(',')[1]))
y=np.array(y); t=np.arange(len(y),dtype=float)
def model(p,tt):
    out=np.full_like(tt,p[0])
    for i in range((len(p)-1)//3):
        w,a,b=p[1+3*i:4+3*i]; out+=a*np.cos(w*tt)+b*np.sin(w*tt)
    return out
def clean(tt,yy,k=5,step=0.002):
    grid=np.radians(np.r_[np.arange(12,17,step),np.arange(27,31,step)])
    r=yy-yy.mean(); found=[]
    for _ in range(k):
        C=np.cos(np.outer(grid,tt)); S=np.sin(np.outer(grid,tt))
        P=(C@r)**2+(S@r)**2; w=grid[np.argmax(P)]
        A=np.c_[np.cos(w*tt),np.sin(w*tt)]; c,*_=np.linalg.lstsq(A,r,rcond=None)
        r=r-A@c; found.append(w)
    p0=[yy.mean()]
    for w in found:
        A=np.c_[np.cos(w*tt),np.sin(w*tt)]; c,*_=np.linalg.lstsq(A,yy-yy.mean(),rcond=None); p0+=[w,*c]
    fit=least_squares(lambda p: model(p,tt)-yy,p0,x_scale='jac',max_nfev=20000)
    out=[(math.degrees(fit.x[1+3*i]),math.hypot(*fit.x[2+3*i:4+3*i])) for i in range(k)]
    return sorted(out), np.std(fit.fun), np.std(yy)
def match(found):
    m={}
    for n,v in pred.items():
        sp,a=min(found,key=lambda s:abs(s[0]-v)); m[n]=(sp,a)
    return m
full,res,sd=clean(t,y)
print(f'full year: data sd {sd:.3f} m, residual rms {res:.3f} m')
print('blind peaks found (deg/h, amp m):',[(round(s,5),round(a,3)) for s,a in full])
Q=[]
for k in range(4):
    sl=slice(k*len(y)//4,(k+1)*len(y)//4)
    Q.append(match(clean(t[sl],y[sl])[0]))
F=match(full)
print(f"{'':4s}{'predicted':>12s}{'year fit':>12s}{'quarters':>12s}{'SE':>10s}{'z':>7s}{'amp m':>7s}")
for n,v in pred.items():
    qs=np.array([q[n][0] for q in Q]); se=qs.std(ddof=1)/2; z=(qs.mean()-v)/se
    print(f"{n:4s}{v:12.6f}{F[n][0]:12.6f}{qs.mean():12.6f}{se:10.1e}{z:7.2f}{F[n][1]:7.3f}  {'PASS' if abs(z)<=2 else 'FAIL'}   year-fit offset {F[n][0]-v:+.1e}")
th=math.radians(F['M2'][0]); print(f"M2: theta = {th:.6f} rad per hour, tau = 2cos(theta) = {2*math.cos(th):.6f}  (elliptic), period {360/F['M2'][0]:.6f} h vs predicted 12.420601")
