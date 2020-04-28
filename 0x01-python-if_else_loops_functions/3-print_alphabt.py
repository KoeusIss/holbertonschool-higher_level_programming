#!/usr/bin/python3
for a in range(97, 97 + 26):
    if chr(a) != 'q' and chr(a) != 'e':
        print("{}".format(chr(a)), end='')
