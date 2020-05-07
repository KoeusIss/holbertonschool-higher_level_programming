#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not roman_string.isalpha():
        return 0
    value = 0
    last = ""
    for c in roman_string:
        if c not in roman:
            return 0
        elif (c == "V" or c == "X") and last == "I":
            value += roman[c] - 2
        else:
            value += roman[c]
        last = c
    return value
