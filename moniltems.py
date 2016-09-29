#!/usr/bin/env python
# coding = utf-8
import json
import urllib
import inspect
import os, time ,  socket

userDefine_check_time = 0
userDefine_json = []

class mon:
    def __init__(self):
        self.data = {}

    def getLoadAvg(self):
        with open('/proc/loadavg')  as load_open:
            a = load_open.read().split()[:3]
            return float(a[0])

    def getMemTotal(self):
        with open('/proc/meminfo') as mem_open:
            a = int(mem_open.readline().split()[1]
            return a/1024

    def getMemUsage(self, noBufferCache=True):
        if no
