#!/usr/bin/python3
'''write a file'''


def write_file(filename="", text=""):
    '''function which writes a file'''
    with open(filename, mode="w", encoding="utf-8") as the_file:
        return the_file.write(text)
