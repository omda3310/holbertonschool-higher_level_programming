#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_directory = {}
    for val in a_dictionary:
        new_directory[val] = a_dictionary[val] * 2
    return new_directory
