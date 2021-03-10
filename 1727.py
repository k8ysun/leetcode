#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:53:10 2021

@author: ysun
"""

# 贪心算法
# 和leetcode 85相似
# time complexity - O(m * nlogn), space complexity O(mn)

class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        # matrix transpose
        matrix_t = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix_t[j][i] = matrix[i][j]

        # transform matrix transposed to matrix height
        m, n = len(matrix_t), len(matrix_t[0])
        matrix_h = []
        for i in range(m):
            row_h = []
            v = 0
            for j in range(n):
                if matrix_t[i][j] == 1:
                    v += 1
                else:
                    v = 0
                row_h.append(v)
            matrix_h.append(row_h)
        
        ans = 0
        h_max = pow(10, 9)
        for k in range(n):
            matrix_h = sorted(matrix_h, key = lambda x:x[k] * (-1))
            h = h_max
            width = 0
            for i in range(m):
                h = min(h, matrix_h[i][k])
                if h == 0:
                    break
                width += 1
                ans = max(ans, h * width)
        return ans 
    



cl = Solution()
matrix = [[1,1,0],[1,0,1]]

res = cl.largestSubmatrix(matrix)