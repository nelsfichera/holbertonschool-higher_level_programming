#!/usr/bin/python3
''' sends post to query the search user api'''
from sys import argv
from requests import post
if __name__ == '__main__':
    if len(argv) > 1 and bool(argv[1]):
        value = argv[1]
    else:
        value = ''
    payload = {'q': value}
    response = post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        json = response.json()
        if bool(json):
            print("[{}] {}".format(json["id"], json["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")