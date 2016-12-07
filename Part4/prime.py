#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sat Apr  2 21:29:54 2016

"""Tell whether a number is prime
"""

def prime(x):
    if x <= 1:
        # Prime MUST be a natural number
        return False
    
    factor = int(x ** 0.5);
    while factor > 1:
        if x % factor == 0:
            return True
        factor -= 1
    return False

print("prime(%s): %s" % (17, prime(17)))
print("prime(%s): %s" % (14, prime(14)))
print("prime(%s): %s" % (-2, prime(-2)))
print("prime(%s): %s" % (12.0, prime(12.0)))
print("prime(%s): %s" % (12.0001, prime(12.0001)))
print("prime(%s): %s" % (123418917983, prime(123418917983)))
