"""error_of CLI — the error is the signal.

Subcommands:
  fixedpoint EXPR [--x0 X]   iterate x<-f(x) to the float floor; report the residual as structure
  fibcode encode N           Fibonacci (no-11) code of a positive integer
  fibcode decode CODE        decode a Fibonacci codeword
  fibcode check CODE         is this a valid (corruption-free) codeword?
  complexity [FILE]          linear complexity (shortest LFSR) of a byte stream (stdin if no FILE)
  pisano N                   Pisano period of 1/N on the phi-carrier (= period of Fibonacci mod N)
  approx X [--max-denom D]   best rational p/q approximating X (continued-fraction convergent)
"""
import argparse, json, sys
from . import fixedpoint, fibcode, complexity, numth


def _fixedpoint(a):
    r = fixedpoint.iterate_to_floor(a.expr, x0=a.x0)
    if r.get("diverged"):
        print(f"diverged after {r['steps']} steps (hit inf/nan) — expr: {r['expr']}")
        return 1
    print(f"expr              : x <- {r['expr']}")
    print(f"fixed point       : {r['fixed_point']:.16g}")
    print(f"steps to floor    : {r['steps_to_floor']}   (infinity -> finite, at machine epsilon)")
    print(f"final residual    : {r['final_residual']:.3e}   (the substrate's resolution)")
    print(f"convergence rate  : {r['convergence_rate']:.6f}   (|e_{{n+1}}/e_n| — the error's decay)")
    print(f"multiplier f'(x*) : {r['multiplier_fprime']:.6f}   (the pole / the geometry the error knows)")
    print(f"contractive       : {r['contractive']}")
    return 0


def _fibcode(a):
    if a.op == "encode":
        print(fibcode.encode(int(a.arg)))
    elif a.op == "decode":
        print(fibcode.decode(a.arg))
    elif a.op == "check":
        ok = fibcode.is_valid(a.arg)
        print("valid" if ok else "CORRUPT (no-11 boundary violated)")
        return 0 if ok else 1
    return 0


def _complexity(a):
    data = open(a.file, "rb").read() if a.file else sys.stdin.buffer.read()
    bits = complexity.bytes_to_bits(data)
    L = complexity.linear_complexity(bits)
    n = len(bits)
    ratio = L / n if n else 0.0
    verdict = ("structured / compressible" if ratio < 0.4 else
               "near-random (a wall — no linear structure)" if ratio > 0.45 else
               "partially structured")
    print(f"bits              : {n}")
    print(f"linear complexity : {L}   (shortest LFSR = recognition cost = #poles)")
    print(f"complexity / n    : {ratio:.3f}   -> {verdict}")
    return 0


def _pisano(a):
    print(numth.pisano(int(a.n)))
    return 0


def _approx(a):
    p, q = numth.best_rational(float(a.x), max_denom=a.max_denom)
    print(f"{p}/{q} = {p/q:.12g}   (error {abs(p/q - float(a.x)):.3e})")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="error_of", description="the error is the signal")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("fixedpoint", help="iterate to the float floor; read the residual")
    p.add_argument("expr"); p.add_argument("--x0", type=float, default=1.0)
    p.set_defaults(fn=_fixedpoint)

    p = sub.add_parser("fibcode", help="Fibonacci (no-11) integer code")
    p.add_argument("op", choices=["encode", "decode", "check"]); p.add_argument("arg")
    p.set_defaults(fn=_fibcode)

    p = sub.add_parser("complexity", help="linear complexity of a byte stream")
    p.add_argument("file", nargs="?"); p.set_defaults(fn=_complexity)

    p = sub.add_parser("pisano", help="Pisano period of N")
    p.add_argument("n"); p.set_defaults(fn=_pisano)

    p = sub.add_parser("approx", help="best rational approximation of X")
    p.add_argument("x"); p.add_argument("--max-denom", type=int, default=10**6, dest="max_denom")
    p.set_defaults(fn=_approx)

    args = ap.parse_args(argv)
    return args.fn(args)
