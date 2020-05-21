#!/usr/bin/python3

"""
TextIndentaion module
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of those characters:
    '.' '?' ':'

    Args:
        text (str): a given string

    Raises:
        TypeError: if argument passed is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    pass
