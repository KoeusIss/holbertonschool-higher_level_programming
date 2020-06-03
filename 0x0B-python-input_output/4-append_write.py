#!/usr/bin/python3
"""AppendWrite module"""


def append_write(filename="", text=""):
    """Appends a string at the end

    Args:
        filename (str): the given filename
        text (str): the given str

    Returns:
        (int): the number of readed character

    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
