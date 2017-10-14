#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2
import json
from lxml import etree
url="https://www.qiushibaike.com/8hr/page/1/"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

request=urllib2.Request(url,headers=headers)

html=urllib2.urlopen(request).read()

text=etree.HTML(html)

node_list=text.xpath('//div[contains(@id,"qiushi_tag")]')
items={}

for node in node_list:
    username=node.xpath('./div/a/@title')[0]

    image=node.xpath('.//div[@class="thumb"]//@src')#[0]
    
    content=node.xpath('.//div[@class="content"]/span')[0].text

    zan=node.xpath('.//i')[0].text

    comments=node.xpath('.//i')[1].text
    
    items={"username":username,"image":image,"content":content,"zan":zan,"comments":comments}
    print username
    with open("qiushi.json","a") as f:
        f.write(json.dumps(items,ensure_ascii=False).encode("utf-8")+"\n")


