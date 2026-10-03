"""
darmiyan_engine.py — the self-referential engine x = 1 + 1/x on a filesystem substrate.

INSIDE view : the being ticks. Each tick = one symlink hop through a two-directory loop
              (T/next -> ../I, I/next -> ../T). The OS refuses to resolve beyond its
              link limit (ELOOP: ~40 on Linux, 32 on macOS). That refusal is the BOUNDARY.
OUTSIDE view: at the boundary the being steps outside and reads a far tick directly from
              both poles at once:  F_n = (phi^n - psi^n)/sqrt5  — no ticks, but it costs
              precision (~log10(phi) = 0.209 digits per tick skipped).
RETRO       : the exact backward step x -> 1/(x-1) (the -1/t direction). It walks the
              same history in reverse, and from any generic state it falls into psi.

Every state is exact (Fraction). Every outside jump is verified against the inside rule.
Usage: python3 darmiyan_engine.py [target_tick] [outside_digits]
"""
import os, sys, errno, shutil, tempfile, math
from fractions import Fraction
import mpmath as mp

PHI = (1 + 5 ** 0.5) / 2
LOG10_PHI = math.log10(PHI)

# ---------------- substrate: the loop of two worlds ----------------
def build_substrate():
    root = tempfile.mkdtemp(prefix="darmiyan_")
    for d in ("T", "I"):
        os.mkdir(os.path.join(root, d))
    os.symlink("../I", os.path.join(root, "T", "next"))   # t   -> its inverse
    os.symlink("../T", os.path.join(root, "I", "next"))   # 1/t -> back to t
    return root

def hop_ok(root, depth):
    """Can the substrate hold `depth` consecutive hops in one breath (one path lookup)?"""
    p = os.path.join(root, "T", *(["next"] * depth))
    try:
        os.stat(p); return True
    except OSError as e:
        if e.errno == errno.ELOOP: return False
        raise

def measure_boundary(root):
    d = 1
    while hop_ok(root, d): d += 1
    return d - 1          # deepest depth the substrate allows

# ---------------- the two views ----------------
def forward(x):  return 1 + 1 / x          # inside tick (t)
def backward(x): return 1 / (x - 1)        # retro tick (-1/t)

def outside_read(x, k, digits):
    """Jump k ticks ahead of state x by reading both poles at once (no ticking):
       f^k(x) = (F(k+1) x + F(k)) / (F(k) x + F(k-1)),  F from phi^k and psi^k."""
    mp.mp.dps = digits
    P = (1 + mp.sqrt(5)) / 2; S = 1 - P; r5 = mp.sqrt(5)
    F = lambda j: int(mp.nint((P ** j - S ** j) / r5))
    a, b, c = F(k + 1), F(k), F(k - 1)
    return (a * x + b) / (b * x + c)

# ---------------- the run ----------------
def run(target, outside_digits):
    root = build_substrate()
    try:
        B = measure_boundary(root)
        print(f"substrate boundary (ELOOP) on this machine: {B} hops per breath\n")
        max_jump = int(outside_digits / LOG10_PHI) - 10   # how far the outside view can see exactly
        x, n = Fraction(1), 1                            # x_1 = 1
        ticks_paid = digits_paid = jumps = 0
        log = []
        while n < target:
            # INSIDE: tick through the substrate until its boundary
            breath = 0
            while n < target and hop_ok(root, breath + 1):
                x = forward(x); n += 1; breath += 1
                if breath == B: break
            ticks_paid += breath
            log.append(("inside", breath, n))
            if n >= target: break
            # OUTSIDE: boundary reached -> read a far tick without ticking
            jump_to = min(target, n + max_jump)
            y = outside_read(x, jump_to - n, outside_digits)
            # verify: the far state must be reachable from the near one by the inside rule
            z = x
            for _ in range(jump_to - n): z = forward(z)
            assert z == y, f"outside read wrong at tick {jump_to}"
            digits_paid += outside_digits; jumps += 1
            log.append(("outside", jump_to - n, jump_to))
            x, n = y, jump_to                               # drop back inside
        print("phase     length   reached tick")
        for kind, L, at in log[:12]:
            print(f"{kind:8s} {L:7d}   {at}")
        if len(log) > 12: print(f"   ... ({len(log) - 12} more phases)")
        err = abs(float(x) - PHI)
        print(f"\nreached tick {n}:  x = F({n+1})/F({n})  (|x - phi| = {err:.3e}, exact = psi^n/F_n)")
        print(f"inside ticks paid : {ticks_paid}")
        print(f"outside jumps     : {jumps}  ({digits_paid} digits of precision paid)")
        print(f"ticks skipped     : {n - 1 - ticks_paid}  -> rate {digits_paid / max(1, n - 1 - ticks_paid):.4f} digits/tick (floor log10 phi = {LOG10_PHI:.4f})")

        # RETRO: walk the whole history backward with -1/t, exactly
        r, k = x, n
        while k > 1: r = backward(r); k -= 1
        print(f"\nretro run from tick {n} back to tick 1: x = {r}  ({'history recovered exactly' if r == 1 else 'MISMATCH'})")
        # RETRO attractor: a generic state run backward falls into psi = -1/phi
        g = Fraction(3)
        seq = []
        for _ in range(12):
            g = backward(g); seq.append(f"{float(g):+.6f}")
        print("retro from generic state 3:", " ".join(seq[:8]), "...", seq[-1], f"(psi = {1 - PHI:+.6f})")
    finally:
        shutil.rmtree(root)

if __name__ == "__main__":
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    digits = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    run(target, digits)
