#!/bin/bash
# Bash script that takes in a URL, sends a request to it and displays the size in bytes
curl -s "$1" | wc -c
