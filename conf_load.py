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
import re
import configparser
import log

import crawler

class GetConf(object):
    """
    get option from configuration file
    """

    def __init__(self, conf_file, section_name):
        cg = configparser.ConfigParser()
        conf_file_path = os.path.join('./conf/', conf_file)

        self.spider_log = log.LogManager()
        if os.path.isfile(conf_file_path):
            self.name = cg.read(conf_file_path)
        else:
            self.spider_log.logger.error('config does not exist')
            raise Exception('Config does not exist')

        try:
            self.section_name = cg.options(section_name)
        except configparser.NoSectionError as se:
            print ('No such section in config')
            self.spider_log.logger.error('section wrong')
            raise Exception('section wrong')

        try:
            self.url_list_file = cg.get(section_name, 'url_list_file')
        except configparser.NoOptionError as se:
            print ('url_list_file option does not exist')
            self.spider_log.logger.error('url_list_file option does not exist')

        try:
            self.output_path = cg.get(section_name, 'output_path')
        except configparser.NoOptionError as se:
            print ('output_path option does not exist')
            self.spider_log.logger.error('output_path option does not exist')

        try:
            self.crawl_depth = cg.getint(section_name, 'crawl_depth')
        except configparser.NoOptionError as se:
            print ('No such crawl_depth option in config')
            self.spider_log.logger.error('crawl_depth option does not exist')
        except ValueError as ve:
            print('crawl_depth config is not a number')
            self.spider_log.logger.error('crawl_depth config is not a number')

        try:
            self.crawl_inter = cg.getint(section_name, 'crawl_inter')
        except configparser.NoOptionError as se:
            print ('No crawl_inter option in config')
            self.spider_log.logger.error('crawl_inter option does not exist')
        except ValueError as ve:
            print('crawl_inter config is not a number')
            self.spider_log.logger.error('crawl_inter config is not a number')

        try:
            self.crawl_timeout = cg.getint(section_name, 'crawl_timeout')
        except configparser.NoOptionError as se:
            print ('No crawl_timeout option in config')
            self.spider_log.logger.error('crawl_timeout option does not exist')
        except ValueError as ve:
            print('crawl_timeout config is not a number')
            self.spider_log.logger.error('crawl_timeout config is not a number')

        try:
            self.thread_count = cg.getint(section_name, 'thread_count')
        except configparser.NoOptionError as se:
            print ('No thread_count option in config')
            self.spider_log.logger.error('thread_count option does not exist')
        except ValueError as ve:
            print('thread_count config is not a number')
            self.spider_log.logger.error('thread_count config is not a number')

        try:
            self.target_pattern = cg.get(section_name, 'target_pattern')
        except configparser.NoOptionError as se:
            print ('No target_pattern option in config')
            self.spider_log.logger.error('target_pattern option does not exist')

        try:
            self.log_path = cg.get(section_name, 'log_path')
        except configparser.NoOptionError as se:
            print ('No log_path option in config')
            self.spider_log.logger.error('log_path option does not exist')

def get_conf(conf_file):
    conf_url_path = os.path.join('./conf/', conf_file)
    # with open(url, 'r') as f:
    #     print(f.readlines())
    cg = configparser.ConfigParser()
    file_name = cg.read(conf_url_path)
    print (file_name)
    try:
        url_list_path = cg.get('spider', 'url_list_file')
        print(url_list_path)
    except:
        pass

    with open(url_list_path, 'r') as f:
        for line in f:
            # print(line)
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            for i in urls:
                print i
                # crawler.get_url_content(i)

        # print(f.readlines())

if __name__ == '__main__':
    # get_conf('spider.conf')

    c_test = GetConf('spider.conf', 'spider')
    # crawler.logtest()
    print(c_test.name)
