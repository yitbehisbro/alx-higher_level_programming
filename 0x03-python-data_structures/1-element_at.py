#!/usr/bin/python3
def element_at(my_list, idx):
    return (my_list[idx] if len(my_list) >= idx >= 0 else None)
