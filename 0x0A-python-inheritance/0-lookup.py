#!/usr/bin/python3


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj (object): the given object

    Returns:
        (list): objects list

    """
    return dir(obj)
