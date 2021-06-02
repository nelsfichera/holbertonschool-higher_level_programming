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

    def __str__(self):
        '''prints the formatted string regarding class'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        '''returns the area of a rectangle'''
        return self.__width * self.__height


class Square(Rectangle):
    '''create square subclass'''
    def __init__(self, size):
        '''initializes and validates the size of the square'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''prints the formatted square description'''
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        '''returns the area of a square'''
        return super().area()
