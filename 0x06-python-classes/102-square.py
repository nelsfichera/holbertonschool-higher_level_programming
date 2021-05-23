#!/usr/bin/python3
'''define a square'''


class Square:
    '''define a square'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        '''returns the area of square instance'''
        return (self.__size * self.__size)

    def my_print(self):
        '''my_print prints using #'''
        if self.__size > 0:
            if self.__position[1] > 0:
                lines = "\n" * self.__position[1]
                print(lines, end='')
            for lines in range(0, self.__size):
                for column in range(0, self.__size + self.__position[0]):
                    if column >= self.__position[0]:
                        print("#", end='')
                    else:
                        print(" ", end='')
                print()
        else:
            print()

    @property
    def size(self):
        '''return size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the value of square instance'''
        if isinstance(value, (int)) is True:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        '''gets the value of position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''set the position for printing'''
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be atuple of 2 positive integers")
        else:
            self.__positon = value

    def __str__(self):
        '''method for printing'''
        square_string = ""
        if self.__size > 0:
            square_string += "\n" * self.__position[1]
            for x in range(0, self.__size):
                square_string += (" " * self.__position[0] +
                                  "#" * self.__size + "\n")
        return square_string[0: -1]
