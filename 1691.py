#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 08:31:05 2021

@author: ysun
"""



# the sufficient and necessary condition that cubid_j can be put on cubid_i is:
# cubid_i.sort(); 
# cubid_j.sort();
# cubid_i[0] >= cubid_j[0] and  cubid_i[1] >= cubid_j[1] and  cubid_i[2] >= cubid_j[2]

# so the greedy strategt is to sort the edges of cubid firstly and set the longest edge as the height
# And deduplicate cubid and DFS 



class Solution:
    def maxHeight(self, cuboids) -> int:
        # sort the edges of cubid interbally
        for c in cuboids:
            c.sort()
        
        # count the uniq cubids - deduplication
        for i in range(len(cuboids)):
            self.cuboids[i] = tuple(cuboids[i])
        from collections import Counter
        self.count_cub = Counter(cuboids)


        # build the graph by the domination relation between cubids
        self.cub_uniq = list(self.count_cub.keys())
        from collections import defaultdict
        self.edges_out = defaultdict(list)
        for ci in self.cub_uniq:
            for cj in self.cub_uniq:
                if ci == cj:
                    continue
                if self.checkDomination(ci, cj):
                    self.edges_out[ci].append(cj)
                if self.checkDomination(cj, ci):
                    self.edges_out[cj].append(ci)
        
        # find answer by DFS
        self.mem = {}
        ans = 0
        for cub in self.cub_uniq:
            ans = max(ans, self.helper(cub))
        return ans 
    
    def helper(self, cub):
        if cub not in self.mem:
            score_next = 0
            for cub_next in self.edges_out[cub]:
                score_next = max(score_next, self.helper(cub_next))
            score = score_next + self.count_cub[cub] * cub[2]
            self.mem[cub] = score
        return self.mem[cub]
        
 
    def checkDomination(self, cub_i, cub_j):
        return cub_i[0] >= cub_j[0] and cub_i[1] >= cub_j[1] and cub_i[2] >= cub_j[2]
    
    
cuboids =[[50,45,20],[95,37,53],[45,23,12]]
cl = Solution()
res = cl.maxHeight(cuboids)