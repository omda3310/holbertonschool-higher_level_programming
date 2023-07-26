#!/usr/bin/python3
"""add_item method"""

import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"


if __name__ == "__main__":
    """test"""
    if exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    """load file"""
    my_list.extend(sys.argv[1:])
    """Save the list"""
    save_to_json_file(my_list, filename)
