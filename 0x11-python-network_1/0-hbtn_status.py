#!/usr/bin/python3
'''module storing script to fetch body'''
from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as f:
        body = f.read
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))