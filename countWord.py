# -*- encoding: utf- -*-
import os, string, codecs
import sys, time

def readflie():
    wordlist=[]
    templist=[]
    wordcount={}
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
    

    for tempword in templist:
        i=0
        for word in wordlist:

            if word == tempword:
                    i=i+1
                    print i
                    wordcount[tempword]=i

    print wordcount

if __name__ == "__main__":
    readflie()
