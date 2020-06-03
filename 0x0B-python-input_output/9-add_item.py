#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""Operations"""
try:
    lst = load_from_json_file("add_item.json")
except FileNotFoundError:
    lst = []
save_to_json_file(lst + sys.argv[1:], "add_item.json")
