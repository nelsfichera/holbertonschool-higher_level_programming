#!/usr/bin/python3
'''requests value of response header'''
from urllib.request import urlopen
from sys import argv as av


if __name__ == "__main__":
    with urlopen(av[1]) as response:
        headers = response.info()
        header = "X-Request-Id"
        print(headers.get(header))