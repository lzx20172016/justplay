#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2
import urllib

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule "


headers={
"Host":"fanyi.youdao.com",
"Accept":"application/json, text/javascript, */*; q=0.01",
"X-Requested-With":"XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
}

key=raw_input("please input words that you want to translate:")

formdata={
    "type":"AUTO",
    "i":key,
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_REALTIME",
    "typoResult":"true"
}

data=urllib.urlencode(formdata)

request=urllib2.Request(url,data=data,headers=headers)

print urllib2.urlopen(request).read()


