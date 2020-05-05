#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specefic position

    Args:
        my_list: the given list
        idx: a given position
        element: the newly replaced element

    Returns:
        The original list: if idx is negative
        The original list: if idx out of range
        The new list: if succeed
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
