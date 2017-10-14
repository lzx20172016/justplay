#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib
import urllib2
import cookielib

cookie=cookielib.CookieJar()

cookie_handler=urllib2.HTTPCookieProcessor(cookie)

opener=urllib2.build_opener(cookie_handler)

opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")]


url="http://www.renren.com/PLogin.do"
#url="http://www.renren.com/SysHome.do"

data={"email":"18815569470","password":"lzx19940428"}

data=urllib.urlencode(data)

request=urllib2.Request(url,data=data)
response=opener.open(request)
print response.read()


response_li=opener.open("http://www.renren.com/872201594/profile")

print response_li.read()



