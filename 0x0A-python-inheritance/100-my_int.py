#!/usr/bin/python3
'''adv my int q'''


class MyInt(int):
    '''inherit from integer and flip signs'''

    def __eq__(self, other):
        '''not equal to'''
        return int(self) != other

    def __ne__(self, other):
        '''equal to'''
        return int(self) == other
