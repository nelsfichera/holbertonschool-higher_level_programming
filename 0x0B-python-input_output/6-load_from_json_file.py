#!/usr/bin/python3
'''create object from json'''
import json


def load_from_jston_file(filename):
    '''creates an object from a json file no permissions management'''
    with open(filename, encoding="utf-8") as the_file:
        return json.load(the_file)
