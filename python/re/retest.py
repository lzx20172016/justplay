#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re

pattern=re.compile(r"\d+")

#m=pattern.match("aaa123bbb456",3,5)
m=pattern.match("aaa123bbb456",3,6)

print m.group()

