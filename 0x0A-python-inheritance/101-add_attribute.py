#!/usr/bin/python3
'''add an attribute if able'''


def add_attribute(object, name, value):
    '''adds a new attribute to the object'''
    if hasattr(object, "__dict__") is not True:
        raise TypeError("can't add new attribute")
    else:
        object.__setattr__(name, value)
