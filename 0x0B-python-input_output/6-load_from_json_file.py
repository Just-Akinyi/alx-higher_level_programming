#!/usr/bin/python3
"""Defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Create an Object from a “JSON file”"""

    with open(filename) as file:
        return json.load(file)
