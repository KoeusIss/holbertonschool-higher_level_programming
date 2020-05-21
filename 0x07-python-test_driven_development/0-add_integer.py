#!/usr/bin/python3
"""
Add integer module
"""


def add_integer(a, b=98):
    """
    Add two integer a and b

    Args:
        a (int/float): the first integer
        b (int/float): the second integer

    Raises:
        TypeError: when passing non integer argument

    Returns:
        (int): sum of a and b as integer

    """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
        return
    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")
        return
    return int(a) + int(b)
