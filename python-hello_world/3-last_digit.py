#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
print("Last digit of {}".format(number), end=" ")
print("is {}".format(last_digit), end=" ")
if int(last_digit) > 0:
 print("and is greater than 5")
elif int(last_digit) == 0:
 print("and is 0")
elif int(last_digit) < 6 and int(last_digit) != 0:
 print("and is less than 6 and not 0")
else:
 print("wrong output")

