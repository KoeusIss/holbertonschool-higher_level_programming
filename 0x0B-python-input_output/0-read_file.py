#!/usr/bin/python3
"""ReadFile module"""


def read_file(filename=""):
    """Reads a text file and prints it out

    Args:
        filename (str): the filename of the text file

    """
    with open(filename, encoding="UTF-8") as f:
        string = f.read()
        print(string, end="")
