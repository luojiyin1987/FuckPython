#!/usr/bin/python
# coding=utf-8

import unitest

def pmt(s):
    """
    PartialMatchTable
    """
    prefix = [s[:i+1] for i in range (len(s)-1)]
    postfix = [s[i+1:] for i in range(len(s)-1)] 
    intersection = list(set(prefix) & set(postfix))
    if intersection:
        return len(interserction[0])
    return 0

def kmp(big, small):
    i = 0
    while i<len(big) - len(small)+ 1:
        match = True
        for j in range(len(small)):
            if big[i+j] != small[j]:
                match = False
                break
            if match:
                return True

            
