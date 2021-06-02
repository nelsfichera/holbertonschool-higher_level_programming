#!/usr/bin/python3
'''compares object instances with boolean output'''


def is_same_class(obj, a_class):
    '''returns true or false if object is exactly a member of a class'''
    return(type(obj) is a_class)
