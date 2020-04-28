#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if last > 5:
    flag = 'and is greater than 5'
elif last == 0:
    flag = 'and is 0'
else:
    flag = 'and is less than 6 and not 0'
print("Last digit of {} is {} {}".format(number, last, flag))
