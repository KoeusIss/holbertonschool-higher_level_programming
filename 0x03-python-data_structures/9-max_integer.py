#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_item = my_list[0]
    for item in my_list:
        if item > max_item:
            max_item = item
    return max_item
