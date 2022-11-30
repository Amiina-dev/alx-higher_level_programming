#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number <= 0:
    last = number % 10
else:
    last = ((number * -1) % 10) * -1

message = "Last digit of %d is %d and is" % (number, last)

if last == 0:
    print(message, "0")
elif remainder > 5:
    print(message, "greater than 5")
else:
    print(message, "less than 6 and not 0")
