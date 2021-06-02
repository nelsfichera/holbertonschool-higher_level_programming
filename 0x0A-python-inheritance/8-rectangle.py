#!/usr/bin/python3
'''add integer validator to base geometry class'''


class BaseGeometry:
    '''class which defines geometry'''

    def area(self):
        ''' raises an exception when area is not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates that value is a positive integer'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than zero".format(name))


class Rectangle(BaseGeometry):
    '''create rectangle subclass'''
    def __init__(self, width, height):
        '''initializes and validates height and width'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
