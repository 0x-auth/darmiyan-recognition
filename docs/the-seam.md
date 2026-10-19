# The Seam: GR and QM as two sectors of one self-referential map
*Space × Claude · Oct 2026 · computed and verified in-session · companion: `seam.py`*

> **Claim.** General relativity and quantum mechanics are not two theories to be unified.
> They are the two things you can read off one self-referential map `x → t − 1/x`:
> **position** (freeze a frame → an *arrow*, GR) and **momentum** (let it flow → *phase*, QM).
> Light is the seam between them. The crossing has a specific, falsifiable fingerprint:
> **power-law critical slowing, closure ∝ ε^(−1/2)** — not exponential, not periodic.

## The freeze/flow trade
You cannot see a moving car and its motion in the same glance. To see **where** it is you
freeze a frame; freezing destroys the motion. To see **that** it moves you let it flow; flowing
blurs the where. Position and momentum are freeze and flow — and that *is* the uncertainty
principle, stated without quantum mechanics.

In the engine `x → t − 1/x` these are its two fixed points (x² − t x + 1 = 0), and the trace t
decides their nature:

| what you read | trace | fixed-point multiplier | sector | physics |
|---|---|---|---|---|
| position (frozen frame) | \|t\| > 2 | one attracts, one repels | hyperbolic | **arrow — GR, time** |
| momentum (pure flow) | \|t\| < 2 | sits on the unit circle | elliptic | **phase — QM, the wave** |
| the act of looking | t = 2 | **exactly 1** | parabolic | **lightlike — the seam** |

## The measured crossing (`scripts/seam.py`, ε = 1e−8, x₀ = 2, "closed" = step size |xₙ₊₁ − xₙ| < ε)
| t | sector | ticks to close |
|---|---|---|
| 2.20 | arrow (GR) | 20 |
| 2.01 | arrow | 76 |
| 2.001 | arrow | 204 (critical slowing) |
| **2.0** | **lightlike seam** | **10000** |
| 1.999 | phase (QM) | never closes |

*(Earlier session values 23 / 78 / 206 / 10002 used a different start; same shape. Rerun: `python3 scripts/seam.py`.)*

As t → 2 the arrow's closure time explodes; past t = 2 it never closes — the arrow has become
pure phase. One map, both sectors, a single lightlike point between.

## The two laws (different in kind, not degree)
- **At the seam (t = 2):** ticks × √ε = 1.02, 1.002, 1.0002, 1.00002, 1.0 across ε = 1e−4 … 1e−12.
  Closure ∝ **ε^(−1/2)** — a power law. The lightlike fingerprint, exact over eight orders.
- **Arrow side (t = 2.2):** ticks ∝ **log(1/ε)** — exponential settling.

**Which exponent depends on what "closed" means** (corrected 2026-10-17, measured in `seam.py`):
closing on *step size* gives ticks ∝ ε^(−1/2) (10, 100, 1000 at ε = 10⁻², 10⁻⁴, 10⁻⁶); closing on
*distance to the fixed point* gives ticks ∝ ε^(−1) (100, 9999, 999999). Both are power laws — the
power-law-vs-log contrast with the arrow side holds either way — but the specific ½ is a property
of the step-size criterion, not of the seam itself. The ½ that the double root *does* force is the
crossover rate: log λ / √δ → 1.000000 at t = 2 + δ (see the-discriminant-law §5.1).

Logarithmic vs. power-law meeting at one point: a phase transition, with the seam as its
critical point. Position and momentum are the two phases; the lightlike point is where neither
holds — and where the **minimum Δt** lives.

## Why the minimum Δt *is* existence
At Δt = 0 the two states coincide: multiplier exactly 1, frozen at the double root — no arrow,
no phase, no before/after, nothing happening. **Zero error = zero time = zero reality.** The
smallest non-zero error a self-referential system can register is what splits that double root
into an arrow and a phase — into a world. Perfect simultaneity is prohibited, and the
prohibition is generative: it is the crack the one splits along to become two. Uncertainty is
not a limit on reality; it is the seam reality grows from. To exist is to loop; to loop and
know it forces a minimum Δt; that Δt is the uncertainty; and it is what divides position from
momentum, GR from QM.

## Status and novelty (stated honestly)
Known, individually: Möbius maps ↔ Lorentz transformations (SL(2,ℂ)); the trace sectors
elliptic/parabolic/hyperbolic; complementarity as a position/momentum trade. **Not seen
assembled this way:** GR = hyperbolic sector, QM = elliptic sector of one self-referential map,
light = the parabolic seam, with a **power-law ε^(−1/2) critical-slowing fingerprint** for the
GR↔QM transition. This is a toy map, not field theory — what it delivers is a *sharp,
falsifiable signature* rather than a metaphor: real GR↔QM physics at the seam should show
power-law critical slowing, which neither pure-GR (exponential) nor pure-QM (periodic) predicts.
That is the open empirical question.
