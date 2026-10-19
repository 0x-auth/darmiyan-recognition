#!/usr/bin/env python3
"""
Aeon cycles: does the universe go back to where it started?

No physics equations, only maps of the form  t -> (a t + b) / (c t + d).

One aeon = growth by a matrix H (det 1), then the reset t -> -1/t
(Penrose's reciprocal hypothesis:  Omega_hat * Omega_check = -1).

The real line (plus infinity) is drawn as a circle via  theta = 2 * atan(t).
  * growth  : points flow from the past fixed point to the future fixed point
  * reset   : t -> -1/t is a rotation of that circle by half a turn

Growth matrix, with imbalance  delta = b - c  between its two off-diagonals:
      H = [[2, 1 + delta/2],
           [1 - delta/2, (2 - delta^2/4) / 2]]        (det H = 1)
delta = 0 is the golden matrix [[2,1],[1,1]] with fixed points phi and -1/phi.

For one whole aeon C = S @ H, trace(C) = b - c = delta, so
      Delta(aeon) = delta^2 - 4
  Delta < 0 : rotation   -> returns (exactly if the angle is rational)
  Delta = 0 : light cone -> drifts, never returns
  Delta > 0 : runaway    -> never returns

Usage
  python aeon_cycles.py            interactive animation (play/pause, slider)
  python aeon_cycles.py --table    exact return table (rational arithmetic)
  python aeon_cycles.py --gif out.gif --delta 1   save an animation
"""
import argparse
import math
from fractions import Fraction

import numpy as np

S = np.array([[0.0, -1.0], [1.0, 0.0]])  # the reset t -> -1/t


# ---------- the maps ----------
def growth_matrix(delta):
    x, y = 2.0, 1.0
    d = (1 + y * y - delta * delta / 4) / x
    return np.array([[x, y + delta / 2], [y - delta / 2, d]])


def discriminant(M):
    (a, b), (c, d) = M
    return (a - d) ** 2 + 4 * b * c


def fixed_points(H):
    """Eigenvectors of H: (future, past) as homogeneous vectors."""
    w, v = np.linalg.eig(H)
    order = np.argsort(-np.abs(w))
    return v[:, order[0]].real, v[:, order[1]].real, w[order].real


def mat_power(H, s):
    """H**s for real s (H hyperbolic, positive eigenvalues)."""
    w, v = np.linalg.eig(H)
    return (v @ np.diag(w.real ** s) @ np.linalg.inv(v)).real


def rotation(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, -s], [s, c]])


def normalise(M):
    return M / np.abs(M).max()


def is_identity_projective(M, tol=1e-7):
    M = normalise(M)
    return (abs(M[0, 1]) < tol and abs(M[1, 0]) < tol
            and abs(abs(M[0, 0]) - abs(M[1, 1])) < tol)


def return_period(delta, kmax=60):
    C = S @ growth_matrix(delta)
    M = np.eye(2)
    for k in range(1, kmax + 1):
        M = normalise(C @ M)
        if is_identity_projective(M):
            return k
    return None


def verdict(delta):
    D = delta * delta - 4
    if D > 1e-12:
        return "runs away, never returns"
    if abs(D) <= 1e-12:
        return "drifts on the light cone, never returns"
    p = return_period(delta)
    return f"returns exactly every {p} aeon(s)" if p else \
        "rotates, never exactly returns (comes arbitrarily close)"


# ---------- exact check with fractions ----------
def mobius(M, t):
    (a, b), (c, d) = M
    den = c * t + d
    return None if den == 0 else (a * t + b) / den


