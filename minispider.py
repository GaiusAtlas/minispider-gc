#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#########################################################
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
#
#########################################################

'''
minispider
'''
import argparse
import conf_load
import log


def parse_args_init():
    parser = argparse.ArgumentParser(description='To get spider configuration.')
    parser.add_argument('--conf', '-c', help='get config file',required=True)
    parser.add_argument('--sect', '-s', help='get section from file',default='spider')
    parser.add_argument('--version','-v',action='version',version='1.0.0',help='显示版本信息')
    args_p = parser.parse_args()
    return args_p

class MiniSpider(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    import crawler
    try:
        args = parse_args_init()
        spider_log = log.LogManager()
        SpiderConf = conf_load.GetConf(args.conf,args.sect)
        print(SpiderConf.name)
        print(SpiderConf.output_path)
    except Exception as e:
        print(e)