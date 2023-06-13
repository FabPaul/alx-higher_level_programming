#!/usr/bin/python3

""" Module for a function that returns the JSON representation of an object """

import json


def to_json_string(my_obj):
    """ Function that returns json to object (string) """

    return json.dumps(my_obj)
