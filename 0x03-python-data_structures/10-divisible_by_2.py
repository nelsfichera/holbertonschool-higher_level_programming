#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        index = 0
        for x in my_list:
            if x % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
                index += 1
        return new_list
