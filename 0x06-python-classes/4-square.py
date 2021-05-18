#!/usr/bin/python3
"""Further articulation of square class"""


class Square:
    """Define the square"""
    def __init__(self, size=0):
        """sets size"""
        self.size = size

        @property
        def size(self):
            """Retrieves the property"""
            return self.__size

        @size.setter
        def size(self, size):
            """Sets the property and checks errors"""
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

        def area(self):
            """Returns area of square"""
            return self.__size ** 2
