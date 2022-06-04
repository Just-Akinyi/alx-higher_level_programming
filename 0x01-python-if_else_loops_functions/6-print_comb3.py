#!/usr/bin/python3
for num in range(0, 90):
    print("{}".format(num)) + end = ", "
    if (num < 10):
        print("{:02d}".format(num))
    elif (num == 89):
        print("{}".format(num))
