#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re
import urllib2

class Spider:
    def __init__(self):
        self.page=3
        self.switch=True

    def loadPage(self):
        
        print "it is downloading..."
        url="http://www.neihan8.com/article/index_"+str(self.page)+".html"
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
        request=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(request)
        html=response.read()
#    print html
        pattern=re.compile('<div\sclass="desc">(.*?)</div>',re.S)
        content_list=pattern.findall(html)
        
        self.dealPage(content_list)

    def dealPage(self,content_list):
        
        for item in content_list:
            item=item.replace("<p>","").replace("</p>","").replace("<br>","")
            item=item+"\n"
            item=item+"\n"
            self.writePage(item)
#    print item
            print
    def writePage(self,item):
        print "it is writing..."
        with open("duanzi.txt","a")as f:
            f.write(item)
    def startWork(self):

        while self.switch:
            self.loadPage()
            command=raw_input("if you want to continue to spider,please input enter")
            if command=="quit":
                self.switch=False
            self.page+=1
        print "thank you for using!"
if __name__=="__main__":
    duanziSpider=Spider()
    duanziSpider.startWork()
#  duanziSpider.loadPage()







