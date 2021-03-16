#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:36:47 2021

@author: ysun
"""

# xor的结果和运算顺序无关 - 通过dp来求每个coordinate的值
# 第k大 - 堆排序
# time complexity - m * n(dp) + m * n * logk(heap) = m * n * logk
# space complexity - m * n

class Solution:
    def kthLargestValue(self, matrix, k: int) -> int:
        import heapq
        
        matrix_left = []
        for m in matrix:
            v = 0
            ml = []
            for i in range(len(m)):
                v = v ^ m[i]
                ml.append(v)
            matrix_left.append(ml)
        
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        h = []
        heapq.heapify(h)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    x_ij = matrix_left[i][j]
                elif j == 0:
                    x_ij = dp[i - 1][j] ^ matrix[i][j]
                else:
                    x_ij = dp[i - 1][j] ^ matrix_left[i][j - 1] ^ matrix[i][j]
                dp[i][j] = x_ij
                if len(h) < k:
                    heapq.heappush(h, x_ij)
                else:
                    top = heapq.heappop(h)
                    heapq.heappush(h, max(top, x_ij))
        return heapq.heappop(h)
    
    
matrix = [[5,2],[1,6]]
k = 2
cl = Solution()
res = cl.kthLargestValue(matrix, k)