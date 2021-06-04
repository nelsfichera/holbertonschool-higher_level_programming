#!/usr/bin/python3
''' read a file'''


def read_file(filename=""):
    '''reads a file passed as argument'''
    with open(filename, encoding='utf-8') as the_file:
        print(the_file.read(), end="")
