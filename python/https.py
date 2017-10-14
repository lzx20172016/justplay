#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2
import urllib

import ssl

context=ssl._create_unverified_context()
url="http://www.12306.cn/mormhweb/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE"}

request=urllib2.Request(url,headers=headers)

response=urllib2.urlopen(request,context=context)

print response.read()
