#!/usr/bin/python3
import unittest
from factorial import factorial, MAX_N
from io import StringIO
import sys

class TestFactorial(unittest.TestCase):
    def setUp(self):
        """Capture stdout for testing step-by-step output"""
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Restore stdout"""
        sys.stdout = sys.__stdout__

    def test_positive_numbers(self):
        """Test factorial with various positive numbers"""
        test_cases = {
            1: 1,
            2: 2,
            3: 6,
            4: 24,
            5: 120,
            10: 3628800
        }
        for n, expected in test_cases.items():
            with self.subTest(n=n):
                self.assertEqual(factorial(n), expected)

    def test_zero(self):
        """Test factorial of zero"""
        self.assertEqual(factorial(0), 1)

    def test_negative_numbers(self):
        """Test factorial with negative numbers"""
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertIn("negative", str(context.exception))

    def test_large_numbers(self):
        """Test factorial with numbers larger than MAX_N"""
        with self.assertRaises(ValueError) as context:
            factorial(MAX_N + 1)
        self.assertIn("too large", str(context.exception))

    def test_show_steps(self):
        """Test step-by-step calculation display"""
        factorial(3, show_steps=True)
        output = self.held_output.getvalue()
        self.assertIn("Calculating 3!", output)
        self.assertIn("Starting with 1", output)
        self.assertIn("× 3 = 3", output)
        self.assertIn("× 2 = 6", output)

    def test_show_steps_zero(self):
        """Test step-by-step display for zero"""
        factorial(0, show_steps=True)
        output = self.held_output.getvalue()
        self.assertIn("Calculating 0!", output)
        self.assertIn("0! is defined as 1", output)

if __name__ == '__main__':
    unittest.main(verbosity=2) 