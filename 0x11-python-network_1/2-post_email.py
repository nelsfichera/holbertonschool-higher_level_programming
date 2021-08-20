#!/usr/bin/python3
'''makes a post request with email and url passed as args'''
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv as av


if __name__ == "__main__":
    d = {"email": av[2]}
    data = urlencode(d)
    data = data.encode('utf-8')

    request = Request(av[1], data)
    with urlopen(request) as response:
        print(response.read().decode("utf-8"))