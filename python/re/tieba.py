#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib
import urllib2
from lxml import etree

def loadPage(url):
    print url
        
    print "it is downloading..."
#   url="http://www.neihan8.com/article/index_"+str(self.page)+".html"
#    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
#   request=urllib2.Request(url,headers=headers)
    request=urllib2.Request(url)
    html=urllib2.urlopen(request).read()
#print html
    content=etree.HTML(html)
    print content
    link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
#link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
    print link_list
    for link in link_list:
        fulllink="http://tieba.baidu.com"+link
#print link
        loadImage(fulllink)

def loadImage(link):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
    request=urllib2.Request(link,headers=headers)
    html=urllib2.urlopen(request).read()
    content=etree.HTML(html)
    link_list=content.xpath('//img[@class="BDE_Image"]/@src')
    for link in link_list:
        writeImage(link)
#       print link
def writeImage(link):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
    request=urllib2.Request(link,headers=headers)
    image=urllib2.urlopen(request).read()
    filename=link[-5:]
    with open(filename,"wb")as f:
        f.write(image)
    print "_"*30

def tiebaSpider(url,beginPage,endPage):
    """
        combie all page
        url:tiebaurl the head part
    """
    for page in range(beginPage,endPage+1):
        pn=(page-1)*50
        fullurl=url+"&pn="+str(pn)
        loadPage(fullurl)
        print "thanks for using"
if __name__ == "__main__":
    kw=raw_input("please input name of tieba:")
    beginPage=int(raw_input("please input the start page:"))
    endPage=int(raw_input("please input the end page:"))
    
    url="http://tieba.baidu.com/f?"
    key=urllib.urlencode({"kw":kw})
    fullurl=url+key
    tiebaSpider(fullurl,beginPage,endPage)
