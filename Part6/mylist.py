#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Mon Aug 31 23:04:07 2015
# File: mylist.py
# Description: 

class MyList(list): pass

class MyListSub(MyList):
    counter = 0
    def __add__(self, y):
        print "Invoking operator + of MyListSub"
        MyListSub.counter += 1
        return MyList.__add__(self, y)

    __radd__ = __add__

    @staticmethod
    def AdditionCount():
        return MyListSub.counter

if __name__ == '__main__':
    x = [1, 2, 3]
    mlist = MyList(x)
    print "-" * 20, "Test for MyList", "-" * 20
    print "mlist = %s" % mlist
    print "mlist[1] = %s" % mlist[1]
    print "mlist[:] = %s" % mlist[:]
    print "mlist + [4] = %s" % (mlist + [4])
    print "mlist + MyList([4]) = %s" % (mlist + MyList([4]))
    mlist.append(-1)
    print "mlist.append(-1) => %s" % mlist
    mlist.sort()
    print "mlist.sort() => %s" % mlist
    print "[val for val in mlist] => %s\n" % [val for val in mlist]

    print "-" * 20, "Test for MyListSub", "-" * 20
    mlistsub = MyListSub(x)
    print "mlistsub = %s" % mlistsub
    print "mlistsub + [4] = %s" % (mlistsub + [4])
    print "[4] + mlistsub = %s" % ([4] + mlistsub)
    print "We've called operator + of MyListSub for %d times" % (
        MyListSub.AdditionCount())
