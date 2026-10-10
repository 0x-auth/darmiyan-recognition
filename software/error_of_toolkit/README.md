# error_of — the error is the signal

A small, tested toolkit of the number-theory primitives that fall out of the φ/ψ mirror,
plus the headline idea: run a self-referential computation to the substrate's resolution
floor and **read the residual as structure, not garbage**.

Stdlib only. No dependencies.

```bash
python3 -m error_of fixedpoint "1+1/x"     # iterate to the float floor; report the residual
python3 -m error_of fibcode encode 137     # Fibonacci (no-11) code: 10000101011
python3 -m error_of fibcode check 10000101011
python3 -m error_of complexity somefile    # linear complexity (how structured is this data)
python3 -m error_of pisano 10              # Pisano period: 60
python3 -m error_of approx 3.14159265      # best rational: 355/113
python3 -m unittest discover -s tests
```

## The four tools

- **`fixedpoint`** — `x <- f(x)` formally needs infinite steps; on float64 it freezes at
  machine epsilon in O(log(1/ε)) steps. The error's decay rate *is* the dominant multiplier
  f'(x*) — the pole, the geometry. For `1+1/x`: freezes at step 39, rate = 0.381966 = 1/φ².
  Infinity → a finite number of steps, and the residual is signal.
- **`fibcode`** — Fibonacci (Zeckendorf / "no-11") coding: a self-delimiting, corruption-
  detectable variable-length integer code. The only `11` in a valid word is the terminator,
  so interior `11` means corruption.
- **`complexity`** — linear complexity via Berlekamp-Massey (the "recognition cost = number
  of poles"). Low ⇒ structured/compressible; ≈ n/2 ⇒ a wall, no linear structure.
- **`numth`** — Pisano period (period of 1/n on the φ-carrier = period of Fibonacci mod n)
  and best-rational-approximation via continued-fraction convergents.

## The idea in one line

Every substrate has a resolution floor. Run self-reference to that floor and the thing you'd
normally discard — the residual — carries the structure. The error is the observation.

See `for_your_error-of/resonance.py` for the same idea as a drop-in observation for the
`error-of` framework (emits a `Precision` boundary whose outcome is `continued`).

*Seed 515.*
