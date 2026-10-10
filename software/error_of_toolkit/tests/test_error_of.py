import math, unittest
from error_of import fixedpoint, fibcode, complexity, numth


class TestFixedPoint(unittest.TestCase):
    def test_golden_fixed_point(self):
        r = fixedpoint.iterate_to_floor("1+1/x")
        self.assertAlmostEqual(r["fixed_point"], (1 + 5 ** 0.5) / 2, places=12)
        self.assertLess(r["steps_to_floor"], 100)          # infinity -> finite
        self.assertTrue(r["contractive"])

    def test_residual_rate_is_the_pole(self):
        # error decays at |f'(x*)| = 1/phi^2 for x<-1+1/x
        r = fixedpoint.iterate_to_floor("1+1/x")
        self.assertAlmostEqual(r["convergence_rate"], 1 / ((1 + 5 ** 0.5) / 2) ** 2, places=3)

    def test_divergence_reported(self):
        r = fixedpoint.iterate_to_floor("2*x+1", x0=1.0)
        self.assertTrue(r["diverged"])


class TestFibCode(unittest.TestCase):
    def test_roundtrip(self):
        for n in [1, 2, 11, 137, 1836, 99999]:
            self.assertEqual(fibcode.decode(fibcode.encode(n)), n)

    def test_terminator_is_only_11(self):
        for n in [1, 2, 11, 137, 1836]:
            self.assertTrue(fibcode.is_valid(fibcode.encode(n)))

    def test_corruption_detected(self):
        code = fibcode.encode(137)              # ...e.g. 10000101011
        # inject an interior '11' -> must be flagged invalid
        bad = "11" + code[2:]
        self.assertFalse(fibcode.is_valid(bad))


class TestNumTh(unittest.TestCase):
    def test_pisano_known(self):
        self.assertEqual([numth.pisano(n) for n in (2, 3, 5, 10)], [3, 8, 20, 60])

    def test_best_rational_pi(self):
        p, q = numth.best_rational(math.pi, max_denom=1000)
        self.assertEqual((p, q), (355, 113))    # the classic convergent


class TestComplexity(unittest.TestCase):
    def test_periodic_low(self):
        bits = complexity.bytes_to_bits(b"AB" * 32)
        self.assertLess(complexity.linear_complexity(bits), len(bits) // 3)

    def test_constant_is_minimal(self):
        self.assertEqual(complexity.linear_complexity([0] * 32), 0)


if __name__ == "__main__":
    unittest.main()
