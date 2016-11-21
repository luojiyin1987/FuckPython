#!/usr/bin/env python
#coding:utf-8
import string , random

fild = string.letters + string.digits

def getRandom():
    return "".join(random.sample(fild,4))

def concatenate(group):
    return "-".join(getRandom() for i in range(group))

def generate(n):
    return [concatenate(5)  for i in range(n)]

if __name__ == '__main__':
    print generate(200)
