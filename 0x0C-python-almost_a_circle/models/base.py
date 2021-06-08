#!/usr/bin/python3
'''all the class are belong to us'''
import json


class Base:
    '''the base of all classes'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constructs the class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''json string rep of dicts'''
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''returns list from json string'''
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''saves json rep of list_objs to a file'''
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as the_file:
            the_file.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''returns instance with attributes already set'''
        if (cls.__name__ == "Rectangle"):
            mannequin = cls(1, 1)
        if (cls.__name__ == "Square"):
            mannequin = cls(1)
        mannequin.update(**dictionary)
        return mannequin

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        try:
            filename = cls.__name__ + ".json"
            with open(filename, encoding="utf-8") as the_file:
                return cls.create(cls.from_json_string(the_file))
        except FileNotFoundError:
            return []
