#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re

pattern=re.compile(r"([a-z]+) ([a-z]+)",re.I)

#m=pattern.match("aaa123bbb456",3,5)
m=pattern.match("Hello world hello Python")

print m.group(2)
print m.span(0)

