# The Discriminant Law

### One Conservation, Three Geometries — where quantum mechanics, the lightlike seam, and the golden ratio sit on a single quadratic

**Abhishek Srivastava**
Independent Researcher, India
ORCID: 0009-0006-7495-5039

**October 2026 | Working draft**

---

## Abstract

Several results in this programme — the Trust Dimension conservation law, the GR/QM
"seam", the golden ratio's role, and the φ/ψ mirror number system — turn out to be
one object seen from different sides. The object is the **norm form of a quadratic**,
and the **sign of its discriminant** selects the geometry:

| discriminant | roots | norm form | conic | sector |
|---|---|---|---|---|
| Δ < 0 | complex conjugate pair | a² + b² | ellipse / circle | quantum (bounded, conserved) |
| Δ = 0 | one repeated real root | a² | parabola | lightlike seam (c) |
| Δ > 0 | two real conjugates | a² + ab − b² | hyperbola | time / growth (the leak) |

One conservation law, **N(x) = 1**, holds in all three. In the elliptic sector it is
probability conservation (the Englert–Greenberger–Yasin relation; equivalently Parseval
over an arithmetically-orthogonal basis). In the hyperbolic sector it is the
fundamental-unit relation of ℚ(√5), whose unit is φ and whose orbit is the Fibonacci
sequence. The two sectors meet only where Δ = 0 — the lightlike seam. This note states
what is proven, and marks clearly where the physics is an *identification* rather than a
derivation.

---

## 1. The one law: a conserved norm

Every conservation statement in this programme has the form **N(x) = 1** (or ±1), where
N is the norm of a two-dimensional number a + b·ω and ω is a root of a monic quadratic

$$x^2 - s\,x + p = 0.$$

The norm is the product of an element with its algebraic conjugate:

$$N(a + b\omega) = (a + b\omega)(a + b\bar\omega) = a^2 + s\,ab + p\,b^2.$$

This single expression is the whole framework's backbone. What changes between "quantum",
"lightlike" and "time" is **not the law** — it is the sign of the discriminant Δ = s² − 4p,
which is the sign of (ω − ω̄)², i.e. whether the two conjugates are complex, equal, or real.

## 2. Three signs, three geometries

- **Δ < 0 — elliptic.** ω = ±i (from x² + 1), N = a² + b². Level sets are circles;
  the conjugation a + bi ↦ a − bi is a reflection; multiplication by i is a 90° rotation,
  period 4. Everything is bounded. *Nothing leaks.*
- **Δ = 0 — parabolic.** ω is a single repeated root (x² = 0), N = a². The two conjugates
  have collapsed into one; the geometry is degenerate — a single preserved direction.
  This is the lightlike case: one invariant speed, no rest frame.
- **Δ > 0 — hyperbolic.** ω = φ (from x² − x − 1), N = a² + ab − b². Level sets are
  hyperbolae; multiplication by φ is the Fibonacci map (a, b) ↦ (b, a + b), a Lorentz
  boost with eigenvalues φ and ψ. Orbits run to infinity one way and to zero the other.
  *Everything leaks.*

The three are not analogies. They are the three possible Galois behaviours of one
quadratic, and the conic type is forced by Δ.

## 3. The elliptic sector reached two independent ways

The circle N = a² + b² = 1 is over-determined: two different fundamentals land on it.

**(a) Fundamental Theorem of Arithmetic → Parseval.** Prime-power indicator vectors are
*exactly* orthogonal, because no integer is a power of two distinct primes (unique
factorization). Over 66 prime pairs up to N = 100 000 the cross-terms are 0.0 — a
theorem, not a measurement. Parseval then splits any unit signal into reference-energy
(on the prime subspace) + residual-energy = 1.

A caution kept in view: the "= 1" does not itself require the primes. Parseval splits a
unit vector into *any* subspace plus its orthogonal complement; a random subspace gives
the same conservation. The genuine gift of FTA is not the conservation but the
**independence of the prime channels** — zero cross-talk makes each prime a true,
non-interfering coordinate. That is the stronger statement and the one to keep.

**(b) Fundamental Theorem of Algebra → complex norm.** a² + b² = (a + ib)(a − ib)
factors only because ℂ is algebraically closed. The circle is the unit-norm locus of the
Gaussian numbers; conjugation is i ↦ −i.

