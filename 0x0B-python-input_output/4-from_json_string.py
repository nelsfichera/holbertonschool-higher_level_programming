#!/usr/bin/python3
'''return an object represented by json string'''
import json


def from_json_string(my_str):
    '''turns JSON into string'''
    return json.loads(my_str)
