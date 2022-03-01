# -*- coding: utf-8 -*-

import threading

import URL_List
import conf_load
import url_load
import html_parse
import log

class CrawlThreadManager(threading.Thread):
    '''
    params: input_url_queue ,url from a queue to crawl
            Res_Table,put result to a queue which can be get by DownloadThread
    '''
    def __init__(self, input_url_queue, res_url_queue, conf,name):
        threading.Thread.__init__(self)
        self.name = name
        self.input_url_queue = input_url_queue  #get url from url_table(queue)
        self.url_list_o = []          #get new url from url queue ,wait for another crawl process
        self.res_list = []           #put download url in ,wait for download
        self.res_url_queue = res_url_queue
        self.max_depth = conf.max_depth
        self.crawl_interval = conf.crawl_interval
        self.crawl_timeout = conf.crawl_timeout
        self.thread_count = conf.thread_count

    def run(self):
        while 1:
            url_to_process = self.input_url_queue.get()
            res_to_process = None

            if url_to_process:
                print 'thread{}'.format(threading.currentThread().name), 'get', url_to_process.url, 'depth:', url_to_process.depth
            else:
                res_to_process = self.res_url_queue.get()

            if url_to_process:
                if url_to_process.depth < self.max_depth:
                    self.res_list = html_parse.getpic(url_to_process.url)
                    self.url_list_o = html_parse.geturladd(url_to_process, url_to_process.depth+1)

                    self.input_url_queue.put_url_list_o(self.url_list_o)
                    self.res_url_queue.put_res_list(self.res_list)

                    self.input_url_queue.task_done()
                elif url_to_process.depth == self.max_depth:
                    print '**************************max _depth**********************************'
                    self.res_list = html_parse.getpic(url_to_process.url)
                    if self.res_list:
                        self.res_url_queue.put_res_list(self.res_list)

                    self.input_url_queue.task_done()
                else:
                    pass

            if res_to_process:
                print 'thread{}'.format(threading.currentThread().name), 'will download', res_to_process
                html_parse.downloadpic(res_to_process)
                self.res_url_queue.task_done()

def initCrawlThread(conf,input_queue,res_queue):
    for i in range(0, conf.thread_count):
        thread_name = 'spider_No_{}'.format(i)
        thread1 = CrawlThreadManager(input_queue, res_queue, conf, thread_name)
        thread1.start()

        print thread_name, 'start '


if __name__=='__main__':
    CONF = conf_load.GetConf('spider.conf')
    url_ori = url_load.get_first_url(CONF)
    input_queue = URL_List.URL_queue()
    input_queue.put_url_list_o(url_ori)
    res_queue = URL_List.URL_queue()

    initCrawlThread(CONF, input_queue, res_queue)
    # input_queue.join()
    # res_queue.join()