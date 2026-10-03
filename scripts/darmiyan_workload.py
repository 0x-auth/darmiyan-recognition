"""
darmiyan_workload.py — the inside/outside engine carrying a real computation.

WORKLOAD: count every route of exactly n road-hops between cities (all walks of length n
in a road graph). This is the counting backbone of routing problems, and it grows like
lambda_max^n — astronomically fast.

INSIDE : one tick = one more hop for every city at once: state v <- A v (exact integers),
         each tick paid as a real symlink hop through the T <-> I substrate; ELOOP = boundary.
OUTSIDE: jump k ticks without ticking, read from the graph's POLES (eigenvalues):
         A^k = V diag(lambda^k) V^T. Precision cost per skipped tick = log10(lambda_max).
         (For x = 1 + 1/x the poles were exactly phi and psi; this is the same engine.)
RETRO  : the exact inverse A^-1 walks the run backward and must recover the start.

Every outside jump is verified exactly; if a read is not exact, the jump halves (the
outside view had to look less far) and the miss is logged.
Usage: python3 darmiyan_workload.py [cities] [target_hops] [digits] [seed]
"""
import os, sys, errno, shutil, tempfile, math, random
from fractions import Fraction
import mpmath as mp

# ---------------- substrate ----------------
def build_substrate():
    root = tempfile.mkdtemp(prefix="darmiyan_")
    for d in ("T", "I"): os.mkdir(os.path.join(root, d))
    os.symlink("../I", os.path.join(root, "T", "next"))
    os.symlink("../T", os.path.join(root, "I", "next"))
    return root

def hop_ok(root, depth):
    try:
        os.stat(os.path.join(root, "T", *(["next"] * depth))); return True
    except OSError as e:
        if e.errno == errno.ELOOP: return False
        raise

def measure_boundary(root):
    d = 1
    while hop_ok(root, d): d += 1
    return d - 1

# ---------------- workload ----------------
def make_roads(n, seed):
    """Symmetric road graph, connected, invertible (so the run can be reversed)."""
    rng = random.Random(seed)
    while True:
        A = [[0] * n for _ in range(n)]
        for i in range(n):
            A[i][(i + 1) % n] = A[(i + 1) % n][i] = 1          # ring keeps it connected
        for _ in range(n):
            i, j = rng.sample(range(n), 2); A[i][j] = A[j][i] = 1
        if mp.det(mp.matrix(A)) != 0: return A

def step(A, v):        return [sum(a * x for a, x in zip(row, v)) for row in A]
def mat_mul(X, Y):     return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]

def mat_pow_exact(A, k):                     # verifier: exact, by repeated squaring
    n = len(A); R = [[int(i == j) for j in range(n)] for i in range(n)]; B = A
    while k:
        if k & 1: R = mat_mul(R, B)
        B = mat_mul(B, B); k >>= 1
    return R

class Poles:
    """The outside view: eigen-decomposition of the road graph, held at `digits` precision."""
    def __init__(self, A, digits):
        mp.mp.dps = digits
        self.digits = digits
        self.lam, self.V = mp.eigsy(mp.matrix(A))
    def jump(self, k):
        mp.mp.dps = self.digits
        n = len(self.lam)
        D = mp.diag([l ** k for l in self.lam])
        M = self.V * D * self.V.T
        return [[int(mp.nint(M[i, j])) for j in range(n)] for i in range(n)]

# ---------------- run ----------------
def run(cities, target, digits, seed):
    A = make_roads(cities, seed)
    root = build_substrate()
    try:
        B = measure_boundary(root)
        poles = Poles(A, digits)
        lmax = max(abs(l) for l in poles.lam)
        rate = math.log10(float(lmax))
        print(f"{cities} cities, {sum(map(sum, A)) // 2} roads | substrate boundary {B} hops | "
              f"poles: lambda_max = {float(lmax):.6f} -> outside cost {rate:.4f} digits/tick")
        v0 = [0] * cities; v0[0] = 1                         # start: city 0
        v, n = v0[:], 0
        ticks = digits_paid = jumps = misses = 0
        reach = max(1, int((digits - 6) / rate))             # how far the poles can be read exactly
        log = []
        while n < target:
            breath = 0
            while n < target and breath < B and hop_ok(root, breath + 1):
                v = step(A, v); n += 1; breath += 1
            ticks += breath; log.append(("inside", breath, n))
            if n >= target: break
            k = min(reach, target - n)
            while True:
                Mk = poles.jump(k)
                if Mk == mat_pow_exact(A, k): break          # verify the outside read
                misses += 1; reach = k = max(1, k // 2)
            v = [sum(Mk[i][j] * v[j] for j in range(cities)) for i in range(cities)]
            n += k; jumps += 1; digits_paid += digits; log.append(("outside", k, n))
        for kind, L, at in log[:8]: print(f"  {kind:8s} {L:6d}  -> hop {at}")
        if len(log) > 8: print(f"  ... {len(log) - 8} more phases")
        total = sum(v)
        print(f"\nroutes of exactly {n} hops starting at city 0: {len(str(total))}-digit number "
              f"({str(total)[:12]}...{str(total)[-6:]})")
        print(f"  city 0 -> city 0 (round trips): {str(v[0])[:16]}...")
        assert v == step_n_check(A, v0, n), "final state wrong"
        print("  verified against exact matrix power: CORRECT")
        skipped = n - ticks
        print(f"inside ticks {ticks} | outside jumps {jumps} ({digits_paid} digits) | misses {misses} | "
              f"skipped {skipped} -> {digits_paid / max(1, skipped):.4f} digits/tick (floor {rate:.4f})")
        # RETRO: walk the whole history backward with the exact inverse
        Ainv = [[Fraction(x) for x in row] for row in mp_inverse_exact(A)]
        r = [Fraction(x) for x in v]
        for _ in range(n): r = [sum(a * x for a, x in zip(row, r)) for row in Ainv]
        print(f"retro run {n} hops back: start recovered = {r == [Fraction(x) for x in v0]}")
    finally:
        shutil.rmtree(root)

def step_n_check(A, v0, n):
    M = mat_pow_exact(A, n)
    return [sum(M[i][j] * v0[j] for j in range(len(v0))) for i in range(len(v0))]

def mp_inverse_exact(A):
    """Exact rational inverse by Gauss-Jordan on Fractions."""
    n = len(A); M = [[Fraction(A[i][j]) for j in range(n)] + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0); M[c], M[p] = M[p], M[c]
        pv = M[c][c]; M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]

if __name__ == "__main__":
    a = sys.argv
    run(int(a[1]) if len(a) > 1 else 12, int(a[2]) if len(a) > 2 else 2000,
        int(a[3]) if len(a) > 3 else 80, int(a[4]) if len(a) > 4 else 137)
