#!/usr/bin/python3
"""Program to add load and save a add_item.json file"""

import sys


if __name__ == "__main__":

    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        l_items = load("add_item.json")
    except FileNotFoundError:
        l_items = []

    l_items.extend(sys.argv[1:])
    save(l_items, "add_item.json")
