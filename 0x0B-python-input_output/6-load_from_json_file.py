#!/usr/bin/python3

""" Module of a function that Creates object from a JSON file """

import json


def load_from_json_file(filename):
    """ Function that creates an object from a json file """

    with open(filename) as f:
        return json.load(f)
