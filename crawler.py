#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#########################################################
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
#
#########################################################

'''
爬虫本虫
'''

import os
import time

import requests
import log


class Crawler(object):
    def __init__(self, conf, url_table):
        self.max_depth = conf.max_depth
        self.crawl_interval = conf.crawl_interval
        self.url_table = url_table

    def get_url_content(self, url):
        header_to_take = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        print('start')
        r = requests.get(url, headers=header_to_take)
        print('stop')
        print(r.content)
        # print r.status_code

    def test(self,):
        print('test')

def logtest():
    logtest = log.LogManager()
    print('sleep start')
    time.sleep(10)
    logtest.logger.debug('log from crawl')
    print('sleep end')

if __name__=='__main__':
    import conf_load
    urltable=[]
    CONF = conf_load.GetConf('spider.conf', 'spider')
    url_test = 'https://www.douban.com'
    cp = Crawler(CONF, urltable)
    cp.get_url_content(url_test)
    # cp.test()