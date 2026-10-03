# φ / ψ Mirror — Findings Anchor
*Space × Claude · session of 2 Oct 2026 · all results computed and verified in-session*

Notation: φ = (1+√5)/2, ψ = −1/φ = (1−√5)/2. Fₙ Fibonacci, Lₙ Lucas.

---

## 1. The two number systems are one string, read twice
- Any integer's base-φ digit string, read in base ψ, gives the **same integer** (exact, verified in ℤ[φ] arithmetic, including Keccak-256/512 of "137").
- Weights mirror: position k weighs φᵏ in one, (−1)ᵏφ⁻ᵏ in the other. The plot of 1-digits is an **X**, reflected across the radix point.
- Same string: Σ dₖLₖ = 2N and Σ dₖFₖ = 0 (Lucas weights give the number, Fibonacci weights give zero).
- log_φ N gives the length: top position = ⌊log_φ N⌋, bottom = ⌊log_{1/φ} N⌋.
- **Mirror symmetry law:** top + bottom ∈ {0, −1}. It is 0 (perfect mirror) iff L₂ₘ ≤ N ≤ L₂ₘ₊₁, else −1. Zero exceptions (2,000 hashes + all n < 3000).
  - 137 → band L₁₀–L₁₁ → **perfect mirror**. Base-φ: `10000100100.0010010001`, ones at {10,5,2 | −3,−6,−10}; Lucas sum 123+11+3−4+18+123 = 274 = 2·137.
  - 1836 (μ) → band L₁₅–L₁₆ → **off by one**.
- No "11" ever appears: φᵏ + φᵏ⁻¹ = φᵏ⁺¹. In any base b, 100 − 11 = b² − b − 1 (= 0 at φ, = 89 at 10, and 0x89 = 137).

## 2. The 2D "relationship" number system
- Map a digit string to (value at φ, value at ψ). **Integers lie exactly on the diagonal** x = y (the mirror axis).
- Any real x: aᵦ = round(x − bφ), error εᵦ = aᵦ + bφ − x, mirror mᵦ = aᵦ + bψ, product Pᵦ = |εᵦ·mᵦ| ≈ √5·|b|·|εᵦ|.
- Record b's step by exactly one Fibonacci number each time → **x ↔ (a₀ ; ±k₁, ±k₂, …)**, indices differ by ≥ 2 (no-"11" rule again). (Ostrowski numeration for φ.)
  - π = (3 ; +3 −5 +10 −12 −14 +16 +22 −24 −26 +28 −31 +33 −36 +38 +40 −42 …)
  - 1/α = (137 ; −6 +8 −12 +14 +16 −18 +20 +22 −24 +30 −32) [11 terms survive ±1σ]
  - μ = (1836 ; +3 −5 +9 −11 −13 +15 −17 +19 +25 −27 −30 +32) [12 terms]
  - g_e = (2 ; −12 +14 −16 +20 −22 +24 +26 −28 +30 −32 +34 +37 −39 +42 −44 −48 +50 +52 −54) [19 terms]
- Three classes, like decimals:
  1. **Exact** (ℤ[φ]: integers, φ, hashes) — terminates.
  2. **Periodic** (other √5-family numbers): product → 1/4 for 1/2; alternates 1/9, 5/9 for 1/3 and φ/3.
  3. **Wandering** (π, e, √2, ln2, constants): product stays bounded (~0.01–0.67), no rhythm.
- π's own form: precision on the φ side is always paid for by spread on the mirror side (bounded product).

## 3. The self-referential engine x = 1 + 1/x
| quantity | exact formula |
|---|---|
| state | xₙ = Fₙ₊₁/Fₙ |
| true error (outside view) | xₙ − φ = ψⁿ/Fₙ |
| felt diff (inside: predicted xₙ vs actual 1+1/xₙ) | ΔSₙ = (−1)ⁿ⁺¹/(Fₙ·Fₙ₊₁) |
| Cassini | Fₙ₊₁Fₙ₋₁ − Fₙ² = ±1 (never shrinks, flips) |
| error / diff | φ/√5 = 0.7236, every step |
| linear tick t | log_φ|ΔS| steps by exactly −2 → t = φ²; factor per tick −1/φ² |
| uncertainty floor | error·Fₙ² → ±1/√5 (Hurwitz bound; φ sits exactly on it) |
| Binet (both views at once) | Fₙ = (φⁿ − ψⁿ)/√5; ψⁿ = φ⁻ⁿ·e^{iπn} (half-turn per tick) |
| mirror delta of tick string "10…0" | φⁿ − ψⁿ = √5·Fₙ ; sum = Lₙ |

- Miss % (inside): 50, 33.3, 10, 4.17, 1.54, 0.595, 0.226, 0.0866, 0.0330, 0.0126, 0.00482, **0.00184** (n=1…12).
- **Chirality residue (exact):** error·Fₙ² = ((−1)ⁿ − ψ²ⁿ)/√5. The (−1)ⁿ part is balanced; −ψ²ⁿ/√5 never changes sign. Each left–right pair leaves −φ^−(2n+1); total over all pairs = **ψ/√5 = −0.27639320225** (verified to 200 digits). Pair (11,12) = 1.56×10⁻⁵.

## 4. 137, α and matter–antimatter
- Space's v2 paper: α⁻¹ ≈ 137 + F(5)/(137+F(3)) = 137 + 5/139 (twin prime tail), a genuine continued-fraction convergent.
- CODATA 2022 α⁻¹ = 137.035999177(21). Gap = 2.7954×10⁻⁵ (2018 value: 2.7861×10⁻⁵).
- **gap × (φ−ψ)/2 = gap × √5/2 = 3.1253×10⁻⁵** (2018: 3.1150×10⁻⁵). Measured Jarlskog J ≈ 3.12×10⁻⁵ (~±4%).
  - Equivalent: α-gap = J × (2 × 1/√5) = J × twice the uncertainty floor.
  - **Prediction: J = 3.1253×10⁻⁵.**