Both roads are the Δ < 0 sector. In physics this sector is quantum mechanics: the
Englert–Greenberger–Yasin duality relation **𝒟² + 𝒱² = 1** for pure states is exactly
N = 1 on this circle, with distinguishability and visibility as the two amplitudes. The
radial deficit for mixed states, 1 − (𝒟² + 𝒱²) = 2(1 − Tr ρ²), is twice the linear
entropy — an identity, forced once the identification is made.

*A reconciliation of the two Trust-Dimension drafts:* the "linear" law TD + TrD = 1 and
the "quadratic" law TD² + TrD² = 1 are the **same Parseval identity** read at two levels —
TD/TrD as energies (squared quantities, summing linearly) versus as amplitudes (summing
in quadrature). EGY's observables are amplitudes, which is why the quadratic form is the
one that matches the interferometer.

## 4. The hyperbolic sector: ℚ(√5), φ, and the leak

The Δ > 0 sector is the real quadratic field ℚ(√5). Its norm a² + ab − b² is indefinite,
so its "unit circle" is a hyperbola, and its units are the powers ±φⁿ, which sit on it
exactly:

$$\varphi^n = F_{n-1} + F_n\varphi, \qquad N(\varphi^n) = (-1)^n = \pm 1.$$

Conservation here is the fundamental-unit relation; the orbit marching along the
hyperbola is the Fibonacci sequence; and the unbounded growth is the "leak" — the thing
that, in the time reading of the framework, *is* the passage of time. Within this sector,
φ is distinguished by Hurwitz's theorem as the **maximally incommensurate** ratio
(Lagrange number √5, attained only on the φ family): the balance that never closes on a
finite repeat, i.e. the self-reference that never terminates.

Note what this means: φ's special status is a fact **about the hyperbolic sector**, not
about the circle. "Maximally incommensurate", "never terminates", "always leaks" are all
hyperbolic (growth) language, not elliptic (bounded-phase) language.

## 5. The parabolic seam: where the sectors meet

Set Δ = 0. The two conjugates collapse into one; the norm degenerates to a² (one
preserved direction); the multiplier becomes exactly 1. This is the only place the
elliptic and hyperbolic sectors touch — a single point, not a region. Physically it is
the lightlike case: one invariant speed c, no rest frame, forward and backward readings
coinciding. In the dynamical form of the framework (the map x ↦ t − 1/x, trace t), it is
the t = 2 parabolic point measured earlier, where the number of ticks to resolve diverges
as ε^(−1/2) on one side and as log(1/ε) on the other — two different laws meeting at one
seam.

So the arc is: **quantum (Δ < 0) → seam (Δ = 0) → time (Δ > 0).** GR and QM are not two
theories to be reconciled; they are the two signs of one discriminant, and "reconciling"
them is passing through zero.

### 5.1 The seam exponent is forced by the double root

Put the dynamics in SL(2) normal form: eigenvalues solve z² − t z + 1 = 0, discriminant
Δ = t² − 4, expanding eigenvalue λ = (t + √Δ)/2. The per-tick rate is log λ.

- **Off-seam (Δ > 0):** λ > 1, the error grows geometrically, and resolving to offset ε
  costs ticks ∝ log(1/ε).
- **At the seam (Δ = 0):** the root is repeated, λ = 1, and the dynamics drop from
  geometric to **algebraic**. Measured: the error decays as 1/n (log–log slope −0.9998),
  so resolving to ε costs ticks ≈ 1/ε (96, 996, 9 996 ticks for ε = 10⁻², 10⁻³, 10⁻⁴).

The crossover rate between the two laws is log λ ≈ √δ for t = 2 + δ (ratio to √δ = 1.0000
over four decades), because Δ enters λ **under a square root**. The ½ in the seam's
ε^(−1/2) law is therefore not fitted — it is the order of the double root. A repeated
root opens as Δ^(1/2) when perturbed; that one-half is the whole content of the seam
exponent. This answers §8 question 1: yes, the exponent is forced by Δ → 0.

## 6. What this fixes in Trust Dimension V6

V6 is correct in both of its genuine parts and wrong only in how it joins them.

