#!/usr/bin/env python3
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Thu Apr  7 23:33:20 2016

"""A new set which supports doing union/intersection multiple objects
simultaneously, though this can't be called by operator expressions
(only 2 operands allowed)
"""

class Set:
    def __init__(self, value = []):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):           return len(self.data)
    def __getitem__(self, key):  return self.data[key]
    def __and__(self, other):    return self.intersect(other)
    def __or__(self, other):     return self.union(other)
    def __repr__(self):          return 'Set:' + repr(self.data)
    def __iter__(self):          return iter(self.data)

    
class MySet(Set):
    def intersect(self, *others):
        res = []
        for x in self.data:
            for other_list in others:
                if not x in other_list:
                    break
            else:
                res.append(x)
        return Set(res)
        
    def union(self, *others):
        res = self.data[:]
        for other_list in others:
            for x in other_list:
                if not x in res:
                    res.append(x)
        return Set(res)

    def append(self, other):
        if not other in self.data:
            self.data.append(other)
            
    __add__ = Set.__or__
    __radd__ = __add__
        
    
if __name__ == "__main__":
    x = Set([1, 2, 3])
    y = Set([3, 4, 5])
    print("-" * 20, "Test for Set", "-" * 20)
    print("%s & %s = %s" % (x, y, x & y))
    print("%s | %s = %s" % (x, y, x | y))

    s = Set("hello")
    print("s = %s, s[2] = %s" % (s, s[2]))
    print("Iterating %s: " % s, end='')
    for c in s:
        print(c, end='')
    print("\n%s & %s = %s\n" % (s, "world", s & "world"))

    print("-" * 20, "Test for MySet", "-" * 20)
    xx = MySet("hello")
    yy = MySet("world")
    ss = list("love")
    print("Union of <%s>, <%s>, <%s> = %s" % (xx, yy, ss, xx.union(yy, ss)))
    print("Intersection of <%s>, <%s>, <%s> = %s"
          % (xx, yy, ss, xx.intersect(yy, ss)))
    print("%s + %s = %s" % (xx, yy, xx + yy))
    print("%s.append('z') => " % xx, end='')
    xx.append('z')
    print(xx)
