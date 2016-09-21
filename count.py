#coding=utf-8
import jieba

file = open("word.txt")

while 1:
    line = file.readline()
    print line
    fullMode = jieba.cut(line, cut_all=True)
    defaultMode = jieba.cut(line, cut_all=False)
    searchMode = jieba.cut_for_search(line)

    print "全模式: \n",' '.join(fullMode)
    print "精确模式: \n", ' '.join(defaultMode)
    print '搜索引擎模式: \n',' '.join(searchMode)
    if not line:
        print "finish"
        break
file.close()    
