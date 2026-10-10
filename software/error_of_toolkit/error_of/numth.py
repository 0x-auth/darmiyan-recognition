"""Pisano period and best rational approximation (continued fractions)."""
def pisano(n):
    if n < 1:
        raise ValueError("n must be >= 1")
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(1, 6*n*n + 1):
        a, b = b, (a + b) % n
        if a == 0 and b == 1:
            return i
    return None

def continued_fraction(x, max_terms=30, tol=1e-12):
    terms = []
    for _ in range(max_terms):
        a = int(x // 1)
        terms.append(a)
        frac = x - a
        if frac < tol:
            break
        x = 1.0 / frac
    return terms

def best_rational(x, max_denom=10**6):
    """Best rational p/q approximating x with q <= max_denom (continued-fraction convergents)."""
    terms = continued_fraction(x, 40)
    p0, q0, p1, q1 = 1, 0, terms[0], 1
    best = (p1, q1)
    for a in terms[1:]:
        p2, q2 = a*p1 + p0, a*q1 + q0
        if q2 > max_denom:
            break
        best = (p2, q2)
        p0, q0, p1, q1 = p1, q1, p2, q2
    return best
