import unittest

from multiplier import multiply


class MultiplyTests(unittest.TestCase):
    def test_multiply_positive_numbers(self) -> None:
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self) -> None:
        self.assertEqual(multiply(99, 0), 0)

    def test_multiply_negative_numbers(self) -> None:
        self.assertEqual(multiply(-2, -8), 16)


if __name__ == "__main__":
    unittest.main()
