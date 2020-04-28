#!/usr/bin/python3
def remove_char_at(astr, n):
    i = 0
    c_str = ""
    for c in astr:
        if i == n:
            c_str = c_str + ''
        else:
            c_str = c_str + c
        i = i + 1
    return c_str
