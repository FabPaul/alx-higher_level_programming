#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    result = []

    for i in range (0, list_length):
        try:
            elem1 = my_list_1[i]
            elem2 = my_list_2[i]
            division = elem1 / elem2

        except TypeError:
            print('Wrong type')
            division = 0

        except ZeroDivisionError:
            print('division by 0')
            division = 0

        except IndexError:
            print('out of range')
            division = 0

        finally:
            result.append(division)

    return result