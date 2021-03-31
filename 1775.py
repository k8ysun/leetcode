#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:29:01 2021

@author: ysun
"""

'''
greedy method
time complexity O(nlogn)
space complexity O(1)
'''


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 < s2:
            nums1, nums2 = nums2, nums1
        diff = max(s1, s2) - min(s1, s2)

        ans = 0
        nums1 = sorted(nums1)
        nums2 = sorted(nums2, key = lambda x:x * (-1))
    
        while nums1 or nums2:
            if diff <= 0:
                return ans
            ans += 1
            if len(nums1) == 0:
                diff -= (6 - nums2.pop())
            elif len(nums2) == 0:
                diff -= (nums1.pop() - 1)
            elif nums1[-1] - 1 >= 6 - nums2[-1]:
                diff -= (nums1.pop() - 1)
            else:
                diff -= (6 - nums2.pop())
        if diff > 0:
            return -1 
        return ans 