#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range (len(my_list)):
        i = my_list.reverse(i)
        print("{}".format(i))
