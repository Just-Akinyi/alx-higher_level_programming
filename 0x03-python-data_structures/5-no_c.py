#!/usr/bin/python3
def no_c(my_string):
    my_string_list = list(my_string)
    index_count = 0
    for index in my_string_list:
        if index == 'c' or index == 'C':
            my_string_list[index_count] = ""
        index_count += 1
    return "".join(my_string_list)

