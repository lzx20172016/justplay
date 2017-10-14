#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2
import urllib

url="http://www.baidu.com/s"
headers={"User-Agent":"Mozilla.."}

keyword=raw_input("please input string you want to search:")

wd={"wd":keyword}
wd=urllib.urlencode(wd)

fullurl=url+"?"+wd
print fullurl

request=urllib2.Request(fullurl,headers=headers)

response=urllib2.urlopen(request)

#print response.read()

