#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:38:56 2021

@author: ysun
"""

'''
典型的区间dp问题，需要注意的是至少在python里最好不要图省事用记忆华搜索，很容易超时，还是要老老实实的正向做dp
time complexity - O(N^2)
space complexity - O(N)
'''


class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        n, m = len(nums), len(multipliers)

        dp = {}
        i, j = 0, n - m
        while j < n:
            dp[(i, j)] = max(nums[i] * multipliers[-1], nums[j] * multipliers[-1])
            i += 1
            j += 1
        
        delta = n - m + 1
        while delta < n:
            i, j = 0, delta 
            idx_reverse = n - m - delta - 1
            dp_new = {}
            while j < n:
                v0 = nums[i] * multipliers[idx_reverse] + dp[(i + 1, j)]
                v1 = nums[j] * multipliers[idx_reverse] + dp[(i, j - 1)]
                dp_new[(i, j)] = max(v0, v1)
                i += 1
                j += 1
            delta += 1
            dp = dp_new
        return dp[(0, n - 1)]