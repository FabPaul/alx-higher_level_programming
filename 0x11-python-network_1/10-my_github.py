#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    req = requests.get(url, auth=auth).json()
    print(req.get("id"))
