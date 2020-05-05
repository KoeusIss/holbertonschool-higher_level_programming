#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Rerieves element from a list

    Args:
        my_list: the given list
        idx: the meant index position

    Returns:
        None: if idx is negative
        None: if idx out of range
        List item at idx: if succeed
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]
