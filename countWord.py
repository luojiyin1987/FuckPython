# -*- encoding: utf- -*-
import os, string, codecs
import sys, time

def readflie():
    wordlist=[]
    templist=[]
    wordcount={}
    tempdict={}
    base=open('EnglishWord.txt', 'r')
    baseinfo=base.readlines()
    for  i in baseinfo:
        words=i.split(' ')
        for word in words:
            if word !='\t' and word != '\n' and word !=' ' and len(word)>=2:
                word = word.replace('\t', '')
                word = word.replace('\n', '')
                word = word.replace(',',  '')
                word = word.replace('.\n','')
                word = word.replace('.','')

                if word !='':
                    wordlist.append(word)
                    #print word
    base.close()

    for word in wordlist:

        if word not in templist:
            templist.append(word)
            wordcount[word]=1
        if word in templist:
            wordcount[word]=wordcount[word]+1

    for word in   wordcount:
        print  '%s 次数是  %d' %(word, wordcount[word])



    #for   word in wordcount:
    #    print   '%s, value=%d' %(word, wordcount[word])

if __name__ == "__main__":
    readflie()
