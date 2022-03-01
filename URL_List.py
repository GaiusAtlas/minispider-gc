# -*- coding: utf-8 -*-
'''
构建队列，主要用于
1.放置待分析url
2.放置待下载url

'''
import Queue
import threading
import time

import url_load
import conf_load

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
        self.url_list = set()
        self.res_list = set()
        self.time_out = 5
        self.lock = threading.Lock()
        self.cnt = 5

    def put(self, url):
        return self.queue.put(url)

    def get(self,):
        try:
            return self.queue.get(timeout=self.time_out)
        except Queue.Empty:
            print 'empty for now,program will wait'

    def put_url_list_o(self, url_list_o):
        self.lock.acquire()
        for url_o in url_list_o:
            if url_o.url:
                if url_o.url not in self.url_list:   #去重
                    self.url_list.add(url_o.url)
                    self.put(url_o)
                    print 'put url:', url_o.url, 'depth:', url_o.depth
        self.lock.release()

    def put_res_list(self, res_list):
        self.lock.acquire()
        print 'res list original', res_list
        for url in res_list:
            if url:
                if url not in self.res_list:   #去重
                    self.res_list.add(url)
                    self.put(url)
                    print 'put res:', url
                else:
                    print 'chongfu'
        self.lock.release()

    def join(self):
        return self.queue.join()

    def task_done(self):
        return self.queue.task_done()

def get_url1(q):
    cnt = 5
    while cnt>0:
        u = q.get()
        if u:
            print 'get', u.url, u.depth
            q.task_done()
            print 'cnt:', cnt
            print 'q done'
            cnt = 5
        else:
            cnt -= 1
            print cnt
def get_url(q):

    u = q.get()
    if u.url:
        print 'get', u.url, u.depth
        q.task_done()
    q.join()

def put_url(q,list):
    q.put_list(list)


class threadTest(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self,queue):
        pass


def init_url_table(conf,queue):

    inq = URL_queue()
    CONF = conf_load.GetConf('spider.conf')
    url_ori = url_load.UrlLoadManager(CONF).get_url_list()
    url_ori_o = []
    for i, u in enumerate(url_ori):
        url_ori_o[i] = URL_O(url=u, depth=0)
    inq.put_list((url_ori_o))
    return inq

if __name__=='__main__':
    inq = URL_queue()
    CONF = conf_load.GetConf('spider.conf')
    url_ori = url_load.get_first_url(CONF)
    inq.put_url_list_o(url_ori)

    t1 = threading.Thread(target=put_url, args=(inq, url_ori))
    t2 = threading.Thread(target=get_url1, args=(inq,))
    # t1.start()
    t2.start()
    # t1.join()
    t2.join()
    # t3 = threadTest()
    # t3.start()
    # t3.join()





