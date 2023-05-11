#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    plus = 0

    for i in range(1, len(sys.argv)):
        plus += int(sys.argv[i])

    print(plus)
