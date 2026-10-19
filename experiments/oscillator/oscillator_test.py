#!/usr/bin/env python3
"""
oscillator_test.py — run the pre-registered trace-map test on a real recording.

Input : a CSV with a time column and one or more value columns
        (phyphox "Acceleration" / "Linear Acceleration" export works as is).
Output: the fitted per-sample angle theta = omega*dt with an error bar, the
        normalised trace tau = 2 cos(theta), the damping per sample, and a
        PASS / FAIL against ONE rational angle 2*pi*p/q chosen in advance.

What it does, in order (no step looks at the verdict before it is computed):
  1. load, pick the value column (given, or the one with most variance)
  2. check sampling: report median dt and jitter, resample to a uniform grid
  3. remove the offset/drift (gravity, slow tilt) with a low-order polynomial
  4. fit x[n+1] = c1*x[n] + c2*x[n-1]   (AR(2); total least squares by default)
       damping per sample  r   = sqrt(-c2)
       normalised trace    tau = c1 / r          (det normalisation)
       angle per sample    theta = arccos(tau/2)
  5. error bar from K independent segments (spread of theta across segments)
  6. cross-check: FFT peak frequency (independent of the AR fit)
  7. verdict: PASS if |theta - 2*pi*p/q| <= 2 * SE, else FAIL

Honest scope (from the pre-registration review):
  x[n+1] = tau*x[n] - x[n-1] holds for ANY sampled sinusoid, so a PASS shows the
  oscillator is close to linear and its sampled angle sits where you set it
  (via pendulum length and sample rate). It does not show the trace map is a
  law of nature. A FAIL means the angle is outside the error bar: report it.

Usage
  python oscillator_test.py run.csv --p 1 --q 100
  python oscillator_test.py run.csv --p 1 --q 100 --col "Acceleration y (m/s^2)"
  python oscillator_test.py r1.csv r2.csv r3.csv --p 1 --q 100     # several runs
  python oscillator_test.py r1.csv r2.csv --f 1.0                   # predicted Hz instead
  python oscillator_test.py --selftest                             # synthetic check

Choosing p/q in advance: theta = 2*pi*dt/T. With phyphox at ~100 Hz (dt = 0.01 s),
a pendulum of period T = 1.00 s gives theta = 2*pi/100 -> p=1, q=100. Small-angle
period T = 2*pi*sqrt(L/g), so L = g*(T/2pi)^2 = 0.248 m for T = 1 s. Write p, q
and L down BEFORE recording. (Note: tangential acceleration oscillates at the
pendulum frequency; the radial/centripetal component at TWICE it.)
"""
import argparse
import csv
import math
import sys

import numpy as np


# ---------------------------------------------------------------- loading
def load_csv(path, col=None):
    with open(path, newline="", encoding="utf-8-sig") as f:
        sample = f.read(4096)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        except csv.Error:
            dialect = csv.excel
        rows = list(csv.reader(f, dialect))
    header, data = rows[0], rows[1:]
    arr = []
    for r in data:
        try:
            arr.append([float(v) for v in r])
        except ValueError:
            continue
    arr = np.array(arr)
    if arr.ndim != 2 or arr.shape[1] < 2:
        sys.exit(f"{path}: need a time column plus at least one value column")
    t = arr[:, 0]
    if col is None:
        j = 1 + int(np.argmax(arr[:, 1:].var(axis=0)))
    else:
        if col not in header:
            sys.exit(f"{path}: column {col!r} not found. Columns: {header}")
        j = header.index(col)
    return t, arr[:, j], header[j]


# ---------------------------------------------------------------- steps
def resample(t, x):
    dts = np.diff(t)
    dt = float((t[-1] - t[0]) / (len(t) - 1))   # mean rate; median is quantised by timestamp rounding
    jitter = float(np.std(dts) / dt)
    grid = np.arange(t[0], t[-1], dt)
    return grid, np.interp(grid, t, x), dt, jitter


def detrend(x, deg=2):
    n = np.arange(len(x))
    return x - np.polyval(np.polyfit(n, x, deg), n)


def ar2(x, method="tls"):
    """Fit x[n+1] = c1 x[n] + c2 x[n-1]. Returns c1, c2."""
    X = np.c_[x[2:], x[1:-1], x[:-2]]
    if method == "ols":
        A = X[:, 1:]
        c, *_ = np.linalg.lstsq(A, X[:, 0], rcond=None)
        return float(c[0]), float(c[1])
    X = X - X.mean(axis=0)
    _, _, vt = np.linalg.svd(X, full_matrices=False)
    v = vt[-1]
    return float(-v[1] / v[0]), float(-v[2] / v[0])


