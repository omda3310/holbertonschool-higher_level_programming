#!/usr/bin/python3
"""add_item method"""

import sys
import json
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fil = "add_item.json"


if __name__ == "__main__":
    """test"""
    if exists(fil):
        my_list = load_from_json_file(fil)
    else:
        my_list = []
    """load file"""
    my_list.extend(sys.argv[1:])
    """Save the list"""
    save_to_json_file(my_list, fil)
