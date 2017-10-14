#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2

test="admin"

password="123456"

webserver="192.168.0.105:80"
passwordMgr=urllib2.HTTPPasswordMgrWithDefaultRealm()

#add acount information
passwordMgr.add_password(None,webserver,test,password)

httpauth_handler=urllib2.HTTPBasicAuthHandler(passwordMgr)

opener=urllib2.build_opener(httpauth_handler)

request=urllib2.Request("http://"+webserver)

response=opener.open(request)
#response=urllib2.urlopen(request)
print response.read()
