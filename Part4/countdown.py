#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Sat Aug 15 15:12:49 2015
# File: countdown.py
# Description: 

def countdown(x):
    if x <= 0:
        print "stop"
    else:
        print x
        countdown(x - 1)

def countdown_gen(x):
    for val in range(x, 0, -1):
        print val
        yield val
    print "stop"
        
countdown(5)
print '-' * 60
list(countdown_gen(5))
