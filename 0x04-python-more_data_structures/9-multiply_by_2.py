#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        n_dic = a_dictionary.copy()
        for i in list(n_dic.keys()):
            n_dic[i] *= 2
        return n_dic
