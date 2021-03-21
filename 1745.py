#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 09:34:47 2021

@author: ysun
"""

# 看到数据规模，马上应该得出是O(N^2)的复杂度，在这种提醒下马上应该由时间复杂度想到是区间dp
# 由区间dp得到了任意i, j之间是否是回文
# 再枚举i, j判断是否符合要求
# time complexity - O(N^2), space complexity - O(N^2)



class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dp = {}
        for i in range(len(s)):
            dp[(i, i)] = True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[(i, i + 1)] = True
            else:
                dp[(i, i + 1)] = False
        
        delta = 2
        while delta < len(s):
            idx = 0
            while idx + delta < len(s):
                if s[idx] == s[idx + delta] and dp[(idx + 1, idx + delta - 1)]:
                    dp[(idx, idx + delta)] = True
                else:
                    dp[(idx), idx + delta] = False
                idx += 1
            delta += 1
        
        for i in range(1, len(s)):
            if dp[(0, i - 1)]:
                for j in range(i, len(s) - 1):
                    if dp[(i, j)] and dp[(j + 1, len(s) - 1)]:
                        return True
        return False


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaxyaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
cl = Solution()
res = cl.checkPartitioning(s)         