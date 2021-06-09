#!/usr/bin/python3
'''test rectangle methods and attributes'''
import pep8
import unittest
from unittest.mock import patch
from io import StringIO
import models.base
import models.rectangle
import models.square

Rectangle = models.rectangle.Rectangle
Base = models.base.Base
Square = models.square.Square


class RectangleTest(unittest.TestCase):
    '''test rectangle methods and attr'''

    def setUp(self):
        '''setup for tests'''
        self.ae = self.assertEqual
        Base._Base__nb_objects = 0

    def test_init(self):
        '''instances'''
        r = Rectangle(10, 2)
        self.ae(r.id, 1)
        rr = Rectangle(2, 10)
        self.ae(rr.id, 2)
        rrr = Rectangle(10, 2, 0, 0, 12)
        self.ae(rrr.id, 12)

    def test_rectangle_values(self):
        '''test for normal values'''
        r1 = Rectangle(1, 2, 3, 4)
        self.ae(r1.width, 1)
        self.ae(r1.height, 2)
        self.ae(r1.x, 3)
        self.ae(r1.y, 4)

    def test_typeerror(self):
        '''test for type error'''
        r2 = Rectangle(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r2.width = "e"
        with self.assertRaises(TypeError):
            r2.height = "4"
        with self.assertRaises(TypeError):
            r2.x = "9"
        with self.assertRaises(TypeError):
            r2.y = "5"

    def test_valueerror(self):
        '''test value error'''
        r3 = Rectangle(1, 1, 1, 1)
        with self.assertRaises(ValueError):
            r3.width = 0
        with self.assertRaises(ValueError):
            r3.height = -1
        with self.assertRaises(ValueError):
            r3.x = -3
        with self.assertRaises(ValueError):
            r3.y = -2

    def test_area(self):
        '''test for area'''
        r4 = Rectangle(4, 2)
        self.ae(r4.area(), 8)
        r5 = Rectangle(5, 6, 0, 0, 13)
        self.ae(r5.area(), 30)

    def pep8_test(self):
        '''test for pep8'''
        pep8style = pep8.StyleGuide(quiet=True)
        report = pep8style.check_files(["models/rectangle.py"])
        self.ae(result.total_errors, 0, "Found errors")

    def test_display_0(self):
        """tests simple display"""
        expected = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(4, 6)
            r1.display()
            self.ae(fake_out.getvalue(), expected)
        expected = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 2)
            r1.display()
            self.ae(fake_out.getvalue(), expected)

    def test_str_overwrite(self):
        """tests __str__ method"""
        expected = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(4, 6, 2, 1, 12)
            print(r1)
            self.ae(fake_out.getvalue(), expected)
        expected = "[Rectangle] (1) 1/0 - 5/5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(5, 5, 1)
            print(r1)
            self.ae(fake_out.getvalue(), expected)

    def test_display_1(self):
        """tests simple display"""
        expected = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 3, 2, 2)
            r1.display()
            self.ae(fake_out.getvalue(), expected)
        expected = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(3, 2, 1, 0)
            r1.display()
            self.ae(fake_out.getvalue(), expected)

    def test_update_0(self):
        """tests update"""
        expected = "[Rectangle] (1) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            print(r1)
            self.ae(fake_out.getvalue(), expected)
        expected = "[Rectangle] (89) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(89)
            print(r1)
            self.ae(fake_out.getvalue(), expected)
        expected = "[Rectangle] (89) 4/5 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(89, 2, 3, 4, 5)
            print(r1)
            self.ae(fake_out.getvalue(), expected)

    def test_update_1(self):
        """tests update"""
        r1 = Rectangle(10, 10, 10, 10)
        expected = "[Rectangle] (89) 3/1 - 2/10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(y=1, width=2, x=3, id=89)
            print(r1)
            self.ae(fake_out.getvalue(), expected)
        expected = "[Rectangle] (89) 1/3 - 4/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(x=1, height=2, y=3, width=4)
            print(r1)
            self.ae(fake_out.getvalue(), expected)

    def test_to_dict(self):
        """tests to dict"""
        self.maxDif = None

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(r1_dictionary, expected)

        expected = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(type(r1_dictionary))
            self.ae(fake_out.getvalue(), expected)

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(r2.to_dictionary(), expected)
