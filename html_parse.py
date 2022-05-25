#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import threading

import requests
import urllib2
from bs4 import BeautifulSoup
import re

import URL_List
import log

def changeCoding(req):
    '''

    :param req:
    :return: encoding
    '''
    if req.encoding == 'ISO-8859-1':
        # print 'ISO'
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding
    else:
        encoding = req.encoding
    return encoding

def getpic(url_pic, timeout_conf):
    '''

    :param url_pic:
    :return:
    '''
    piclist=[]
    f = None
    header_to_take = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    try:
        f = requests.get(url_pic, headers=header_to_take,timeout=timeout_conf)
    except requests.exceptions.Timeout:
        print 'get pic address timeout'
        # logmanager.logger.error('get pic address{} timeout'.format(url_pic))
    if f:
        print(f.status_code)

        f.encoding = changeCoding(f)
        bs_readf = BeautifulSoup(f.text, 'lxml')

        all_img = bs_readf.find_all('img', {'src':True})

        for i in all_img:
            url_toget = i.attrs['src']
            # print 'ori img:', url_toget

            p = re.compile(r'^.*.(jpg|png|jpeg)$')
            p1 = re.compile(r'^.*./(.*\.)(jpg|png|jpeg)$')
            pstart = re.compile(r'^(http|https).*$')
            ptype1 = re.compile(r'^//.*$')
            ptype2 = re.compile(r'^/\w+.*$')
            pmatch = p1.match(url_toget)

            if pmatch:
                pic_name = pmatch.group(1)+pmatch.group(2)
                if pstart.match(url_toget):
                    pass
                    # print 'original:', url_toget

                elif ptype1.match(url_toget):
                    url_toget = 'http:' + url_toget
                    # print 'mod+http:' + url_toget
                elif ptype2.match(url_toget):
                    url_toget = url_pic + url_toget
                    # print 'mod+url:' + url_toget
                else:
                    pass
                    # print 'no process' + url_toget
                if url_toget not in piclist:
                    piclist.append(url_toget)

                # try:
                #     with open('./output/{}'.format(pic_name), 'wb') as f:   #这里文件名字要改一下，还要放到按网址建立的文件夹
                #         f.write(requests.get(url_toget).content)
                # except IOError as ioe:
                #     print ('IO wrong')

        return piclist

        # print 'thread',threading.currentThread().name,' webpage {}'.format(url_pic),'get',piclist
        # return piclist


def geturladd(url_to_take, depth, timeout_conf):
    url_list_o=[]
    f = None
    header_to_take = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    try:
        f = requests.get(url_to_take.url, headers=header_to_take,timeout=timeout_conf)
    except requests.exceptions.Timeout:
        print 'get url add timeout'
        # logmanager.logger.error('get url addresss {} timeout'.format(url_to_take))
    if f:
        print(f.status_code)
        bs_readf = BeautifulSoup(f.text, 'lxml')
        # with open('./output/1.html', 'w') as k:
        #     k.write(requests.get(url_to_take).content)
        for id, i in enumerate(bs_readf.find_all('a', {"href": True})):
            # print 'original:', i
            url_toget = i.attrs['href']

            pstart = re.compile(r'^(\s*http|\s*https).*(\.htm|\.html)$')
            if pstart.match(url_toget):
                # print 'ori:', url_toget
                url_o = URL_List.URL_O(url_toget, depth)
                url_list_o.append(url_o)
            else:
                pass
            # print 'webpage {}'.format(url_to_take), 'get', url_list_o
        return url_list_o


def downloadpic(url, timeout_conf):
    p1 = re.compile(r'^.*./(.*\.)(jpg|png|jpeg)$')
    pmatch = p1.match(url)
    pic_name = pmatch.group(1) + pmatch.group(2)
    pic_data = None
    header_to_take = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

    try:
        pic_data = requests.get(url, headers=header_to_take, timeout=timeout_conf).content
    except requests.exceptions.Timeout:
        print '超时未下载{}'.format(pic_name)
        # logmanager.logger.error('超时未下载{}'.format(pic_name))
    if pic_data:
        try:
            with open('./output/{}'.format(pic_name), 'wb') as f:  # 这里文件名字要改一下，还要放到按网址建立的文件夹
                f.write(pic_data)
        except IOError as ioe:
            print ('IO wrong')


if __name__ == '__main__':
    url = 'https://docs.python-requests.org/en/latest/'
    url1 = 'http://www.baidu.com'
    urls = 'https://www.sina.com.cn'
    urlw = 'https://www.163.com'
    urld = 'https://www.douban.com'
    urlm = 'https://movie.douban.com/subject/35242938/'
    urly = 'http://sports.sina.com.cn/g/premierleague/index.shtml'
    # geturl(url1)
    getpic(urly)
    # geturl_demo(urly)
    # geturladd(urly,0)
    # req = requests.get(urly)
    # print (changeCoding(req))


    # uo = geturladd(urlw, 0)
    # # print uo
    # for i in uo:
    #     print i.url, 'depth:',i.depth
    # downloadpic('https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2678037153.jpg')