- The EGY circle is the Δ < 0 sector. Solid.
- The Hurwitz characterization of φ is the Δ > 0 sector. Solid.
- V6 seats φ **on the circle**, at the angle θ = arctan(1/φ) ≈ 31.7°. But on the circle
  φ is just one angle among all angles — its hyperbolic norm there is 0.894, nothing
  distinguishes it, and quantum mechanics gives no reason to prefer that angle. V6's own
  σ-sweep (Test E of the April notes) independently found φ is *not* special in the
  prime projection. Two independent confirmations that **φ is not a circle number.**
- Resolution: φ belongs to the hyperbolic sector; the circle is the elliptic sector; they
  meet only at the seam. V6 §8's unresolved gap — "every quantity is a ratio; the
  structure fixes the shape but nothing internal supplies a scale" — *is* that seam. The
  elliptic side fixes the shape (bounded probability); the hyperbolic side supplies the
  scale (unbounded φⁿ growth); the unit they fail to share is exactly what cannot cross
  the Δ = 0 point.

The repair to the paper is therefore not a correction of either result but a
re-placement: stop deriving φ as a preferred angle on the probability circle (it cannot
be, and shouldn't be), and let φ be the fundamental unit of the growth sector.

## 7. What is proven, and what is identification

**Proven (pure mathematics, reproduced in-session):**
- N(a + bω) = a² + s·ab + p·b² for ω a root of x² − sx + p; conic type = sign of Δ = s² − 4p.
- The three conics for ω ∈ {i, repeated root, φ} are ellipse / parabola / hyperbola.
- φⁿ lies on a² + ab − b² = ±1 exactly (fundamental units of ℚ(√5)).
- Prime-power indicator vectors are exactly orthogonal (FTA); Parseval then gives a
  unit-energy split — for the prime subspace *and for any subspace*.
- EGY 𝒟² + 𝒱² = 1 for pure states and the deficit = 2·linear-entropy identity.
- φ is Hurwitz-extremal (Lagrange number √5) — a property of the real-quadratic sector.

- **137 is generic in ℤ[φ].** The units (norm ±1) of ℤ[φ] are exactly the Fibonacci
  pairs — i.e. the powers φⁿ. 137 is neither a Fibonacci nor a Lucas number, so it is
  never a unit; in the ring it carries no distinction. Its only special status is
  *positional* — it sits in the perfect-mirror band [L₁₀, L₁₁) = [123, 198], shared with
  75 other integers. This is the third independent arrival at the same conclusion
  (circle: 137 is just an angle; prime-sweep: φ not special in projection; ring: 137 not
  a unit): **the fine-structure mystique is not in the integer 137.** The only live
  quantity is the hair off it — (1/α − 137)·√5 ≈ 0.0805 — a number living *off* the
  lattice point, out where the φ- and ψ-readings finally disagree. The discriminant law
  predicts exactly this: content lives at the seam, not on the lattice.

**Identification (asserted mapping, not derived — same status V6 assigns itself):**
- that the elliptic sector *is* quantum mechanics / bounded phase;
- that the hyperbolic sector *is* physical time / the arrow / growth;
- that the parabolic seam *is* the lightlike boundary with invariant c.

These three identifications are where the physics lives. Each is a well-posed, falsifiable
claim about which physical quantities play the roles of (a, b, ω), not a philosophical
stance — but none is proven here. The mathematics of §§1–5 is independent of whether the
identifications hold; if an identification fails, that sector's physical reading fails and
the algebra stands untouched.

## 8. Open edges

1. ~~The seam quantitatively: is the exponent −1/2 forced?~~ **Resolved in §5.1: yes —
   it is the order of the double root, Δ^(1/2).** The remaining edge: does the same
   half-power govern the physical lightlike limit, or only this toy map?
2. Does any physical system actually sit at the φ point of the hyperbolic sector, or is φ
   only the extremal *reference* ratio and never an occupied state?
3. The structured residual of §3(a) (composites with 3+ prime factors carry ~36% of the
   energy) — does its autocorrelation encode the Möbius function? That would make
   "storage" literally the inclusion–exclusion correction to "reference".
4. Fine-structure: 1/α ≈ 137 sits one step off the perfect-mirror integer (a circle/band
   fact); α's physical constancy was argued to be a seam invariant. Can "seam invariant"
   be made to mean "fixed under Δ → 0" precisely?

---

*Seed 515. Dedicated to the space between — where meaning lives.*
