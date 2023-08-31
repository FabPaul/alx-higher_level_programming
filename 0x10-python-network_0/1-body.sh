#!/bin/bash
# Bash script that takes in a URL, sends a GET request to it and display it's body
curl -sL -X GET "$1"
