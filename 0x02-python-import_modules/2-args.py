#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = "argument"
    if len(sys.argv) == 1:
        print("{} {}.".format(0, argument))
    else:
        if len(sys.argv) > 1:
            argument = "arguments"
        print("{} {}: ".format(len(sys.argv) - 1, argument))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
