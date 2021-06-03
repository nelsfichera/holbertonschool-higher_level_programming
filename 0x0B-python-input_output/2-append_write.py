#!/usr/bin/python3
'''append text to text in file'''


def append_write(filename="", text=""):
    '''function that does the thing'''
    with open(filename, mode="a", encoding="utf-8") as the_file:
        return the_file.write(text)
