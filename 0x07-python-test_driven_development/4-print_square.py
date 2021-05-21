#!/usr/bin/python3
'''Prints squares of given size'''


def print_square(size):
    '''Prints square where size (int)
    is the size of the square. raises
    errors when size is not an into or
    when size is less than zero
    '''
    if (type(size) is float and size < 0) or type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(0, size):
        print("#" * size)
