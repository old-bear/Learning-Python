#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Thu Apr  7 22:02:29 2016

"""Interface of add and its implementataions on list/dict 
"""

class Adder:
    def __init__(self, start=[]):
        if isinstance(start, Adder):
            self.data = start.data
        else:
            self.data = start

    def add(self, y):
        """Returns the result whose type=type(y)
        """ 
        print("Not Implemented")

    def __add__(self, y):
        """Returns a new object of Adder as the result
        """
        return self.__class__(self.add(y))

    __radd__ = __add__

    def __repr__(self):
        return "%s<%s>" % (self.__class__.__name__, self.data)

    
class ListAdder(Adder):
    def add(self, y):
        return self.data + y

    
class DictAdder(Adder):
    def add(self, y):
        tmp = self.data.copy()
        tmp.update(y)
        return tmp


if __name__ == "__main__":
    x = Adder(3)
    print("%s.add(4): " % x, end='')
    x.add(4)                    # Not Implemented

    y = ListAdder([3])
    print("%s + [4] = %s" % (y, y + [4]))

    z = DictAdder({'a': 3})
    print("{'a': 4} + %s = %s" % (z, {'a': 4} + z))
