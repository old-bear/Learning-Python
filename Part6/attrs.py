#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Thu Apr  7 23:12:01 2016

"""A class which trace all its attribute qualifications,
though operators can't be intercepted in py3
"""

class Attrs:
    def __getattribute__(self, name):
        print("Fetch attribute=%s" % name)
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        print("Assign value=%s to attribute=%s" % (value, name))
        return object.__setattr__(self, name, value)
        

def CatchTypeError(func):
    try:
        func()
    except TypeError as e:
        print("Caught TypeError:", e)

    
if __name__ == "__main__":
    a = Attrs();
    print("a =", a)
    print("a.x = 4 => ", end='')
    a.x = 4
    print("a.x += 4 => ")
    a.x += 4

    print("\nHowever, builtin operations can' be intercepted")
    print("a + 3 => ", end='')
    CatchTypeError(lambda: a + 3)
    print("a[4] => ", end='')
    CatchTypeError(lambda: a[4])    
