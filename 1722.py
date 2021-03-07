#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 07:00:04 2021

@author: ysun
"""

# 并查集，通过allowedSwaps的下标之间相互连通，然后再看source和target之间一个并查集内部的差异值。
# 注意差异值的求法

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        self.group = list(range(n))
        for a, b in allowedSwaps:
            ga, gb = self.find(a), self.find(b)
            self.group[gb] = ga 
        
        from collections import defaultdict
        count_source, count_target = defaultdict(dict), defaultdict(dict)
        for i in range(len(source)):
            gi = self.find(i)
            if source[i] in count_source[gi]:
                count_source[gi][source[i]] += 1
            else:
                count_source[gi][source[i]] = 1
            if target[i] in count_target[gi]:
                count_target[gi][target[i]] += 1
            else:
                count_target[gi][target[i]] = 1
        ans = 0
        for g in count_source:
            for key in count_source[g]:
                if key not in count_target[g]:
                    vt = 0
                else:
                    vt = count_target[g][key]
                if count_source[g][key] - vt > 0:
                    ans +=count_source[g][key] - vt
        return ans 


    def find(self, idx):
        idx_cache = []
        while self.group[idx] != idx:
            idx_cache.append(idx)
            idx = self.group[idx]
        for ic in idx_cache:
            self.group[ic] = idx 
        return idx 