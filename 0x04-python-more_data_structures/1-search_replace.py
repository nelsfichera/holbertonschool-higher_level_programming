#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    x = 0
    while x < len(my_list):
        if my_list[x] == search:
            new_list[x] == replace
        x += 1
    return new_list
