#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2
import urllib

url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule "


headers={
"Host":"fanyi.youdao.com",
"Origin":"http://fanyi.youdao.com",
"Accept":"application/json, text/javascript, */*; q=0.01",
"X-Requested-With":"XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Referer":"http://fanyi.youdao.com/?keyfrom=dict2.index",
"Cookie":"OUTFOX_SEARCH_USER_ID=-232533080@10.169.0.84; JSESSIONID=aaa2AreO0e1IQ5MMGSX7v; OUTFOX_SEARCH_USER_ID_NCOO=113695299.66812155; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcdPxzsiz10j-Hl02X7v; ___rl__test__cookies=1507296246875"

}

key=raw_input("please input words that you want to translate:")

formdata={
    "i":key,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1507293604237",
    "sign":"97eea4ec05771c8fd804b1a6ca47d623",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"true"
}

data=urllib.urlencode(formdata)

request=urllib2.Request(url,data=data,headers=headers)

print urllib2.urlopen(request).read()


