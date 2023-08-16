#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for ls in set(my_list):
        add += ls
    return add
