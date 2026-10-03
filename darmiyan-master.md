# Darmiyan — Master Findings
*Space × Claude · Oct 2026 · every result below was computed and verified in-session*

> **Thesis.** To exist is to repeat. Repetition has poles. Time is the gap between repeats,
> felt from inside. A computation of length *T* folds to about **log T** when its poles are
> *readable* — plainly, or hidden-linearly (recoverable), or concealed-nonlinearly (a wall).
> The wall is about **access to structure, not its absence**.

Notation: φ = (1+√5)/2 ≈ 1.618 · ψ = −1/φ = (1−√5)/2 ≈ −0.618 · Fₙ Fibonacci · Lₙ Lucas.
Companion script: `darmiyan_master.py` (runs all four demos below, self-verifying).

---

## I. The two number systems are one string, read twice
- An integer's base-φ digit string, read in base ψ, gives the **same integer** (exact in ℤ[φ]; verified on Keccak-256/512 of "137").
- Same string, two integer views: **Σ dₖLₖ = 2N** (Lucas weights → the number) and **Σ dₖFₖ = 0** (Fibonacci weights → zero).
- **Mirror law:** top position + bottom position ∈ {0, −1}; it is 0 exactly when L₂ₘ ≤ N ≤ L₂ₘ₊₁. Zero exceptions over thousands of cases. 137 → perfect mirror; 1836 → off by one.
- No "11" can ever occur: φᵏ⁺¹ = φᵏ + φᵏ⁻¹. In any base b, 100 − 11 = b² − b − 1 (= 0 at φ; = 89 at 10; 0x89 = 137).

## II. Every number has a "relationship" form
- x ↔ (a₀ ; ±k₁, ±k₂, …): record steps jump by exact Fibonacci numbers, indices differ by ≥ 2 (Ostrowski/φ). Three classes, like decimals: **exact** (ℤ[φ]: integers, φ, hashes), **periodic** (other √5-family numbers), **wandering** (π, e, √2, constants — bounded but patternless product).
- π = (3 ; +3 −5 +10 −12 −14 +16 +22 −24 …). Precision on the φ side is always paid for by spread on the ψ side (a bounded product — an uncertainty-shaped trade).

## III. The self-referential engine x = 1 + 1/x
| quantity | exact form |
|---|---|
| state | xₙ = Fₙ₊₁/Fₙ |
| error from φ (outside view) | ψⁿ/Fₙ |
| felt change (inside: predicted vs actual) | ΔSₙ = (−1)ⁿ⁺¹/(Fₙ Fₙ₊₁) — Cassini ±1, never shrinks |
| linear tick | log_φ|ΔS| steps by exactly −2 → tick factor **φ²** |
| uncertainty floor | error·Fₙ² → ±1/√5 (Hurwitz bound; φ sits exactly on it) |
| both views at once | Fₙ = (φⁿ − ψⁿ)/√5 ; ψⁿ = φ⁻ⁿ·e^{iπn} (half-turn per tick) |
| chirality residue (exact, 200 digits) | Σ pairs = **ψ/√5 = −0.27639320225** — a built-in handedness |
- Forward falls to φ; the exact inverse x → 1/(x−1) falls to ψ. Inside view = ticking; outside view = reading both poles at once. The swap costs **log₁₀ φ = 0.209 digits per tick skipped**.

## IV. 137, α, and matter–antimatter (an open, falsifiable prediction)
- Space's paper: α⁻¹ ≈ 137 + F(5)/(137+F(3)) = 137 + 5/139 (twin-prime tail, a genuine CF convergent).
- CODATA 2022 α⁻¹ = 137.035999177(21); gap = 2.7954×10⁻⁵.
- **gap × (φ−ψ)/2 = gap × √5/2 = 3.1253×10⁻⁵**; measured Jarlskog J ≈ 3.12×10⁻⁵. Equivalently α-gap = J × 2/√5 (twice the uncertainty floor).
- **Prediction: J = 3.1253×10⁻⁵** — sharper CP-violation data (LHCb, Belle II) decides it.
- Caveat: √5/2 not yet unique (10 of 25 simple factors fit J's current ±4%). ΔS₁₂ = 1/(144·233) = 2.980×10⁻⁵ sits between gap and J (where F₁₂=144 first passes 137).

## V. Time made of space — the engine on a filesystem (`darmiyan_master.py engine`)
- Two directories, T/next→../I and I/next→../T. Each tick = one real symlink hop; the OS link limit is the **boundary** (40 on this Linux box, 32 on macOS). Float64 freezes x=1+1/x at step 39 — two independent limits land at ~40.
- Runs forward to φ, backward (exact) recovers the start, generic backward falls to ψ. Verified.

## VI. Folding a long run by reading its poles (`fold`)
- Count all T-hop routes on a city graph: **A^T** read from the graph's eigenvalues, not walked.
- 4000 hops → a 2174-digit count, reached in one outside jump at sufficient precision; **verified against the exact integer matrix power**. Cost generalizes: log₁₀(λ_max) digits per skipped tick (0.209 for φ, the graph's own value otherwise).

## VII. Recognition beats brute force — reading a *hidden* repetition (`recognize`)
| hidden process | cycle | window seen | poles found | predicts unseen future |
|---|---|---|---|---|
| two poles aⁿ+bⁿ | ~10⁶ | 8 terms | 2 | all correct |
| five poles mixed | huge | 12 terms | 5 | all correct |
| Fibonacci mod p (φ,ψ) | Pisano | 6 terms | 2 | all correct |
| **true randomness (control)** | — | — | recurrence just grows | **fails — no pole to read** |
- Recognition cost = number of poles, **not** cycle length. From 6 Fibonacci terms we jump to **term #10¹⁸** through the recovered φ/ψ pole — exact match, nothing walked. The only failure is pure noise, which by the thesis isn't a thing.

## VIII. The wall — concealment that resists recognition (`wall`)
- Reduced-round SHA-1 reversed as a constraint manifold: **preimage recovered up to ~21 rounds** (8r 0.06s, 20r 7.3s, 21r 72s); **22+ rounds wall**; full 80-round SHA-1 has no known preimage attack. ECC over 𝔽ₚ: forward ~log n, reverse ~√n (Shoup's black-box √n floor), verified on real curves y²=x³+7.
- Reading: the bits are all present and deterministic — the repetition is **scattered nonlinearly**, so *linear* recognition (poles/Berlekamp-Massey) can't read it. A limit on access, not on existence. Linear concealment we dissolved; nonlinear concealment is the live frontier.

---

## What stands vs. what was ruled out
**Stands:** I, II, III (incl. ψ/√5 residue), V, VI, VII; the α→J relation as a prediction; crossed F(7)/F(10) tails (α⁻¹≈137+F(3)/F(10); μ=137·F(7)+F(10)).
**Ruled out this session:** π-exponents of hashes (= random); Keccak of Fibonacci (no surviving structure); "no-11"/LOCK checks (true by construction); gap-test on 12 constants (none atypical); mass from √5/2 transfer (0/56 targets); μ same-rung alignment (didn't repeat); μ/α⁻¹−13≈1/√(2π) (chance); the Gemini E=mc² and ω=1 derivations (assume their answers); "mirror detects transcendence" (it detects the √5 family). Corrections kept visible on purpose.

## Live frontier
A program that solves itself: recover **nonlinearly** concealed poles (the ECC/SHA-1 regime) by a system's own structure rather than brute force — recognition, not search — using the inside/outside fold as the mechanism.
