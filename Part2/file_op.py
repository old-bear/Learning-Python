#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Tue Jul 28 23:55:16 2015
# File: file_op.py
# Description: Basic file operations

f = open("myfile.txt", "w")
f.write("Hello file world!")
f.close()

for line in open("myfile.txt", "r"):
    print(line)
