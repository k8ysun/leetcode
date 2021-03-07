#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 08:00:07 2021

@author: ysun
"""

# 1. 将arr去掉没在target中出现过的元素
# 2. 将arr剩下的值转化成其在target上出现的次序，转化为求LCS最长上升子序列问题
# 3. 使用优化过的DP求解最长上升子序列问题


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # 1. 将arr去掉没在target中出现过的元素
        target_set = set(target)
        arr_valid = [v for v in arr if v in target_set]

        # 2. 将arr剩下的值转化成其在target上出现的次序，转化为求LCS最长上升子序列问题
        idx_target = {}
        for i in range(len(target)):
            idx_target[target[i]] = i 
        
        idx_arr = [idx_target[v] for v in arr_valid]

        # 3. 使用优化过的DP求解最长上升子序列问题
        dp = [-1]
        for idx in idx_arr:
            if idx > dp[-1]:
                dp.append(idx)
                continue
            start, end = 0, len(dp) - 1
            while start <= end:
                if end - start == 1:
                    if dp[start] < idx and dp[end] >= idx:
                        dp[end] = idx
                    else:
                        dp[end + 1] = idx
                    break
                else:
                    mid = (start + end) // 2
                    if dp[mid] < idx and dp[mid + 1] >= idx:
                        dp[mid + 1] = idx
                        break 
                    elif dp[mid] >= idx:
                        end = mid 
                    else:
                        start = mid 
        return len(target) - (len(dp) - 1)