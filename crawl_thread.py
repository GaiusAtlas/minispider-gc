# -*- coding: utf-8 -*-

import threading
import time

import URL_List
import conf_load
import url_load
import html_parse
import log
import const

class Crawler(threading.Thread):
    '''
    params: input_url_queue ,url from a queue to crawl
            Res_Table,put result to a queue which can be get by DownloadThread
    '''
    def __init__(self, input_queue, conf, name):
        threading.Thread.__init__(self)
        self.spider_log = log.LogManager()
        self.name = name
        self.conf = conf
        self.input_queue = input_queue  #get url from Url_List(queue)
        self.max_depth = self.conf.max_depth
        self.crawl_interval = self.conf.crawl_interval
        self.crawl_timeout = self.conf.crawl_timeout
        #self.thread_count = conf.thread_count
        self.daemon = True            

    def run(self):
        while True:
            #get url to process
            url_to_process = self.input_queue.get()
            url_update = []
            if url_to_process != const.EMPTY:
                self.spider_log.info("Thread {} get {}, depth:{}".format(self.name, \
                        url_to_process.url, url_to_process.depth), display=True)            
                url_parse = html_parse.HtmlParseDriver(url_to_process, self.conf)
                ret_d = const.INITIAL
                ret_update = const.INITIAL

                if url_to_process.depth < self.max_depth:
                    ret_d = url_parse.download_content()
                    url_update = url_parse.update_Url() 
                    if url_update == const.ERROR:
                        self.spider_log.error("{} Update failure".format(url_to_process.url))
                        break
                    self.input_queue.put_url_list_o(url_update)             
                elif url_to_process.depth == self.max_depth:
                    ret_d = url_parse.download_content()
                else:
                    pass

                # Download Result Log
                if ret_d == const.OK:
                    self.spider_log.debug("Thread {} download {} success, depth {}"\
                        .format(self.name, url_to_process.url,url_to_process.depth), display=True)
                elif ret_d == const.ERROR:
                    self.spider_log.debug("Thread {} download {} fail, depth {}"\
                        .format(self.name, url_to_process.url,url_to_process.depth), display=True)
                else:
                    pass
              
                self.input_queue.task_done()

            time.sleep(self.crawl_interval)


def initCrawlThread(conf,input_queue):
    for i in range(0, conf.thread_count):
        thread_name = 'spider_No_{}'.format(i)
        s_thread = Crawler(input_queue, conf, thread_name)
        s_thread.start()

        print thread_name, 'start '
    input_queue.join()
    res_queue.join()


if __name__=='__main__':
    CONF = conf_load.GetConf('spider.conf')
    CONF.conf_init()
    url_ori = url_load.get_first_url(CONF)
    input_queue = URL_List.URL_queue()
    input_queue.put_url_list_o(url_ori)
    res_queue = URL_List.URL_queue()

    initCrawlThread(CONF, input_queue)
    input_queue.join()
