#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for x in my_list:
        if (x % 2) == 0:
            new_list.append(x)
            return False
        else:
            new_list.append(x)
            return True
