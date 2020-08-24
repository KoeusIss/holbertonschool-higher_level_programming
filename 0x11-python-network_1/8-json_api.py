#!/usr/bin/python3
"""Requests"""
import requests
import sys


if __name__ == '__main__':
    data = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        if not r.json():
            print("No result")
        else:
            print("[{}] {}".format(r.json().get("id"), r.json().get("name")))
    except ValueError:
        print("Not a valid JSON")
