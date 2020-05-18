#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers and print the result
    """
    try:
        result = a/b
    except:
        result =  None
    finally:
        print('Inside result: {}'.format(result))
        return result
