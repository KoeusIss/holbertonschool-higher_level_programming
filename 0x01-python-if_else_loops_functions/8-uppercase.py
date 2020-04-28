#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            cc = ord(c) - 32
        else:
            cc = ord(c)
        print("{:c}".format(cc), end='')
    print(end='\n')
