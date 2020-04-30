#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for i in range(0, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
