#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Sat Aug 15 12:42:21 2015
# File: prime.py
# Description: 

def prime(x):
    if x <= 1:
        print "%s is not a natural number" % x
        return False
    
    factor = x // 2;
    while factor > 1:
        if x % factor == 0:
            return True
        factor -= 1
        
    return False

print "prime(%s): %s" % (17, prime(17))
print "prime(%s): %s" % (14, prime(14))
print "prime(%s): %s" % (-2, prime(-2))
print "prime(%s): %s" % (12.0, prime(12.0))
print "prime(%s): %s" % (12.0001, prime(12.0001))
