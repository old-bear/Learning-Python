#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Thu Aug 13 23:55:13 2015
# File: adder.py
# Description: 

def list_adder(*args):
    # Intentionally raise exception when `args' is empty
    sum = args[0]
    for val in args[1:]:
        sum += val
    return sum

print 'list_adder(1, 2, 3) = %s' % list_adder(1, 2, 3)
print "list_adder('a', 'b', 'c') = %s" % list_adder('a', 'b', 'c')
print "list_adder(*'asdf') = %s" % list_adder(*'asdf')

# `+' not supported between dicts
# print list_adder({1:'a'}, {2:'b'})

# `+' not supported between string and integer
# print list_adder('a', 1)

# Raise exception without operands
# print list_adder()

print '-' * 60

def dict_adder(**args):
    values = args.values()
    # Intentionally raise exception when `args' is empty
    sum = values[0]
    for val in values[1:]:
        sum += val
    return sum

print 'dict_adder(a=1, b=2, c=3) = %s' % dict_adder(a=1, b=2, c=3)
print "dict_adder(a='a', b='b', c='c') = %s" % dict_adder(a='a', b='b', c='c')
print ("dict_adder(**{'a':1, 'b':2, 'c':3}) = %s"
       % dict_adder(**{'a':1, 'b':2, 'c':3}))

# `+' not supported between string and integer
# print dict_adder(a=1, b='2')

# Raise exception without operands
# print dict_adder()
