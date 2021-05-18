#!/usr/bin/python3
"""Square class with size and error checks"""


class Square:
    """Define square of size"""
    def __init__(self, size=0):
        """Sets size and error checks"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
