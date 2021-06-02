#!/usr/bin/python3
'''returns boolean values for object of a class or inherited from a class'''


def is_kind_of_class(obj, a_class):
    ''''method to determine inheritance from a class'''
    return isinstance(obj, a_class)
