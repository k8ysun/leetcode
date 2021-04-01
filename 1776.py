#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:02:28 2021

@author: ysun
"""
'''
堆，并查集，贪心
堆 用来存放 撞车事件和序号 按照撞车时间排序
并查集 需要两个 分别维护车队的车头和车尾
'''


import heapq

class Solution:
    def getCollisionTimes(self, cars) :
        speed = [c[1] for c in cars]
        pos = [c[0] for c in cars]
        h = []
        for i in range(len(cars) - 1):
            if speed[i + 1] < speed[i]:
                t = (cars[i + 1][0] - cars[i][0]) / (speed[i] - speed[i + 1])
                h.append((t, i))
        heapq.heapify(h)
        ans = [-1] * len(cars)
        self.grp = list(range(len(cars)))
        self.grp_inv = list(range(len(cars)))
        while h:
            t, idx = heapq.heappop(h)
            if ans[idx] != -1:
                continue
            ans[idx] = t 
            idx_next = self.find(idx + 1)
            self.grp[idx] = idx_next

            
            idx_inv = self.find_inv(idx)
            self.grp_inv[idx + 1] = idx_inv
            if idx_inv == 0:
                continue
            if ans[idx_inv - 1] != -1:
                continue
            
            sp0 = speed[idx_inv - 1]
            sp1 = speed[idx_next]
            if sp0 > sp1:
                t = (pos[idx_next] - pos[idx_inv - 1]) / (sp0 - sp1)
                heapq.heappush(h, (t, idx_inv - 1))
        return ans 

    def find_inv(self, i):
        cache = []
        while self.grp_inv[i] != i:
            cache.append(i)
            i = self.grp_inv[i]
        for c in cache:
            self.grp_inv[c] = i 
        return i
            
    def find(self, i):
        cache = []
        while self.grp[i] != i:
            cache.append(i)
            i = self.grp[i]
        for c in cache:
            self.grp[c] = i 
        return i
    
cars = [[3,4],[5,4],[6,3],[9,1]]
cl = Solution()
res = cl.getCollisionTimes(cars)