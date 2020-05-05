#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integer in the list in reverse order

    Args:
        my_list: the given list

    Returns:
        Nothing, just print out the list reversely
    """
    if not my_list:
        return None
    my_list.reverse()
    for item in my_list:
        print('{:d}'.format(item))
