#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sat Apr  2 22:22:09 2016

"""Different ways to calculator factorials and their performance
"""

import timeit

setup = """
import math
import operator
from functools import reduce

def recursive_fact(n):
    return n * recursive_fact(n - 1) if n > 1 else 1

def reduce_fact(n):
    return reduce(operator.mul, range(n, 1, -1))

def loop_fact(n):
    ret = 1
    for val in range(n, 1, -1):
        ret *= val
    return val
                  
def math_fact(n):
    return math.factorial(n)
"""

print("Best of 3 in running recursive_fact(500) for 1000 times: ",
      min(timeit.repeat(stmt="recursive_fact(500)", setup=setup,
                        repeat=3, number=1000)))
print("Best of 3 in running reduce_fact(500) for 1000 times: ",
      min(timeit.repeat(stmt="reduce_fact(500)", setup=setup,
                        repeat=3, number=1000)))
print("Best of 3 in running loop_fact(500) for 1000 times: ",
      min(timeit.repeat(stmt="loop_fact(500)", setup=setup,
                        repeat=3, number=1000)))
print("Best of 3 in running math_fact(500) for 1000 times: ",
      min(timeit.repeat(stmt="math_fact(500)", setup=setup,
                        repeat=3, number=1000)))
