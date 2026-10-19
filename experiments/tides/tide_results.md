# Tide test — real data, astronomical predictions fixed in advance

*2026-10-17 · data: NOAA CO-OPS station 9414290 (San Francisco), hourly heights, all of 2023, 8,760 samples, none missing*

## Why tides

A tide is a real physical sum of oscillators whose frequencies are set by the Moon's and Sun's motion.
The predictions can't be tuned to the data, and no one had to record anything.

## Protocol

`PREREGISTRATION_tides.md` was written before download. It fixed the station, the year, the 5 constituents
with their speeds, the method and the PASS rule (|z| ≤ 2, with z from 4 independent quarters).

**Amendment 1:** the first pre-registered fit failed to converge (0.5% start offset ≈ 44 cycles of phase drift
over a year; residual 0.545 m, M2 amplitude 0.05 m). That run is void. The replacement is **blind** to the
predictions: strongest periodogram peak, subtract, repeat (CLEAN), then a joint refinement. Peaks are matched to
names only after fitting. The verdict rule is unchanged.

## Result (pre-registered rule, 5 blind peaks)

| | predicted °/h | blind fit, full year | offset | quarters z | amplitude | verdict |
|---|---|---|---|---|---|---|
| M2 | 28.984104 | 28.983923 | −1.8×10⁻⁴ | +0.18 | 0.550 m | PASS |
| S2 | 30.000000 | 30.002768 | +2.8×10⁻³ | +0.64 | 0.142 m | PASS |
| N2 | 28.439729 | 28.439203 | −5.3×10⁻⁴ | −0.51 | 0.121 m | PASS |
| K1 | 15.041069 | 15.042903 | +1.8×10⁻³ | −1.21 | 0.404 m | PASS |
| O1 | 13.943036 | 13.942566 | −4.7×10⁻⁴ | **−3.96** | 0.267 m | **FAIL** |

- M2 period found blind: **12.420679 h, predicted 12.420601 h** (6 ppm).
- Residual rms 0.141 m on data sd 0.554 m.
- **4 of 5 PASS, O1 FAILS** under the rule. The failure is reported as the result.

## Post-hoc (does not change the verdict)

The same blind method with 8 peaks found three lines I had *not* predicted, each at its known
astronomical speed (speeds recalled, not looked up):

- **Q1** at 13.3977 (known 13.3987)
- **P1** at 14.9591 (known 14.9589)
- **K2** at 30.0823 (known 30.0821)

Modelling them moves O1 from z = −3.96 to −2.04 (borderline) and drops the residual to 0.108 m.
O1's remaining −4.7×10⁻⁴ °/h offset is untested. It might come from nodal (18.6-year) modulation, which one year
cannot resolve.

## The trace-map reading

Each constituent is one elliptic map. For M2 at Δt = 1 h:
θ = 0.505865 rad per sample, **τ = 2cos θ = 1.749511 (|τ| < 2, elliptic: rotation, never settles)**.
The real sea is a superposition of several such rotations, each with τ fixed by astronomy.

## What this does and doesn't show

**Shows:** the analysis machinery recovers real, externally fixed frequencies blind, to ppm (M2), and reports a
failure when one occurs (O1).

**Doesn't show:** that the trace map is a law of nature. Any sum of sinusoids obeys the same per-constituent
identity, and tidal theory already predicts these frequencies. The test that can fail on the framework's own
terms is still the golden-curve breakup in the standard map.

## Files

- `fetch_data.py` — re-downloads the exact NOAA record and checks its sha256 (efa55a20…2f42); the raw CSV is not committed
- `PREREGISTRATION_tides.md` — predictions and method, plus Amendment 1
- `tide_test.py` — the blind analysis (`python3 experiments/tides/tide_test.py`, needs numpy + scipy)
- `tide_test_void_run.py` — the original pre-registered fit that failed to converge, kept for the record
