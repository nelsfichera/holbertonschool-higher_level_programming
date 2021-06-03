#!/usr/bin/python3
'''save to json 'file'''
import json


def save_to_json_file(my_obj, filename):
    '''function that does the thing'''
    with open(filename, mode="w", encoding="utf-8") as the_file:
        the_file.write(json.dumps(my_obj))
