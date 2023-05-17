#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''
    uniq_num = set()
    sum_total = 0

    for i in my_list:
        if i not in uniq_num:
            sum_total = i
            uniq_num.add(i)

    return sum_total '''

    new_list = sum(set(my_list))

    return new_list
