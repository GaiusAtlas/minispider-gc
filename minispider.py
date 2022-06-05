#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
minispider
'''
import sys
import argparse

import conf_load
import log

def parse_args_init():
    parser = argparse.ArgumentParser(prog="mini_spider", description='Crawl some infomation.')
    #parser.add_argument('--conf', '-c', help='get config file', required=True)
    parser.add_argument('--conf', '-c', help='input config file into program', required=True)
    parser.add_argument('--sect', '-s', help='get section from file', default='spider')
    parser.add_argument('--version','-v',action='version',version='1.0.0', help='显示版本信息')
    args_p = parser.parse_args()
    return args_p

def prog_init():
    """program initial
    """
    


class MiniSpider(object):
    def __init__(self,):
        self.spider_log = log.LogManager()
    
    def _parse_args_init():
        parser = argparse.ArgumentParser(prog="mini_spider", description='Crawl some infomation.')
        #parser.add_argument('--conf', '-c', help='get config file', required=True)
        parser.add_argument('--conf', '-c', help='input config file into program', required=True)
        parser.add_argument('--sect', '-s', help='get section from file', default='spider')
        parser.add_argument('--version','-v',action='version',version='1.0.0', help='显示版本信息')
        args_p = parser.parse_args()
        return args_p
    
    def status_init(self,):
        args = self._parse_args_init()
        self.conf = conf_load.GetConf(args.conf, args.sect)
        self.conf.conf_init()


if __name__ == '__main__':
    #args initial
    args = parse_args_init()
    #log initial
    spider_log = log.LogManager()
    #conf initial
    SpiderConf = conf_load.GetConf(args.conf, args.sect)
    ret = SpiderConf.conf_init()
    if ret == 1:
        spider_log.error("Configuration initial failure")
        sys.exit(1)
    spider_pro = MiniSpider(SpiderConf)
    print(SpiderConf.name)
    print(SpiderConf.output_directory)
    