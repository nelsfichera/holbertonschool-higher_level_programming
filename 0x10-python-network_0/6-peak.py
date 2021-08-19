#!/usr/bin/python3
'''stores find_peak function'''


def find_peak(list_of_integers):
    '''finds the max num from list'''
    if bool(list_of_integers):
        list_of_integers.sort()
        return(list_of_integers[-1])
    else:
        return (None)