def read_angle(c1, c2):
    if c2 >= 0:
        return None
    r = math.sqrt(-c2)
    tau = c1 / r
    if abs(tau) >= 2:
        return dict(r=r, tau=tau, theta=None)
    return dict(r=r, tau=tau, theta=math.acos(tau / 2))


def fft_angle(x):
    n = len(x)
    w = np.hanning(n)
    X = np.abs(np.fft.rfft(x * w))
    k = int(np.argmax(X[1:])) + 1
    if 1 <= k < len(X) - 1:  # parabolic interpolation of the peak
        a, b, c = np.log(X[k - 1] + 1e-300), np.log(X[k] + 1e-300), np.log(X[k + 1] + 1e-300)
        k = k + 0.5 * (a - c) / (a - 2 * b + c)
    return 2 * math.pi * k / n


def bandpass(x, theta0, width=0.3):
    """Keep only frequencies within +/- width*theta0 of the main peak."""
    X = np.fft.rfft(x)
    w = 2 * math.pi * np.arange(len(X)) / len(x)
    X[np.abs(w - theta0) > width * theta0] = 0
    return np.fft.irfft(X, len(x))


def trace_reading(x, theta0, method):
    """Band-pass around the peak, decimate to ~6 samples/cycle (well-conditioned
    trace), fit AR(2), and convert the angle back to the original sampling."""
    D = max(1, int(round((math.pi / 3) / theta0)))
    xb = bandpass(x, theta0)[::D]
    a = read_angle(*ar2(xb, method))
    if not a or a["theta"] is None:
        return a
    return dict(r=a["r"] ** (1 / D), tau=2 * math.cos(a["theta"] / D),
                theta=a["theta"] / D, D=D, tau_decimated=a["tau"])


def nls_angle(x, theta0):
    """Independent cross-check: damped-sinusoid least squares."""
    try:
        from scipy.optimize import curve_fit
    except ImportError:
        return None
    n = np.arange(len(x), dtype=float)
    f = lambda n, A, th, ph, lam: A * np.exp(-lam * n) * np.cos(th * n + ph)
    A0 = math.sqrt(2) * float(np.std(x))
    best = None
    for ph0 in (0, math.pi / 2, math.pi, 3 * math.pi / 2):
        try:
            p, _ = curve_fit(f, n, x, p0=[A0, theta0, ph0, 0.0], maxfev=20000)
            res = float(np.sum((f(n, *p) - x) ** 2))
            if best is None or res < best[0]:
                best = (res, p)
        except Exception:
            pass
    return None if best is None else (float(abs(best[1][1])), float(math.exp(-best[1][3])))


SE_FLOOR = 1e-9


def analyse(t, x, method, segments):
    g, xu, dt, jitter = resample(t, x)
    xu = detrend(xu)
    theta0 = fft_angle(xu)
    nls = nls_angle(xu, theta0)
    trace = trace_reading(xu, theta0, method)
    primary = nls[0] if nls else (trace["theta"] if trace else None)
    seg_thetas = []
    for s in np.array_split(xu, segments):
        if len(s) < 50:
            continue
        s = detrend(s)
        t0 = fft_angle(s)
        a = nls_angle(s, t0) if nls else None
        th = a[0] if a else (trace_reading(s, t0, method) or {}).get("theta")
        if th is not None:
            seg_thetas.append(th)
    se = float(np.std(seg_thetas, ddof=1) / math.sqrt(len(seg_thetas))) if len(seg_thetas) > 1 else float("nan")
    se = max(se, SE_FLOOR) if se == se else se
    return dict(dt=dt, jitter=jitter, n=len(xu), theta=primary, trace=trace, seg=seg_thetas,
                se=se, fft=theta0, nls=nls, duration=g[-1] - g[0])


def report(name, res, p, q, fpred=None, ferr=0.0):
    print(f"\n== {name}")
    print(f"  samples {res['n']}  duration {res['duration']:.2f} s  mean dt {res['dt']*1e3:.5f} ms  "
          f"dt jitter {100*res['jitter']:.2f}%")
    th, se, w = res["theta"], res["se"], res["trace"]
    if th is None:
        print("  no oscillation found: no angle to read")
        return None
    f = th / (2 * math.pi * res["dt"])
    cycles = f * res["duration"]
    src = "damped-sine fit" if res["nls"] else "AR(2) trace fit (scipy missing)"
    print(f"  theta = {th:.7f} rad/sample  (+/- {se:.2e}, from {len(res['seg'])} segments; {src})")
    print(f"  tau = 2cos(theta) = {2*math.cos(th):.7f}", end="")
    print(f"   damping per sample r = {res['nls'][1]:.7f}  (det = r^2)" if res["nls"] else "")
    print(f"  frequency {f:.5f} Hz, period {1/f:.5f} s, {cycles:.1f} cycles recorded")
    print(f"  cross-checks: FFT peak {res['fft']:.7f} (diff {res['fft']-th:+.1e})", end="")
    if w and w.get("theta") is not None:
        print(f", AR(2) trace fit {w['theta']:.7f} (diff {w['theta']-th:+.1e}; normalised tau {w['tau']:.7f})")
    else:
        print()
    if cycles < 30:
        print("  WARNING: fewer than 30 cycles (pre-registration asks for >= 30)")
    if fpred is not None:
        target = 2 * math.pi * fpred * res["dt"]
        se = math.hypot(se, 2 * math.pi * ferr * res["dt"])   # prediction uncertainty (e.g. from L)
        label = f"predicted {fpred} +/- {ferr} Hz -> 2*pi*f*dt"
    else:
        target = 2 * math.pi * p / q
        label = f"2*pi*{p}/{q}"
    z = (th - target) / se if se and se == se and se > 0 else float("inf")
    verdict = "PASS" if abs(z) <= 2 else "FAIL"
    print(f"  pre-registered target {label} = {target:.7f}   z = {z:+.2f}   -> {verdict}")
    return th, se, verdict, target


