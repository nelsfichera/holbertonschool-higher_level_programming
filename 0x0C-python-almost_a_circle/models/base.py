#!/usr/bin/python3
'''all the class are belong to us'''
import json
import csv


class Base:
    '''the base of all classes'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constructs the class'''
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''json string rep of dicts'''
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''returns list from json string'''
        if type(json_string) == dict:
            return json_string
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''saves json rep of list_objs to a file'''
        with open("{}.json".format(cls.__name__), 'w+') as file:
             dict_list = [obj.to_dictionary() for obj in list_objs]
             json_str = cls.to_json_string(dict_list)
             file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        '''returns instance with attributes already set'''
        mannequin = cls(1, 1)
        mannequin.update(**dictionary)
        return mannequin

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        try:
            filename = cls.__name__ + ".json"
            with open(filename, mode='r') as the_file:
                content = cls.from_json_string(the_file.read())
                instances = []
                for x in content:
                    instances.append(cls.create(**x))
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save csv objs to file'''
        name = cls.__name__ + ".csv"
        rect = ("id", "width", "height", "x", "y")
        sq = ("id", "size", "x", "y")

        if list_objs is None:
            list_objs = []
        if cls.__name__ == "Rectangle":
            list_objs = ([getattr(obj, i) for i in rect] for obj in list_objs)
            with open(name, "w") as the_file:
                write = csv.writer(the_file)
                for a in list_objs:
                    write.writerow(a)

        if cls.__name__ == "Square":
            list_objs = ([getattr(obj, i) for i in sq] for obj in list_objs)
            with open(name, "w") as the_file:
                write = csv.writer(the_file)
                for a in list_objs:
                    write.writerow(a)

    @classmethod
    def load_from_file_csv(cls):
        '''loads a list from csv file'''
        filename = cls.__name__ + ".csv"

        try:
            with open(fiilename, mode='r') as the_file:
                instances = []
                read = csv.DictReader(the_file)
                for row in read:
                    instances.append(cls.create(**row))
                return instances
        except FileNotFoundError:
            return []
