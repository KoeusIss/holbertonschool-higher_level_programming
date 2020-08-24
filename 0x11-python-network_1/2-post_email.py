#!/usr/bin/python3
"""UrlLibRequest"""
from urllib import parse, request
import sys


if __name__ == '__main__':
    data = parse.urlencode({"email": sys.argv[2]})
    data = data.encode()
    with request.urlopen(sys.argv[1], data) as res:
        body = res.read()
    print(body.decode("utf8"))
