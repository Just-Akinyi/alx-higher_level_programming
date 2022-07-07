#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list):
        maxnum = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > maxnum:
                maxnum = my_list[i]
        return maxnum
    return None
