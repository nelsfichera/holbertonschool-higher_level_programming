#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list) - 1
    if idx < 0:
        return None
    if idx > list_len:
        return None
    return my_list[idx]
