import unittest
from calculator import add, multiply, power

class TestCalculatorFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        # Lisää tarvittaessa muita testejä
        self.assertNotEqual(add(5,5),11)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)
        self.assertEqual(multiply(-3, 6), -18)
        # Lisää tarvittaessa muita testejä

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, 2), 4)
        # Lisää tarvittaessa muita testejä

if __name__ == '__main__':
    unittest.main()
