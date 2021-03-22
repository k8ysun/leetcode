#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:49:25 2021

@author: ysun
"""

'''
greedy
Need to compare the two words by dictional order - count the character to avoid repeated computation.
time complexity - O(N) - need to compare 26 times at most in everyround
space complexity - O(N)
'''




from collections import deque

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1, w2 = self.stringToDeque(word1), self.stringToDeque(word2)
        ans = []
        while w1 or w2:
            if len(w1) == 0:
                ans.append(self.wordOutput(w2))
            elif len(w2) == 0:
                ans.append(self.wordOutput(w1))
            else:
                if self.dictOrderCompare(w1, w2):
                    ans.append(self.wordOutput(w1))
                else:
                    ans.append(self.wordOutput(w2))
        return ''.join(ans)
            
    def dictOrderCompare(self, w1, w2):
        i, j = 0, 0
        while i < len(w1) and j < len(w2):
            if w1[i] == w2[j]:
                i += 1
                j += 1
            elif w1[i][0] > w2[j][0]:
                return True
            elif w1[i][0] < w2[j][0]:
                return False
            elif w1[i][1] < w2[j][1]:
                i += 1
            else:
                j += 1
        if i == len(w1):
            return False
        else:
            return True
        
            
    def wordOutput(self, word):
        out = word[0][0]
        word[0][1] -= 1
        if word[0][1] == 0:
            word.popleft()
        return out
        
    
    def stringToDeque(self, word):
        w = deque([])
        c = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                c += 1
            else:
                w.append([word[i - 1], c])
                c = 1
        w.append([word[-1], c])
        return w