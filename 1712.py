#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 11:09:00 2021

@author: ysun
"""


# 三指针，不需要求前缀和，注意元素值可能为零
# 注意就是对于某个i不符合要求，也不代表其后来的i都无效

class Solution:
    def waysToSplit(self, nums) -> int:

        sum_tot = sum(nums)
        mod = pow(10, 9) + 7
        ans = 0
        i0, i1 = 1,1
        s0 = nums[0] + nums[1]
        s1 = s0
        sum_left = 0
        for i in range(len(nums) - 2):
            sum_left += nums[i]
            
            i0 = max(i0, i + 1)
            s0 = max(s0, sum_left + nums[i + 1])
            while i0 <= len(nums) - 2:
                if s0  - sum_left >= sum_left:
                    break
                i0 += 1
                s0 += nums[i0]
                
            if s0 - sum_left < sum_left:
                break
            
            
            i1 = max(i0, i1)
            s1 = max(s0, s1)
            while i1 <= len(nums) - 3:
                if s1 + nums[i1 + 1] - sum_left > sum_tot - (s1 + nums[i1 + 1]) :
                    break
                i1 += 1
                s1 += nums[i1]
            

            if s1  - sum_left > sum_tot - s1 :
                continue

            if i <= 10:
                print(i0, i1)
            ans += (i1 - i0 + 1)



            ans %= mod
            
                
        return ans
                
nums = [0] * pow(10, 5)        
 
cl = Solution()
res = cl.waysToSplit(nums) 
   

            
            