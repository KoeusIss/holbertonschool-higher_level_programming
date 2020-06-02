#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """Returns if the object is an instance of the given calss or an inherited
        class of it.

    Args:
        obj (object): the given object
        a_class (class): the given inspected class

    Returns:
        (True) if the obj is an instance of the class or inheriten
        (False) otherwise

    """
    return isinstance(obj, a_class)
