#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns key with the biggest integer value
    """
    if a_dictionary is None or a_dictionary is {}:
        return None
    else:
        return max(a_dictionary)
