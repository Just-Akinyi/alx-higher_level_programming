#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0 and idx > my_list.len):
        return None
    return my_list[idx]
