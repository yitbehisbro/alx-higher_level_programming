#!/usr/bin/python3
def element_at(my_list, idx):
    if idx <= len(my_list) and idx >= 0:
        index_at = my_list[idx]
        return index_at
    else:
        return None
