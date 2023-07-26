#!/usr/bin/python3
"""add_item method"""

import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fl = "add_item.json"
jlist = []

if os.path.exists(fl):
    jlist = load_from_json_file(fl)

for i in range(1, len(sys.argv)):
    jlist.append(sys.argv[i])

save_to_json_file(jlist, fl)
