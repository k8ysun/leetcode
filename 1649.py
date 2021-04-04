#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:13:46 2021

@author: ysun
"""

# First attemp of Fenwick tree!!!
# 树状数组和线段树相比最大的优势是虽然时间复杂度相同，但是必须要dfs，实际运行时间远少于线段树，必须熟练掌握！！！
# time complexity O(nlogv) 
# n - length of array
# v - max value of array
# space complexity O(n)


class Solution(object):
    def createSortedArray(self, array):
        """
        :type instructions: List[int]
        :rtype: int
        """
        v_max = max(array)
        self.bit = [0] * (v_max + 2)
        mod = pow(10, 9) + 7
        
        ans = 0
        for v in array:
            q0 = self.query(v - 1)
            q1 = self.query(v_max) - self.query(v)
            ans += min(q0, q1)
            ans %= mod
            self.add(v)
        return ans
        
    def query(self, idx):
        q = 0
        while idx > 0:
            q += self.bit[idx]
            c = idx & ((-1) * idx)
            idx -= c
        return q
    
    def add(self, idx):
        while idx < len(self.bit):
            self.bit[idx] += 1
            c = idx & ((-1) * idx)
            idx += c 
        
        
    

cl = Solution()
array = [1,3,3,3,2,4,2,1,2]
ans = cl.createSortedArray(array)      
        