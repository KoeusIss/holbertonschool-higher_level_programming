#!/usr/bin/python3
"""WriteFile module"""


def write_file(filename="", text=""):
    """Writes a string to text file

    Args:
        filename (str): the text file name
        text (str): the given string

    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
