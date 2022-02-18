#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os.path

import requests
from bs4 import BeautifulSoup
import re

url = 'https://docs.python-requests.org/en/latest/'
url1 = 'http://www.baidu.com'
header_to_take = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
f = requests.get(url, header_to_take)
# print(f.text)
bs_readf = BeautifulSoup(f.text, 'lxml')
for id,i in enumerate(bs_readf.find_all('img')):
    # print(i.attrs['src'])
    url_toget = i.attrs['src']
    p = re.compile(r'^.*.(jpg|png|jpeg)$')
    pstart = re.compile(r'^(http|https).*$')
    if p.match(url_toget):
        if pstart.match(url_toget):
            pass
        else:
            url_toget = os.path.join(url, url_toget)
        with open('./output/{}.png'.format(id), 'wb') as f:
            f.write(requests.get(url_toget).content)
        # print i.attrs['src']

# print bs_readf.img.attrs['src']