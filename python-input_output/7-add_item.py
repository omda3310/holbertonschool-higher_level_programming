#!/usr/bin/python3
"""add_item method"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list1 = list(sys.argv[1:])

try:
    mlist = load_from_json_file('add_item.json')
except Exception:
    mlist = []

mlist.extend(list1)
save_to_json_file(mlist, 'add_item.json')
