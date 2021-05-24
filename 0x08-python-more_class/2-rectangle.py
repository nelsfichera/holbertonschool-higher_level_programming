#!/usr/bin/python3
'''Module for storing rectangle class'''


class Rectangle:
    '''Rectangle class with height and width'''
    def __init__(self, width=0, height=0):
        '''init with width and height as args'''
        self.width = width
        self.height = height

    @property
    def height(self):
        '''gets the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height, raises errors'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        '''gets the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width, raises errors'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        '''returns the area of a rectangle'''
        return (self.__height * self.__width)

    def perimeter(self):
        '''returns the perimeter of a rectangle'''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)
