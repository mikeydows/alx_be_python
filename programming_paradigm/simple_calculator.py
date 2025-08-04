import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Initialize a new calculator instance before each test."""
        self.calc = SimpleCalculator()

    # -------------------------
    # ADDITION TEST CASES
    # -------------------------
    def test_addition_basic(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -4), -5)
        self.assertEqual(self.calc.add(-3, 3), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_with_floats(self):
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)  # float precision

    def test_addition_large_numbers(self):
        self.assertEqual(self.calc.add(10**6, 10**6), 2_000_000)

    # -------------------------
    # SUBTRACTION TEST CASES
    # -------------------------
    def test_subtraction_basic(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtraction_with_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.calc.subtract(-3, 2), -5)

    # -------------------------
    # MULTIPLICATION TEST CASES
    # -------------------------
    def test_multiplication_basic(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        self.assertEqual(self.calc.multiply(-3, 2), -6)

    def test_multiplication_with_floats(self):
        self.assertAlmostEqual(self.calc.multiply(1.5, 2.0), 3.0)

    def test_multiplication_large_numbers(self):
        self.assertEqual(self.calc.multiply(100000, 10000), 1_000_000_000)

    # -------------------------
    # DIVISION TEST CASES
    # -------------------------
    def test_division_basic(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        self.assertEqual(self.calc.divide(0, 3), 0.0)

    def test_division_with_floats(self):
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_precision(self):
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333, places=6)

    def test_division_large_numbers(self):
        self.assertEqual(self.calc.divide(1_000_000, 10), 100_000)

if __name__ == '__main__':
    unittest.main()
