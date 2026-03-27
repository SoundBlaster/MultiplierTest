import unittest

from multiplier import multiply


class MultiplyTests(unittest.TestCase):
    def test_multiply_positive_integers(self) -> None:
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self) -> None:
        self.assertEqual(multiply(99, 0), 0)

    def test_multiply_negative_numbers(self) -> None:
        self.assertEqual(multiply(-2, -8), 16)

    def test_multiply_floats(self) -> None:
        self.assertAlmostEqual(multiply(2.5, 0.4), 1.0)

    def test_multiply_mixed_numeric_types(self) -> None:
        self.assertEqual(multiply(2, 2.5), 5.0)


if __name__ == "__main__":
    unittest.main()
