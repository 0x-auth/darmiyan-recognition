#!/usr/bin/env python3
"""
trace_dial — classify the self-referential map M(z) = tau - 1/z by its trace.
Three regimes, split by one knife-edge at tau = 2:
    |tau| < 2   elliptic     -> rotates, never settles   (centres off the real line)
    |tau| = 2   parabolic    -> the two centres MERGE at a boundary point
    |tau| > 2   hyperbolic   -> settles                  (centres are inverse points, product 1)

USAGE
    python3 trace_dial.py 0 1 2 3            # tau values as args
    python3 trace_dial.py --file taus.txt    # one tau per line (blank lines / # comments ok)
    printf "1.9\n2\n2.1\n" | python3 trace_dial.py        # or from stdin
    python3 trace_dial.py 3 --orbit 8 --seed 2        # show an 8-step orbit from z0=2
    python3 trace_dial.py --matrix 1 1 1 0            # any Mobius map a b c d -> (az+b)/(cz+d)

Only the standard library. The matrix is normalised to det 1 before the trace is read.

Fix 2026-10-17: --matrix with det < 0 (e.g. Fibonacci [[1,1],[1,0]]) is orientation-reversing and
always hyperbolic; it was misread as elliptic. Classification now uses disc = (a-d)^2 + 4bc, and the
matrix's own fixed points ((a-d) +/- sqrt(disc)) / 2c are printed.
"""
import argparse, cmath, math, sys


def classify(tau, eps=1e-9):
    d = tau * tau - 4
    re = tau / 2
    if abs(d) <= eps:
        return dict(kind="parabolic", fixed=[complex(re, 0), complex(re, 0)],
                    note="two centres merge at z = %.6g (the critical edge, your t=1)" % re)
    r = cmath.sqrt(d) / 2
    fp = [re + r, re - r]
    if d < 0:
        ang = math.degrees(math.acos(max(-1.0, min(1.0, tau / 2)))) if abs(tau) <= 2 else None
        return dict(kind="elliptic", fixed=fp,
                    note="rotation %.4g deg/step, never settles (|z|=1 pair)" % ang)
    att = max(fp, key=abs)                       # attracting fixed point = larger |.|
    rate = abs((min(fp, key=abs)))               # |contraction| per step near attractor
    return dict(kind="hyperbolic", fixed=fp,
                note="settles to %.6g  (centres are inverse points, product=%.4g)"
                     % (att.real, (fp[0] * fp[1]).real))


def orbit(tau, z0, n):
    z, out = complex(z0), [complex(z0)]
    for _ in range(n):
        if abs(z) < 1e-12:
            out.append(float("inf")); break
        z = tau - 1 / z
        out.append(z)
    return out


def fnum(z):
    z = complex(z)
    if abs(z.imag) < 1e-9:
        return "%.5g" % z.real
    return "%.5g%+.5gi" % (z.real, z.imag)


def report(tau, args):
    c = classify(tau)
    print("tau = %-8.5g  %-11s  %s" % (tau, c["kind"], c["note"]))
    print("    centres: %s , %s" % (fnum(c["fixed"][0]), fnum(c["fixed"][1])))
    if args.orbit:
        o = orbit(tau, args.seed, args.orbit)
        print("    orbit z0=%s: %s" % (fnum(args.seed), " -> ".join(fnum(z) for z in o)))


def read_values(args):
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            raw = f.read()
    elif args.values:
        raw = " ".join(args.values)
    elif not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        sys.exit("give tau values as args, --file, or on stdin (see --help)")
    vals = []
    for tok in raw.replace(",", " ").split():
        if tok.startswith("#"):
            continue
        try:
            vals.append(float(tok))
        except ValueError:
            pass
    return vals


def main():
    ap = argparse.ArgumentParser(description="classify M(z)=tau-1/z by its trace")
    ap.add_argument("values", nargs="*", help="tau values")
    ap.add_argument("--file", help="file with one tau per line")
    ap.add_argument("--orbit", type=int, default=0, metavar="N", help="also print an N-step orbit")
    ap.add_argument("--seed", type=float, default=2.0, help="orbit start z0 (default 2)")
    ap.add_argument("--matrix", nargs=4, type=float, metavar=("a", "b", "c", "d"),
                    help="classify any Mobius map (az+b)/(cz+d) via its normalised trace")
    a = ap.parse_args()

    if a.matrix:
        A, B, C, D = a.matrix
        det = A * D - B * C
        if abs(det) < 1e-12:
            sys.exit("degenerate matrix (det=0)")
        disc = (A - D) ** 2 + 4 * B * C            # = trace^2 - 4*det
        print("matrix [[%g %g][%g %g]]  det=%g  disc=%g" % (A, B, C, D, det, disc))
        if abs(C) > 1e-12:
            r = cmath.sqrt(disc)
            print("    own fixed points: %s , %s" % (fnum((A - D + r) / (2 * C)), fnum((A - D - r) / (2 * C))))
        if det < 0:
            print("    det<0: orientation-reversing -> always hyperbolic (two real fixed points)")
            return
        report((A + D) / math.sqrt(det), a)
        return

    for tau in read_values(a):
        report(tau, a)


if __name__ == "__main__":
    main()
