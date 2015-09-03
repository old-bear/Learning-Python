#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Mon Aug 10 23:26:12 2015
# File: loop_simplify.py
# Description: Simplify the following loop logic
#
# L = [1, 2, 4, 8, 16, 32, 64]
# X = 5
# 
# found = False
# i = 0
# while not found and i < len(L):
#     if 2 ** X == L[i]:
#         found = True
#     else
#         i = i+1
#
# if found:
#     print('at index', i)
# else:
#     print(X, 'not found')

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

# Use `for' loop with `else' to simplify 
for i in range(len(L)):
    if 2 ** X == L[i]:
        print 'at index', i
        break
else:
    print X, 'not found'

# Use `in' test
if 2 ** X in L:
    print 'at index', L.index(2 ** X)
else:
    print X, 'not found'
