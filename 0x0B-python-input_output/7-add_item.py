#!/usr/bin/python3
'''add args from python list and save to file'''
import json
import os.path
from sys import argv
'''load previous files'''
save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file
'''add the arguments to a python list and save to file'''
if __name__ == "__main__":
    the_list = []
    if os.path.exists("add_item.json"):
        the_list = load_from("add_item.json")
    the_list.append(argv[1:])
    save_to(the_list, "add_item.json")
