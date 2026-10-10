"""error-of: resonance — the Precision boundary, crossed instead of stopped.

Drop-in for the error-of framework (sits next to core.py, heal.py).

Your `Precision` class names the boundary "the number representation", with the
assumption "an exact quantity should survive the round trip". The usual reading is
that hitting the floating-point floor is a *failure* of that assumption.

This module reads it the other way. A self-referential map x <- f(x) formally needs
infinite steps; on a real substrate it freezes at machine epsilon in O(log(1/eps))
steps. The convergence error is not garbage — the decay rate of the residual is the
dominant multiplier f'(x*), i.e. the pole, the geometry of the fixed point. So the
Precision boundary is *crossed* (outcome "continued"), and what you carry across is
the residual read as structure.

Usage, matching the ERROR-OF observation protocol (one JSON line to stderr, which
`error-of run` captures as a first-hand observation):

    from error_of.resonance import observe_fixed_point
    result = observe_fixed_point("1+1/x")        # emits ERROR-OF, returns the structure

It is self-contained (stdlib only) so it drops in without touching the rest.
"""
import json
import math
import sys

_SAFE = {k: getattr(math, k) for k in
         ("sqrt", "sin", "cos", "tan", "exp", "log", "pi", "e",
          "cosh", "sinh", "tanh", "atan")}


def _make_f(expr):
    code = compile(expr, "<f>", "eval")
    return lambda x: eval(code, {"__builtins__": {}}, dict(_SAFE, x=x))


def _observe(**kw):
    """Emit one ERROR-OF observation line (the framework's self-report protocol)."""
    print("ERROR-OF " + json.dumps(kw, default=str), file=sys.stderr)


def run_to_floor(expr, x0=1.0, max_steps=100000):
    """Iterate x <- f(x) to the float floor. Return the fixed point, the step count,
    the final residual, and the residual's decay rate (= the pole / multiplier)."""
    f = _make_f(expr)
    x = float(x0)
    errs = []
    step = 0
    while step < max_steps:
        xn = f(x)
        step += 1
        if math.isinf(xn) or math.isnan(xn):
            return {"expr": expr, "diverged": True, "steps": step}
        if xn == x:                       # resolution floor: cannot resolve further
            break
        errs.append(abs(xn - x))
        x = xn
    # rate from the clean window (exclude ratios taken at the noise floor)
    floor = max(errs[-1] if errs else 0.0, 1e-12) * 1e3
    ratios = [errs[i + 1] / errs[i] for i in range(len(errs) - 1)
              if errs[i] > floor and errs[i + 1] > 0]
    rate = sum(ratios[-10:]) / len(ratios[-10:]) if ratios else float("nan")
    h = 1e-7
    try:
        mult = (f(x + h) - f(x - h)) / (2 * h)
    except Exception:
        mult = float("nan")
    return {"expr": expr, "diverged": False, "fixed_point": x,
            "steps": step, "residual": errs[-1] if errs else 0.0,
            "rate": rate, "pole": mult}


def observe_fixed_point(expr, x0=1.0):
    """Run to the floor and emit a Precision observation whose outcome is 'continued':
    the error was the signal. Returns the result dict."""
    r = run_to_floor(expr, x0)
    if r.get("diverged"):
        _observe(**{"class": "Precision"}, boundary="the number representation",
                 observation=f"x <- {expr} diverged to inf/nan after {r['steps']} steps",
                 assumption="the iteration has an attracting fixed point",
                 transformation="none — the map is not contractive from this x0",
                 outcome="stopped")
        return r
    _observe(**{"class": "Precision"}, boundary="the number representation",
             observation=(f"x <- {expr} reached the float floor at step {r['steps']} "
                          f"(residual {r['residual']:.2e} = machine epsilon)"),
             assumption="an exact quantity should survive the round trip",
             transformation=(f"read the residual's decay rate {r['rate']:.6f} as the pole "
                             f"f'(x*)={r['pole']:.6f} — infinity became {r['steps']} finite steps"),
             outcome="continued")
    return r


if __name__ == "__main__":
    expr = sys.argv[1] if len(sys.argv) > 1 else "1+1/x"
    res = observe_fixed_point(expr)
    if not res.get("diverged"):
        print(f"fixed point {res['fixed_point']:.15g}  in {res['steps']} steps; "
              f"the error's decay rate {res['rate']:.6f} is the pole.")
