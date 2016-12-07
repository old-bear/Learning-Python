#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sat Apr  2 21:02:26 2016

"""Tools to copy and add dicts
"""

def copyDict(adict):
    return {key: adict[key] for key in adict}

d1 = {1: 'a', 2: 'b'}
d2 = copyDict(d1)
print("d1 =", d1, ", now copy d1 to d2")
d1[1] = 'aa'
print("After changes d1 =", d1, ", but d2 =", d2)

def addDict(dict1, dict2):
    ret = copyDict(dict1)
    for key in dict2:
        if key not in ret:
            ret[key] = dict2[key]
        else:
            ret[key] += dict2[key]
    return ret

del d2[2]
d2[3] = 'c'
print("-" * 60)
print("Addition for dict:", d1, "+", d2, "=", addDict(d1, d2))
