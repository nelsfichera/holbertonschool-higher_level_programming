#!/usr/bin/python3
'''add private instance method area to base geometry class'''


class BaseGeometry:
    '''class which defines geometry'''
    def area(self):
        ''' raises an exception when area is not implemented'''
        raise Exception("area() is not implemented")
