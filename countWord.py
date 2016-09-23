#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, string, codecs
import sys, time

def readfile():
    wordlist=[]
    base=open('base.txt','r')
    baseinfo=base.readlines()
    tagf=open(tag.txt.'r')
    tagfinfo=tagf.readlines()
    for i in tagfinfo:
        tags=i.split(' ')
    for i in baseinfo:
        words=i.split(' ')
        for word in words:
            if word !='\t' and word !='\n' and word !=' ' and word != '' and word>=2:
                word=word.replace('\t','')
                word=word.replace('\n','')
                word=word.replace(' ', '')
                word=word.replace('.\n','')
                if word!='':
                    wordlist.append(word)

        for x in range(len(wordlist))
            tag=tags[x]
            for k in range(len(wordlist)):
                if tag in wordlist[k]:
                    words=wordlist[k].split(tag)
                    del wordlist[k]
                    for j in range(len(words)):
                        if words[j]!='':
                        wordlist.append(words[j])

    base.close()
    tagf.close()
    return wordlist

def getStr(word, count, allwordnum):
    countStr=word+'---------' +str(count)+'----------'+str(allowordnum)
    return countStr

if __name__ =="__main__"
    wordcnt={}
    wordlist=readlist()
    wordlistall=wordlist
    allwordnum=len(wordlistall)
    outdate=open('count.txt','w')
    print '******************************'
    print(u'提示')
    print(u'            1.要统计的文章放在base.txt')
    print(u'            2.单词分割符在tag.txt,默认已对换码符，换行符，空格，句号处理')
    print(u'            3.统计的结果保存在count.txt')

    for i in wordlistall:
        if i in wordcnt:
            wordcnt[i] +=1
        else:
            wordcnt[i]=1

    for word, cnt in wordcnt.iteritems():
        print word+'-----------' +str(cnt)+'-------'+str(allwordnum)
        outdata.write(getStr(word,cnt,allwordnum)+'\n')

    print(u'完成')
    print(u'按任意键退出')
    outdate.close()
    os.system("pause")



