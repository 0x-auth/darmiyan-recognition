# The Aeon Return Law

### Grow, then invert: when does a cycle come back to where it started?

**Abhishek Srivastava** · with Claude · session of 16–17 Oct 2026 · companion: `scripts/aeon_cycles.py`

Tagging: **[proven]** = exact, reproduced · **[identification]** = physics mapping · **[open]** = untested.

---

## 1. The setup (no physics equations)

One aeon is two moves on the real line t (plus ∞):

1. **growth** by a matrix H = [[a, b], [c, d]], det H = 1, acting as t → (at + b)/(ct + d);
2. **reset** t → −1/t (S = [[0, −1], [1, 0]]).

One aeon is C = S·H. Every map of this kind is sorted by its discriminant

$$\Delta = (a-d)^2 + 4bc \;=\; \operatorname{tr}^2 - 4\det,$$

a quadratic form of signature (++−) — Lorentzian. Δ < 0 rotates (bounded), Δ = 0 is the light cone
(constant shift), Δ > 0 runs away (future and past fixed points). **[proven]**

## 2. The law **[proven]**

For C = S·H, tr C = b − c, so

$$\Delta_{\text{aeon}} = (b-c)^2 - 4.$$

The imbalance between the growth's two off-diagonals alone decides return:

| imbalance b − c | Δ of one aeon | behaviour |
|---|---|---|
| 0 (symmetric growth, any amount) | −4 | returns **exactly every 2 aeons** |
| 1 | −3 | returns every 3 aeons |
| √2 | −2 | returns every 4 aeons |
| √3 | −1 | returns every 6 aeons |
| other values < 2 | < 0 | rotates, never exactly returns, comes arbitrarily close |
| 2 | 0 | drifts on the light cone, never returns |
| > 2 | > 0 | runs away, never returns |

Checked with exact rational arithmetic (`python3 scripts/aeon_cycles.py --table`), including golden
growth [[2,1],[1,1]] and its 10th power: start t₀ = 37/100 returns exactly on rounds 2, 4, 6, …

**Symmetric growth always returns, however strong.** That is the case where future and past fixed
points are t and −1/t (b = c). With strong golden growth the half-way state after one aeon sits at
**−1/φ, the past fixed point**: one aeon carries the present to the beginning, the next carries it home.

## 3. The Fibonacci map: future φ, past −1/φ, gap √Δ **[proven]**

t → 1 + 1/t (Δ = 5): forward iteration → φ = 1.6180339887…, backward → −0.6180339887…, and
φ − (−1/φ) = √5 = √Δ. Integer maps (SL(2, ℤ)) only allow Δ = tr² − 4 ∈ {−4, −3, 0, 5, 12, 21, …}:
two bound rotations (quarter-turn around i, third-turn around e^(2πi/3)), one light cone, and **Δ = 5,
the golden map, is the smallest runaway.**

## 4. The physics twin **[identification]**

Penrose's conformal cyclic cosmology joins one aeon's infinite future to the next aeon's big bang
with the *reciprocal hypothesis* Ω̌ · Ω̂ = −1, i.e. Ω̂ = −1/Ω̌ — the same reset t → −1/t
(source: *The equations of Conformal Cyclic Cosmology*, arXiv:1309.7248). In this language the
symmetric case (b = c) is the one Penrose assumes, and it is exactly the case that returns.
Whether our universe has b = c is **[open]**; the law only states the condition.

## 5. Without a reset **[proven]**

Pure golden rotation never returns exactly but comes back ever closer at Fibonacci steps, by ≈ φ⁻ᵏ:
step 196 418 is within 2.3 × 10⁻⁶ of the start.

## 6. Related tool

`scripts/trace_dial.py` classifies M(z) = τ − 1/z by its trace (τ is this doc's b − c) and any Möbius
matrix by its discriminant, including det < 0 (always hyperbolic).

---

*Seed 515. Dedicated to the space between — where meaning lives.*