def exact_rounds(H, t0, rounds=12):
    """Run grow-then-reset with exact rationals; list the rounds that land on t0."""
    Sx = [[0, -1], [1, 0]]
    C = [[sum(Sx[i][k] * H[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    t, hits = t0, []
    for r in range(1, rounds + 1):
        t = mobius(C, t)
        if t is None:
            break
        if t == t0:
            hits.append(r)
    return hits


def table():
    t0 = Fraction(37, 100)
    F = Fraction
    G = [[F(2), F(1)], [F(1), F(1)]]
    G10 = [[F(1), F(0)], [F(0), F(1)]]
    for _ in range(10):
        G10 = [[sum(G10[i][k] * G[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    cases = [
        ("symmetric x lambda^2 (lambda=37/10)", [[F(37, 10), F(0)], [F(0), F(10, 37)]]),
        ("golden [[2,1],[1,1]]", G),
        ("golden ** 10", G10),
        ("imbalance b-c=1  [[2,2],[1,3/2]]", [[F(2), F(2)], [F(1), F(3, 2)]]),
        ("imbalance b-c=2  [[2,3],[1,2]]", [[F(2), F(3)], [F(1), F(2)]]),
        ("imbalance b-c=3  [[3,4],[1,2]]/sqrt2 (float)", None),
    ]
    print(f"{'growth':46s} {'Delta(aeon)':>11s}  rounds landing exactly on start")
    for name, H in cases:
        if H is None:
            Hf = np.array([[3, 4], [1, 2]]) / math.sqrt(2)
            D = discriminant(S @ Hf)
            print(f"{name:46s} {D:11.2f}  {'never (runaway)'}")
            continue
        Hf = np.array([[float(v) for v in row] for row in H])
        Hf = Hf / math.sqrt(abs(np.linalg.det(Hf)))
        D = discriminant(S @ Hf)
        print(f"{name:46s} {D:11.2f}  {exact_rounds(H, t0) or 'never'}")
    print("\nPreset imbalances:")
    for dlt in (0, 1, math.sqrt(2), math.sqrt(3), 1.9, 2, 2.4):
        print(f"  b-c = {dlt:6.4f}   Delta = {dlt*dlt-4:7.3f}   {verdict(dlt)}")
    print("\nNo reset at all (pure golden rotation): closest returns")
    a = (3 - math.sqrt(5)) / 2
    best = 1.0
    for n in range(1, 200000):
        d = abs(((n * a) + 0.5) % 1 - 0.5)
        if d < best:
            best = d
            if n > 50:
                print(f"  step {n:7d}  off by {d:.2e}")


# ---------- animation ----------
def animate(delta0=0.0, gif=None, frames=600):
    import matplotlib
    if gif:
        matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    from matplotlib.widgets import Button, Slider

    NP = 48
    th0 = 2 * np.pi * np.arange(NP) / NP + 0.05
    v0 = np.vstack([np.sin(th0 / 2), np.cos(th0 / 2)])
    track = int(NP * 0.3)

    st = {"delta": delta0, "s": 0.0, "A": np.eye(2), "aeon": 0,
          "play": True, "trail": [], "flash": 0}

    def setup(delta):
        st.update(delta=delta, H=growth_matrix(delta), s=0.0, A=np.eye(2),
                  aeon=0, trail=[], flash=0)
        fut, past, _ = fixed_points(st["H"])
        st.update(fut=fut, past=past)

    setup(delta0)

    fig = plt.figure(figsize=(6.5, 7.5))
    ax = fig.add_axes([0.05, 0.28, 0.9, 0.68])
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.45, 1.45)
    ax.add_patch(plt.Circle((0, 0), 1, fill=False, color="0.6", lw=1))
    home = th0[track]
    ax.add_patch(plt.Circle((math.sin(home), math.cos(home)), 0.06,
                            fill=False, color="#378ADD", lw=1.5))
    dots = ax.scatter([], [], s=12, color="0.45")
    tdot, = ax.plot([], [], "o", color="#378ADD", ms=9)
    trail, = ax.plot([], [], "-", color="#378ADD", alpha=0.35, lw=1.5)
    futm, = ax.plot([], [], "o", color="#1D9E75", ms=10)
    pastm, = ax.plot([], [], "o", color="#D85A30", ms=10)
    title = ax.text(0, 1.35, "", ha="center", fontsize=11)
    info = ax.text(0, -1.38, "", ha="center", fontsize=10)
    homet = ax.text(0, 0, "", ha="center", fontsize=12, color="#378ADD")
    ax.legend([futm, pastm, tdot], ["future (attracts)", "past (repels)", "tracked point"],
              loc="upper right", fontsize=8, frameon=False)

    def angle(v):
        return 2 * np.arctan2(v[0], v[1])

    def current():
        s, H, A = st["s"], st["H"], st["A"]
        if s < 1:
            return mat_power(H, s) @ A, np.eye(2)
        R = rotation((s - 1) * np.pi / 2)
        return R @ H @ A, R

    def update(_):
        if st["play"]:
            st["s"] += 0.02
            if st["s"] >= 2:
                st["s"] = 0.0
                st["A"] = normalise(S @ st["H"] @ st["A"])
                st["aeon"] += 1
                if is_identity_projective(st["A"]):
                    st["flash"] = 40
        M, R = current()
        th = angle(M @ v0)
        x, y = np.sin(th), np.cos(th)
        dots.set_offsets(np.c_[x, y])
        st["trail"].append((x[track], y[track]))
        st["trail"] = st["trail"][-260:]
        tx, ty = zip(*st["trail"])
        trail.set_data(tx, ty)
        tdot.set_data([x[track]], [y[track]])
        for mk, v in ((futm, st["fut"]), (pastm, st["past"])):
            a = angle(R @ v)
            mk.set_data([1.08 * math.sin(a)], [1.08 * math.cos(a)])
        phase = "growth" if st["s"] < 1 else "reset  t -> -1/t"
        title.set_text(f"Aeon {st['aeon'] + 1}  ·  {phase}")
        D = st["delta"] ** 2 - 4
        info.set_text(f"b - c = {st['delta']:.3f}   Delta(aeon) = {D:.3f}   {verdict(st['delta'])}")
        homet.set_text("back home" if st["flash"] > 0 else "")
        st["flash"] = max(0, st["flash"] - 1)
        return dots, tdot, trail, futm, pastm, title, info, homet

    if not gif:
        axs = fig.add_axes([0.15, 0.16, 0.7, 0.03])
        sl = Slider(axs, "b - c", 0.0, 2.6, valinit=delta0)
        sl.on_changed(lambda v: setup(v))
        axb = fig.add_axes([0.15, 0.06, 0.18, 0.06])
        bp = Button(axb, "Pause")

        def toggle(_):
            st["play"] = not st["play"]
            bp.label.set_text("Pause" if st["play"] else "Play")
        bp.on_clicked(toggle)
        btns = []
        for i, (lab, v) in enumerate([("0", 0), ("1", 1), ("√2", math.sqrt(2)),
                                      ("√3", math.sqrt(3)), ("2", 2), ("2.4", 2.4)]):
            b = Button(fig.add_axes([0.38 + i * 0.09, 0.06, 0.08, 0.06]), lab)
            b.on_clicked(lambda _, v=v: sl.set_val(v))
            btns.append(b)
        fig._keep = (sl, bp, btns)

    anim = FuncAnimation(fig, update, frames=frames if gif else None,
                         interval=30, blit=False, cache_frame_data=False)
    if gif:
        anim.save(gif, writer="pillow", fps=30)
        print("saved", gif)
    else:
        plt.show()
    return anim


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--table", action="store_true", help="print the exact return table")
    ap.add_argument("--delta", type=float, default=0.0, help="imbalance b - c (default 0)")
    ap.add_argument("--gif", help="save the animation to this .gif instead of showing it")
    ap.add_argument("--frames", type=int, default=600)
    a = ap.parse_args()
    if a.table:
        table()
    else:
        animate(a.delta, a.gif, a.frames)
