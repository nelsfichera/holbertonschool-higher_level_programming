#!/usr/bin/python3
'''create the student class'''


class Student:
    '''define the student'''
    def __init__(self, first_name, last_name, age):
        '''init values'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''return the dict rep of a student'''
        if type(attrs) is list:
            new_dict = {}
            for element in attrs:
                if type(element) is str:
                    try:
                        new_dict[element] = self.__dict__[element]
                    except:
                        pass
            return new_dict
        return vars(self)

    def reload_from_json(self, json):
        '''replaces all attributes of student instance'''
        for element in json:
            self.__dict__[element] = json[element]
