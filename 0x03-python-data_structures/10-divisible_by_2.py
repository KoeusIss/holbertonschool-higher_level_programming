#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    truth = []
    for item in my_list:
        truth.append(True) if item % 2 == 0 else truth.append(False)
    return truth
