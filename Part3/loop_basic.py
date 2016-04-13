#!/usr/bin/env python3
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sun Mar 27 14:05:39 2016

"""Exercises for basic loop coding
"""

test_str = "hello world"
print("'%s' to ASCII code: [" % test_str, end='')

total = 0
for ch in test_str:
    if total > 0: print(' ', end='')
    print(ord(ch), end='')
    total += ord(ch)
print("], sum = %s" % total)

l1 = list(map(ord, test_str))
l2 = [ord(ch) for ch in test_str]
print("Use map function: %s" % l1)
print("Use list comprehension: %s" % l2)
