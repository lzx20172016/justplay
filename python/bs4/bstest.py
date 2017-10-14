#!/usr/bin/python
# _*_ coding:utf-8 _*_

from bs4 import BeautifulSoup
import requests
import time


def captcha(captcha_data):
    with open("/home/lzxice/Desktop/captcha.jpg","wb")as f:
        f.write(captcha_data)
    text=raw_input("please input check code:")
    return text

def zhihuLogin():
#form a session object
    sess=requests.Session()

    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

    html=sess.get("https://www.zhihu.com/#signin",headers=headers).text
    bs=BeautifulSoup(html,"lxml")
    

    _xsrf=bs.find("input",attrs={"name":"_xsrf"}).get("value")
    
    captcha_url="https://www.zhihu.com/captcha.gif?r=%d&type=login"%(time.time()*1000)
    captcha_data=sess.get(captcha_url,headers=headers).content
    text=captcha(captcha_data)
#print captcha_url
#   print _xsrf
    data={
        "_xsrf":_xsrf,
        "phone_num":"18815569470",
        "password":"lzx19940428",
        "captcha":text
    }
    response=sess.post("https://www.zhihu.com/login/phone_num",data=data,headers=headers)
#print response.text
    response=sess.get("https://www.zhihu.com/people/labc-47/activities",headers=headers)
    with open("my.html","w")as f:
        f.write(response.text.encode("utf-8"))
#print response.text

if __name__ == "__main__":
    zhihuLogin()
