#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints integer with format flags
    """
    try:
        print('{:d}'.format(value))
    except:
        return False
    return True
