#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Tue Jul 28 23:32:39 2015
# File: tuple_assign.py
# Description: Experiment for tuple assignment

X = 'spam'
Y = 'eggs'
print("(X, Y) = (%s, %s)" % (X, Y))

# swap the 2 objects X, Y pointed to
# actually it's rather assignment statements than
# tuple assignment since tuples are immutable
(X, Y) = (Y, X)
print("After (X, Y) = (Y, X), (X, Y) = (%s, %s)" % (X, Y))
