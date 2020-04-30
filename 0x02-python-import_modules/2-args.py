#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lst = sys.argv
    arg = "argument"
    if len(lst) == 1:
        print("{} {}.".format(len(lst) - 1, arg))
    else:
        if len(lst) > 1:
            arg = "arguments"
        print("{} {}: ".format(len(lst) - 1, arg))
        for i in range(1, len(lst)):
            print("{}: {}".format(i, lst[i]))
