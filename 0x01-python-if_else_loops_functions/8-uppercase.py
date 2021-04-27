#!/usr/bin/python3
def uppercase(str):
    for char in str:
        newChar = char
    if ord(char) >= 97 and ord(char) <= 122:
        newChar = chr(ord(char) - 32)
        print("{}".format(newChar), end="")
        print("")
