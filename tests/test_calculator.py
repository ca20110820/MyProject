import unittest
from my_package2.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(1, 1)
        self.assertEqual(result, 2)

    def test_subtract(self):
        result = Calculator.subtract(2, 1)
        self.assertEqual(result, 1)

    def test_divide(self):
        result = Calculator.divide(4, 2)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = Calculator.multiply(3, 2)
        self.assertEqual(result, 6)
    
    def test_double_number(self):
        result = Calculator.double_number(5)
        self.assertEqual(result, 10)
    
    def test_square_number(self):
        result = Calculator.square_number(2)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
