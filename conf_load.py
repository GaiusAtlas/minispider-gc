#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#########################################################
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
#
#########################################################
"""
configration file load
"""
import os
import configparser

def get_conf(conf_file):
    conf_url = os.path.join('./conf/', conf_file)
    # with open(url, 'r') as f:
    #     print(f.readlines())
    cg = configparser.ConfigParser()
    file_name = cg.read(conf_url)
    print (file_name)
    print (cg.get('spider', 'url_list_file'))


def sum(nums):
    print(sum(nums))


