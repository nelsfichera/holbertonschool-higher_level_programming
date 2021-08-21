#!/usr/bin/python3
'''gets response of specific header at given url'''
from requests import get
from sys import argv
if __name__ == "__main__":
    print(get(argv[1]).headers.get("X-Request-Id"))
