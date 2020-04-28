def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            cc = chr(ord(c) - 32)
        else:
            cc = c
        print("{}".format(cc), end='')
    print(end='\n')