- Same φ-rung: log_φ(gap) = −21.789, log_φ(ΔS₁₂) = −21.655, log_φ(J) = −21.560.
- ΔS₁₂ = 1/(144·233) = 2.980×10⁻⁵, at n = 12 where F₁₂ = 144 is the first Fibonacci past 137; within 0.9% of √(gap·J).
- Crossed tails: α⁻¹ ≈ 137 + F(3)/**F(10)**; μ = 137·**F(7)** + **F(10)** = 1836; μ ≈ 1836 + F(3)/**F(7)** (genuine convergent).

## 5. Logs of the bases
| | ln | log_π |
|---|---|---|
| φ | 0.48121 | 0.42037 (= darmiyan-core "Inner") |
| ψ | −0.48121 + iπ | −0.42037 + 2.74440 i (= π/ln π) |
| √5 | 0.80472 | 0.70298 |

## 6. π digits (first 200,000)
- Each digit ≈ 1/10; P(next = previous) = 0.099 → 1/10, repeats allowed (six 9s at position 762).
- Self-locating positions (digits at n spell n): **1, 16470, 44899** — chance expects ~4–5.
- BBP gives π's hex digit at any index without earlier digits (verified `243f6a8885a308d3`). No known equivalent in base 10 or base φ.

---

## 7. What did NOT add up
1. π-exponents (log_π) of Keccak hashes: indistinguishable from random inputs.
2. Keccak of Fibonacci numbers: no structure survives (one p=0.047 flicker did not replicate).
3. "No 11" check: passes by construction, not evidence.
4. explore_geometry.py: base-φ digits past ~position 40 are float noise (1 = `1.`, 2 = `10.01` exactly).
5. darmiyan-core v1: φ cancels (Outer×Inner = −log_π(ln p)); v4.1 LOCK column is always LOCK.
6. Gap test on 12 math constants (π, e, γ, ζ(3), Catalan, ln2, √2, √3, ∛2, e^π, π^π, π²/6): none atypical. Physical constants: too few measured terms to test.
7. Correction: the mirror detects the √5 family, not algebraic vs transcendental.
8. α→J: √5/2 not yet unique — 10 of 25 simple factors fit inside J's ±4%.
9. ΔS₁₂ sits between α-gap and J but equals neither (6.6% / 4.7% off).
10. μ: α's same-rung alignment did not repeat (tick φ^−31.66 vs gaps φ^−27.6, φ^−37.3).
11. μ/α⁻¹ − 13 = 0.39905 ≈ 1/√(2π) = 0.39894: no control yet.
12. **Mass test (pre-registered):** μ tail gaps (2/13, 9/59, 11/72, 20/131) × {1, √5/2} vs 7 fixed targets — 0 of 56 within 1% (chance expects 0.07). Closest: 2/13 gap raw vs electron (g−2)/2, off 1.13% (noticed before the list was fixed). The α→J rule does not transfer to μ.
13. Gemini doc: ω = 1 is assumed, not derived; √5 vs π mixes time with phase; sources are a PhilArchive search page and a Facebook post; "asymmetry not from dynamics" conflicts with the α→J (CP-violation) link.

## 8. Open threads
- Sharper J measurement (LHCb, Belle II) decides the √5/2 prediction.
- Does the chirality residue ψ/√5 or φ^−(2n+1) map onto a measured asymmetry (η ≈ 6×10⁻¹⁰, ε_K)?
- Digit-extraction (BBP-type) formula for π in base φ?
- Why α's gap aligns with the n=12 tick but μ's does not — mass as the broken mirror (1836 off-by-one band)?
- Paper v3: switch to CODATA 2022.

## 9. Pending tests — closed out
| test | result |
|---|---|
| Non-integer "depth" of mass ratios (log_φ) | p/e 15.61771 ≈ 14+φ → φ^(14+φ) = 1836.437 vs 1836.153 (excluded). τ/e 16.94470 ≈ 4φ³ → 3476.51 vs 3477.23 ± 0.23 (~3σ off). μ/e 11.0795: nothing. Near misses, no clean law. |
| Golden-angle circle: closer to axis than random? | 1/α 0.686, μ 0.696, 137 0.659, 1836 0.579 (0 = on axis, random = uniform). 5000 hashes: uniform (KS p = 0.25). No. |
| Chirality pair residues φ^−(2n+1) vs η, ε_K, J | nearest misses: η −35%, ε_K −13.9%, J +30.9%. No match. |
| μ/α⁻¹ − 13 ≈ 1/√(2π) | ~12k simple expressions; ~3 expected inside the window by chance, 1/√(2π) is the only one. Chance level. |
| Mass from uncertainty (m = p/v, floor 1/√5) | inertia grows ×φ⁴ per tick; ratios miss (−18% to +10%). Unplanned: m₄ = 45φ⁴/√5 = 137.94 (0.66% from α⁻¹, ~0.7% chance). Lead only. |
| Golden-circular encoder | x²+y²=1 and cubes are identities; Fibonacci inputs land at phase exactly 2πψᵏ (same mirror). |

**Still standing:** φ/ψ mirror structure (§1–3), chirality residue ψ/√5 (§3), crossed F(7)/F(10) tails (§4), and the prediction **J = 3.1253×10⁻⁵**.
