#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2

#http_handler=urllib2.HTTPHandler()
#increase an argument debuglevel=1 it will open model of debug log
#when excute print send package
http_handler=urllib2.HTTPHandler(debuglevel=1)

#form an object opener
opener=urllib2.build_opener(http_handler)

request=urllib2.Request("http://www.baidu.com/")

response=opener.open(request)
#print response.read()
