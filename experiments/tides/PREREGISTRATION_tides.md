# Pre-registration — tide test (written before any data was downloaded)

Written: 2026-10-17, before fetching any tide data.

## Predictions (astronomical tidal speeds, standard Doodson values, degrees per hour)

| constituent | speed (°/h) | period (h) | origin |
|---|---|---|---|
| M2 | 28.9841042 | 12.4206012 | principal lunar semidiurnal |
| S2 | 30.0000000 | 12.0000000 | principal solar semidiurnal |
| N2 | 28.4397295 | 12.6583482 | larger lunar elliptic |
| K1 | 15.0410686 | 23.9344697 | lunisolar diurnal |
| O1 | 13.9430356 | 25.8193417 | lunar diurnal |

These values are from my own knowledge (not looked up in this session), fixed before seeing data.

## Data

NOAA CO-OPS hourly heights (product `hourly_height`, datum MLLW, metric, GMT), one station,
one calendar year. Station chosen before download: 9414290 (San Francisco). Year: 2023.

## Method (fixed in advance)

1. Fit a sum of 5 sinusoids + constant, with all 5 frequencies FREE (nonlinear least squares),
   initial guesses offset by +0.5% from the predictions so the fit must find them.
2. Error bars: fit each of 4 independent quarters of the year (frequencies free, M2/S2/N2 resolved
   within a quarter: separations of 14.8 and 27.6 days are shorter than 91 days); SE = spread/√4.
3. Verdict per constituent: PASS if |fitted − predicted| ≤ 2·SE, else FAIL.
4. Map reading: per-sample angle θ = speed·Δt (Δt = 1 h), τ = 2cos θ, checked for M2.

No change to station, year, constituents or method after seeing data.

## Amendment 1 (after the first run, before any verdict was accepted)

The pre-registered fit (free NLS started 0.5% off) failed to converge: residual rms 0.545 m,
fitted M2 amplitude 0.052 m (San Francisco's M2 is ~0.5 m). Over a year, a 0.5% start offset
is ~44 cycles of phase error, so the fit fell into a wrong local minimum. That run is void.

Replacement method, BLIND to the predictions: scan 12–17 °/h and 27–31 °/h on a fine grid,
pick the strongest periodogram peak, fit and subtract it, repeat 5 times (CLEAN), then refine all
5 frequencies jointly from those blind starting points. Match found peaks to constituents only
after the fit. Error bars and verdict rule unchanged (4 quarters, PASS if |z| ≤ 2).
