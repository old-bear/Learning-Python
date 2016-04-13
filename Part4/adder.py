#!/usr/bin/env python3
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sat Apr  2 20:45:16 2016

"""Functions return the sum of all the arguments
"""

from functools import reduce
import operator

def list_adder(*args):
    return reduce(operator.add, args)

print("list_adder(1, 2, 3) =", list_adder(1, 2, 3))
print("list_adder('a', 'b', 'c') =", list_adder('a', 'b', 'c'))
print("list_adder(*'asdf') =", list_adder(*"asdf"))

# `+' not supported between dicts
# print list_adder({1: 'a'}, {2: 'b'})

# `+' not supported between string and integer
# print list_adder('a', 1)

# Raise exception without operands
# print list_adder()

print('-' * 60)

def dict_adder(**args):
    values = list(args.values())
    # Intentionally raise exception when `args' is empty
    sum = values[0]
    for val in values[1:]:
        sum += val
    return sum

print("dict_adder(a=1, b=2, c=3) =", dict_adder(a=1, b=2, c=3))
print("dict_adder(a='a', b='b', c='c') =", dict_adder(a='a', b='b', c='c'))
print("dict_adder(**{'a': 1, 'b': 2, 'c': 3}) =",
       dict_adder(**{'a': 1, 'b': 2, 'c': 3}))

# `+' not supported between string and integer
# print dict_adder(a=1, b='2')

# Raise exception without operands
# print dict_adder()
