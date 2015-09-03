#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Sat Aug 15 12:58:24 2015
# File: sqrt_perf.py
# Description: 

import math
import timeit

mylist = range(1000)

def math_sqrt(l):
    return [math.sqrt(val) for val in l]

def operator_sqrt(l):
    return [val ** 0.5 for val in l]

def builtin_pow(l):
    return [pow(val, 0.5) for val in l]

print ("Best of 3 round in running math.sqrt for 10000 times: %s"
       % min(timeit.repeat(stmt=lambda: math_sqrt(mylist),
                           repeat=3, number=10000)))
print ("Best of 3 round in running ** for 10000 times: %s"
       % min(timeit.repeat(stmt=lambda: operator_sqrt(mylist),
                           repeat=3, number=10000)))
print ("Best of 3 round in running pow for 10000 times: %s"
       % min(timeit.repeat(stmt=lambda: builtin_pow(mylist),
                           repeat=3, number=10000)))
