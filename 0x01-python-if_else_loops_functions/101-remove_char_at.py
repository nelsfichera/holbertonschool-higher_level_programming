#!/usr/bin/python3
def remove_char_at(str, n):
    strNew = ""
    i = 0
    for x in str:
        if (i != n):
            strNew += x
        i += 1
    return strNew
