#!/usr/bin/python3
"""Module that tests square methods and attributes"""

import pep8
import unittest
from unittest.mock import patch
from io import StringIO
import models.base
import models.rectangle
import models.square

Square = models.square.Square
Rectangle = models.rectangle.Rectangle
Base = models.base.Base


class SquareTest(unittest.TestCase):
    """Test for square"""

    def setUp(self):
        """setup assertEquals"""

        self.ae = self.assertEqual
        Base._Base__nb_objects = 0

    def test_value_square(self):
        """test normal values"""

        s1 = Square(2, 3, 4)

        self.ae(s1.size, 2)
        self.ae(s1.x, 3)
        self.ae(s1.y, 4)

    def test_typeerror(self):
        """test for typeerror"""

        s = Square(1, 1, 1)

        with self.assertRaises(TypeError):
            s.size = "e"

        with self.assertRaises(TypeError):
            s.x = "9"

        with self.assertRaises(TypeError):
            s.y = "5"

    def test_valueerror(self):
        """test for valueerror"""

        s = Square(1, 1, 1)

        with self.assertRaises(ValueError):
            s.size = 0

        with self.assertRaises(ValueError):
            s.x = -3

        with self.assertRaises(ValueError):
            s.y = -2

    def test_area(self):
        """test for area"""

        s = Square(2, 2)
        self.ae(s.area(), 4)

        s2 = Square(5, 0, 0, 13)
        self.ae(s2.area(), 25)

        with self.assertRaises(ValueError):
            s3 = Square(-3, 0, 0)

    def test_pep8_conformance(self):
        """test that we conform to pep8"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/square.py"])
        self.ae(result.total_errors, 0,
                "Found code style errors (and warnings).")

    def test_square_init(self):
        """tests square init"""
        expected = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(5)
            print(s1)
            self.ae(fake_out.getvalue(), expected)
        expected = "25\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1.area())
            self.ae(fake_out.getvalue(), expected)
        expected = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.ae(fake_out.getvalue(), expected)

        expected = "[Square] (2) 1/3 - 3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s2 = Square(3, 1, 3)
            print(s2)
            self.ae(fake_out.getvalue(), expected)

    def test_square_get_set(self):
        """tests getter and setter of square"""
        expected = "[Square] (1) 0/0 - 10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(5)
            s1.size = 10
            print(s1)
            self.ae(fake_out.getvalue(), expected)

    def test_square_set_error(self):
        """tests error if bad size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square(5)
            s1.size = "9"

    def test_square_update(self):
        """tests update of square"""
        expected = "[Square] (89) 12/1 - 7\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(5)
            s1.size = 10
            s1.update(size=7, id=89, y=1, x=12)
            print(s1)
            self.ae(fake_out.getvalue(), expected)

    def test_square_to_dict(self):
        """tests square to dict"""
        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(s1_dictionary, expected)
