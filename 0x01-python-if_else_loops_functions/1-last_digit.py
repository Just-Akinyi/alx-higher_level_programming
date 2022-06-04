#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
print("Last digit of {} is {} and is ".format(number, lastdigit), end="")
if (lastdigit > 5):
    print("and is greater than 5")
elif (lastdigit < 5):
    print("and is less than 6 and not 0")
elif (lastdigit == 0):
    print("and is 0")
