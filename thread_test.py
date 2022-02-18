# -*- coding: utf-8 -*-

"""
thread practise
"""
import os
import threading
import time

balance = 0
lock = threading.Lock()

def loop():
    print('thread %s is running...' % threading.currentThread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.currentThread().name, n))
        time.sleep(1)

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

# def run_thread(n):
#     for i in range(2000000):
#         change_it(n)

def run_thread(n):
    for i in range(2000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1 = threading.Thread(target=run_thread,name='change',args=(5,))
t2 = threading.Thread(target=run_thread,name='change',args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
# print('thread %s is running...' % threading.currentThread().name )
# t = threading.Thread(target = loop, name = 'LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)