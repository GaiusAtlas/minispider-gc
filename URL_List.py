# -*- coding: utf-8 -*-
'''
构建队列，主要用于放置待分析url
'''
import Queue
import threading
import time

import url_load
import conf_load
import log
import const

class URL_O(object):
    '''
    url object with url address and depth information
    '''
    def __init__(self, url, depth):
        self.url = url
        self.depth = depth

class URL_queue(object):
    '''
    URL list to crawl
    '''
    def __init__(self):
        self.queue = Queue.Queue()
        self.spider_log = log.LogManager()
        self.url_list = set()
        self.res_list = set()
        self.time_out = 3
        self.lock = threading.Lock()

    def put(self, url):
        return self.queue.put(url)

    def get(self,):
        if self.queue.empty() is False:
            return self.queue.get(timeout=self.time_out)
        else:
            return const.EMPTY

    def put_url_list_o(self, url_list_o):
        self.lock.acquire()
        for url_o in url_list_o:
            if url_o.url:
                if url_o.url not in self.url_list:   #去重
                    self.url_list.add(url_o.url)
                    self.put(url_o)
                    self.spider_log.debug("Put url {} depth {} in queue."\
                        .format(url_o.url, url_o.depth))                   
        self.lock.release()

    def join(self):
        return self.queue.join()

    def task_done(self):
        return self.queue.task_done()


if __name__=='__main__':
    inq = URL_queue()
    CONF = conf_load.GetConf('spider.conf')
    CONF.conf_init()
    url_ori = url_load.get_first_url(CONF)
    inq.put_url_list_o(url_ori)





