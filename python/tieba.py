#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2
import urllib

def loadPage(url,filename):
    """
        hello world
    """
    print "it is downloading"+filename
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE"}
    request=urllib2.Request(url,headers=headers)
    return urllib2.urlopen(request).read()

def writePage(html,filename):
    """
        function:write html into local
        html:response content
    """
    print "it is saving"+filename
    with open(filename,"w")as f:#it is euql with open write close
        f.write(html)
    print "-"*30
def tiebaSpider(fullurl,beginPage,endPage):
    """
        combie all page
        url:tiebaurl the head part
    """
    for page in range(beginPage,endPage+1):
        pn=(page-1)*50
        filename="the"+str(page)+"page.html"
        fullurl=url+"&pn="+str(pn)
#print fullurl
        html=loadPage(fullurl,filename)
#        print html
        writePage(html,filename)
        print "thanks for using"
if __name__ == "__main__":
    kw=raw_input("please input name of tieba:")
    beginPage=int(raw_input("please input the start page:"))
    endPage=int(raw_input("please input the end page:"))
    
    url="http://tieba.baidu.com/f?"
    key=urllib.urlencode({"kw":kw})
    fullurl=url+key
    tiebaSpider(fullurl,beginPage,endPage)


