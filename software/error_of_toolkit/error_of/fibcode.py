"""Fibonacci coding: the 'no-11' phinary. Self-delimiting, corruption-detectable integer code.

Each codeword is the Zeckendorf representation (no two consecutive Fibonacci terms) written
low-to-high, with a terminating '1' appended. Because Zeckendorf forbids adjacent 1s, the only
'11' in a valid codeword is the boundary: terminator + the preceding set bit. That makes the
code self-synchronizing and lets many single-bit corruptions be detected.
"""
def _fibs(upto):
    f = [1, 2]
    while f[-1] <= upto:
        f.append(f[-1] + f[-2])
    return f

def encode(n):
    if n < 1:
        raise ValueError("Fibonacci coding is for positive integers")
    fs = _fibs(n)
    bits = []
    for f in reversed(fs):
        if f <= n:
            bits.append("1"); n -= f
        else:
            bits.append("0")
    # strip leading zeros, reverse to low->high, append terminator
    first = bits.index("1")
    low_to_high = bits[first:][::-1]
    return "".join(low_to_high) + "1"

def decode(code):
    if not code.endswith("1"):
        raise ValueError("missing terminator")
    body = code[:-1]
    fs = _fibs(2 ** (len(body) + 2))
    total = 0
    for bit, f in zip(body, fs):   # body is low->high
        if bit == "1":
            total += f
    return total

def is_valid(code):
    """A valid codeword has exactly one '11' and it is at the very end."""
    return code.endswith("1") and code.count("11") == 1 and code.rfind("11") == len(code) - 2
