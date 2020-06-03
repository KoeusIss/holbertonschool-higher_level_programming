#!/usr/bin/python3
"""SaveToJsonFile module"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file

    Args:
        my_obj (object): given object
        filename (str): a given text file name

    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
