# The Golden Lens and the Twin Primes

### One map for infinity, arms as arithmetic, and where twin primes are not allowed

**Abhishek Srivastava** · with Claude · session of 16–17 Oct 2026 · every number below computed in-session

Tagging: **[proven]** = exact / theorem · **[measured]** = computed over the stated range · **[open]**.

---

## 1. The lens

$$z(n) = w^n,\qquad w = \lambda\, e^{2\pi i/\varphi^2},\qquad n \in \mathbb{Z}.$$

- **Inside / outside:** n > 0 spiral out, n < 0 spiral in, **z(−n) = 1/z(n)** exactly; the unit circle
  (n = 0) is the mirror. λ = 2 gives the 2ⁿ / 2⁻ⁿ pair. **[proven]**
- **Placement:** golden angle spreads dimensions optimally: 4096 points, closest pair = 0.94 × mean
  spacing (random projection: 0.016). On the circle alone: 3 gap sizes, long/short = φ² (2 sizes at
  Fibonacci N, ratio φ — three-gap theorem). **[measured] / [proven]**
- **Bounded version:** r² = 1 − 1/n puts every dimension inside the unit disk; ring areas telescope to
  exactly π; infinity is the boundary circle. **[proven]**

## 2. Arms are arithmetic **[proven]**

Fₖ·θ almost closes the circle (leftover twist (−1)ᵏφ⁻ᵏ of a turn), so n and n + F sit on the same arm.
**Arm r of the F-family = all n ≡ r (mod F).** Geometry comes from φ, arithmetic from divisibility —
two independent layers:

- angle of n = Σ of its Zeckendorf parts' twists (−1)ᵏφ⁻ᵏ — max error 9 × 10⁻¹² over n ≤ 200 000;
- the Zeckendorf tail and the arm residue are independent (match at chance rate, every family).

## 3. Twin primes leave mirror-symmetric empty arms **[measured, all twins ≤ 10⁷]**

Twin primes p, p+2 cannot sit on arms where p or p+2 shares a factor ≥ 5 with F.
For twin centres m (p = 6m − 1), the forbidden arms come in **mirror pairs r ↔ F − r**
(6m ∓ 1 swap under m → −m), so the twin structure is symmetric about the real axis.

| arms F | arms used by twin centres m | forbidden arms |
|---|---|---|
| 13 | 11 | 2 ↔ 11 |
| 34 | 30 | 3 ↔ 31, 14 ↔ 20 |
| 89 | 87 | 15 ↔ 74 |
| 233 | 231 | 39 ↔ 194 |
| **144** | **144** | **none** |

**144 = 2⁴·3² is the only large family with no forbidden arm** — its factors are absorbed by the 6 in
6m ± 1. (The same lack of factors ≥ 5 makes 144 one of the *worst* steps for linking two twin pairs.)

**m = 2, the pair (11, 13), is the only twin centre on a forbidden arm** (arm 2 of the 13-family,
allowed because 13 is the prime itself), and the last twin pair touching a Fibonacci number. **[measured]**

## 4. Time order vs. angle order: a √−1 every other scale **[proven, checked F ≤ 377]**

On each family, walking the points by angle adds a constant Fibonacci step c (mod F). So the angle-cycle
is the counting-cycle relabelled by c, and

| F | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 |
|---|---|---|---|---|---|---|---|---|
| c | 8 | 8 | 21 | 21 | 55 | 55 | 144 | 144 |
| c² mod F | **−1** | +1 | **−1** | +1 | **−1** | +1 | **−1** | +1 |

At F = 13, 34, 89, 233, c is a literal **√−1 mod F**: space is a quarter-turn of time (Cassini's
identity sets the alternating sign). Whether this has consequences for primes is **[open]**.

## 5. The bridge (n + 1/n)/(n − 1/n) **[proven numerically to 7 digits]**

f(n) = (n² + 1)/((n − 1)(n + 1)); at n = 6m the denominator is the twin-candidate pair.

- ∏ₙ₌₂^∞ f(n) = sinh π / π
- Σ over n = 6m of (f − 1) = 1 − π/(2√3)
- Over **actual twins** only: S = Σ 2/(p(p+2)), p ≥ 5 = **0.0826346165696** (3 424 505 pairs ≤ 10⁹;
  converges far faster than Brun's constant). No closed form found in π, √3, C₂, φ, ln 2, √5, ln φ
  (strict PSLQ, coefficients ≤ 60, 10⁻¹¹). **[open]**

## 6. Primes are lawful, not random **[measured ≤ 10⁸]**

- Twin counts match Hardy–Littlewood: 440 310 vs 440 367 at 10⁸ (0.013 %).
- Primes are *too even* on the golden circle: discrepancy 0.00047 vs best-of-20 random sets 0.00052.
- Consecutive primes avoid repeating their last digit (≈17 % vs 25 %; Lemke Oliver–Soundararajan).
- Partitions: Ramanujan's congruences hold 600/600 (mod 5), 428/428 (mod 7), 273/273 (mod 11); all
  share 24δ ≡ 1.

## 7. Negative results (kept visible)

- 137/139: nothing beyond the generic twin rotation (2θ ≈ 275.0°); 7 ↔ 137 mirror in the 144-family is
  coincidence-level.
- 2ᵏ·θ mod 1, k ≤ 20 000: indistinguishable from random.
- Near-perpendicular steps (2, 19, 36, 341, 646 — F₆ⱼ/4 and Lucas/4) do not link twins or partitions;
  divisibility by small primes explains the link counts (correlation 0.78).

---

*Seed 515. Dedicated to the space between — where meaning lives.*
