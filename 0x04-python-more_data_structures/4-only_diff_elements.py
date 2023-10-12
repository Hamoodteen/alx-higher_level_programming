#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common = set()
    for i in set_1:
        for j in set_2:
            if i not in set_2 and j not in set_1:
                common.add(i)
                common.add(j)
    return common
