#!/usr/bin/python3
"""add_item method"""


import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
fl = "add_item.json"


if __name__ == "__main__":
    """test"""
    if os.path.exists(fl):
        my_list = load_from_json_file(fl)
    """load file"""
    for i in range(1, len(sys.argv)):
        my_list.extend(sys.argv[i])
    """Save the list"""
    save_to_json_file(my_list, fl)
