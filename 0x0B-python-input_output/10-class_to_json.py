#!/usr/bin/python3
"""ClassToJson module"""


def class_to_json(obj):
    """Returns the dictionnary decriptions with simple data  structure list
        for JSON serialization of an object

    Args:
        obj (object): the class object

    Returns:
        (str): a json representation of a class

    """
    return obj.__dict__
