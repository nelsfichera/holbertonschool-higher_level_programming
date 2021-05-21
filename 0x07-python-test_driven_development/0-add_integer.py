#!/usr/bin/python3
'''Adds integers'''


def add_integer(a, b=98):
    '''add_integer: adds numbers a + b
       receives ints and floats
       casts all floats to ints prior to operation
       returns sum of a and b
       raises type errors as needed
    '''
    if type(a) in (int, float):
        a = int(a)
    else:
        raise TypeError('a must be an integer')
    if type(b) in (int, float):
        b = int(b)
    else:
        raise TypeError('b must be an integer')
    return a + b
