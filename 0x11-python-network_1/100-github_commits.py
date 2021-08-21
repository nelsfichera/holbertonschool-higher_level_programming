#!/usr/bin/python3
'''prints the last ten commits of user's repo'''
from sys import argv as av
from requests import get
if __name__ == "__main__":

    url = "https://api.github.com/repos/{}/{}/commits?".format(av[2], av[1])
    r = get(url)
    commits = r.json()
    for commit in commits[:10]:
        print(commit['sha'], end=": ")
        print(commit['commit']['author']['name'])
