#!/usr/bin/python3
"""Requests"""
import requests
import sys


if __name__ == '__main__':
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
