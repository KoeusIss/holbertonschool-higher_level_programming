#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    Prints an integer, redirect error to the stderr
    """
    import sys
    try:
        print('{:d}'.format(value))
        return True
    except Exception as exception:
        print('Exception: {}'.format(exception), file=sys.stderr)
        return False
