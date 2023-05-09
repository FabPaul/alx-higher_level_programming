#!/usr/bin/python3
def uppercase(str):
    val = ''
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            val += chr(ord(i) - 32)
        else:
            val += i
    print('{}' .format(val), end='')
