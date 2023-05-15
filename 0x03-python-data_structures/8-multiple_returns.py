#!/usr/bin/python3

def multiple_returns(sentence):

    a = len(sentence)
    initial_value = sentence[0]

    if a == 0:
        initial_value = None

    return (a, initial_value)
