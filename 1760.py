#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:47:44 2021

@author: ysun
"""

'''
经典二分问题
'''

class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        self.nums = nums
        start, end = 1, max(nums)
        while start <= end:
            if start == end:
                return start
            elif end - start == 1:
                if self._operations_compute(start) <= maxOperations:
                    return start
                else:
                    return end 
            else:
                mid = (start + end) // 2
                c0, c1 = self._operations_compute(mid - 1), self._operations_compute(mid)
                if c0 > maxOperations and c1 <= maxOperations:
                    return mid 
                elif c0 <= maxOperations:
                    end = mid 
                else:
                    start = mid 
    
    def _operations_compute(self, v):
        c = 0
        for n in self.nums:
            c += (n - 1) // v
        return c 
    
    
nums = [7,17]
maxOperations = 2

cl = Solution()
res = cl.minimumSize(nums, maxOperations)