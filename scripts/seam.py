#!/usr/bin/env python3
"""
seam.py — the trace-map seam x -> t - 1/x, measured.  (companion to docs/the-seam.md)

Prints three things:
  1. ticks to close vs trace t, for TWO closure criteria
       step     : |x[n+1] - x[n]| < eps        (what the-seam.md table uses)
       distance : |x[n] - fixed point| < eps
  2. the seam law at t = 2 under each criterion
       step     -> ticks ~ eps^(-1/2)
       distance -> ticks ~ eps^(-1)
     i.e. the exponent depends on how "closed" is defined.
  3. the crossover rate log(lambda) / sqrt(delta) at t = 2 + delta -> 1.
     THIS one-half is the one forced by the double root (Delta = t^2 - 4 under a sqrt).

Corrects an earlier conflation (MASTER §2, the-discriminant-law §5.1): the ε^(-1/2) closure law
and the √δ crossover are two different half-powers.
"""
import math


def ticks(t, eps, mode, x0=2.0, cap=10**7):
    disc = t * t - 4
    fp = (t + math.sqrt(disc)) / 2 if disc >= 0 else None
    x = x0
    for n in range(1, cap):
        x2 = t - 1 / x
        if mode == "step" and abs(x2 - x) < eps:
            return n
        if mode == "distance" and fp is not None and abs(x2 - fp) < eps:
            return n
        x = x2
    return None


if __name__ == "__main__":
    eps = 1e-8
    print(f"1. ticks to close, eps = {eps:g}, x0 = 2")
    print(f"   {'t':>7} {'sector':>10} {'step':>10} {'distance':>12}")
    for t in (2.2, 2.01, 2.001, 2.0, 1.999):
        sec = "arrow" if t > 2 else ("seam" if t == 2 else "phase")
        s = ticks(t, eps, "step", cap=10**6)
        d = ticks(t, eps, "distance", cap=10**6)
        print(f"   {t:7.3f} {sec:>10} {str(s or 'never'):>10} {str(d or '>1e6' if t >= 2 else 'never'):>12}")
    print("\n2. seam law at t = 2")
    print(f"   {'eps':>8} {'step':>8} {'step*sqrt(eps)':>15} {'distance':>10} {'distance*eps':>13}")
    for e in (1e-2, 1e-4, 1e-6):
        s, d = ticks(2.0, e, "step"), ticks(2.0, e, "distance")
        print(f"   {e:8.0e} {s:8d} {s*math.sqrt(e):15.4f} {d:10d} {d*e:13.4f}")
    print("\n3. crossover rate at t = 2 + delta")
    for dl in (1e-2, 1e-4, 1e-6, 1e-8):
        t = 2 + dl
        lam = (t + math.sqrt(t * t - 4)) / 2
        print(f"   delta = {dl:6.0e}   log(lambda)/sqrt(delta) = {math.log(lam)/math.sqrt(dl):.6f}")
