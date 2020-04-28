#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i != j:
            if i < 8:
                print("{:d}{:d}".format(i, j), end=', ')
            else:
                print("{:d}{:d}".format(i, j), end='\n')
