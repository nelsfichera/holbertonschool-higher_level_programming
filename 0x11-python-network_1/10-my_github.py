#!/usr/bin/python3
'''print github userid using github api'''
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv
if __name__ == "__main__":
    r = get('https://api.github.com/user', auth=HTTPBasicAuth(argv[1], argv[2]))
    try:
        info = r.json()
        print(info['id'])
    except:
        print('None')