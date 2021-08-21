#!/usr/bin/python3
'''posts email to url'''
from requests import post
from sys import argv

if __name__ == "__main__":
    payload = {"email": argv[2]}
    print(post(argv[1], data=payload).text)
