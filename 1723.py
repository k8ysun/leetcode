#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:44:11 2021

@author: ysun
"""

# 位运算
# 状态压缩DP
# 利用位运算求子集
# 异或运算求补集
# 剪枝
# 时间复杂度待补充

class Solution:
    def minimumTimeRequired(self, jobs, k: int) -> int:
        # preprocess
        cache = {}
        cache_count = {}
        n = len(jobs)
        for v in range(1 << n):
            v_cache = v
            sum_v = 0
            count_v = 0
            idx = 0

            while v > 0:
                if v % 2 == 1:
                    sum_v += jobs[idx]
                    count_v += 1
                    
                v = v >> 1
                idx += 1
            cache[v_cache] = sum_v
            cache_count[v_cache] = count_v
        
        
        state_full = (1 << n) - 1
        dp = {}
        dp[0] = 0
        self.debug = []
        for i in range(k):
            dp_new = {}
            for state in dp:
                state_emp = state ^ state_full
                state_child = state_emp
                while state_child:

                    v_max = max(dp[state], cache[state_child])

                    state_new = state_child | state

                    state_child = (state_child - 1) & state_emp
                    
                    count_new = cache_count[state_new]
                    
                    if count_new > n - (k - i - 1):
                        continue
                    
                    if state_new in dp_new:
                        dp_new[state_new] = min(dp_new[state_new], v_max)
                    else:
                        dp_new[state_new] = v_max

            dp = dp_new
        return dp[state_full]
                    
                    
                
            
            
            
            
            
    
jobs = [331,769,967,535,243,239,529,102,250,469,261,283]
k = 10

cl = Solution()
res = cl.minimumTimeRequired(jobs, k)


