#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:08:42 2021

@author: ysun
"""

# the number of 'H' and 'V' is fixed, find the kth smallest permutation by binary search


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        self.mem = {}
        m, n = destination
        self.ans = []


        # m - number of V
        # n - number of H
        self.helper(m, n, k)
        return ''.join(self.ans)

    def helper(self, m, n, k):
        if m == 0 and n == 0:
            return 
        elif m == 0:
            self.ans.extend(['H'] * n)
            return 
        elif n == 0:
            self.ans.extend(['V'] * m)
            return 
        else:
            v = self.combCompute(m + n - 1, n - 1)
            if v >= k:
                self.ans.append('H')
                self.helper(m, n - 1, k)
            else:
                self.ans.append('V')
                self.helper(m - 1, n, k - v)

    # compute the combinition number by iteration method
    def combCompute(self, mn, m):
        if (mn, m) in self.mem:
            return self.mem[(mn, m)]
        
        if m == 0 or m == mn:
            return 1
        
        self.mem[(mn, m)] = self.combCompute(mn - 1, m - 1) + self.combCompute(mn - 1, m)
        return self.mem[(mn, m)]