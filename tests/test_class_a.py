import unittest
from my_package2.class_a import ClassA


class TestClassA(unittest.TestCase):
    def setUp(self):
        self.class_a = ClassA()
    
    def test_addition(self):
        result = self.class_a.addition(1, 1)
        self.assertEqual(result, 2)

    def test_subtraction(self):
        result = self.class_a.subtraction(2, 1)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
