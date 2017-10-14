#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2
import json
import jsonpath
#from jsonpath_rw import jsonpath,parse

url="http://www.lagou.com/lbs/getAllCitySearchLabels.json"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
request=urllib2.Request(url,headers=headers)

response=urllib2.urlopen(request)

html=response.read()

unicodestr=json.loads(html)

#python form list
city_list=jsonpath.jsonpath(unicodestr,"$..name")

for item in city_list:
    print item

#array=json.dumps(city_list)
array=json.dumps(city_list,ensure_ascii=False)

with open("lagoucity.json","w") as f:
    f.write(array.encode("utf-8"))




