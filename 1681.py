#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 09:53:15 2021

@author: ysun
"""




class Solution:
    def minimumIncompatibility(self, nums, k: int) -> int:
        g_len = len(nums) // k
        nums.sort()
        v_max = 10000
        dp = []
        for _ in range(1 << len(nums)):
            dp.append([v_max] * len(nums))
        
        # initialize 
        states = set([])
        for idx in range(len(nums)):
            dp[1 << idx][idx] = 0
            states.add((1 << idx, idx))
        
        for it in range(1, len(nums)):
            states_new = set([])
            # it % g_len == 0 new group built
            # it % g_len != 0 expand old group
            if it % g_len == 0:
                for mask, i in states:
                    for j in range(len(nums)):
                        if mask & (1 << j) != 0:
                            continue
                        mask_new = mask | (1 << j)
                        dp[mask_new][j] = min(dp[mask_new][j], dp[mask][i])
                        states_new.add((mask_new, j))
            else:
                for mask, i in states:
                    for j in range(i + 1, len(nums)):
                        if nums[j] == nums[i]:
                            continue
                        if mask & (1 << j) != 0:
                            continue
                        mask_new = mask | (1 << j)
                        dp[mask_new][j] = min(dp[mask_new][j], dp[mask][i] + nums[j] - nums[i])
                        states_new.add((mask_new, j))
            states = states_new

        ans = min(dp[-1])
        if ans == v_max:
            return -1
        else:
            return ans