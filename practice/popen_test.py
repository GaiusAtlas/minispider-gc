#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import threading
from threading import Thread
import subprocess
from Queue import Queue

num_threads=3
ips = ['127.0.0.1','116.56.148.187']
q = Queue()

def pingme(i,queue):
    while True:
        ip = queue.get()
        print('Thread %s pinging %s'% (i,ip))
        ret = subprocess.call('ping -c 1 %s'% ip, shell=True, stdout=subprocess.PIPE)
        if 0 == ret:
            print(' %s is alive' % ip)
        else:
            print('%s is down' % ip)
        queue.task_done()

for i in range(num_threads):
    t = Thread(target=pingme, args=(i, q))
    t.setDaemon(True)
    t.start()

for ip in ips:
    q.put(ip)
print('main thread waiting')

q.join()
print ("done")