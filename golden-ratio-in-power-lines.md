# The Golden Ratio Hiding in Electrical Lines
*A one-page curiosity for people who build and maintain power lines*

---

## 1. The experiment you can do on a bench

Take identical resistors (say 1 Ω each) and build a **ladder**: one resistor in series, one resistor to ground, then repeat.

```
 IN ──[R]──┬──[R]──┬──[R]──┬── …
           │       │       │
          [R]     [R]     [R]
           │       │       │
 GND ──────┴───────┴───────┴── …
```

Measure the resistance at the input as you add sections:

| sections | input resistance (Ω) |
|---|---|
| 1 | 2.000 |
| 2 | 1.667 |
| 3 | 1.625 |
| 4 | 1.619 |
| 5 | 1.6182 |
| 6 | 1.61806 |
| very long | **1.618034…** |

That final number is the **golden ratio, φ = (1 + √5)/2**, the same number found in sunflowers, shells and classical architecture.

**Why:** a very long ladder looks the same from its input whether you add one more section or not. So its resistance R must satisfy R = 1 + (1 × R)/(1 + R), which simplifies to R² = R + 1. The positive answer is φ.

The fractions along the way (2/1, 5/3, 13/8, 34/21, 89/55…) are ratios of **Fibonacci numbers**.

---

## 2. Two practical facts that fall out

- **Voltage drops by a fixed factor per section.** In a long ladder of equal resistors, each section passes on only **1/φ² ≈ 38.2%** of the voltage it receives. The drop is geometric, not linear.
- **A short ladder is "almost" a long one.** After about 5–6 sections the input resistance is already within 0.01% of the infinite value. The leftover error shrinks by a constant factor each section.

---

## 3. Why this matters on real lines

A transmission line is modelled exactly like this ladder: every kilometre adds a bit of **series impedance** (conductor resistance and inductance) and a bit of **shunt admittance** (capacitance and leakage to ground). The golden ratio appears in the special case where series and shunt values are equal. The *method* is the same in every case:

- A long line settles to a single **characteristic impedance**, the line's equivalent of φ.
- Voltage and current change by a **fixed factor per kilometre** (the propagation constant), just like the 1/φ² per section above.

**The same ladder explains insulator strings.** A string of disc insulators is a ladder too: each disc is a series capacitance, and each disc also has a small stray capacitance to the tower (a shunt to ground). Because of that ladder effect, the voltage is **not shared equally**. The disc nearest the live conductor carries the largest share. This is why:

- the conductor-end disc fails first,
- *string efficiency* is always below 100%,
- **grading rings** (arcing rings) are fitted at the line end to even out the voltage.

---

## 4. The one-line takeaway

> Any chain of identical repeating sections (a resistor ladder, a long line, an insulator string) settles to a fixed value and changes by a fixed factor per section. In the simplest case that value is the golden ratio.

Engineers use this to analyse a long line from its **"poles"** (characteristic values) directly, instead of calculating section by section.

---
*Prepared by Space with Claude (Anthropic), Oct 2026.*
