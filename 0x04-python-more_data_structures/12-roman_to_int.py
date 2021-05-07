#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    key = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ints = [key[N] for N in roman_string]
    return sum(map((lambda x, y: -x if x < y else x), ints, ints[1:] + [0]))
