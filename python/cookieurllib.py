#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2


headers={
"Host":"zhibo.renren.com",
"Connection":"keep-alive",
#"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-CN,zh;q=0.8",
"Cookie":"anonymid=j8gnnpvb-7zsn1; depovince=GW; _r01_=1; springskin=set; jebe_key=904a1ff2-25a8-410a-9ae7-25d8ee21fa6b%7Cc99583126a31f2f3084dcc04a97a576d%7C1507340597551%7C1%7C1507340595706; _de=C9EDF44BA583193F8E67F0A45D7FB76A; p=80f65f3b4271d5453807c5582be5d4543; ap=944414883; ln_uact=18815569470; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; wp_fold=0"
}
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
