#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Mon Aug 31 23:54:05 2015
# File: attrs.py
# Description: 

class Attrs:
    def __getattr__(self, name):
        print "Fetch attribute=%s" % name

    def __setattr__(self, name, value):
        print "Assign value=%s to attribute=%s" % (value, name)

def CatchTypeError(func):
    try:
        func()
    except TypeError:
        pass                    # Expected
        
if __name__ == '__main__':
    a = Attrs();
    a.x
    a.y = 4
    CatchTypeError(lambda: a + 3)
    CatchTypeError(lambda: a[4])
    
