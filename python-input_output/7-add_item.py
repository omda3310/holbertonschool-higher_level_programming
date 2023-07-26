#!/usr/bin/python3
"""add_item method"""


import sys
import json
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
fl = "add_item.json"


if __name__ == "__main__":
    """test"""
    if exists(fl):
        my_list = load_from_json_file(fl)
    """load file"""
    my_list.extend(sys.argv[1:])
    """Save the list"""
    save_to_json_file(my_list, fl)
