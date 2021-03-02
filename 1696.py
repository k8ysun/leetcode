#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 08:45:28 2021

@author: ysun
"""



# 单调队列


class Solution:
    def maxResult(self, nums, k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        from collections import deque
        queue = deque([])
        queue.append((0, nums[0]))

        for i in range(1, len(nums)):
            while queue:
                if i - queue[0][0] > k:
                    queue.popleft()
                else:
                    break
            vi = queue[0][1] + nums[i]
            while queue:
                if queue[-1][1] <= vi:
                    queue.pop()
                else:
                    break 
            queue.append((i, vi))
        return queue[-1][1]
    
    
cl = Solution()
nums = [1,-5,-20,4,-1,3,-6,-3]
k = 2
res = cl.maxResult(nums, k)