#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sun Mar 27 00:13:45 2016

"""Basic file operations
"""

f = open("myfile.txt", "w")
f.write("Hello file world!")
f.close()

for line in open("myfile.txt", "r"):
    print(line)
