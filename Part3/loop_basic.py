#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Mon Aug 10 22:39:09 2015
# File: loop_basic.py
# Description: Exercises for basic loop coding

test_str = 'hello world'

print "'%s' to ASCII code: [" % test_str,
total = 0
for ch in test_str:
    total += ord(ch)
    print ord(ch),
print "], sum = %s" % total

l1 = map(ord, test_str)
l2 = [ord(ch) for ch in test_str]
print "Or use map(ord, '%s'): %s" % (test_str, l1)
print "Or use [ord(ch) for ch in '%s']: %s" % (test_str, l2)
