#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple
    """
    if not my_list:
        return 0
    somme = sum([x * y for x, y in my_list])
    return somme / sum([y for x, y in my_list])
