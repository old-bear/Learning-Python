#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Sat Aug 15 10:39:43 2015
# File: dict_tools.py
# Description: 

def copyDict(adict):
    return { key:adict[key] for key in adict }

d1 = { 1:'a', 2:'b' }
d2 = copyDict(d1)
print "d1 = %s, copy d2 = d1" % d1
d2[1] = 'aa'
print "After changes on d[1], d2 = %s" % d2

def addDict(dict1, dict2):
    ret = copyDict(dict1)
    for key in dict2:
        if key not in ret:
            ret[key] = dict2[key]
    return ret

d2[3] = 'c'
print "-" * 60
print "Add d2[3] and then d1 unions d2 = %s" % addDict(d1, d2)
