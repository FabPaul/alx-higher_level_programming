#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8). """

import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        response = urlopen(req)
    except HTTPError as e:
        if hasttr(e, 