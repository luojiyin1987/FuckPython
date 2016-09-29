# -*- encoding: utf8  -*-
import re
import os

def readfile():
    wordlist=[]
    templist=[]
    wordcount={}
    pattern=re.compile(r'\w+')
    textpattern=re.compile(r'\W')
    with open('EnglishWord.txt') as f:
        f.seek(0, os.SEEK_END)
        textlength= f.tell()
        i = 0 
        offset = 0
        while(textlength - 4096 * i  >0):
            f.seek(4096 * i - offset )
            content = f.read(4096 + offset)
            temp = content[-1]
            temp1= f.read(1)
            if ( len(re.findall(pattern,temp))==1  and  len(re.findall(pattern,temp1)) == 1  and (textlength - 4096 * i  >0)):
                index=content.rindex(' ')
                offset = 4096 -index + offset -1
                todocontent = content[0:index]
            else:
                todocontent = content
                offset = 0

            i +=1 
            wordlist=re.findall(pattern,todocontent)
            for word in wordlist:
                if word not in templist:
                    templist.append(word)
                    wordcount[word] = 1
                else:
                    wordcount[word] +=1

    wordcount=sorted(wordcount.iteritems(), key=lambda d:d[1], reverse=True)
    
    for word in wordcount:
        print word

if __name__== "__main__":
    readfile()

