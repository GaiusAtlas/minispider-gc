#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
configration file load
"""
import os
import re
import configparser
import log
import const

class GetConf(object):
    """
    get option from configuration file
    """
    def __init__(self, conf_file, section_name="spider"):
        self.cg = configparser.ConfigParser()
        self.conf_file = conf_file
        self.conf_file_path = os.path.join('./conf/', self.conf_file)
        self.spider_log = log.LogManager()
        self.section_name = section_name          

    def conf_init(self,):
        """conf value load
        """
        try:
            if os.path.isfile(self.conf_file_path):
                self.name = self.cg.read(self.conf_file_path)
            else:
                self.spider_log.error('config file "%s" does not exist' % self.conf_file_path)
                return const.ERROR       
        except Exception as e:
            self.spider_log.error('Config-file error:' + str(e))
            return const.ERROR
        try:
            self.url_list_file = self.cg.get(self.section_name, 'url_list_file')
            self.output_directory = self.cg.get(self.section_name, 'output_directory')
            self.max_depth = self.cg.getint(self.section_name, 'max_depth')
            self.crawl_interval = self.cg.getint(self.section_name, 'crawl_interval')
            self.crawl_timeout = self.cg.getint(self.section_name, 'crawl_timeout')
            self.thread_count = self.cg.getint(self.section_name, 'thread_count')
            self.target_pattern = self.cg.get(self.section_name, 'target_pattern')
            self.log_path = self.cg.get(self.section_name, 'log_path')
        except configparser.NoSectionError as e:
            self.spider_log.error(e)
            return const.ERROR 
        except configparser.NoOptionError as e:
            self.spider_log.error(e)
            return const.ERROR
        except ValueError as ve:
            self.spider_log.error('Load int value error, check conf file')
            return const.ERROR
        except Exception as e:
            self.spider_log.error('Config-file Load error:' + e)
            return const.ERROR
        return const.OK

if __name__ == '__main__':
    c_test = GetConf('spider.conf', 'spider')
    c_test.conf_init()
    print(c_test.name)
