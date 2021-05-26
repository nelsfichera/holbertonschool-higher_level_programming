#!/usr/bin/python3
'''Print name'''


def say_my_name(first_name, last_name=""):
    '''Prints given and surnames
    Given name is the first argument
    Surname is second argument
    Raises errors when types are not strings
    '''

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
