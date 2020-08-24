#!/usr/bin/python3
"""UrlLibRequest"""
from urllib import error, request
import sys


if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as res:
            body = res.read()
            print(body.decode("utf8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
