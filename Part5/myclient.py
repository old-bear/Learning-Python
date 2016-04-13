#!/usr/bin/env python3
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Sun Apr  3 23:35:14 2016

"""Client script that imports mymod
"""

from mymod import *

test("myclient.py")
print("After from mymod import *, dir():", dir())
print('-' * 60)

import mypkg.mymod as pkgmod
pkgmod.test("myclient.py")
print("After import mypkg.mymod as pkgmod, dir():", dir())
