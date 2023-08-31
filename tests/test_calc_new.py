import unittest
from parameterized import parameterized

from app.error import InvalidInputException
from app.main import Calculator


class TestNewCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    @parameterized.expand(
        [
            (2, 2, 1.0),
            (2.2, 2.5, 0.8604881976177822),
            (-2.5, 3.1, None),
        ]
    )
    def test_log(self, a, b, expected_result):
        try:
            actual_result = self.calc.log(a, b)
            self.assertEqual(actual_result, expected_result)
        except InvalidInputException:
            self.assertIsNone(expected_result)

    @parameterized.expand([
        ("strings", 'aaa', 'bbb', TypeError),
        ("int_None", 1, None, TypeError),
        ("None_float", None, 1.1, TypeError),
        ("None_None", None, None, TypeError)

    ])
    def test_sum_invalid_values(self, name, a, b, expected_result):
        with self.assertRaises(expected_result):
            self.calc.log(a, b)


if __name__ == '__main__':
    unittest.main()
