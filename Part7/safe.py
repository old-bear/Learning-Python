#!/usr/bin/env python3
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sun Apr 10 16:24:08 2016

"""Wraps a function to catch all its exceptions and prints them out
"""

import sys
import traceback
from oops import oops

def safe(func, *pargs, **kargs):
    try:
        func(*pargs, **kargs)
    except:
        traceback.print_exc()
        print("Caught %s: %s" % sys.exc_info()[:2])

if __name__ == "__main__":
    safe(oops)
