"""Iterate a self-referential map to the floating-point floor; read the residual as signal.

The headline idea: x <- f(x) formally needs infinite steps, but on a real substrate it
freezes at machine epsilon in O(log(1/eps)) steps. The convergence error is not garbage —
its decay rate is the dominant multiplier (the pole / the geometry) of the fixed point.
"""
import math

_SAFE = {k: getattr(math, k) for k in
         ("sqrt","sin","cos","tan","exp","log","pi","e","cosh","sinh","tanh","atan")}

def make_f(expr):
    code = compile(expr, "<f>", "eval")
    def f(x):
        return eval(code, {"__builtins__": {}}, dict(_SAFE, x=x))
    return f

def iterate_to_floor(expr, x0=1.0, max_steps=100000):
    """Return dict: fixed point, steps to the float floor, residual, inferred rate & pole."""
    f = make_f(expr)
    x = float(x0)
    errs, xs = [], [x]
    step = 0
    while step < max_steps:
        xn = f(x)
        step += 1
        if xn == x:                 # hit the resolution floor: cannot resolve further
            break
        if math.isinf(xn) or math.isnan(xn):
            return {"expr": expr, "diverged": True, "steps": step}
        errs.append(abs(xn - x))
        xs.append(xn); x = xn
    # residual-as-signal: ratio of successive deltas -> |f'(x*)| = the dominant multiplier.
    # Read the rate from the CLEAN window (deltas well above the noise floor); ratios taken
    # too close to machine epsilon are corrupted by rounding and must be excluded.
    floor = max(errs[-1] if errs else 0.0, 1e-12) * 1e3
    ratios = [errs[i+1]/errs[i] for i in range(len(errs)-1)
              if errs[i] > floor and errs[i+1] > 0]
    tail = ratios[-10:] if ratios else []
    rate = sum(tail)/len(tail) if tail else float("nan")
    # numeric derivative at the fixed point = the pole/multiplier
    h = 1e-7
    try:
        mult = (f(x+h) - f(x-h)) / (2*h)
    except Exception:
        mult = float("nan")
    return {
        "expr": expr, "diverged": False,
        "fixed_point": x, "steps_to_floor": step,
        "final_residual": errs[-1] if errs else 0.0,
        "convergence_rate": rate,          # |error_{n+1}/error_n|
        "multiplier_fprime": mult,         # f'(x*) — the pole
        "contractive": abs(mult) < 1 if not math.isnan(mult) else None,
    }
