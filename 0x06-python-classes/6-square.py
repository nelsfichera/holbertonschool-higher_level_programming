#!/usr/bin/python3
"""Further articulation of square class"""


class Square:
    """Define the square"""
    def __init__(self, size=0):
        """sets size & position"""
        self.size = size
        self.position = position

        @property
        def size(self):
            """Retrieves size"""
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

        @property
        def position(self):
            """Retrieve position"""
            return self.__position

        @position.setter
        def position(self, position):
            """Sets the position and checks errors"""
            if type(position) is not tuple or len(position) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            elif type(position[0]) is not int or type(position[1]) is not int:
                raise TypeError("position must be a tuple of 2 positive integers")
            elif position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = position

        def area(self):
            """Returns area of square"""
            return self.__size ** 2

        def my_print(self):
            """Prints square"""
            if self.__size == 0:
                print("")
            else:
                for x in range(self.__position[1]):
                    print("")
                for x in range(self.__size):
                    for y in range(self.__position[0]):
                        print(" ", end="")
                    for y in range(self.__size):
                        print("#", end="")
                    print("")
