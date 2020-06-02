#!/usr/bin/python3


def is_same_class(obj, a_class):
    """Returns if an object is an instance of the given class ou nn

    Args:
        obj (object): the given object
        a_class (class): the given class

    Returns:
        (True) if the obj is an instance of a_class
        (False) otherwise

    """
    return isinstance(obj, a_class)