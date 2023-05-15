#!/usr/bin/python3

def multiple_returns(sentence):

    a = len(sentence)
    initial_value = sentence[0]

    if a == 0:
        return (0, None)

    else:
        return (a, initial_value)
