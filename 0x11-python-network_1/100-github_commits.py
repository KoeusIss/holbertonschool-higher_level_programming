#!/usr/bin/python3
"""Requests"""
import requests
import sys


if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.
                     format(sys.argv[2], sys.argv[1]))
    for c in r.json()[0:10]:
        print("{}: {}".format(c.get('sha'),
                              c.get('commit').get('author').get('name')))
