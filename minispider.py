#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
minispider
'''
import sys
import argparse

import conf_load
import log
import crawl_thread
import const
import url_load
import URL_List

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
        self.conf = None
        self.input_queue = None
        self.url_ori = None
    
    def _parse_args_init(self,):
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
        conf_ret = self.conf.conf_init()
        if conf_ret == const.ERROR:
            self.spider_log.error("Configuration initial fail")
            return const.ERROR
        self.url_ori = url_load.get_first_url(self.conf)
        if self.url_ori == const.ERROR:
            self.spider_log.error("Original url load fail")
            return const.ERROR
        self.input_queue = URL_List.URL_queue()
        return const.OK

    def start_crawl(self,):
        self.input_queue.put_url_list_o(self.url_ori)
        for i in range(0, self.conf.thread_count):
            thread_name = 'Spider_No_{}'.format(i)
            s_thread = crawl_thread.Crawler(self.input_queue, self.conf, thread_name)
            s_thread.start()
            self.spider_log.info("{} Start working.".format(thread_name))
        self.input_queue.join()


if __name__ == '__main__':
    spider = MiniSpider()
    init_ret = spider.status_init()
    if init_ret == const.ERROR:
        sys.exit()
    spider.start_crawl()
    """
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
    """

   
    