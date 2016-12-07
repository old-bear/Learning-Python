#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Thu Apr  7 22:27:24 2016

"""Extension for builtin list
"""

class MyList(list):
    # Just inherit from list to acquire all the methods of list
    # such as operators, append, sort, constructors(through list/MyList)
    pass

class MyListSub(MyList):
    total_add_count = 0
    
    def __add__(self, y):
        print("Invoking operator+ of MyListSub")
        if "add_count" in self.__dict__:
            self.add_count += 1
        else:
            self.add_count = 1
        MyListSub.total_add_count += 1
        return MyList.__add__(self, y)

    __radd__ = __add__

    @staticmethod
    def add_count():
        return MyListSub.total_add_count

    
if __name__ == "__main__":
    x = [1, 2, 3]
    mlist = MyList(x)
    print("-" * 20, "Test for MyList", "-" * 20)
    print("mlist = %s" % mlist)
    print("mlist[1] = %s" % mlist[1])
    print("mlist[:] = %s" % mlist[:])
    print("mlist + [4] = %s" % (mlist + [4]))
    print("mlist + MyList([4]) = %s" % (mlist + MyList([4])))
    mlist.append(-1)
    print("mlist.append(-1) => %s" % mlist)
    mlist.sort()
    print("mlist.sort() => %s" % mlist)
    print("[val for val in mlist] => %s\n" % [val for val in mlist])

    print("-" * 20, "Test for MyListSub", "-" * 20)
    mlistsub = MyListSub(x)
    print("mlistsub = %s" % mlistsub)
    print("mlistsub + [4] = %s" % (mlistsub + [4]))
    print("[4] + mlistsub = %s\n" % ([4] + mlistsub))
    mlistsub2 = MyListSub(x + [11])
    print("mlistsub2 = %s" % mlistsub2)
    print("mlistsub2 + [4] = %s\n" % (mlistsub2 + [4]))
    print("Summary: \noperator+ called on mlistsub: %d times\n"
          "operator+ called on mlistsub2: %d times\n"\
          "operator+ called on MyListSub: %d times in total"
          % (mlistsub.add_count, mlistsub2.add_count, MyListSub.add_count()))
