#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Mon Aug 10 23:05:34 2015
# File: sort_dict.py
# Description: Print dictionary in sorted order

person = { 'name' : 'Bear', 'age' : 26, 'jobs' : ['engineer'],
           'email' : 'jrjbear@gmail.com' }

print "Print dictionay directly:", person
print "After sorted: {",
for key in sorted(person):
    print key, "=>", person[key], ",",
print "\b\b}"
