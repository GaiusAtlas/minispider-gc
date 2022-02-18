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
        self.crawl_depth = conf.crawl_depth
        self.crawl_inter = conf.crawl_inter
        self.url_table = url_table

    def get_url_content(url):
        pass

def get_url_content(url):
    header_to_take = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    print('start')
    r = requests.get(url, headers=header_to_take)
    print('stop')
    print(r.content)
    print r.status_code
    # print r.content

def logtest():
    logtest = log.LogManager()
    print('sleep start')
    time.sleep(10)
    logtest.logger.debug('log from crawl')
    print('sleep end')
