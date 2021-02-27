#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:09:59 2021

@author: ysun
"""

# for every pair, compute the critical points that it needs 0/1/2 manipulations
# sort all critical points
# scan all critical points with ascending order


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        from collections import defaultdict
        
        landmarks = set([])
        land0, land1, land2 = defaultdict(int), defaultdict(int), defaultdict(int)
        land3 = defaultdict(int)
        

        for i in range(len(nums)):
            if i > len(nums) - 1- i:
                break
            a, b = nums[i], nums[len(nums) - 1- i]
            a, b = min(a, b), max(a, b)
            landmarks.add(a + b)
            land1[a + b] += 1
            landmarks.add(a + 1)
            land0[a + 1] += 1
            landmarks.add(a + b + 1)
            land2[a + b + 1] += 1
            landmarks.add(b + limit + 1)
            land3[b + limit + 1] += 1
        
        landmarks = sorted(list(landmarks))

        ans = len(nums)
        step_cur = len(nums)
        for v in landmarks:
            step_cur -= land0[v]
            step_cur -= land1[v]
            step_cur += land2[v]
            step_cur += land3[v]
            ans = min(ans, step_cur )
        return ans