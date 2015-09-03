#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Sat Aug 15 15:30:23 2015
# File: factorial.py
# Description: 

import math
import timeit

def recursive_fact(n):
    return n * recursive_fact(n - 1) if n > 1 else 1

def reduce_fact(n):
    return reduce(lambda x, y: x * y, range(n, 1, -1))

def loop_fact(n):
    ret = 1
    for val in range(n, 1, -1):
        ret *= val
    return val
                  
def math_fact(n):
    return math.factorial(n)

print ("Best of 3 in running recursive_fact(500) for 1000 times: %s"
       % min(timeit.repeat(stmt=lambda: recursive_fact(500), number=1000)))
print ("Best of 3 in running reduce_fact(500) for 1000 times: %s"
       % min(timeit.repeat(stmt=lambda: reduce_fact(500), number=1000)))
print ("Best of 3 in running loop_fact(500) for 1000 times: %s"
       % min(timeit.repeat(stmt=lambda: loop_fact(500), number=1000)))
print ("Best of 3 in running math_fact(500) for 1000 times: %s"
       % min(timeit.repeat(stmt=lambda: math_fact(500), number=1000)))
