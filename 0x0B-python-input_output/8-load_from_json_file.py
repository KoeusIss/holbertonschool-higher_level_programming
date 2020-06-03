#!/usr/bin/python3
"""LoadFromJsonFile module"""
import json


def load_from_json_file(filename):
    """Creates object from a JSON file

    Args:
        filename (str): a text file name

    Returns:
        (object): object newly created

    """
    with open(filename, "r+", encoding="utf-8") as f:
        return json.load(f)
