#!/usr/bin/python3
"""Number of lines module"""


def number_of_lines(filename=""):
    """Returns the number of lines in a text file

    Args:
        filename (str): text file name

    """
    with open(filename, encoding="utf-8") as f:
        number = 0
        for line in f:
            number += 1

    return number
