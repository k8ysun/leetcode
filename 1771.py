#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:21:58 2021

@author: ysun
"""

# DP - 先确定word1和word2至少有一个元素被选中，然后用动态规划计算区间内的最长回文子序列
# time complexity - O(N^2)
# space complexity - O(N^2)


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        left, right = {}, {}
        for i in range(len(word1)):
            if word1[i] not in left:
                left[word1[i]] = i 
        for i in range(len(word2) - 1, -1, -1):
            if word2[i] not in right:
                right[word2[i]] = i 

        for key in right:
            right[key] += len(word1)
        self.word = word1 + word2
        self.mem = {}
        ans = 0
        for key in left:
            if key not in right:
                continue
            ans = max(ans, 2 + self.helper(left[key] + 1, right[key] - 1))
        return ans 

    def helper(self, i, j):
        if i > j:
            return 0
        elif i == j:
            return 1
        elif j - i == 1:
            if self.word[i] == self.word[j]:
                return 2
            else:
                return 1
        else:
            key = (i, j)
            if key not in self.mem:
                r = max(self.helper(i + 1, j), self.helper(i, j - 1))
                if self.word[i] == self.word[j]:
                    r = max(r, 2 + self.helper(i + 1, j - 1))
                self.mem[key] = r 
            return self.mem[key]