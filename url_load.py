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

class UrlParge(object):
    pass

def is_url_valid(url_address_list):
    p = re.compile(r'^https?://\w.+$')
    for url_addr in url_address_list:
        print(p.match(url_addr).group(0))

l1 = ['https://www.baidu.com','http://www.douban.com']

if __name__=='__main__':
    is_url_valid(l1)