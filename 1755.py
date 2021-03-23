#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:28:16 2021

@author: ysun
"""

'''
知识盲点 - 不难看出是组合问题， 组合的问题的时间复杂度是2^n, n = 40 无法承受
40给出的提示是我们可以拆成20-20,但是combine的时候如果是naive的方法，那么时间复杂度还是2^40，
所以先排序，再二分搜索。
时间复杂度 - 生成组合 O(2^(n / 2 + 1))
         - 排序 n / 2 * 2 ^ (n / 2) = n * 2 ^ (n //2 + 1)
         - 二分搜索 - 2^(n / 2) * (n / 2) = n * 2 ^ (n / 2 + 1)
空间复杂度  - 2^(n /2 + 1)
'''



class Solution:
    def minAbsDifference(self, nums, goal: int) -> int:
        nums0, nums1 = nums[:len(nums) // 2], nums[len(nums) // 2:]
        comb0, comb1 = self._comb_generate(nums0, 0), self._comb_generate(nums1, 0)
        y = sorted(list(comb1))
        
        ans = abs(goal)
        for x in comb0:
            if y[-1] >= goal - x:
                start, end = 0, len(y) - 1
                while start <= end:
                    if start == end:
                        idx_target = start
                        break
                    elif end - start == 1:
                        if y[start] >= goal - x:
                            idx_target = start
                        else:
                            idx_target = end
                        break
                    else:
                        mid = (start + end) // 2
                        if y[mid - 1] < goal - x and y[mid] >= goal - x:
                            idx_target = mid 
                            break
                        elif y[mid - 1] >= goal - x:
                            end = mid
                        else:
                            start = mid
                ans = min(ans, x + y[idx_target] - goal)
                if idx_target > 0:
                    ans = min(ans, goal - x - y[idx_target - 1])
            else:
                ans = min(ans, goal - x - y[-1])
        return ans
                                        
        
    def _comb_generate(self, array, idx):
        if idx == len(array):
            return set([0])
        comb_next = self._comb_generate(array, idx + 1)
        comb_new = set([])
        for c in comb_next:
            comb_new.add(c + array[idx])
        return comb_next.union(comb_new)
        
        
        
    
    
    
nums = [1556913,-259675,-7667451,-4380629,-4643857,-1436369,7695949,-4357992,-842512,-118463] * 4
goal = -9681425
cl = Solution()
res = cl.minAbsDifference(nums, goal)