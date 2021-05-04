#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for n in x:
            if n != x[-1]:
                print("{:d} ".format(n), end="")
	    else:
                print("{:d}".format(n), end="")
	print('')
