#!/usr/bin/python3
"""Requests"""
import requests
import sys


if __name__ == '__main__':
    q = sys.argv[1] or "" 
    r = requests.post('http://0.0.0.0:5000/search_user', q)
    try:
        if not r.json():
            print("No result")
        else:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    except ValueError:
        print("Not a valid JSON")