def combine(results, p, q):
    th = np.array([r[0] - r[3] for r in results])   # offsets from each run's own target
    print("\n== all runs")
    print(f"  runs {len(th)}   mean offset from target {th.mean():+.2e}   spread (sd) {th.std(ddof=1) if len(th)>1 else float('nan'):.2e}")
    if len(th) > 1:
        se_between = th.std(ddof=1) / math.sqrt(len(th))
        se_within = math.sqrt(sum(r[1] ** 2 for r in results)) / len(th)
        se = max(se_between, se_within)
        z = th.mean() / se
        print(f"  error bar {se:.2e} (larger of run-to-run {se_between:.1e} and within-run {se_within:.1e})")
        print(f"  z = {z:+.2f}   -> {'PASS' if abs(z) <= 2 else 'FAIL'}")


# ---------------------------------------------------------------- self test
def selftest():
    rng = np.random.default_rng(42)
    p, q = 1, 100
    print("SELFTEST: synthetic phyphox-like recordings, true theta = 2*pi*p/q unless noted")
    cases = [
        ("clean", dict(noise=0.0, damp=1.0, jitter=0.0, theta=2 * math.pi * p / q)),
        ("noise 5% + damping + 3% jitter", dict(noise=0.05, damp=0.9995, jitter=0.03, theta=2 * math.pi * p / q)),
        ("noise 20%", dict(noise=0.20, damp=0.9995, jitter=0.03, theta=2 * math.pi * p / q)),
        ("WRONG angle (+1%) -> must FAIL", dict(noise=0.05, damp=0.9995, jitter=0.03, theta=2 * math.pi * p / q * 1.01)),
    ]
    import tempfile, os
    for name, c in cases:
        dt = 0.01
        n = 6000
        t = np.cumsum(dt * (1 + c["jitter"] * rng.standard_normal(n)))
        t -= t[0]
        omega = c["theta"] / dt
        x = 9.81 + 3.0 * c["damp"] ** (t / dt) * np.cos(omega * t + 0.3) + 0.02 * t
        x += c["noise"] * 3.0 * rng.standard_normal(n)
        fd, path = tempfile.mkstemp(suffix=".csv")
        with os.fdopen(fd, "w") as f:
            f.write('"Time (s)","Acceleration y (m/s^2)"\n')
            for a, b in zip(t, x):
                f.write(f"{a:.6f},{b:.6f}\n")
        tt, xx, _ = load_csv(path)
        report(name, analyse(tt, xx, "tls", 10), p, q)
        os.remove(path)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--p", type=int, help="pre-registered numerator")
    ap.add_argument("--q", type=int, help="pre-registered denominator")
    ap.add_argument("--f", type=float, help="pre-registered frequency in Hz (e.g. from pendulum length); "
                    "target becomes 2*pi*f*dt with dt measured from the timestamps")
    ap.add_argument("--ferr", type=float, default=0.0, help="uncertainty of --f in Hz (e.g. from measuring L)")
    ap.add_argument("--col", help="value column name (default: highest variance)")
    ap.add_argument("--method", choices=["tls", "ols"], default="tls")
    ap.add_argument("--segments", type=int, default=10)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return
    if not a.files or (a.f is None and (a.p is None or a.q is None)):
        ap.error("give CSV file(s) and a pre-registered target: --p and --q, or --f (or --selftest)")
    out = []
    for path in a.files:
        t, x, cname = load_csv(path, a.col)
        r = report(f"{path}  [{cname}]", analyse(t, x, a.method, a.segments), a.p, a.q, a.f, a.ferr)
        if r:
            out.append(r)
    if len(out) > 1:
        combine(out, a.p, a.q)


if __name__ == "__main__":
    main()
