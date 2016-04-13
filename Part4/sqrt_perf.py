#!/usr/bin/env python3
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sat Apr  2 21:41:05 2016

"""Different ways to calculate square root and their performance
"""

import timeit

setup = """
import math
l = range(1000)

def for_loop_sqrt(l):
    res = []
    for val in l:
        res.append(math.sqrt(val))
    return res

def list_comp_operator_sqrt(l):
    return [val ** 0.5 for val in l]

def list_comp_math_sqrt(l):
    return [math.sqrt(val) for val in l]

def list_comp_pow_sqrt(l):
    return [pow(val, 0.5) for val in l]

def map_sqrt(l):
    return list(map(math.sqrt, l))

def generator_sqrt(l):
    return list(val ** 0.5 for val in l)
"""

print("Best of 3 round in running for_loop_sqrt 10000 times: ",
      min(timeit.repeat(stmt="for_loop_sqrt(l)", setup=setup,
                        repeat=3, number=10000)))
print("Best of 3 round in running map_sqrt 10000 times: ",
      min(timeit.repeat(stmt="map_sqrt(l)", setup=setup,
                        repeat=3, number=10000)))
print("Best of 3 round in running generator_sqrt 10000 times: ",
      min(timeit.repeat(stmt="generator_sqrt(l)", setup=setup,
                        repeat=3, number=10000)))
print("Best of 3 round in running list_comp_operator_sqrt 10000 times: ",
      min(timeit.repeat(stmt="list_comp_operator_sqrt(l)", setup=setup,
                        repeat=3, number=10000)))
print("Best of 3 round in running list_comp_math_sqrt 10000 times: ",
      min(timeit.repeat(stmt="list_comp_math_sqrt(l)", setup=setup,
                        repeat=3, number=10000)))
print("Best of 3 round in running list_comp_pow_sqrt 10000 times: ",
      min(timeit.repeat(stmt="list_comp_pow_sqrt(l)", setup=setup,
                        repeat=3, number=10000)))
