#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a name exception with a message
    """
    try:
        raise NameError(message)
    except:
        raise
