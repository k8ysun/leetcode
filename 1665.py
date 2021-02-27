#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:32:18 2021

@author: ysun
"""


# greedy method, can prove that the optimal algorithm is to do the task with order
# by minimum - actual

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        for i in range(len(tasks)):
            tasks[i].append(tasks[i][1] - tasks[i][0])
        
        tasks = sorted(tasks , key = lambda x:x[2] * (-1))

        v = 0
        ans = 0
        for i in range(len(tasks)):
            ans = max(ans, tasks[i][1] - v)
            v -= tasks[i][0]
        return ans