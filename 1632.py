#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 21:00:31 2021

@author: ysun
"""


、from collections import defaultdict

class Solution:
    def matrixRankTransform(self, matrix):
        self.m, self.n = len(matrix), len(matrix[0])
        self.group = list(range(self.m * self.n))
        
        # 每一行，每一列上，值相同的元素有一条边，做并查集
        for i in range(self.m):
            d = {}
            for j in range(self.n):
                if matrix[i][j] not in d:
                    d[matrix[i][j]] = i * self.n + j
                else:
                    g0 = self.find(d[matrix[i][j]])
                    self.group[i * self.n + j] = g0
        
        for j in range(self.n):
            d = {}
            for i in range(self.m):
                if matrix[i][j] not in d:
                    d[matrix[i][j]] = i * self.n + j
                else:
                    g0 = self.find(d[matrix[i][j]])
                    g1 = self.find(i * self.n + j)
                    self.group[g1] = g0
        
        # 每个独立值内部有哪几个小组，每个组内有哪些元素
        d0 = defaultdict(dict)
        for i in range(self.m):
            for j in range(self.n):
                v = matrix[i][j]
                g = self.find(i * self.n + j)
                if g in d0[v]:
                    d0[v][g].append((i, j))
                else:
                    d0[v][g] = [(i, j)]
        
        # 从唯一值由低到高，每个唯一值内部，每个组内所有元素的rank必须相等，取每个元素独立所能去到的rank的最大值
        # 记录更新当前每一行每一列的rank的最大值
        ans = [[-1] * self.n for _ in range(self.m)]
        rank_row = [0] * self.m
        rank_col = [0] * self.n
        for v in sorted(list(d0.keys())):
            dv = d0[v]
            for g in list(dv.keys()):
                poses = dv[g]
                r = -1
                for i, j in poses:
                    r = max(r, rank_row[i] + 1)
                    r = max(r, rank_col[j] + 1)
                for i, j in poses:
                    ans[i][j] = r
                    rank_row[i] = r
                    rank_col[j] = r
        return ans
                    
                    
    def find(self, idx):
        cache = []
        while self.group[idx] != idx:
            cache.append(idx)
            idx = self.group[idx]
        
        for c in cache:
            self.group[c] = idx
        return idx
    
    


cl = Solution()
matrix = [[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]]

ans = cl.matrixRankTransform(matrix) 
     
   