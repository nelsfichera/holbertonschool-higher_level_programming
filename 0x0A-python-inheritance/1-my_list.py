#!/usr/bin/python3
''' Stores the MyList class'''


class MyList(list):
    ''' list class for myself'''
    def print_sorted(self):
        '''prints a list in ascending order'''
        print(sorted(self))
