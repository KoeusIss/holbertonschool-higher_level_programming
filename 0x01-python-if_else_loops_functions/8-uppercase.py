def uppercase(str):
    """
    signature: uppercase(str)
    Docstring: Transforms a string into uppercase
    str: string to be converted
    """
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            cc = chr(ord(c) - 32)
        else:
            cc = c
        print("{}".format(cc), end='')
    print(end='\n')
