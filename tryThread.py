#!/usr/bin/python
# -*- coding:UTF-8  -*-

import thread
import time

def print_time(threadName,delay):
    count = 0
    while count <5:
        time.sleep(delay)
        count +=1
        print "%s: %s %d" %(threadName, time.ctime(time.time()),count)


try:
    thread.start_new_thread(print_time, ("Thread-1",2))
    thread.start_new_thread(print_time, ("Thread-2",6))
except:
    print "Error: unable to start thread"

while 1:
    pass
