# -*- coding: UTF-8 -*-
import threading
import time

def test():
    for i in range(5):
        print('thread %s' %threading.current_thread().name)
        print i

def changen(para):
    lock.acquire()
    global list1
    for i in range(5):
        list1[i] = para
        time.sleep(1)
        # print 'now:',list1
    print'修改全局变量为', list1
    lock.release()
    # print'修改全局变量为',list1 #如果把打印语句放在这里，loc已经释放，此时下一个进程已经在执行print之前工作了，所以不对
if __name__ =='__main__':
    list1 = [None]*5
    lock = threading.Lock()
    hi_thread = threading.Thread(target=changen, args=('hi',))
    hello_thread = threading.Thread(target=changen, args=('hello',))
    hi_thread.start()
    hello_thread.start()




    # t1 = threading.Thread(target=test, name='test')
    # t2 = threading.Thread(target=test, name='test2')
    # t1.start()
    # t1.join()
    # t2.start()
    # t2.join()