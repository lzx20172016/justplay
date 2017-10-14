#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re

pattern=re.compile(r"\d+")

#m=pattern.search(r"aaa123bb546")
#m=pattern.search(r"aaa123bb546",2,5)
m=pattern.search("aaa 123 546")

#m=pattern.match("aaa123bbb456",3,5)
#m=pattern.match("aaa123bbb456",3,6)

print m.group()
print m.span()

