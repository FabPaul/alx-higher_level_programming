#!/usr/bin/python3

def multiple_returns(sentence):

    a = len(sentence)

    if a == 0:
        initial_value = None
    else:
        initial_value = sentence[0]

    return (a, initial_value)
