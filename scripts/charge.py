"""
charge.py — where charge comes from in the self-referential framework.

Mass was the MAGNITUDE of self-reference (|phi^n|, always positive, additive).
Charge is a SECOND, independent sign the magnitude does not fix:
  Sign 1 (which pole):  phi forward/attract  vs  psi backward/repel   -> matter / antimatter
  Sign 2 (tick parity): Cassini (-1)^n, flips every tick, pole-independent -> +/- charge
Reading one pole lets the signed part survive (charged); reading both cancels it (neutral).
mass = sum (phi+psi=1, survives) ; charge = signed difference (cancels in pairs).
"""
import numpy as np
P=(1+np.sqrt(5))/2; S=1-P

def state(n, pole=+1, read="one"):
    base = P if pole>0 else S
    mag = abs(base**n)                 # MASS: magnitude, sign-free
    parity = (-1)**n                   # CHARGE sign: Cassini parity
    if read=="both":                   # read both poles -> charge cancels
        charge = 0; mass = P**n + S**n # the real, surviving sum
    else:                              # read one pole -> charge survives
        charge = parity; mass = mag
    return mass, charge

print("particle    pole  read   mass        charge")
print("-"*50)
rows=[("matter e-",   +1,"one"),("matter e+ (parity)", +1,"one"),
      ("antimatter",  -1,"one"),("neutrino (neutral)", +1,"both")]
for name,pole,read in rows:
    m,c=state(5,pole,read)
    print(f"{name:20s} {pole:+d}   {read:4s}  {m:8.4f}   {c:+d}")
print()
print(f"mass  = phi+psi sum  = {P+S:.4f}  (survives: mass is always +, additive, conserved)")
print(f"charge= phi-psi diff = {P-S:.4f} -> its SIGN (Cassini) is +/-, cancels in pairs")
print()
print("Summary: mass = how much the loop repeats (magnitude).")
print("         charge = which way its mirror flips (parity), surviving only when read one-sided.")
print("         neutral = both flips read at once -> charge cancels, mass remains.")
