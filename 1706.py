#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 06:08:32 2021

@author: ysun
"""



# 并查集, 通过隔板的形状选择连接上下行的格子
# 在并查的时候优先分配序号大的组号
# 最后看第一行的格子是否和最后一行在一个组里
# 注意行数比grid的行数多一行



class Solution:
    def findBall(self, grid):
        m, n = len(grid), len(grid[0])
        
        self.group = list(range((m + 1) * n))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if j == n - 1:
                        continue
                    if grid[i][j + 1] == 1:
                        g0 = self.find(i * n + j)
                        g1 = self.find((i + 1) * n + j + 1)
                        self.group[g0] = max(g0, g1)
                        self.group[g1] = max(g0, g1)
                else:
                    if j == 0:
                        continue
                    if grid[i][j - 1] == -1:
                        g0 = self.find(i * n + j)
                        g1 = self.find((i + 1) * n + j - 1)
                        self.group[g0], self.group[g1] = max(g0, g1), max(g0, g1)
        
        ans = []
        for j in range(n):
            gj = self.find(j)
            if gj >= m * n:
                ans.append(gj - m * n)
            else:
                ans.append(-1)
        return ans 

    def find(self, idx):
        idx_cache = []
        while self.group[idx] != idx:
            idx_cache.append(idx)
            idx = self.group[idx]
        for ic in idx_cache:
            self.group[ic] = idx 
        return idx 
    

grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]

cl = Solution()
res = cl.findBall(grid)

group = cl.group   
    