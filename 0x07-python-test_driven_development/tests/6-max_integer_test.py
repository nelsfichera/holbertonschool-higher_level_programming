#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to evaluate different cases"""

    def test_integer_numbers(self):
        """Checks for max integer in list of integers"""
        # All positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        # All negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        # Negative and positive integers
        self.assertEqual(max_integer([-1, 2, -3, -4]), 2)
        # One integer
        self.assertEqual(max_integer([1]), 1)
        # One negative integer
        self.assertEqual(max_integer([-20]), -20)

    def test_float_numbers(self):
        """Check for floats"""
        # Check for a infinite number
        self.assertEqual(max_integer([1, 2, 4, 10e+1000]), 10e+1000)
        # Check all positive float numbers
        self.assertEqual(max_integer([1.0, 2.4, 4.3, 100.4]), 100.4)
        # Check all negative float numbers
        self.assertEqual(max_integer([-1.0, -2.2, -4.3, -100.4]), -1.0)
        # Check infinite numbers
        self.assertEqual(max_integer([1, 3, 200, 10000, 100e+1000]), 100e+1000)
        # Check infinite numbers
        self.assertEqual(max_integer([1, 3, 200, 5000, -100e+1000]), 5000)

    def test_strings(self):
        """Check for strings as args"""
        # Check for list with a string inside
        self.assertEqual(max_integer(['who is it']), 'who is it')
        # Check for string as argument
        self.assertEqual(max_integer('who is it'), 'no one')
        # Check for a list of strings
        self.assertEqual(max_integer(['this', 'is', 'many']), 'strings')
        # Check between a upper and lower case
        self.assertEqual(max_integer(['X', 'x']), 'x')

    def test_extreme_cases(self):
        """Checks for max in list of integers"""
        # A empty list
        self.assertEqual(max_integer([]), None)
        # Zero argumments
        self.assertEqual(max_integer(), None)
        # Tuple as a argument
        self.assertEqual(max_integer((1, 2, 100, -4)), 100)
        # -Inf vs inf
        self.assertEqual(max_integer([-100e+1000, 100e+1000]), 100e+1000)
        # With Operation inside
        self.assertEqual(max_integer([25 // 5, 1]), 5)

    def test_raise_type(self):
        """Check for raises TypeError"""
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, ['help', 2, 5, 20])
        self.assertRaises(TypeError, max_integer, [2, 5, "help", 20])
        with self.assertRaises(TypeError):
            max_integer(1, 4, 6, 5)
        with self.assertRaises(TypeError):
            max_integer([1, 2j])
        with self.assertRaises(ValueError):
            max_integer([1, 2, int("two")])
        with self.assertRaises(TypeError):
            max_integer(2)
