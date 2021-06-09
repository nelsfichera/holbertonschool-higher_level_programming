#!/usr/bin/python3
'''test the base class'''

import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class BaseTest(unittest.TestCase):
   '''test base methods'''

    def test_id(self):
        '''test for num of instances and args'''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b1.id, 1)
	self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
	self.assertEqual(b4.id, 12)
	self.assertEqual(b5.id, 4)

    def test_negative(self):
        '''tests bad values'''
        try:
            b1 = Base(-2)
        except Exception as e:
            self.assertEqual(print(e), e)

    def test_to_json(self):
        '''test for none and normal vals'''
        test_dict = {'x': 2, 'width': 10, 'id': 5, 'height': 7, 'y': 8}
        r1 = Rectangle(10, 7, 2, 8, 5)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.ae(dictionary, test_dict)

        json2 = Base.to_json_string(None)
        self.ae(json_2, "[]")

    def test_pep8(self):
        '''test to conform'''
        pep8style = pep8.StyleGuide(quiet=True)
        report = pep8style.check_files("models/base.py"])
        self.assertEqual(report.total_errors, 0, "Found errors")

if __name__ == '__main__':
    unittest.main()
    from ...models.base import Base
