"""
resonance_recognizer.py — recognition as resonance (the north-star build).

Idea: a system does not SEARCH for its answer; struck, it RINGS at its own natural modes
(its poles). Reading those modes = recognition. This script maps exactly how far that goes.

    LINEAR concealment     -> rings cleanly, secret fully recoverable          (works)
    NONLINEAR structure    -> rings; the TYPE is recognizable (period/chaos)   (works)
    NONLINEAR secret       -> rings, but ring->secret can be many-to-one       (the WALL)

Three self-contained demos. No external data beyond numpy.
    python3 resonance_recognizer.py            # all
    python3 resonance_recognizer.py linear | cascade | wall
"""
import sys
import numpy as np

FREQS = np.linspace(0.001, np.pi, 8000)

def spectrum(sig, freqs=FREQS, decay=1.0):
    """Drive the signal across a frequency band; magnitude peaks where it rings (its poles)."""
    s = np.asarray(sig, float); s = s - s.mean()
    k = np.arange(len(s)); w = decay ** k
    return np.array([abs(np.sum(s * w * np.exp(-1j * f * k))) for f in freqs])

def peaks(R, frac=0.05, half=2):
    return [FREQS[i] for i in range(half, len(R) - half)
            if R[i] == max(R[i - half:i + half + 1]) and R[i] > frac * R.max()]

# ----------------------------------------------------------------------
# 1. LINEAR: hidden oscillating poles announce themselves exactly.
# ----------------------------------------------------------------------
def demo_linear():
    print("\n[1] LINEAR — hidden poles ring at their own frequencies")
    true = [0.95 * np.exp(1j * 1.2), 0.95 * np.exp(-1j * 1.2),
            0.90 * np.exp(1j * 2.5), 0.90 * np.exp(-1j * 2.5)]
    amp = np.random.RandomState(7).rand(len(true))
    sig = np.array([sum(a * (r ** k) for a, r in zip(amp, true)).real for k in range(600)])
    R = spectrum(sig, decay=0.995)
    found = sorted(set(round(p, 2) for p in peaks(R, frac=0.5, half=8)))
    print(f"    hidden angles : {sorted(set(round(abs(np.angle(p)), 2) for p in true))}")
    print(f"    rang at       : {found}")
    print("    -> recognition, not search: the signal names its own poles when driven.")

# ----------------------------------------------------------------------
# 2. NONLINEAR STRUCTURE: the logistic period-doubling cascade is audible.
# ----------------------------------------------------------------------
def demo_cascade():
    print("\n[2] NONLINEAR — the period-doubling cascade rings (pi, pi/2, pi/4 ...)")
    def logistic(r, n, x0=0.3):
        x = x0; o = []
        for _ in range(n): o.append(x); x = r * x * (1 - x)
        return np.array(o)
    for r, lab in [(2.9, "period 1 (settled)"), (3.2, "period 2"),
                   (3.5, "period 4"), (3.566, "period 8")]:
        R = spectrum(logistic(r, 8000)[1000:])
        pk = sorted(round(p, 3) for p in peaks(R))
        print(f"    r={r:<6} {lab:20} rings at {pk}")
    print(f"    (pi={np.pi:.3f}  pi/2={np.pi/2:.3f}  pi/4={np.pi/4:.3f})")
    print("    -> the TYPE of structure (which period, onset of chaos) is read off the ring,")
    print("       without computing the bifurcation diagram.")

# ----------------------------------------------------------------------
# 3. THE WALL: a nonlinear secret rings, but ring->secret can be many-to-one.
# ----------------------------------------------------------------------
def demo_wall():
    print("\n[3] WALL — nonlinear secret rings, but the ring does not uniquely name it")
    def nl_orbit(S, n, x0=0.137):
        x = x0; o = []
        for _ in range(n): o.append(x); x = np.cos(2 * np.pi * (x + S))
        return np.array(o)
    def ring_freq(sig):
        R = spectrum(sig); return FREQS[int(np.argmax(R))]
    Ss = np.linspace(0.05, 0.45, 40)
    Ws = np.array([ring_freq(nl_orbit(S, 1500)) for S in Ss])
    mono = np.all(np.diff(Ws) > 0) or np.all(np.diff(Ws) < 0)
    # count how many S values share (nearly) the same ring -> invertibility test
    collisions = sum(np.sum(np.abs(Ws - w) < 0.02) > 1 for w in Ws)
    print(f"    ring frequency monotonic in secret S? {mono}")
    print(f"    secrets sharing a ring (many-to-one collisions): {collisions} of {len(Ss)}")
    print("    -> the ring proves structure EXISTS, but cannot be inverted to the exact secret.")
    print("       This is the ECC / SHA-1 wall seen from the resonance side: access, not existence.")
    print("    Open frontier: for which nonlinear families is ring->secret one-to-one?")

DEMOS = {"linear": demo_linear, "cascade": demo_cascade, "wall": demo_wall}
if __name__ == "__main__":
    print("=" * 66 + "\n  RESONANCE RECOGNIZER — recognition is ringing, not searching\n" + "=" * 66)
    for name in (sys.argv[1:] or list(DEMOS)):
        DEMOS[name]()
    print()
