#!/usr/bin/python3
'''Module for storing rectangle class'''


class Rectangle:
    '''Rectangle class with height and width'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''init with width and height as args'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        '''str representation of rectangle'''
        newstr = ''
        if self.__width == 0 or self.__height == 0:
            return newstr
        for x in range(self.__height):
            newstr += ((str(self.print_symbol) * self.__width) + "\n")
        return newstr[:-1]

    def __repr__(self):
        '''prints the representation of rectangle'''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''prints a message when an instance of rectangle is deleted'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
