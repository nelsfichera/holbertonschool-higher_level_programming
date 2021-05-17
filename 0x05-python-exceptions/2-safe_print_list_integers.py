#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_iter = 0
    i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
        print_iter += 1
    print("")
    return print_iter
