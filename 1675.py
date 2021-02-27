#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:15:47 2021

@author: ysun
"""

# list and sort all possible value of every element in nums nlogn
# list all possible value with ascending order and compute the min deviation for every possible min value


import heapq

class Solution:
    def minimumDeviation(self, nums) -> int:
        value_poss = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                value_poss.append([2 * nums[i], nums[i]])
            else:
                pi = [nums[i]]
                while pi[-1] % 2 == 0:
                    pi.append(pi[-1] // 2)
                value_poss.append(pi)
        
        h_max = max([v[-1] for v in value_poss])
        h_min = min([v[-1] for v in value_poss])
        ans = h_max - h_min
        h = []
        for i in range(len(value_poss)):
            h.append([value_poss[i].pop(), i])
        
        heapq.heapify(h)
        while h:
            v, idx = heapq.heappop(h)
            ans = min(ans, h_max - v)
            if ans == 0:
                return 0
            if value_poss[idx] == []:
                break
            v_new = value_poss[idx].pop()
            h_max = max(h_max, v_new)
            heapq.heappush(h,[v_new, idx])
        return ans