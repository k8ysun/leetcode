#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:00:13 2021

@author: ysun
"""

'''
1. transform the element of the matrix to the height of 1 starting from the element
2. compute the area of the matrix that with the element as the most left bottom grid
3. Time Complexity - O(m*n*n), Space Complexity - O(1)
'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        for j in range(n):
            h = 0
            for i in range(m):
                if matrix[i][j] == '1':
                    h += 1
                else:
                    h = 0
                matrix[i][j] = h
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                h = matrix[i][j]
                w = 1
                ans = max(ans, w * h)
                for k in range(j + 1, n):
                    h = min(h, matrix[i][k])
                    w += 1
                    if h == 0:
                        break
                    ans = max(ans, h * w)
        return ans 