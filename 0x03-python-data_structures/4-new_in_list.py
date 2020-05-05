#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specefic position without modifiying
    the original list

    Args:
        my_list: the original list
        idx: the position when the replacement should made
        element: the new element to be inserted to the list
    Returns:
        The newly replaced list if succeed
        The original list if idx is negative
        The original list if idx is out of range
    """
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        new_list = []
        for i in my_list:
            if my_list.index(i) == idx:
                new_list.append(element)
            else:
                new_list.append(i)
    return new_list
