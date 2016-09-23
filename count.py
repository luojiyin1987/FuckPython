#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
from collections  import Counter
import sys
reload(sys)
sys.setdefaultencoding('utf8')

file = open("word.txt")

while 1:
    line = file.readline()
    print line
    words = [word for word in jieba.cut(line, cut_all=False) if len(word)>=2]
    c = Counter(words)


    for word_freq in c.most_common(10):
        word, freq = word_freq
        print "%s 出现次数 %d " %(word,freq)



    #defaultMode = jieba.cut(line, cut_all=False)
    #searchMode = jieba.cut_for_search(line)

   #print "全模式: \n",' '.join(fullMode)
   #print "精确模式: \n", ' '.join(defaultMode)
   # print '搜索引擎模式: \n',' '.join(searchMode)
    if not line:
        print "finish"
        break
file.close()
