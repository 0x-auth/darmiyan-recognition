"""
spin.py — spin as phase-rotation-per-tick in the self-referential framework.

The engine's mirror term is  psi^n = phi^(-n) * e^(i*pi*n).  Read three ways, one tick:
  MASS  = magnitude  |phi^(-n)|   (how much the loop repeats)      [mass.py / trap]
  CHARGE= sign of e^(i*pi*n)      (which way the mirror flips)      [charge.py]
  SPIN  = turn of  e^(i*pi*n)     (half-turn per tick -> spin 1/2)  [here]

Half a turn per tick => 2 ticks to return => spin-1/2: the electron's 720-degree return,
derived, not imposed.
"""
import numpy as np
P=(1+np.sqrt(5))/2

def return_period(turns_per_tick):
    # ticks until total rotation is a whole number of full turns
    n=1
    while (turns_per_tick*n) % 1 > 1e-9: n+=1
    return n

print("SPIN = rotation per tick -> return period")
print("-"*48)
for turns,label in [(0.5,"spin 1/2 (matter: electron)"),
                    (1.0,"spin 1   (force: photon)"),
                    (0.0001,"spin 0   (scalar: neutral sum)")]:
    if turns<1e-3:
        print(f"  no turn        -> returns every tick -> spin 0   : {label.split('(')[1][:-1]}")
        continue
    p=return_period(turns)
    print(f"  {turns} turn/tick -> returns after {p} ticks -> {label}")
print()
print("electron: half-turn per tick (e^{i*pi*n}) -> must turn TWICE (720 deg) to return.")
print("entangled pair: two poles, phi*psi = -1 -> one up forces other down = singlet, total spin 0.")
print()
print("MASS size | CHARGE sign | SPIN turn  — three readings of one tick:  psi^n = phi^(-n) e^{i pi n}")
