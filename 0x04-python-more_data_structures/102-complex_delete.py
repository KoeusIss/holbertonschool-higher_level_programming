#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specefic value in adictionary
    """
    for k in list(a_dictionary.keys()):
        if a_dictionary[k] is value:
            del(a_dictionary[k])
    return a_dictionary
