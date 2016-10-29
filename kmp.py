#!/usr/bin/python
# coding=utf-8

import unittest

def pmt(s):
    """
    PartialMatchTable
    """
    prefix = [s[:i+1] for i in range (len(s)-1)]
    postfix = [s[i+1:] for i in range(len(s)-1)] 
    intersection = list(set(prefix) & set(postfix))
    if intersection:
        return len(intersection[0])
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
        #位移位数 ＝ 已经匹配的字节数 － 对应的部分的匹配值
        if  j:
            i += j -pmt(small[:j])
        else:
            i += 1
    return  False

class kmpTests(unittest.TestCase):
    def test_pmt(self):
        self.assertEqual(pmt("A"), 0)
        self.assertEqual(pmt("AB"), 0)
        self.assertEqual(pmt("ABC"), 0)
        self.assertEqual(pmt("ABCD"), 0)
        self.assertEqual(pmt("ABCDA"),0)
        self.assertEqual(pmt("ABCDAB"),0)
        self.assertEqual(pmt("ABCDABD"),0)
        self.assertEqual(pmt("AAAAAA"),5)

    def test_kmp(self):
        self.assertTrue(kmp("ABCD","CD"))
        self.assertFalse(kmp("ABCD","BD"))
        self.assertFalse(kmp("BBC ABCDABCDABDE","ABCDABD"))

if __name__ == '__main__':
    unittest.main()
            
