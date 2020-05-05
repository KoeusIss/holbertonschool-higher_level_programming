#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = 0 if len(tuple_a) < 1 else tuple_a[0]
    a2 = 0 if len(tuple_b) < 1 else tuple_b[0]
    b1 = 0 if len(tuple_a) < 2 else tuple_a[1]
    b2 = 0 if len(tuple_b) < 2 else tuple_b[1]
    return (a1 + a2, b1 + b2)
