#!/usr/bin/python
"""Further articulation of square class"""


class Square:
    """Define square"""
    def __init__(self, size=0):
        """Set size, error check"""
        if type(size) is not int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return area of square"""
        return self.__size ** 2
