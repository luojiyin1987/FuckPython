# !/usr/bin/env python
#encoding: utf-8

import threading
from time import ctime
import time

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        print 'creat %s ' %self.name
        self.res = self.func(*self.args)


class CQueue():
    def __init__(self , len):
        self.cque = []
        self.ppos = 0
        self.gpos = 0
        self.clen = 0
        self.tlen = len

        for i  in range(len):
            self.cque.append(0)

    def get_item(self, n):
        return self.cque[n]

    def set_item(self, n, v):
        self.cque[n] = v

    def is_empty(self):
        return (self.clen == 0)

    def is_full(self):
        return (self.clen == self.tlen)

    def printst(self):
        print 'totalen=%d, clen=%d, ppos=%d, gpos=%d' %(self.tlen, self.clen, self.ppos, self.gpos)
        print str(self.cque)

class Worker():
    def __init__(self, qlen):
        self.cq = CQueue(qlen)
        self.qlock = threading.Lock()
        self.cv = threading.Condition(self.qlock)

    def writer(self):
        '''writer: who writing item to queue.'''
        while True:
            self.cv.acquire()
            print 'writer locked'
            self.cq.ppos += 1
            if self.cq.ppos == self.cq.tlen :
                self.cq.ppos = 0
            self.cq.clen += 1

            self.cv.notify()
            self.cq.printst()
            self.cv.release()
            time.sleep(1)

    def reader(self):
        '''reader who get item from queue'''
        while True:
            self.cv.acquire()
            print 'read locked'
            while self.cq.is_empty():
                self.cv.wait()

            print 'read one : %d' %self.cq.get_item(self.cq.gpos)
            self.cq.set_item(self.cq.gpos, 0)

            self.cq.gpos +=1
            if self.cq.gpos == self.cq.tlen:    #roll
                self.cq.gpos = 0
            self.cq.clen -= 1

            #self.cq.printst()
            self.cv.release()
            time.sleep(1)




def do_work():
    '''do my job'''
    w = Worker(10)
    w.cq.printst()
    threads = []

        #create writer
    for i in range(1):
        t = MyThread(w.writer, (), 'writer')
        threads.append(t)

        #create reader
    for  i in range(2):
        t = MyThread(w.writer, (), 'reader' )
        threads.append(t)

    nth = len(threads)
    for i in range(nth):
        t.start()

    for i in range(nth):
        t.join()

if __name__ == "__main__":
    do_work()
