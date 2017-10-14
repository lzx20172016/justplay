#!/usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2


url="http://www.renren.com/872201594/profile"

headers={
"Host":"www.renren.com",
"Connection":"keep-alive",
#"Cache-Control":"max-age=0",
#"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-CN,zh;q=0.8",
#"Cookie":"anonymid=j8gnnpvb-7zsn1; depovince=GW; _r01_=1; springskin=set; jebe_key=904a1ff2-25a8-410a-9ae7-25d8ee21fa6b%7Cc99583126a31f2f3084dcc04a97a576d%7C1507340597551%7C1%7C1507340595706; _de=C9EDF44BA583193F8E67F0A45D7FB76A; p=80f65f3b4271d5453807c5582be5d4543; ap=944414883; first_login_flag=1; t=c92cfff836e8c6776654cc13cf99c6fd3; societyguester=c92cfff836e8c6776654cc13cf99c6fd3; id=944414883; xnsid=b7b8d23; ln_uact=18815569470; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; JSESSIONID=abciyBy9DgFb_gpvwH07v; BAIDU_SSP_lcr=https://www.baidu.com/link?url=2mDrmaS5CcL7rDgDObRMz1C9df-LGnFcRYDTE58XFbe&wd=&eqid=d80bbe44000038740000000659d832a5; XNESSESSIONID=abc3bP-vrdxW58dDHI07v; ch_id=10050; ver=7.0; loginfrom=null; wp_fold=0"

}
#url="https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7"
#url="https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action="
#headers={"User-Agent":"Mozilla.."}
request=urllib2.Request(url,headers=headers)

response=urllib2.urlopen(request)

print response.read()

