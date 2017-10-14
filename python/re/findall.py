#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re

#pattern=re.compile(r"\d+")
#pattern=re.compile(r"\d?")
#pattern=re.compile(r"\d*")
pattern=re.compile(r"\d+")


#m=pattern.findall("hello 123456 789")
m=pattern.findall("hello123bbb456",1,12)

for i in m:
    print i
print "-----------------------------------"
#pattern=re.compile(r"\d*")
m=pattern.finditer("aaa123bbb456")
for i in m:
    print i.group()
