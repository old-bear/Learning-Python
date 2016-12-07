#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sun Mar 27 14:14:36 2016

"""Print dictionary in sorted order
"""

person = {"name": "Bear", "age": 26,
          "jobs": ["engineer"], "email": "jrjbear@gmail.com"}

print("Print dictionay directly: ", person)
print("After sorted: {", end='')
for key in sorted(person):
    print("%s: %s, " % (key, person[key]), end='')
print("\b\b}")
