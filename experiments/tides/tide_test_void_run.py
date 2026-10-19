"""VOID RUN kept for the record: the originally pre-registered fit, which failed to converge
(see PREREGISTRATION_tides.md, Amendment 1). Expects monthly files in tides/; not used for the verdict."""
import numpy as np, glob, math
from scipy.optimize import least_squares
pred={'M2':28.9841042,'S2':30.0,'N2':28.4397295,'K1':15.0410686,'O1':13.9430356}
names=list(pred)
rows=[]
for f in sorted(glob.glob('tides/sf_2023_*.csv')):
    for line in open(f).read().splitlines()[1:]:
        p=line.split(',')
        try: rows.append(float(p[1]))
        except: rows.append(np.nan)
y=np.array(rows); t=np.arange(len(y),dtype=float)   # hours from 2023-01-01 00:00 GMT
ok=~np.isnan(y); print('samples',len(y),'missing',(~ok).sum())
def fit(tt,yy):
    w0=np.radians([pred[n]*1.005 for n in names])        # start 0.5% off, as pre-registered
    def model(p,tt):
        out=np.full_like(tt,p[0])
        for i in range(5):
            w,a,b=p[1+3*i:4+3*i]; out+=a*np.cos(w*tt)+b*np.sin(w*tt)
        return out
    # linear amplitudes first at the offset frequencies, then free nonlinear fit
    p0=[yy.mean()]
    for w in w0: p0+= [w,0.1,0.1]
    r=least_squares(lambda p: model(p,tt)-yy, p0, x_scale='jac', max_nfev=20000)
    sp=np.degrees([r.x[1+3*i] for i in range(5)])
    amp=[math.hypot(r.x[2+3*i],r.x[3+3*i]) for i in range(5)]
    return sp,amp,np.std(r.fun)
sp,amp,res=fit(t[ok],y[ok])
print(f'full-year residual rms {res:.3f} m')
q=[]
for k in range(4):
    sl=slice(k*len(y)//4,(k+1)*len(y)//4); m=ok[sl]
    q.append(fit(t[sl][m],y[sl][m])[0])
q=np.array(q); se=q.std(axis=0,ddof=1)/2
print(f"{'':4s}{'predicted':>13s}{'fitted (year)':>15s}{'quarters mean':>15s}{'SE':>11s}{'z':>8s}  amp(m)  verdict")
for i,n in enumerate(names):
    z=(q[:,i].mean()-pred[n])/se[i]
    print(f"{n:4s}{pred[n]:13.7f}{sp[i]:15.7f}{q[:,i].mean():15.7f}{se[i]:11.2e}{z:8.2f}  {amp[i]:.3f}   {'PASS' if abs(z)<=2 else 'FAIL'}")
th=math.radians(sp[0]); print(f'M2 per-hour angle theta={th:.6f} rad, tau=2cos(theta)={2*math.cos(th):.6f}, elliptic (|tau|<2), period {360/sp[0]:.5f} h')
# trace-map identity on the real record: x[n+1]+x[n-1] vs tau*x[n] using only M2 band? report raw check
