#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return 0

    value = sum(score * weight for score, weight in my_list)
    value2 = sum(weight for score, weight in my_list)

    return value / value2
