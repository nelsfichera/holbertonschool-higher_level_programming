#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(ord('a'), ord('z') + 1):
            n = ord(c) - 32
        else:
            n = ord(c)
        print("{:c}".format(n), end='')
        print('')
