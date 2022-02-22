#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os.path

import requests
from bs4 import BeautifulSoup
import re

url = 'https://docs.python-requests.org/en/latest/'
url1 = 'http://www.baidu.com'
urls = 'https://www.sina.com.cn'
urlw = 'https://www.163.com'
urld = 'https://www.douban.com'
urlm = 'https://movie.douban.com/subject/35242938/'
header_to_take = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
f = requests.get(urlm, headers=header_to_take)
print(f.status_code)
bs_readf = BeautifulSoup(f.text, 'lxml')
for id,i in enumerate(bs_readf.find_all('img', {"src":True})):
    url_toget = i.attrs['src']
    p = re.compile(r'^.*.(jpg|png|jpeg)$')
    pstart = re.compile(r'^(http|https).*$')
    ptype1 = re.compile(r'^//.*$')
    ptype2 = re.compile(r'^/\w+.*$')
    if p.match(url_toget):
        if pstart.match(url_toget):
            print 'original:', url_toget
        elif ptype1.match(url_toget):
            url_toget = 'http:'+url_toget
            print 'mod+http:'+url_toget
        elif ptype2.match(url_toget):
            url_toget = urlm+url_toget
            print 'mod+url:'+url_toget
        else:
            print 'no process'+url_toget
        with open('./output/{}.png'.format(id), 'wb') as f:
            f.write(requests.get(url_toget).content)
    else:
        pass

print bs_readf.img.attrs['src']