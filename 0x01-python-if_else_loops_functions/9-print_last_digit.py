#!/usr/bin/python3
def print_last_digit(number):
    sign = 1
    if number < 0:
        sign = (-1)
    last = sign * number % 10
    print("{:d}".format(last), end='')
    return last
