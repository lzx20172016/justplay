#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2

#express weather it starts
#proxyswitch=True
proxyswitch=False

#form an object for dealing with handler
httpproxy_handler=urllib2.ProxyHandler({"http":"122.224.227.202:3128"})

#form an object without proxy
nullproxy_handler=urllib2.ProxyHandler({})

if proxyswitch:
    opener=urllib2.build_opener(httpproxy_handler)
else:
    opener=urllib2.build_opener(nullproxy_handler)

#form a global opener,after this all request could use urlopen()
urllib2.install_opener(opener)

request=urllib2.Request("http://www.baidu.com/")
response=urllib2.urlopen(request)

print response.read()

