#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 07:27:36 2021

@author: ysun
"""

# 使用字典树来处理XOR问题
# 对query排序来处理m的约束的问题


class Solution:
    def maximizeXor(self, nums, queries) :
        # nums: List[int]
        # queries: List[List[int]]
        # return : List[int]
        
        # deduplicate nums
        nums = list(set(nums))
        
        # decide the max depth of the dict tree
        depth_max = 0
        for v in nums:
            depth_max = max(depth_max, len(bin(v)) - 2)
        
        for x, m in queries:
            depth_max = max(depth_max, len(bin(x)) - 2)
            
        # sort nums by descending order
        nums = sorted(nums, key = lambda x:x * (-1))
        
        # add idx to every query
        for i in range(len(queries)):
            queries[i].append(i)
        
        # sort queries by m
        queries = sorted(queries, key = lambda x:x[1])
            
        # initialize ans
        ans = [-1] * len(queries)
        
        dt = {}
        # 
        for x, m, idx in queries:
            

            while nums:
                if nums[-1] <= m:
                    v = nums.pop()
 
                    v_bin = bin(v)[2:]
                    v_bin = (depth_max - len(v_bin)) * '0' + v_bin
                    self._build_dt_step(dt, v_bin, 0)
                else:
                    break

            if len(dt) == 0:
                continue
            
            x_bin = bin(x)[2:]
            x_bin = '0' * (depth_max - len(x_bin)) + x_bin
            self.ans_x = []
            self._search_dt_step(dt, x_bin, 0)
            ans[idx] = int(''.join(self.ans_x), 2)
        return ans
            
        
    
    def _search_dt_step(self, node, x_bin, idx):
        
        if idx == len(x_bin):
            return 
        
        options = list(node.keys())
        if len(options) == 2:
            if x_bin[idx] == '1':
                key_chosen = '0'
            else:
                key_chosen = '1'
        else:
            key_chosen = options[0]
        
        if key_chosen != x_bin[idx]:
            self.ans_x.append('1')
        else:
            self.ans_x.append('0')
        self._search_dt_step(node[key_chosen], x_bin, idx + 1)
            
      
        
    def _build_dt_step(self, node, v_bin, idx):
        if idx == len(v_bin):
            return 
        if v_bin[idx] not in node:
            node[v_bin[idx]] = {}
        self._build_dt_step(node[v_bin[idx]], v_bin, idx + 1)
        
         

nums = [536870912,0,534710168,330218644,142254206]
queries = [[558240772,1000000000],[307628050,1000000000],[3319300,1000000000],[2751604,683297522],[214004,404207941]]




cl = Solution()
res = cl.maximizeXor(nums, queries)

