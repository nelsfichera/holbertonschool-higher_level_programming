#!/usr/bin/python3
'''prints content of page or the error code'''
from requests import get
from sys import argv


if __name__ == "__main__":
    response =  get(argv[1])
    status = response.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.text)