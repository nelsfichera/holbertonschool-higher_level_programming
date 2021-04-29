#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n_args = len(argv)
    if n_args == 1:
        print('0')
    elif n_args == 2:
        print("{}".format(argv[1]))
    elif n_args > 2:
        result = 0
        for argument in argv[1:]:
            result = result + int(argument)
        print(result)
