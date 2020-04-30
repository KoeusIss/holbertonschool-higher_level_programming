#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lst = dir(hidden_4.pyc)
    for i in lst:
        if i[:2] != "__":
            print(i)
