#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Mon Aug 31 22:20:20 2015
# File: adder.py
# Description: 

class Adder:
    def __init__(self, start):
        self.data = start

    def add(self, y):
        print "Not Implemented"

    def __add__(self, y):
        return self.add(y)

    __radd__ = __add__


class ListAdder(Adder):
    def add(self, y):
        return self.data + y

class DictAdder(Adder):
    def add(self, y):
        tmp = self.data.copy()
        tmp.update(y)
        return tmp


if __name__ == '__main__':
    x = Adder(3)
    x.add(4)                    # Not Implemented

    x = ListAdder([3])
    print "ListAdder([3]) + [4] = %s" % (x + [4])

    x = DictAdder({'a':3})
    print "DictAdder({'a':3}) + {'a':4} = %s" % (x + {'a':4})
