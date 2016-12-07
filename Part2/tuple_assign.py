#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sun Mar 27 00:04:14 2016

"""Experiment for tuple assignment
"""

X = "spam"
Y = "eggs"
print("(X, Y) = (%s, %s)" % (X, Y))

# swap the 2 objects X, Y pointed to
# actually it's rather object assignment statements
# than tuple assignment since tuples are immutable
(X, Y) = (Y, X)
print("After (X, Y) = (Y, X), (X, Y) = (%s, %s)" % (X, Y))
