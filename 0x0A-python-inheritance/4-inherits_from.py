#!/usr/bin/python3
'''returns boolean value for direct and indirect inheritance'''


def inherits_from(obj, a_class):
    '''returns boolean value for direct and indirect inheritance'''
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
