#!/usr/bin/env python3
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sun Mar 27 14:24:29 2016

"""Simplify the following loop logic
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

found = False
i = 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else
        i = i+1

if found:
    print("at index", i)
else:
    print(X, "not found")
"""

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

# Use `for' loop with `else' to simplify
for (index, value) in enumerate(L):
    if 2 ** X == value:
        print("at index", index)
        break
else:
    print(X, "not found")

# Use `in' test
if 2 ** X in L:
    print("at index", L.index(2 ** X))
else:
    print(X, "not found")
