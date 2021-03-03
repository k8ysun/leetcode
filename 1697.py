#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 07:07:36 2021

@author: ysun
"""



# 并查集
# 1. 对queries和edges排序
# 2. 从limit小的query开始判断，每次判断前，将edge小于当前limit的节点并查集连接，检查时只要检查被检查的两个节点是否联通即可。
# time complexity 
#   - sort queries QlogQ
#   - sort edges MlogM
#   - loop unifound Q + N
# O(QlogQ + MogM + N)

# spaceComplexity
# uniset - O(N)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList, queries) :
        # add index to each query
        for i in range(len(queries)):
            queries[i].append(i)
        
        # sort queries ascendingly
        queries = sorted(queries, key = lambda x:x[2] )

        # sort edgeList descendingly
        edgeList = sorted(edgeList, key = lambda x:x[2] * (-1))

        self.group = list(range(n))
        ans = [False] * len(queries)

        for p, q, limit, idx in queries:
            while edgeList:
                if edgeList[-1][2] < limit:
                    u, v, dist = edgeList.pop()
                    gu, gv = self.find(u), self.find(v)
                    if gu != gv:
                        self.group[gu] = gv
                else:
                    break 
            gp, gq = self.find(p), self.find(q)
            if gp == gq:
                ans[idx] = True 
        return ans 


    def find(self, idx):
        idx_cache = []
        while self.group[idx] != idx:
            idx_cache.append(idx)
            idx = self.group[idx]
        for ic in idx_cache:
            self.group[ic] = idx 
        return idx 
    
    
    
n = 3
edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
queries = [[0,1,2],[0,2,5]]


cl = Solution()
res =cl.distanceLimitedPathsExist(n, edgeList, queries)