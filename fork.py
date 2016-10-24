#!/usr/bin/env python
import os
import time

def task(id):
    print "word %d"   %id

pid = os.fork()
if pid ==0:
    print "I am a child"
else:
    print "I am father child"

print "who am I"
time.sleep(100)


