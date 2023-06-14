#!/usr/bin/python3

""" module of a function that adds, loads and saves args of a python list"""

import sys
""" importing the sys module """

if __name__ == '__main__':

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        items_to_check = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items_to_check = []

    items_to_check.extend(sys.argv[1:])
    save_to_json_file(items_to_check, 'add_item.json')
