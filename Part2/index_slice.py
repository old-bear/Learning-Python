#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Tue Jul 28 22:43:22 2015
# File: index_slice.py
# Description: Experiment for indexing, slicing, and del

L = [0, 1, 2, 3]
print("L = %s" % L)

# list index out of range
# L[100]

# return the whole list when slicing out of range
print("L[-100:100] = %s" % L[-100:100])

# return empty list when slicing in reverse
print("L[100:-100] = %s" % L[100:-100])

# append at the end of L
L[100:-100] = ['?']
print("\nAfter L[100:-100] = ['?'], L = %s" % L)

# insert at the beginning of L
L[-100:-99] = ['#']
print("After L[-100:-99] = ['#'], L = %s" % L)

# append at the end of L
L[100:101] = ['$']
print("After L[100:101] = ['$'], L = %s" % L)

# assignment by index
L[2] = []
print("\nAfter L[2] = [], L = %s" % L)

# remove L[2]
L[2:3] = []
print("After L[2:3] = [], L = %s" % L)

# can only assign an iterable
# L[1:2] = 1

# remove all but the first
del L[1:]
print("\nAfter del L[1:], L = %s" % L)
