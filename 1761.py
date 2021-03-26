#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:29:06 2021

@author: ysun
"""

'''
brute force 
time complexity - O(NM), N - number of nodes, M - number of edges
space complexity - O(N + M) 
'''

from collections import defaultdict

class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        ans = len(edges)
        for n0 in range(1, n + 1):
            for n1 in range(n0 + 1, n + 1):
                if n1 not in graph[n0]:
                    continue
                n2_pool = graph[n0].intersection(graph[n1])
                for n2 in n2_pool:
                    ans = min(ans, len(graph[n0]) + len(graph[n1]) + len(graph[n2]) - 6)
        if ans == len(edges):
            return -1 
        else:
            return ans 