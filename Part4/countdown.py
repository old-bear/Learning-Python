#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sat Apr  2 22:18:50 2016

"""Print count down message
"""

def countdown(x):
    if x <= 0:
        print("stop")
    else:
        print(x, end=" ")
        countdown(x - 1)

def countdown_generator(x):
    for val in range(x, 0, -1):
        print(val, end=" ")
        yield val
    print("stop")

print("Print count down recursively: ", end='')
countdown(5)
print('-' * 60)
print("Print count down using generator: ", end='')
list(countdown_generator(5))
