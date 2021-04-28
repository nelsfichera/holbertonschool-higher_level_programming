#!/usr/bin/python3
for c in (range(ord('z'), ord('a') - 1)):
    if c % 2 != 0:
        ch = c - 32
    else:
        ch = c
    print("{:c}".format(ch), end="")
