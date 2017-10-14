#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2
import urllib

#url="https://www.baidu.com/"
url="https://www.12306.com/"

request=urllib2.Request(url)

response=urllib2.urlopen(request)

print response.read()
