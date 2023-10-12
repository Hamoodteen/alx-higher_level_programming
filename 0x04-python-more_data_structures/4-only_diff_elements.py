#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common = set()
    if len(set_1) == 0:
        return set_2
    if len(set_2) == 0:
        return set_1
    for i in set_1:
        for j in set_2:
            if i not in set_2 and j not in set_1:
                common.add(i)
                common.add(j)
    return common
