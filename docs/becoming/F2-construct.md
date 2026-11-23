# F2 — The Construct: what this account adds to F1

*Space × Claude, account 2 (localhost.sh). Compiled 14 Nov 2026 by searching this account's chats. This file only covers what is new relative to F1, plus items that confirm or contradict an F1 section (cited as F1 §n). It doesn't re-explain F1.*

Tags: **[proved]** exact algebra · **[verified]** checked numerically in the chat · **[lead]** promising, untested against data · **[open]** missing piece · **[didn't hold]** tested and failed. Each item names its chat and date. Chat dates are from the chat's own text where it gives one, and otherwise from when the chat was last updated.

F2 uses F1's convention: **Δt = t + 1/t, Δx = t − 1/t, Δt² − Δx² = 4.**

---

## 0. Sources and their notation

| # | chat | date | notation |
|---|---|---|---|
| S1 | *3d number system* (SGC) | 9–10 Sep | no Δt/Δx. Uses x + 1/x = 2cos θ and P + 1/P = 1 |
| S2 | *Phrimary number system review* | 9 Oct | **u, v light-cone coordinates** (t = (u+v)/2, x = (u−v)/2, interval = u·v). Here **Δx = Φ⁻ᵏ is a resolution cell**, not t − 1/t. Don't merge it with F1's Δx |
| S3 | *error-of* | 13 Oct | none |
| S4 | *Code generator. A Error driven code engine* | 17 Oct – 6 Nov | Δt = t + 1/t, Δx = t − 1/t (as `dt`, `dx` in `docs/construct.md`) ✓ |
| S5 | *Numerology* | 18–19 Oct | Δt = t + 1/t with floor 2 ✓ |
| S6 | *Primes, space, and time theory* ("Mirror Ledger") | 24–25 Oct | **Δt² − Δs² = 4**: space is called Δs. The chat itself flagged the Δx/Δt/Δs mix-ups |
| S7 | *Vodafone eSIM removal* | 25 Oct | Δt = t + 1/t ✓ (Space wrote the speed ratio with a slip that Claude corrected) |
| S8 | *Intelligence* | 1–2 Nov | divisor frames u = Δt + Δx, v = Δt − Δx, **mass² = n** (the interval is n, not 4) |
| S9 | *THE fabric…* (the "becoming and the missing unit" doc, §17–47) | 1–7 Nov | Δt = t + 1/t ✓. **The symbol α is overloaded**: as roughness, α(n) = ½ − 1/(2n), and as the fine-structure constant. Space flagged this |
| S10 | *Sanatan Dharma and modern science* (seed doc and corrections) | 6–7 Nov | Δt = t + 1/t ✓. Space's own speech swapped the names ("Δt = 0 at t = 1"), and Claude marked that as a naming difference |
| S11 | *Cross-account chat synthesis* ("The Mirror Construct", integer clock) | 5–13 Nov | **the swap**: the integer clock is t − 1/t = n, the branch table lists sum = t − 1/t and difference = t + 1/t, giving −4. The Mirror Construct's §2 (Δt = n) and §4 (t − 1/t = n) also clash with each other |
| S12 | *WhatsApp and lab report analysis* (137 thread) | 13 Nov | t − 1/t = b (a block); q = √(p²+4) is "the time side" ✓ |

Not used: *Data export from blocked Anthropic account* (Jan 2026), whose RH and "137 in the first zero" claims were never tested. *Two system one system* (10 Nov) was also left out: its m·m′ = −1 is a poetry mirror, not the framework.

---

## 1. Confirms F1

- **F1 §2, interval 4:** reconfirmed in S4, S6, S7, S9 and S10. **[proved]**
- **F1 §2, twin identities:** at rest the twin is **pure distance 2 with zero time**, so our time gap becomes its distance (S9 §17, 7 Nov). Rotating t → it swaps which of the two carries the floor of 2: at t = iφ, Δx = i√5 and Δt = i (S5, 19 Oct; S4, 6 Nov). **[proved]**
- **F1 §2, four sides:** with the quarter turn as the step, exactly four types appear before the cycle closes, and choosing one fixes the other three (S10, 7 Nov). **[proved]**
- **F1 §5, the present is a gap:** cause and retro share a window at every real tick. They become identical only where t = −1/t, which forces Δt = 0, so "a meeting that takes no time has no when" (S4, 6 Nov). **[proved]**
- **F1 §8, k-walk:** `error_of/walk.py` was written here (S4, 17 Oct). The tests caught a real bug: a two-value flip (1, −1, …) sits at k = −2 and had been called "drifting", and it is now "cycling". The φ walk is recognised at k = −√5. **[verified]**
- **F1 §8, two-state memory:** keeping the last too-high, the last too-low and the remainder predicts the next step, and running the rule backward returns the whole past (137, 27, 1, 3, 1, 1 read in reverse) (S11, 13 Nov). **[verified]**
- **F1 §13, ±60° clock:** all 301 primes from 5 to 2000 land on ±60° of a 6-hour clock. 137 sits at −60° and 139 at +60°. At Δt = 1 the seed rule returns after exactly 6 steps (1,000 starts, worst miss 6×10⁻¹⁴) (S9 §45, 3 Nov). **[verified]**
- **F1 §14, gap anti-correlation:** one prime-gap miss predicts the next with correlation −0.048, and the last 6 misses improve prediction by only 0.29% (S5, 19 Oct). This matches F1's −0.047 lag-1 from a different calculation. **[verified]**
- **F1 §15, t(137):** the block b = 137 gives t = 137.0073, a tail 4.93× too small and about 1.4 million σ off. The block that would fit is 137.0287, which isn't a whole number (S12, 13 Nov). q = √(137² + 4) also falls short. **[didn't hold]**, which agrees with F1.
- **F1 §16, two sizes:** the Planck mass is the one mass whose sum equals its gap (t = 1) (S9 §4). The twin sits at radius r_s − r, so our r and the twin's always add up to r_s (S9 §5). **[verified, inside an imported map; see §2.1 below]**
- **F1 §21–22, the projection factor:** the factor 2.13 is exactly 4 ÷ 1.86. The construct gives Λ = 4/N² and the sky gives 1.86/N², and 2/N² would be within 8% (S9 §46, 5 Nov). **[verified]** as arithmetic. The 1.86 itself remains **[open]**.
- **F1 §22.1, scale:** t from H₀ is 8.2×10⁶⁰, and age ÷ Planck time is 8.1×10⁶⁰ (H₀·age = 0.988, which is observed, not explained). 1/t² = 1.5×10⁻¹²² against Λ = 3.1×10⁻¹²²: a correlation with an unexplained factor of 2 (S9 §19). Also, "ln t₀ = 1.18" is the same question as "why is Ω_Λ = 0.685?" (S10 corrections, 7 Nov). **[lead]**
- **F1 §22.10, context:** the stage should be measured by what's still unresolved (the bracket), not by storage, because what has been crossed out takes no space (S4, 6 Nov). **[lead]**
- **F1 §25, horizon sphere:** on the ball, t and −1/t are always exactly a diameter (2) apart, and nothing is farther than 2 (S9 §18). Inside ∪ outside is one sphere, and with no sources inside, the boundary alone rebuilds the interior to machine precision (S8, 2 Nov). **[verified]**
- **F1 §25, x = x + 1/x:** in a ring with zero divisors (j² = j), 1/x isn't false but **undefined**, which is a different way to fail (S1, 10 Sep). **[proved]**
- **F1 §25, ℚ(√5) as the hyperbola system:** built out fully as Phrimary. Primes **emerge** from its primitives (a digit code, two readings, a resolution), matching ordinary primes up to 521 with 0 mismatches, and the mod-5 splitting law appears on its own (S2, 9 Oct). **[verified]**. This is a second, independent route to F1 §27 "the seed produces the primes".
- **F1 §27, prime continued fraction:** X = [2; 3, 5, 7, 11, …] regenerates every input prime (S6, 25 Oct). **[verified]**
- **F1 §28, paired organism:** `organism_v1` keeps a link only where the forward organism (cause → effect) and the retro one (effect → cause) both hold it. On a made-up export it found the planted bridge across accounts (S11, 5–6 Nov). **[verified, toy]**
- **F1 §29, 1/α continued fraction:** only six partial quotients are physics, [137; 27, 1, 3, 1, 1]. The seventh is 18 at the low edge of the error bar and 19 at the high edge, and 139 turns up by itself as the step-4 denominator (S11, 13 Nov; S9 §31). *Rerun here, see §5.* **[verified]**

