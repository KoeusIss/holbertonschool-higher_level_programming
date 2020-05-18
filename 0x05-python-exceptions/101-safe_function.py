#!/usr/bin/python3
def safe_function(fct, *args):
    """
    Executes a function safely
    """
    import sys
    try:
        return fct(*args)
    except Exception as exception:
        print('{}'.format(exception), file=sys.stderr)
