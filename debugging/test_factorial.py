#!/usr/bin/python3
import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(factorial(5), 120)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
        self.assertEqual(factorial(3), 6)    # 3! = 3 * 2 * 1 = 6
        self.assertEqual(factorial(1), 1)    # 1! = 1
    
    def test_zero(self):
        self.assertEqual(factorial(0), 1)    # 0! = 1 par définition

if __name__ == '__main__':
    unittest.main() 