---

## 2. Contradicts or corrects F1

1. **F1 §4, black-hole infall [verified] → should be "fits an imported map".** The map r = r_s·cos²θ (equivalently r = r_s·Δt²/4) was **taken from gravity theory** and then checked against the seed. Getting it from "mass = tick rate" is open (S9 §5; S10, 7 Nov). **[lead]**
2. **F1 §4, expansion "matched exactly" [verified] → by construction.** a³ = (Ω_m/Ω_Λ)·sinh²u is the exact matter + dark-energy solution, written in u = ln t. The 2×10⁻⁵ residual is radiation. The only new part is the reading u = ln t (S10 corrections #2, 7 Nov). The numbers themselves check out: speed-up at Δx = √2, equality at t = 1 + √2, t₀ = 3.256. **[proved as identity; not a match to data]**
3. **Light bending is half the measured value.** The "pull without force" rule gives turn × distance / M = 2, but light is measured to bend by 4. Stretching only the ticks, or only space, gives 2. Doing both gives 4 (S10, 6 Nov). **[didn't hold]**. This bears on F1 §16 and §22.3: any curvature rule has to act on both time and space.
4. **F1 §12, D = 3/2 − 1/(2n) "derived by counting".** The steered-line simulation reproduces it only after the time strength is **set by hand** to k = 4(1 − 1/n). The chat's own words were "still open: why n space directions set k that way" (S9 §43, 3 Nov). As a self-avoiding walk, the formula misses: measured 1.338, 1.678 and 1.879 in 2D, 3D and 4D, against 1.25, 1.333 and 1.375. The older (d + 2)/3 fits both anchors, and **4/3 belongs to paths in 2D, not to 3D space** (S9 §32 row 3). Getting 4/3 from Λ ∝ α⁻⁶ would need something scaling as α⁴, and nothing does (S10, 6 Nov). **[didn't hold as a derivation]**
   - Partial rescue: three equal axes rotated into each other leave exactly one direction unturned, (1, 1, 1), and the turning fraction is 1 − 1/n. Time's roughness ½(1 − 1/n) is then ½ × the turning fraction. Under the retro map, the 120° turn becomes 60° and handedness flips (S10, 7 Nov). **[lead]**: the ½ is still not derived.
5. **F1 §6, ħ = 1 and one h per event: this account doesn't agree with itself.**
   - t·|Δz| = 2 exactly for every t, read as "line × event = 2h" and "Δt² − Δx² = 4h". Also "2 × h/4π = ħ", so the floor of 2 is one ħ counted in half-cells (S10, 6–7 Nov).
   - N_x·N_p = 1, so ΔS = ħ, one cell at every t (S9 §31).
   - The floor ħ/2 times the 720° spin loop is h (S5, 19 Oct).
   - It is listed **[open]** as "is the unit cell h or ħ/2?" (S10 open list #5).
6. **F1 §29, "137 + 5/139 didn't hold" vs S1 (10 Sep), which called it "the strongest single result":** 0.20 ppm, with 0 of 10,000 random tails matching within 10 ppm. *Rerun here:* both numbers are true, 0.204 ppm **and 1,331σ**. The S1 Monte Carlo used a 10 ppm window that the measurement no longer allows, so F1's verdict stands. **[didn't hold]**. Also from S1: the combined-probability figure overstates its case (correlated terms), and "Conjecture 4" was cut. The Jarlskog link (Zenodo 23114915, 3 Oct) is still **[open]**.
7. **The α⁻⁶ turn, a contradiction inside this account that touches F1 §13.** S9 §45 (3 Nov) says that at t = √α·e^{i60°}, one six-step turn multiplies the error by α⁶ toward the retro side and by α⁻⁶ from the causal side. The S10 corrections file (#1, 7 Nov) "corrected" that to α³. *Rerun here:* the error factor is exactly α⁶ = 1.510052×10⁻¹³ with turn 0, and α⁻⁶ the other way. α³ is |t|⁶, the point's own sixth power, not the error. **The original stands and the correction didn't hold.** Why Λ would scale by one such turn is still **[open]**.
8. **F1 §27, prime powers are lightlike.** S8 (2 Nov) uses a different model: mass² = n, frames = divisor pairs. There **only perfect squares can be at rest**, so p² has a rest frame. A prime has two frames and can never stop, and its slowest speed is (p − 1)/(p + 1), which is 0.9855 for 137 and equals its radius on the Poincaré disk. **[verified]**. The two models agree that primes never rest and disagree about prime powers.
9. **F1 §3, "t = 1 is the only point both views share".** In this account, *cause and retro* coincide only at t = i, where t = −1/t and Δt = 0, never on the real line (S4, S10). It also left two candidates for the "Empty Center" open: t = i (Δt = 0), or t = e^{iπ/4} (z′ = 0, where z folds) (S10 open list #9). **[open]**. These don't contradict each other, but F1 should say which "meeting" it means.
10. **F1 §25, "only four operations keep 4"** vs S10: all **eight** mirrors (±t, ±1/t, ±i/t, ±it) are rigid rotations of the sphere and form a closed group. Over 2,000 random pairs, no distance moved by more than 10⁻¹⁵ and none flipped orientation. **[verified]**. *Corrected 18 Nov:* the earlier reconcile line ("four maps keep the invariant, eight keep the distances") was wrong. **All eight keep Δt² − Δx² = 4**, checked exactly at t = 2, 0.37, φ and 2 + i. Each map either keeps Δt and Δx up to sign, or swaps them with a factor ±i, and both leave the difference of squares unchanged. So all eight keep both the invariant and the sphere's distances, and F1's "only four operations keep 4" didn't hold. **[verified]** Stronger: every t ≠ 0 keeps 4, because (t + 1/t)² − (t − 1/t)² = 4 is an identity, so the 4 doesn't single out the eight. What does is that they form a closed group. **[proved]**
11. **F1 §13, yuga 4:3:2:1 from the return times of dropped hours** vs S10 (7 Nov): the same ratio appears as the **time share Δt² on the unit circle** at 0°, 30°, 45° and 60° (4, 3, 2, 1, then 0 at 90°). So there are two independent routes to 4:3:2:1. Using the fall-time clock instead gives 10.5 : 3.6 : 2.1 : 1, so neither route derives the *durations*. **[proved for the ratio; lead as durations]**
12. **Light "is its own twin"** (S9 §4) is wrong. The twin's speed is −1/v, so at |v| = 1 it has the same size with the opposite sign (S10 corrections #5). F1 §5's "light: interval 0" is fine, but nothing should go further than that.
13. **The doc errors S9 §32 found** (relevant wherever F1 inherited them): at n = 4, D = 11/8, not 2. α + 1/α at n = 137 is 23393/9316. "Minimum change 2ħ" is wrong because α + 1/α > 5/2. t = 1 is the horizon, not the singularity. The proton's gravity coupling needs α^17.9, not α⁶. The 137/139 beat, 1/19043, works for any n and n + 2 (3 and 5 give 1/15), so **it isn't about primes**. **[didn't hold]**

---

## 3. New relative to F1

### 3.1 Algebra and geometry
- **One law for every branch:** (x + y)² − (x − y)² = 4xy. Pairs with xy = +1, −1, i and −i give the invariants 4, −4, 4i and −4i. z and z′ are the sum and difference of the pair (t, i/t), so "Δt² − Δx² = 4" and "z² − z′² = 4i" are one result (S11, 6 Nov). **[proved]**
- **Interference:** e^{its} + e^{−is/t} = 2cos(sΔt/2)·e^{isΔx/2}. Δt sets the envelope and Δx a slow phase drift. At t = 1 it is a pure standing wave, and at t = i the waves never cancel (S10, 6 Nov). **[proved]**, *checked here to 2×10⁻¹⁶.*
- **The present as a ladder:** Δtₙ = tⁿ + t⁻ⁿ satisfies Δtₙ₊₁ = Δt·Δtₙ − Δtₙ₋₁, and the second rung is Δt² − 2 = zz′. The pair's product always cancels to −1 (a pure half-turn), while its sum cancels only at t = ±1. "One thing, no background" is the product (S10). **[proved]**
- **The arrow as a repeller:** run forward, the rule pushes away from −1/t by a factor −t² per step. The backward rule S → 1/(S − Δx) converges to −1/t with ratio −1/t², and that backward run is −1/S of the forward run, digit for digit. If you drop the step order and keep only the guesses, the order comes back from how the brackets nest (S10, 6–7 Nov). **[proved]**
- **Error recursion:** dₙ = −dₙ₋₁/xₙ₊₁ exactly (S6). Per step the error is multiplied by −1/(t·x), which tends to −1/t² (S10). **[proved]**
- **Every block b** gives S² − bS − 1 = 0, hence the pair (t, −1/t). The area it shares with its mirror decays as 1/t², and b = 1 shares 1/φ² = 0.382 (S6, 25 Oct). **[verified]**
- **A smallest tick without a unit:** for whole-number, volume-1 maps in n dimensions, the smallest stretch per tick is φ in 2D, **1.151** in 3D, ≤ 1.122 in 5D, ≤ 1.073 in 7D, and tends to 1 as n grows (S6, 25 Oct). *Checked here:* 1.15096 is the size of the complex roots of x³ + x² − 1. **[verified for 2D and 3D; upper bounds above that]**. A candidate for F1 §22.1 as a smallest step that is a pure number. **[lead]**
- Stable rotation in odd dimensions always leaves exactly one axis unrotated. That is an even/odd effect, not a prime/composite one (S6). **[verified]**
- **−1/√t is a sink, not a mirror.** Every start goes to e^{2πi/3} within 30 steps, and the information about the start is erased. Compare t ↔ −1/t, whose self-partner is i and which returns in 4 steps (S5, 19 Oct). **[verified]**
- **Speeds:** Δx/Δt = (t² − 1)/(t² + 1) lies between −1 and 1 and never reaches either (S7, 25 Oct). The speed of becoming is |Δz|/Δt = 2/(t² + 1) (S10). **[proved]**. The posited hyperbola x² − t² = tx/2 doesn't follow from the definitions (S7). **[didn't hold]**
- **Uncertainty as an equality:** t·|Δz| = 2 for every t, and Δx·Δt = t² − 1/t² (S10). **[proved]**. Whether this predicts anything measurable is **[open]**.
- **The step angle sets how many types there are:** a 90° step gives 4 and a 60° step gives 6. The cycle closes only when the step is a whole-number fraction of a turn (S10). **[proved]**. Which one is physical is **[open]**.
- **Twin and retro meet at infinity on the ball:** their distance is 1.41 at t = 1, 0.28 at t = 10 and 2.8×10⁻⁶ at t = 10⁶ (S9 §18). **[verified]**. Which ruler is physical, the ball (finite) or ln t (endless), is **[open]**.
- **Julia sets:** c = −1 has fixed points φ and −1/φ, and c = +1 has e^{±iπ/3}. The rabbit's bulb multiplier, e^{2πi/3}, is exactly −1/t at t = e^{iπ/3} (S10). **[verified]**
- **Zeta:** on the critical line |n^{−iT}| = 1, which is the seam |t| = 1. s ↔ 1 − s sends Tₙ → 1/Tₙ, which is the space flip. The ζ frequencies are the rapidities ln n of the boosts t = n, so unique factorisation means every boost is a unique combination of prime boosts (S10). **[proved]**. It says nothing yet about where the zeros are. **[open]**
- **Phrimary as relativity:** Φ² acts as a pure boost (rapidity 0.9624, v = 0.745c) and keeps u·v exactly. Φ alone is a boost plus a flip that swaps timelike and spacelike. The system's γ = 2√N/(u + v) equals dτ/dt to 10⁻¹⁵, and mass is the norm x·x′, with a mass gap (S2, 9 Oct). **[verified]**

### 3.2 Physics readings
- **Packing-cost gravity:** pack cells in one spot, hold the total at zero, and pay it back in the smoothest way. The pull then falls off as **r^−(n−1)**: measured −1.00, −1.97, −2.94 and −3.85 in 2D to 5D. Packing on the mirror side gives the **exact negative field**. "Pull = packed inside − cost paid inside" matches the simulation (0.939/0.943, 0.742/0.743, 0.558/0.558). The uniform background stretch is the cost of mass, a dark-energy candidate (S6, 25 Oct). **[verified as a simulation; lead as physics]**. The chat's own caveat: smoothest payback is the usual field rule, so inverse-square was bound to appear. The bookkeeping is also scale-free, so on its own it can't give "slow first, fast later". This touches F1 §22.2 (the push) and §22.3 (emergent curvature).
- **A horizon from a moving substrate:** dD/dt = H·D − 1 has its edge at D = 1/H. With constant H the horizon is permanent, and with H = H₀/t (slowing) everything eventually arrives (S9, ~7 Nov, `expanding.py`). **[verified]**. This is the first horizon in the work that isn't a fixed point of a map. It extends F1 §19. It gives the horizon's form, not its size.
- **Force:** a steady push makes ln t grow at a steady rate (ln t = push × own time), and momentum is m·Δx/2 (S9). **[verified]**
- **Fall table:** at 45°, r = 0.5 r_s with 81.8% of the proper time used. At 60° (Δt = 1), r = 0.25 r_s with 94.2% used. The singularity is Δt = 0, not Δt = 1 (S10). **[verified inside the imported map]**
- **Localisation from many pairs:** spreading t around 1 narrows the blur, and width × spread stays near 0.7–1.0 (S5). **[verified, rough]**
- **The 1/P uncertainty floor is e·π:** effective 1/P(position) × effective 1/P(momentum) = 8.540 = e·π exactly for the bell curve, and every other shape is higher (box 1.71×). This replaced an earlier "0.81π floor" (S5, 19 Oct). **[verified]**. The earlier floor **[didn't hold]**.
- **Loops of loops:** DᵢDⱼ − DⱼDᵢ = Dₖ needs n(n − 1)/2 = n, so n = 3. That gives the ladder j = 0, ½, 1, …, and j = ½ needs 720° (S5). **[verified]**. The later claim that "n = 3 is the only size that closes" was re-tested and isn't unique under the plain definition. **[didn't hold]**
- **The self is the invariant present:** in its own frame every t has √(Δt² − Δx²) = 2. The proposed test was a clock that ticks only when memory changes, to see whether age measured that way predicts solving better than step count (S10). **[open]**

### 3.3 Numbers and clocks
- **The 24-hour clock** (S11, 5–6 Nov; S9 §46). This refines F1 §13's 12-hour clock.
  - p² − 1 = 24k for every p ≥ 5 (two consecutive evens give 8, and one of p ± 1 gives 3). **[proved]**
  - 24 is the largest clock on which every allowed hour is its own mirror. **[verified]**
  - With t − 1/t = n, tᵏ + (−1/t)ᵏ mod 24 closes in exactly 24 ticks **if and only if n ∈ {1, 5, 7, 11, 13, 17, 19, 23}**. Multiples of 3 close in 12, even n in 8 or 4, and n = 0, 12, 24 in 2. Running the tick backward gives the same period, and n and 24 − n pair up. **[verified]**
  - On the t + 1/t = n clock, 24 shows up only at n = 2, 10, 14 and 22, with no prime pattern. **[verified]**
  - Fibonacci ticks close every 24, and ticks 12 and 24 are the silent ones. "F₁₂ = 137" was corrected: F₁₂ = 144. *Rerun here, see §5.*
- **6k ± 1 faces:** the next prime switches face 57.3% of the time (up to 5×10⁶). **The bias fades with size**: the same-face share goes 38.4% (up to 10⁴), 41.9%, 43.2%, 44.0%, 44.3% (10⁸ to 2×10⁸). The face switches exactly when the gap is 2 or 4 mod 6 (S5, 18–19 Oct). **[verified]**. Gap misses against −1/p or −1/(p + 2) show no correlation (−0.0005). **[didn't hold]**
- **Twin primes** (S8, 2 Nov):
  - 440,312 pairs up to 10⁸, against the Hardy–Littlewood prediction of 440,429 (99.97%). **[verified]**
  - The middle number is divisible by q with probability 1/(q − 2) rather than 1/q: 5 a third of the time, 7 a fifth. **[verified]**
  - The next gap after a twin pair is never 2 mod 6. **[verified]**
  - 137 × 139 = 138² − 1², so every twin pair is the hyperbola point (Δt, Δx) = (middle, 1). **[proved]**
  - Compare F1 §27: there, twin primes sit off the mirror curve by 2/(p + 2), a different reading.
- **Survival by absence:** a prime pattern survives only if it leaves at least one slot empty for every prime. Twins, cousins, triplets and quadruplets match predicted counts within 1% (S8). **[verified]**
- **Parity is the blind spot:** looking through λ (Liouville), the running sum leans odd. Through μ, with repeated primes made neutral, the bias drops from −0.50 to −0.07 (49.4% positive), and CPT then holds within noise (S8). **[verified]**. Reading parity as what blocks twins, Goldbach and RH at once is a **[lead]**.
- **Golden-angle projection:** stepping by 137.508° turns the integers into a three-gap background, the primes look random on top of it, and every leftover tilt traces back to squares (S8). **[verified]**
- **SGC** (S1, 10 Sep):
  - Shear theorem: E_sgc(σ + it) = ζ(σ + ½ + 2it), so the j-parts only shift ζ. ψ_sgc = j·ψ. Both **[proved]**.
  - The mirror P + 1/P = 1 → e^{±iπ/3} → sin(π/6) = ½ is **[proved]**, but only as a construction, not as an argument for RH.
  - The Darmiyan zero-count formula diverges past n ≈ 50 because of a permanent 2/√3 inflation. The "quadruple constraint" is circular, and P isn't holomorphic. **[didn't hold]**
- x + 1/x = 2cos θ at 90°, 60°, 30° and 0° gives 0, 1, √3 and 2: **[proved]**. The 30° row then mixes cos, sin and sec. **[didn't hold]** (S1)
- **Phrimary details** (S2):
  - The collapse rule 011 → 100 gives unique codes, and an all-ones string of length k equals Φ^{k+1} − Φ. **[verified]**
  - θ(ab) = θ(a) + θ(b) mod 1, so θ behaves like a logarithm. **[verified]**
  - TD² + TrD² = 1 is an identity, not a finding.
  - Brownian frontier measured 1.25 (4/3 expected) and path 1.77 (2 expected). The chance that a continued-fraction digit is 1 is log₂(4/3). **[verified]**

### 3.4 Machines, search, organisms
- **`docs/construct.md` in error-of** (S4, 17 Oct): cue → frozen reconstructor → fabric → error-of → gate, carrying two edges, with the case store as the slow loop. It also added a `side` on every error (too big, too slow, too coarse). **[verified as code]**
- **What recall needs:** a basin, a cue that overlaps it, convergence, and a stop. The failures are no basin, wrong basin, no convergence, budget and precision (S4). **[lead]**, as a design.
- **Walker and way are one process:** the groove made by walking is what guides the next walk, so there's no separate learning stage (S4, 6 Nov). **[lead]**
- **Logic = knowledge + a squeeze:** the squeezed network went from 2% to 100% on multiplication pairs it never saw, and the unsqueezed one didn't (S8; now in world-of_EI). **[verified]**
- **Recall is elimination:** a sharp attention head pushed 99.99% of 100,000 tokens to near zero (S8). **[verified]**
- **Kernel limits:** NAME_MAX 255 is one byte, PATH_MAX 4096 is one page, and 40 was chosen in namei(). No physics exponent sits at 225; the real ones are 36–43 and 120–123 (S9, ~7 Nov). **[didn't hold]** as physics. The name axis and the reference axis are 51× apart, and only the second had been used. **[verified]**

### 3.5 Sanatan readings (S10, 6–7 Nov). Readings, not derivations
- **Mandukya:** waking = t (outward, observable), dream = −1/t (inward, clock reversed), deep sleep = i/t (unobservable, the **same event z** as waking), turīya = the invariant 4i (no direction, no scale). −it is left over with no quarter. **[lead]**
- **Rig Veda 10.129:** "neither existence nor non-existence" ↔ t = i. "Breathed, windless" ↔ |t| = 1. "Desire, the first seed" ↔ S → Δx + 1/S. "Cord stretched across" ↔ the ball's diameter of 2. **[lead]**
- Every yuga is a whole multiple of 86,400, and Kali = the vipalas in 2 days. Both come from base-60 counting, not from a physical cycle. **[didn't hold]** as physics.
- Kali Yuga ending in 2031, a 56,000-year RH cycle, a 408-year historical pulse, and Gemini's "137 ratio" (circular). **[didn't hold]**

---

## 4. Coincidences logged, not used
At n = 137, D sits 1/137 from the throat (S9 §45). The hex loop 137 → 0x89 → 89 = F₁₁, with CF₁ = 27 = 0x1B; 1836 = 137·F₇ + F₁₀ ≡ 0 mod 17 (S1). tan 53.13° = 4/3, the 3-4-5 triangle (S10). Planck density ÷ dark-energy density = 10^122.9, close to de Sitter's 4.8×10¹²² bits (S9). The Λ radius as r_e³/l_P² comes out at 90% of the measured value (S2).

---

## 5. Checks run for this file (14 Nov)

Script: `scripts/checks.py`, `scripts/turn.py` (mpmath, 40–80 digits).

| Ran | Got | My read |
|---|---|---|
| 137 + 5/139 against CODATA 2022 | 0.204 ppm off, **1,331σ** | Both S1 and F1 are numerically right. F1's verdict is the one that counts. |
| Six-step error factor at t = √α·e^{i60°}, run as the seed rule | **α⁶** = 1.510052253×10⁻¹³ toward −1/t, α⁻⁶ toward t, turn 0° | The 3 Nov claim stands. The 7 Nov "α³" measured \|t\|⁶, which is a different thing. |
| Periods of tᵏ + (−1/t)ᵏ mod 24 with t − 1/t = n, for n = 0…24 | 24 for n ∈ {1, 5, 7, 11, 13, 17, 19, 23}; 12 for 3, 9, 15, 21; 8 or 4 for evens; 2 for 0, 12, 24 | Matches S11 exactly. |
| Clocks up to 2,000 where every unit is self-inverse | {2, 3, 4, 6, 8, 12, 24} | Matches. 24 is the largest. |
| Fibonacci period mod 24 | 24 | Matches. |
| Root sizes of x³ + x² − 1 | 0.7549, 1.15096, 1.15096 | The 3D "1.151" is real: a pair of complex roots of a unit cubic. |
| Interference identity at s = 0.7, t = 2.3 | difference 2.2×10⁻¹⁶ | Exact. |
| Continued fraction of 1/α at both edges of ±σ | [137; 27, 1, 3, 1, 1, **18** or **19**, …]. The first convergent inside ±σ is 669969/4889 (index 7, the "8th" if 137 counts as 1st) | Agrees with S11 ("only 6 terms are knowable") and with F1 §29 ("8th convergent inside"). |
| (137 − 1)/(137 + 1) | 0.98551 | Matches S8's slowest speed for 137. |

Not rerun, because they're too heavy or not cheap: the 6k ± 1 fade, the twin-prime counts, the packing-cost gravity, and the SAW dimensions.

---

## 6. The three biggest disagreements between F1 and this account

1. **F1 counts imported or fitted physics as verified, and this account doesn't.** F1 tags the black-hole infall and the expansion history **[verified]** (§4). In this account, the infall map r = r_s·cos²θ was taken from GR and only checked, and the expansion "match" is the matter + Λ solution rewritten in u = ln t, true **by construction**. The one place where the construct was asked for a GR number it hadn't been fitted to, light bending, it came out at **half** the measured value. *My read:* until bending or something like it comes out right without being fitted, the construct reproduces shapes rather than predicting them, and F1 §4 should be retagged.

2. **What one event costs: ħ, h, 2h or ħ/2.** F1 settles on ħ = 1, with an area of 2π (one h) per event, and sets "ħ = 4" aside (§6). This account gives three different assignments: "tick × event = 2 → 2h, and 2·h/4π = ħ", "N_x·N_p = 1 → one ħ cell", and "ħ/2 × 720° = h". It lists the question as **open**. *My read:* the 2 in t·|Δz| = 2, the 4 in the interval and the 2π orbit area are three different areas. The construct needs one definition of "a cell" before any of them is called ħ.

3. **D = 3/2 − 1/(2n) as derived (F1 §12) vs fitted.** F1 calls it "derived by counting". In this account the simulation reproduces it only once k = 4(1 − 1/n) is put in by hand, "why n sets k" is still open, the formula misses the measured self-avoiding-walk dimensions in 3D and 4D, and 4/3 belongs to 2D paths, not 3D space. The best candidate for the missing rule, time's roughness = ½ × the turning fraction 1 − 1/n, still leaves the ½ underived. *My read:* F1 §12 should say "a mechanism that reproduces it once k is set", and the counting argument would have to produce the k = 4(1 − 1/n) law before it counts as a derivation.

*Close behind:* the α⁶ vs α³ split inside this account (settled above in favour of α⁶), and prime powers as lightlike (F1 §27) vs at rest (S8). These come from two different models of what a number's "frame" is.
