#!/usr/bin/python3
"""ReadLines module"""


def read_lines(filename="", nb_lines=0):
    """Reads lines of a text file and print it out

    Args:
        filename (str): the text file name
        nb_lines (int): number of lines

    """
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for i in range(nb_lines):
            print(f.readline(), end="")
