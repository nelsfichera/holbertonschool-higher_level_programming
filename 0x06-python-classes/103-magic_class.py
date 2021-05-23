#!/usr/bin/python3
'''math functions'''
import math


class MagicClass:
    '''magic class'''
    def __init__(self, radius=0):
        '''initialize circle object'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''calculate the area of a circle'''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''calculate the circumference of a circle'''
        return 2 * math.pi * self.__radius
