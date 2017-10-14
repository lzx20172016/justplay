#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2
import urllib

url="https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action="
#url="https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7"
#url="https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action="
headers={"User-Agent":"Mozilla.."}


formdata={
#"type":"24",
#"interval_id":"100:90",
#"action":"",  
"start":"40",
"limit":"20"
}

data=urllib.urlencode(formdata)

request=urllib2.Request(url,data=data,headers=headers)

response=urllib2.urlopen(request)

print response.read()
