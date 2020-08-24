#!/usr/bin/python3
"""UrlLibRequest"""
import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as res:
        header_var = res.getheader('X-Request-Id')
    print(header_var)
