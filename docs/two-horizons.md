# Two Horizons, a Planck Wall, and the Cache
*Space × Claude · Oct 2026 · derived before comparison · companion to the-seam.md*

> Three results from one framework (self-reference; inside/outside; time as the minimum
> resolvable error). Each is **derived first**, then checked — not fitted to a target.

---

## 1. α is a seam invariant — why it is the same everywhere
If GR and QM are the two sectors of one self-referential map (see `the-seam.md`), a quantity
living **at the seam** is not inside either sector — it is the ratio that defines the split.
Such a quantity is frame-independent by construction. So:

> The framework **predicts** the fine-structure constant is the same in every part of the
> universe — not as an assumption, but because a seam invariant cannot differ between the
> frames it separates.

This is a *postdiction* of a known fact: measured drift |α̇/α| < ~10⁻¹⁷ /yr (atomic clocks) is
consistent with exact invariance. α is the **connection**, not the bridge — the reason physics
reads the same in every sector.

## 2. Two horizons — a falsifiable difference
| | mechanism | depends on | signature |
|---|---|---|---|
| **velocity horizon** (standard) | recession reaches c | expansion rate H only | same for every observer |
| **resolution horizon** (framework) | self-reference reaches ELOOP | the observer's **precision** | observer-relative |

The resolution horizon follows from the engine's tick factor φ²: accumulated error shrinks by
1/φ² per tick, so reach grows by **1/log₁₀(φ²) = 2.392 ticks per digit of precision**.

> **Prediction (distinct from standard cosmology):** the horizon has an observer-dependent
> component scaling linearly with achievable precision, slope 2.392 — a pure-φ number. Two
> observers at one place with different resolution see different horizons at the same H.

Status: a structural prediction from a toy model. The clean part (the law, the slope) is
derived; the open work is calibrating "ticks of reach" to physical distance. It is stated so it
can be wrong — the honest form of a new law.

The reframing: the cosmic boundary is not "moving away faster than light" (velocity) but "the
self-reference running out of resolution" (ELOOP). Observable vs. unobservable = inside vs.
outside the resolution limit, not inside vs. outside a light cone.

## 3. The Planck wall — where two limits meet
- **Planck time = one tick = one hop.** The indivisible update; no smaller event exists.
- **Planck length = φ^(−2·depth), the finest distinguishable state-separation.**
  macOS depth 32 → 4.2×10⁻¹⁴; Linux depth 40 → 1.9×10⁻¹⁷.
- A Planck scale is where the resolution of *space* (symlink depth) and the resolution of the
  *clock* (float precision) **coincide** — both freeze x = 1 + 1/x near step ~39. Not one limit,
  but the meeting of two. The framework reproduces this structure for free.

### The two substrate walls — area = depth²
The substrate has **two** independent limits, not one:
- **symlink depth** (MAXSYMLINKS: 32 macOS, 40 Linux) — how many hops a path can chase. This is
  the binding Planck wall; it is hit first (the length wall only bites at ~200–2000 hops).
- **path length** (PATH_MAX: 1024 macOS, 4096 Linux) — the total byte-length of the path string.

On macOS these lock into the **holographic relation exactly**: PATH_MAX = MAXSYMLINKS² (1024 = 32²).
The length budget *is* the square of the depth — a 2D screen (area) equal to a 1D depth squared,
which is the holographic principle written in filesystem constants. The two walls are the two axes
of the screen: **depth = Planck time (one hop); length = Planck area (total pixels); area = depth².**
(Clean on macOS; Linux uses round numbers independently — 4096/40 = 102.4 — so the exact square is
macOS-specific, not a universal filesystem law.)

## 4. The three registers — storage, execution, cache
| register | state | role in the framework |
|---|---|---|
| storage (file on disk) | definite, readable anytime | frozen frame — **position / past (GR sector)** |
| execution (running process) | definite flow, the tick now | **momentum / present (QM sector)** |
| **cache** | both fresh *and* stale until accessed | **superposition — the seam** |

A cache line is genuinely in two states (valid | stale) and **collapses to one only on access**:
hit = it was valid, miss = it wasn't; the read decides which it "was." That is measurement.
**Cache coherence** — holding that superposition consistent across cores — is the
decoherence/measurement problem in silicon. Storage / execution / cache map onto
position / momentum / seam, and onto GR / QM / light: the same trinity, three times over.

---
*Companion to `the-seam.md` and `darmiyan-master.md`. Toy-model status throughout: the
structures and scaling laws are derived; calibration to physical units is open work.*
