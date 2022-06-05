#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
url file load
"""

import re
import conf_load
import URL_List
import const
import log


def is_url_valid(add):
    '''
    detect url address start with http/https
    '''
    p = re.compile(r'^https?://\w.+$')
    if p.match(add):
        return const.OK
    else:
        return const.ERROR

def get_first_url(conf):
    '''
    read from url_list.txt
    '''
    flg = 0
    url_list = conf.url_list_file
    url_list_address = set()
    url_list_address_o = set()
    spider_log = log.LogManager()
    try:
        with open(url_list, 'r') as f:
            for line in f:
                url_list_address.add(line.strip())
                # print url_list_address
    except IOError as ie:
        spider_log.error("Original url get fail(IO).{}".format(ie))
        return const.ERROR
    except Exception as e:
        spider_log.error("Original url get fail.{}".format(ie))
        return const.ERROR

    # print self.url_list_address
    for add in url_list_address:
        if is_url_valid(add) == const.OK:
            url_list_address_o.add(URL_List.URL_O(add, 0))
    return url_list_address_o

if __name__ == '__main__':

    # l1 = ['https://www.baidu.com', 'http://www.douban.com']
    CONF = conf_load.GetConf('spider.conf')
    CONF.conf_init()
    url_ori = get_first_url(CONF)
    for i in url_ori:
        print i.url, i.depth

