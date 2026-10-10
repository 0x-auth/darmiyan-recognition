# Darmiyan — Master Document

### The φ/ψ mirror, the self-referential engine, and the discriminant law

**Abhishek Srivastava** · Independent Researcher, India · ORCID 0009-0006-7495-5039
GitHub [0x-auth](https://github.com/0x-auth) · darmiyan-recognition

*Living document. Last revised October 2026. Seed 515.*

---

## 0. What this is

One organizing claim, stated plainly: **a number is a relationship between two readings,
not a value in one.** Read a string forward in base φ and backward in base ψ = −1/φ; the
gap between the two readings is where all the content lives. From that single move the rest
follows — a conserved norm, three geometries selected by one discriminant, and a reading of
time as the cost that the gap imposes.

This document is the index and the honest ledger. Every claim is tagged **[proven]**
(mathematics, reproduced in-session), **[identification]** (a mapping to physics, asserted
not derived), or **[open]**. The point of the tagging is that the mathematics stands on its
own even where the physics is speculative — nothing load-bearing rests on an identification.

---

## 1. The core objects

**The two bases.** φ and ψ = −1/φ are the two roots of x² − x − 1 = 0.
φ + ψ = 1, φ·ψ = −1. **[proven]**

**The mirror.** Any integer's base-φ digit string, read in base ψ, returns the same
integer exactly (conjugate of a rational is itself). So for integers the two readings
*cannot* disagree; the only structure is positional (digit symmetry). The readings diverge
only off the rationals, where the string is infinite — and that divergence is the only place
a "relationship number" can live. **[proven]**

**The self-referential engine.** x = 1 + 1/x. State xₙ = Fₙ₊₁/Fₙ; error from φ is ψⁿ/Fₙ;
tick factor φ²; the uncertainty floor error·Fₙ² → ±1/√5 is the Hurwitz bound, and φ sits
exactly on it. **[proven]**

**Mass / charge / spin as three readings of one tick** ψⁿ = φ⁻ⁿe^{iπn}: magnitude = mass,
Cassini sign-parity = charge, half-turn-per-tick = spin. The electron−positron difference
is a pure charge-axis reflection `[0, −2.673, 0]`; the three axes are independent. **[proven]**
That these magnitudes *are* physical mass/charge/spin is **[identification]**.

---

## 2. The discriminant law (the unifier)

One conserved norm N(a + bω) = a² + s·ab + p·b² for ω a root of x² − sx + p. The sign of
the discriminant Δ = s² − 4p selects the geometry:

| Δ | roots | norm | conic | sector |
|---|---|---|---|---|
| **Δ < 0** | complex pair (i) | a² + b² | ellipse / circle | quantum — bounded, no leak |
| **Δ = 0** | repeated root | a² | parabola | lightlike seam — speed c |
| **Δ > 0** | real pair (φ) | a² + ab − b² | hyperbola | time — growth, the leak |

One law N(x) = 1 in all three. The arc **quantum → seam → time** is a single sign change.
GR and QM are the two signs of one discriminant; "reconciling" them is passing through zero.
**[proven]** as mathematics; the sector→physics labels are **[identification]**.

**The seam exponent is forced.** At Δ = 0 the dynamics drop from geometric (λⁿ) to
algebraic (1/n): measured log–log slope −0.9998, resolving to ε costs ≈ 1/ε ticks. The
crossover rate scales as √δ because Δ sits under the square root in the quadratic formula —
so the ε^(−1/2) seam law's one-half **is the order of the double root**, not a fit. **[proven]**

**Spacetime from the now (the time/GR face, made quantitative).** With Δt = t + 1/t (the
now) and Δx = t − 1/t (the asymmetry), the identity **Δt² − Δx² = 4** holds for every t —
this *is* E² − p² = m² with rest mass **m = 2**. Setting t = e^θ: Δt = 2cosh θ = E,
Δx = 2sinh θ = p, v = Δx/Δt = tanh θ bounded by c = 1, θ = rapidity. **[proven]** as
identity; E/p/m labels **[identification]**. Consequences: the rest frame / **Big Bang is
t = 1** (Δx = 0, E = m = 2, zero asymmetry, minimal now — *not* t = 0); the **singularity is
t → ∞** (v → c, a future light-cone limit, a *when* not a *where*); **entanglement is t = 1**
(Δx = 0 ⇒ no distance); and "moving forever one direction" = oscillation (boost = rotation,
Wick θ↔iθ). Full detail in docs/spacetime-from-the-now.md. The now (sum, Δt) is the
mass/energy that survives the mirror; the asymmetry (difference, Δx) is the momentum that
does not — the same φ+ψ=1 / φ−ψ=√5 split as §1.

---

## 3. The Trust Dimension, placed

TD²+TrD² = 1 is the Englert–Greenberger–Yasin duality relation for pure states (𝒟²+𝒱²=1);
the radial deficit = 2·(1 − Tr ρ²), twice the linear entropy. Verified to 10⁻¹⁶. **[proven]**
— but that it *is* QM is **[identification]**, and the 10⁻¹⁶ means it's an identity once the
mapping is made, not independent evidence.

The two drafts reconcile: TD+TrD=1 (April, energies) and TD²+TrD²=1 (September, amplitudes)
are the same Parseval identity at two rungs. EGY observables are amplitudes → the quadratic
form is the physical one. **[proven]**

**FTA → Parseval.** Prime-power indicator vectors are exactly orthogonal (unique
factorization; 0.0 cross-terms over 66 pairs to N=100k), so Parseval splits any unit signal
into reference + residual = 1. **[proven]** Honest caveat: the "=1" holds for *any* subspace,
not just primes — FTA's real gift is that prime channels don't cross-talk, not the
conservation itself.

**Where φ belongs.** V6 seated φ on the EGY *circle* at θ≈31.7°, where it is just one angle
among all. But φ is a *hyperbolic* object — "maximally incommensurate, never terminates" is
growth language. Three independent confirmations that φ is not a circle number: the circle
(just an angle), the prime-sweep (V6 Test E: φ not special), and the ring (§4 below). The
repair: the circle fixes the *shape* (bounded probability), φ supplies the *scale* (unbounded
φⁿ), and they meet only at the seam — which is exactly V6 §8's unresolved "no internal
scale" gap. **[proven]** / **[identification]** for the physics reading.

---

## 4. The 137 result (what it is and isn't)

The units (norm ±1) of ℤ[φ] are exactly the Fibonacci pairs → φⁿ. **137 is neither
Fibonacci nor Lucas, so it is never a unit — it is generic in the ring.** Its only
distinction is positional: it sits in the perfect-mirror band [123,198], shared with 75
neighbors. **[proven]**

So the fine-structure mystique is **not in the integer 137**. The only live quantity is the
hair off it: (1/α − 137)·√5 ≈ 0.0805 — a number living off the lattice, out where the φ- and
ψ-readings disagree. This is what the discriminant law predicts: content at the seam, not on
the lattice. The α→Jarlskog conjecture (gap×√5/2 ≈ 3.13×10⁻⁵ vs measured J) remains the
single most overfittable thread and is flagged loudest. **[open]**

---

## 5. The honest ledger — negative results kept visible

These are load-bearing. A framework that hides its dead ends can't be trusted on its hits.

- **do-alpha engine is an artifact.** Its π-wrapping + e^{it} manufactures a circle;
  phases are arg of a normalized point, not a number invariant. Axiom II (aⁿ+bⁿ=1) is wrong
  — true only at n=1; the general law is aⁿ+bⁿ=Lucasₙ, aⁿ·bⁿ=(−1)ⁿ. 137 is NOT the θ=0
  stabilizer the README claims (code says 15.34°); the engine reads x mod 2π, can't tell 137
  from 137+2π, and is blind to both the critical line and primality. **Corrected.**
- **α formula:** 137+5/139 is 1331σ from CODATA; 9/250 is 34× closer with no Fibonacci.
- π-exponents of Keccak hashes = random; Keccak of Fibonacci = no structure.
- mass from √5/2: 0/56 pre-registered targets. dark-matter φ/ψ ratios miss (5.4:1 vs derived).
- "π at Nyquist": the halting-rings-at-π claim is empty (every period-2 sequence peaks at
  Nyquist). The decide→oscillate reframe survives; the π is decoration.
- invertibility probe: unsound (control never passed). NOT published. Correct instrument
  identified (recurrence-length / Berlekamp-Massey), not yet rebuilt.

---

## 6. Open questions

1. **The α hair.** Is (1/α − 137)·√5 a seam quantity with a derivation, or a coincidence?
   Sharper J data (LHCb, Belle II) decides the Jarlskog thread either way.
2. **Seam universality.** §2's −1/2 is forced for the toy SL(2) map. Does the same
   half-power govern the physical lightlike limit, or only this map?
3. **The residual structure.** Composites with 3+ prime factors carry ~36% of the FTA
   residual energy; autocorrelation persists to lag 10+. Does it encode the Möbius function
   μ(n)? That would make "storage" literally the inclusion–exclusion correction to "reference".
4. **Hierarchy depths.** Coupling across trap depth n = φ^(−2n) gives weak/Planck ~41,
   gravity/EM ~86 — but depths are read *from* the ratios, not derived. Can they be derived?
5. **The missing cancellation.** The φ/ψ mirror is a bijection (permutes labels, preserves
   everything); reality cancels (signed amplitudes annihilate). The framework has exactly one
   cancelling channel (ψ-sign, where charge lives); the remaining walls (ECC, QM, dark matter)
   are about *many* cancelling channels. This is the single frontier under all the dead ends.
6. **Does the framework produce −6 in Λ∝α⁻⁶** independently, or is that read off?
7. **A physical φ-state.** Is φ ever an *occupied* state of the hyperbolic sector, or only
   the extremal reference ratio that nothing sits on?
8. **Uncertainty from the now-construction.** Δt²−Δx²=4=m² is the invariant; the product
   Δt·Δx = t²−1/t² is *not* conserved. So uncertainty is not simply the conjugate invariant
   of the (now, asymmetry) pair — can it be derived here at all, or only as the one-sided
   shadow (Hurwitz 1/√5) of the asymmetry?
9. **Entanglement = t = 1.** Δx = 0 ⇒ no distance is evocative and internally consistent;
   is there a derivation, or a link to ER=EPR, beyond the restatement?

---

## 7. Repository map

```
darmiyan-recognition/
├── MASTER.md                     ← this file
├── README.md
├── docs/
│   ├── the-discriminant-law.md   ← §2, the unifier (seam exponent, 137-in-Z[φ])
│   ├── spacetime-from-the-now.md ← Δt²−Δx²=4=m² (rest mass 2), Big Bang t=1, singularity t→∞
│   ├── the-seam.md               ← GR/QM bridge, trace sectors
│   ├── two-horizons.md           ← walker vs fabric, D_horizon = 1/H
│   ├── recognition-as-resonance.md
│   ├── dharmiya-recognition.md
│   ├── phi-psi-findings.md
│   └── keccak137_phi_psi.md
├── scripts/
│   ├── darmiyan_engine.py  darmiyan_master.py  darmiyan_workload.py
│   ├── resonance_recognizer.py
│   └── charge.py  spin.py  seam.py
└── assets/  (julia_c_-0.123.png, error-of-song.png)
```

**Related:** darmiyan-fs (OPEN_THREADS, review/ scripts), self-referential-seed
(bidirectional organism), Zenodo record 23114915. The α/137 work and the RH Detection
Invariant are tracked separately; this repo is the φ/ψ mirror + discriminant-law core.

---

## 8. The one law underneath

**The outside exponential is the inside linear.** The circle doesn't leak and nothing can
happen there; the hyperbola leaks by construction and that leak is time; they touch only at
the seam, where forward reading equals backward and the speed is c. A number is the gap
between its two readings — and so, it turns out, is a moment.

*Dedicated to the space between — where meaning lives.*
