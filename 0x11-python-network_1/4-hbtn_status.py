#!/usr/bin/python3
'''gets content of url using requests'''
from requests import get

response = get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
