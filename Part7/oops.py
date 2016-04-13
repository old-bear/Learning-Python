#!/usr/bin/env python3
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sun Apr 10 16:05:32 2016

"""Basic try/except operations
"""

from random import choice

class MyError(Exception): pass
    
def oops():
    excp = choice((IndexError, KeyError, MyError("my exception")))
    raise excp

def doom():
    try:
        oops()
    except IndexError:
        print("Caught IndexError")
    except MyError as me:
        print("Caught", me)
    else:
        print("No error occured")

if __name__ == "__main__":
    doom()
