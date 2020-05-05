#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all charcter c and C from a string

    Args:
        my_string: the string to be processing

    Returns: The new string without "c" adn "C" character
    """
    new_string = ""
    for c in my_string:
        if c in "cC":
            continue
        else:
            new_string += c
    return new_string
