#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:57:53 2021

@author: ysun
"""

# DP - this code is dp by row, bilibi is dp by grid




class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        m, n = max(m, n), min(m, n)
        ci_max, ce_max = introvertsCount, extrovertsCount
        
        states_layer = {}
        state_initial = (tuple([0] * n), 0, 0)
        states_layer[state_initial] = 0
        
        from collections import deque
        states_comb = deque([[[], 0, 0]])
        
        for i in range(n):
            s_len = len(states_comb)
            for j in range(s_len):
                s, c1, c2 = states_comb.popleft()
                states_comb.append([s + [0], c1, c2])
                states_comb.append([s + [1], c1 + 1, c2])
                states_comb.append([s + [2], c1, c2 + 1])
                
        for s in states_comb:
            s[0] = tuple(s[0])
        

        self.mem = {}

        for i in range(m):

            d = {}
            for s0 in states_layer:
                b0, ci0, ce0 = s0
                for b1, ci1, ce1 in states_comb:
                    if ci0 + ci1 > ci_max or ce1 + ce0 > ce_max:
                        continue
                    if (b0, b1) not in self.mem:
                        self.helper(b0, b1)   
                    s_new = (b1, ci0 + ci1, ce0 + ce1)
                    if s_new not in d:
                        d[s_new] = states_layer[s0] + self.mem[(b0, b1)]
                    else:
                        d[s_new] = max(d[s_new], states_layer[s0] + self.mem[(b0, b1)])
            states_layer = d
        return max(list(states_layer.values()))
                    

                        
    
    def helper(self, b0, b1):
        v = 0
        for i in range(len(b1)):
            if b1[i] != 0:
                if b0[i] == 1:
                    v -= 30
                elif b0[i] == 2:
                    v += 20
            if b1[i] == 1:
                v += 120
                if b0[i] != 0:
                    v -= 30
                if i > 0 and b1[i - 1] != 0:
                    v -= 30
                if i + 1 < len(b1) and b1[i + 1] != 0:
                    v -= 30
            elif b1[i] == 2:
                v += 40
                if b0[i] != 0:
                    v += 20
                if i > 0 and b1[i - 1] != 0:
                    v += 20
                if i + 1 < len(b1) and b1[i + 1] != 0:
                    v += 20
        self.mem[(b0, b1)] = v

