#!/usr/bin/python3
'''reads response in utf-8 from given url and catches errors'''
from sys import argv as av
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    try:
        with urlopen(av[1]) as response:
            print(response.read().decode("utf-8"))
    
    except HTTPError as err:
        print("Error code: {}".format(err.code))