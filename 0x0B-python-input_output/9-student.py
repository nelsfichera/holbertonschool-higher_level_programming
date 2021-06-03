#!/usr/bin/python3
'''create the student class'''


class Student:
    '''define the student'''
    def __init__(self, first_name, last_name, age):
        '''init values'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''return the dict rep of a student'''
        return vars(self)
