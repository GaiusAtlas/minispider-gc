#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#########################################################
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
#
#########################################################
"""
url file load
"""

import re


class UrlLoadManager(object):
    """
    URL Load from list file ,check where url is valid or not ,return a list which can be used
    """
    def __init__(self, cong):
        self.url_list = cong.url_list_file
        self.url_list_valid = []

    def is_url_valid(self, url_address_list):
        p = re.compile(r'^https?://\w.+$')
        for url_addr in url_address_list:
            print(p.match(url_addr).group(0))
            self.url_list_valid.append(url_addr)
        print ('url valid list:',self.url_list_valid)






if __name__ == '__main__':
    l1 = ['https://www.baidu.com', 'http://www.douban.com']
    urlMa = UrlLoadManager()
    urlMa.is_url_valid(l1)
