#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integer of a list

    Args:
        my_list: integer list

    Returns:
        Nothing, just print out the list
    """
    for item in my_list:
        print('{:d}'.format(item))
