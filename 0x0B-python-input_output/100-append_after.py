#!/usr/bin/python3
"""AppendAfter module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of a text file, after each line containing a specefic
        string

    Args:
        filename (str): the text file name
        search_string (str): the given search string
        new_string (str): the given new string
    """
    with open(filename, "r+", encoding="utf-8") as f:
        string = ""
        for line in f:
            string += line
            if search_string in line:
                string += new_string
        f.seek(0)
        f.write(string)
