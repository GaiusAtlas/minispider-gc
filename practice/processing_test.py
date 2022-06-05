#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os,time,random
import multiprocessing
import threading

#TEST1
# print('Process (%s) start ...' % os.getpid())
#
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parrent is %s.' %(os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
#TEST2

# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['a','b','c']:
#         print('Put %s to queue' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     q = multiprocessing.Queue()
#     pw = multiprocessing.Process(target=write, args=(q,))
#     pr = multiprocessing.Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()

#test3
local_school = threading.local()

def process_student():
    std = local_school.student
    print('hello,%s (in %s)\n'%(std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target = process_thread,args=('Alice',), name = 'Thread-A')
t2 = threading.Thread(target = process_thread,args=('Bob',), name = 'Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()