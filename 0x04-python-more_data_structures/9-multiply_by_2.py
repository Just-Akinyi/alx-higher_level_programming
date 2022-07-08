#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_directory = {}
    for value in a_dictionary:
        new_directory[value] = a_dictionary[value] * 2
    return new_directory
