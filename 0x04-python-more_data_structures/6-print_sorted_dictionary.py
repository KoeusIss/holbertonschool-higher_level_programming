#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictoinary by ordered keys
    """
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
