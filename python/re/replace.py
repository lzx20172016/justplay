#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re

re.compile(r"(\w+) (\w+)")

pattern=re.compile(r"(\w+) (\w+)")

str="hello 123,hello 456"
#m=pattern.sub("hello world",str)
#m=pattern.sub(r"\1 \2",str)
m=pattern.sub(r"\2 \1",str)

print m


pattern=re.compile(r"\d+")
str="abc123abc456"
m=pattern.sub("mmmmmmm",str)
print m
