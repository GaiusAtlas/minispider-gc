#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#########################################################
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
#
#########################################################
"""
log file configration load
"""

import logging
import time
import os

class LogManager(object):
    '''
    init log configuration
    log example :2022-03-30 11:00:14,596 - INFO - test - log.py
    '''
    def __init__(self, ):
        LOG_FORMAT = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s - %(filename)s")
        localtime = time.strftime(r"%Y-%m-%d", time.localtime())
        log_filename = 'spider_' + localtime + '.log'
        log_path = './log'
        
        flevel = logging.DEBUG
        log_file_path = os.path.join(log_path, log_filename)

        self.name = log_filename

        self.logger = logging.getLogger(log_filename)
        self.logger.setLevel(flevel)

        if not self.logger.handlers:
            #avoid log same message
            self.fh = logging.FileHandler(log_file_path)
            self.fh.setLevel(flevel)
            self.fh.setFormatter(LOG_FORMAT)

            self.logger.addHandler(self.fh) 

    def error(self, log_message):
        """output error info & log
        """
        try:
            self.logger.error(log_message)
            print(log_message)
        except Exception as e:
            print(str(e))
    
    def warning(self, log_message):
        """output warning info & log
        """
        try:
            self.logger.warning(log_message)
            print(log_message)
        except Exception as e:
            print(str(e))
    
    def info(self, log_message, display=False):
        """output info log when necessary & log
        """
        try:
            self.logger.info(log_message)
            if display:
                print(log_message)
        except Exception as e:
            print(str(e))

    def debug(self, log_message, display=False):
        """output debug log when necessary & log
        """
        try:
            self.logger.debug(log_message)
            if display:
                print(log_message)
        except Exception as e:
            print(str(e))


if __name__=='__main__':
    spider_log = LogManager()
    spider_log.info('test', True)
    spider_log.info('test2', True)