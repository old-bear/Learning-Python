#!/usr/bin/env python3
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sun Apr  3 23:32:44 2016

"""Count characters/lines of a given file
"""

from functools import reduce

def countLines(name):
    return reduce(lambda x, y: x + 1, open(name), 0)

def countChars(name):
    return reduce(lambda x, y: x + len(y), open(name), 0)

def test(name):
    print("Total lines in %s: %s" % (name, countLines(name)))
    print("Total characters in %s: %s" % (name, countChars(name)))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        for f in sys.argv[1:]:
            print('*' * 60)
            test(f)
    else:
        test("mymod.py")
            
