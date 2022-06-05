#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import encodings
import threading
import os

import requests
from bs4 import BeautifulSoup
import re
import urlparse
import chardet

import URL_List
import log
import conf_load
import const

class HtmlParseDriver(object):
    def __init__(self, url_o, conf):
        self.url = url_o.url
        self.depth = url_o.depth
        self.spider_log = log.LogManager()
        self.timeout = conf.crawl_timeout
        self.header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/79.0.3945.88 Safari/537.36'}
        self.output_path = conf.output_directory

    def log_test(self,):
        self.spider_log.info("here")
        
    def _transcode(self, res):
        """return utf-8 encoding content for saving
        """
        try:
            content = res.content
            url_encoding = res.apparent_encoding
            
            if res.apparent_encoding == None:
                url_encoding = res.encoding    
            elif res.apparent_encoding.lower() == 'gb2312':
                url_encoding = 'GB18030'  
            else:
                pass            
            content = content.decode(url_encoding).encode('utf-8')
            return content
        except UnicodeError as e:
            self.spider_log.warning('{} trans_code_error- {}:'.format(self.url, e))
            return const.ERROR
        except UnicodeEncodeError as e:
            self.spider_log.warning('{} trans_code_error- {}:'.format(self.url, e))
            return const.ERROR
        except UnicodeDecodeError as e:
            self.spider_log.warning('{} trans_code_error- {}:'.format(self.url, e))
            return const.ERROR
        except Exception as e:
            self.spider_log.warning('{} trans_code_error- {}:'.format(self.url, e))
            return const.ERROR

    def _sort_name(self,):
        file_name = str(self.url).split("//")[-1].replace('.','_').replace('/', '_')
        return file_name

    def _trans_rela_to_abs(self, url):
        """trans relative url address to absolute type
        """
        end = re.compile(r'.*\.(htm|html)$')
        start = re.compile(r'^(\s*http|\s*https).*')
        relative_type1 = re.compile(r'^//.*')
        relative_type2 = re.compile(r'^/\w+.*')
        
        if end.match(url):
            # print 'ori:', url_toget
            url = url.strip()
            if start.match(url):
                url_o = URL_List.URL_O(url, self.depth)
            if relative_type1.match(url):
                url = urlparse.urljoin('http:',url)
                url_o = URL_List.URL_O(url, self.depth)
            if relative_type2.match(url):
                url = urlparse.urljoin(self.url, url)
                url_o = URL_List.URL_O(url, self.depth)
        return url_o

    def download_content(self,):   
        try:
            res = requests.get(self.url, headers=self.header, timeout=self.timeout)
        except requests.exceptions.ConnectionError as e:
            self.spider_log.error(r"{} can't connect".format(self.url))
            return const.ERROR
        except requests.exceptions.Timeout:
            self.spider_log.error(r"{} connect timeout".format(self.url))
            return const.ERROR
        except Exception as e:
            self.spider_log.warning('{} download fail - {}:'.format(self.url, e))
            return const.ERROR
        urlname = self._sort_name()
        content = self._transcode(res)
        if content == const.ERROR:
            return const.ERROR
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        download_path = os.path.join(self.output_path, urlname)       
        if res.status_code == 200:
            try:
                with open(download_path, 'w+') as f:  
                    f.write(content)
            except IOError as e:
                self.spider_log.error('Write file error:{}'.format(e))
        else:
            self.spider_log.error(r"{} can't reach,res code:{}".format(self.url, res.status_code))
            return const.ERROR
        return const.OK

    def update_Url(self,):
        try:
            res = requests.get(self.url, headers=self.header, timeout=self.timeout)
        except requests.exceptions.ConnectionError as e:
            self.spider_log.error(r"{} can't connect".format(self.url))
            return const.ERROR
        except requests.exceptions.Timeout:
            self.spider_log.error(r"{} connect timeout".format(self.url))
            return const.ERROR
        except Exception as e:
            self.spider_log.warning('{} download fail - {}:'.format(self.url, e))
            return const.ERROR
        content = self._transcode(res)
        
        if content == const.ERROR:
            return const.ERROR
        bs_read = BeautifulSoup(content, 'lxml')
        url_list_o = []
        self.depth += 1
        for id, i in enumerate(bs_read.find_all('a', {"href": True})):
            url_toget = i.attrs['href']
            end = re.compile(r'.*\.(htm|html)$')
            start = re.compile(r'^(\s*http|\s*https).*')
            relative_type1 = re.compile(r'^//.*')
            relative_type2 = re.compile(r'^/\w+.*')
            
            if end.match(url_toget):
                # print 'ori:', url_toget
                if start.match(url_toget):
                    url_o = URL_List.URL_O(url_toget.strip(), self.depth)
                if relative_type1.match(url_toget):
                    url_toget = urlparse.urljoin('http:',url_toget)
                    url_o = URL_List.URL_O(url_toget.strip(), self.depth)
                if relative_type2.match(url_toget):
                    url_toget = urlparse.urljoin(self.url, url_toget)
                    url_o = URL_List.URL_O(url_toget.strip(), self.depth)
                url_list_o.append(url_o)               
            else:
                pass

        return url_list_o

if __name__ == '__main__':
    url1 = 'http://www.baidu.com'
    urls = 'https://www.sina.com.cn'
    urlw = 'https://www.163.com'
    urld = 'https://www.douban.com'
    urlm = 'https://movie.douban.com/subject/35242938/'
    urly = 'http://sports.sina.com.cn/g/premierleague/index.shtml'
    urlg = "https://www.ip138.com/post/"
    urln = "http://www.asgasdfasdf.com"
    urlt = 'https:/twitter.com'
    urle = "http://xf.house.163.com/bj/0RCF.html"
    urln2 = 'https://slide.news.sina.com.cn/slide_1_86058_547923.html'
    urln3 = 'https://fashion.sina.com.cn/s/ac/2022-06-02/0607/doc-imizirau6027564.shtml'
    urln4 = 'http://slide.baby.sina.com.cn/mxx/slide_10_846_774766.html '
    urln5 = "http://xf.house.163.com/bj/0RCF.html"

    conf = conf_load.GetConf('spider.conf', 'spider')
    conf.conf_init()
    url_o = URL_List.URL_O(urln5, 0)
    k = HtmlParseDriver(url_o, conf)
    #k.download_content()
    url_o = URL_List.URL_O(urly, 0)
    #list = geturladd(url_o)
    #for i in list:
        #print i.url
    #k.update_Url()
    k.download_content()
    k.log_test()
    

