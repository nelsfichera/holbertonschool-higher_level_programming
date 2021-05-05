#!/usr/bin/python3
def no_c(my_string):
    return ("".join(char for c in my_string if char not in "Cc"))
