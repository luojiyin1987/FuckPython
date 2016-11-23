#!/usr/bin/env python
# -*-  coding:utf-8 -*-

import string
import re
import urllib2

class DouBanSpider(object):
    def __init__(self):
        self.page = 1
        self.cur_url = "http://movie.douban.com/top250?start={page}&filter=&type="
        self.datas = []
        self._top_num = 1
        print "豆瓣电影爬虫就绪，准备爬取数据..."

    def get_page(self, cur_page):
        url = self.cur_url
        try:
            my_page = urllib2.urlopen(url.format(page = (cur_page -1) * 25)).read().decode("utf-8")
