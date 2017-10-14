#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re

mm="1234"

#pattern=re.compile(r"[\s\d\\;]+")
pattern=re.compile("[\s\d\\;]+")

#m=pattern.split("a bb\aa;mm; a      a")
m=pattern.split(r"a bb\aa;m1m; a   123   a")
print m

