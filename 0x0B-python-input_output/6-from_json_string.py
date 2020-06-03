#!/usr/bin/python3
"""FromJsonToString module"""
import json


def from_json_string(my_str):
    """Returns an object from json

    Args:
        my_str (str): the given json string

    Returns:
        (object): the object

    """
    return json.loads(my_str)
