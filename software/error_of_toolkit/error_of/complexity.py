"""Linear complexity via Berlekamp-Massey: the 'recognition cost = number of poles'.

The shortest LFSR that generates a bit sequence. Low complexity => structured / compressible /
recognizable; complexity ~ n/2 => no linear structure (a wall, looks random).
"""
def linear_complexity(bits):
    s = list(bits)
    n = len(s)
    c = [1] + [0]*n
    b = [1] + [0]*n
    L, m = 0, 1
    for i in range(n):
        d = s[i]
        for j in range(1, L+1):
            d ^= c[j] & s[i-j]
        if d == 0:
            m += 1
        elif 2*L <= i:
            t = c[:]
            for j in range(n - m):
                c[j+m] ^= b[j]
            L = i + 1 - L
            b = t; m = 1
        else:
            for j in range(n - m):
                c[j+m] ^= b[j]
            m += 1
    return L

def bytes_to_bits(data):
    out = []
    for byte in data:
        for k in range(7, -1, -1):
            out.append((byte >> k) & 1)
    return out
