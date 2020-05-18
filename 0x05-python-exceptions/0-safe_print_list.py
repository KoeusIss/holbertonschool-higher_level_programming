#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements from list
    """
    number = 0
    for n in range(0, x):
        try:
            print('{}'.format(my_list[n]), end='')
            number += 1
        except:
            break
    print()
    return number
