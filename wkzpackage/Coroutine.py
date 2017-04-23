#!/usr/bin/python
# -*- coding:utf-8 -*-

import time

"""
用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高

注意到consumer函数是一个generator（生成器），把一个consumer传入produce后：

首先调用c.next()启动生成器；生成器执行到yield阻塞住,等待生产者发送消息,切换回生产者.

然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

consumer通过yield拿到消息，处理，又通过yield把结果传回；

produce通过send返回值拿到consumer处理的结果，继续生产下一条消息；

produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
"""

#这是个生成器(有yield关键字的函数)
def consumer():
    r = '消费者已启动等等生产者发送资料'                 # 4
    while True:                                     # 5,19,32,45,
        n = yield r                                 # 6,14,20,27,33,40,46
        if not n:                                   # 15,28,41
            return
        print('[CONSUMER] Consuming %s...' % n)     # 16,29,42
        time.sleep(1)                               # 17,30,43
        r = '200 OK'                                # 18,31,44

def produce(c):
    c_next = c.next()                               # 3,7
    print("get consumer info:"+c_next)              # 8
    n = 0                                           # 9
    while n < 3:                                    # 10,23,36,49
        n = n + 1                                   # 11,24,37
        print('[PRODUCER] Producing %s...' % n)     # 12,25,38
        r = c.send(n)                               # 13,21,26,34,39,47
        print('[PRODUCER] Consumer return: %s' % r) # 22,35,48
    c.close()                                       # 50

if __name__=='__main__':
    # c是生成器
    c = consumer()                                  # 1
    produce(c)                                      # 2