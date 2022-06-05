#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
url file load
"""

import re
import conf_load
import URL_List
import const


def is_url_valid(add):
    '''
    detect url address start with http/https or not
    :param add:
    :return: result
    '''
    p = re.compile(r'^https?://\w.+$')
    if p.match(add):
        return const.OK
    else:
        return const.ERROR

def get_first_url(conf):
    '''
    从原始txt文件中读取url，返回给queue供使用
    :param conf:
    :return:url_list
    '''
    flg = 0
    url_list = conf.url_list_file
    url_list_address = set()
    url_list_address_o = set()
    try:
        with open(url_list, 'r') as f:
            for line in f:
                url_list_address.add(line.strip())
                # print url_list_address
    except IOError as ie:
        print 'IO wrong'
    # print self.url_list_address
    for add in url_list_address:
        if is_url_valid(add):
            # print add
            url_list_address_o.add(URL_List.URL_O(add, 0))
    return url_list_address_o

if __name__ == '__main__':

    # l1 = ['https://www.baidu.com', 'http://www.douban.com']
    CONF = conf_load.GetConf('spider.conf')
    CONF.conf_init()
    url_ori = get_first_url(CONF)
    for i in url_ori:
        print i.url, i.depth

