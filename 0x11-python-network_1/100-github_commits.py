#!/usr/bin/python3
"""Requests"""
import requests
import sys


if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.
                     format(repo_name, owner_name))
    for commit in r.json()[:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
