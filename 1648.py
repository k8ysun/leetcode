#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 07:42:16 2021

@author: ysun
"""



# 1. find the key value that each color should remain by binary search
# 2. compute the profits of each color by Arithmetic sequence summation formula



class Solution:
    def maxProfit(self, inventory, orders: int) -> int:
        self.inventory = inventory
        start, end = 1, max(inventory) + 1
        while start <= end:
            if end - start == 1:
                order_end, order_start = self.ordersNumCompute(end), self.ordersNumCompute(start)
                if order_start >= orders and order_end < orders:
                    p = start
                    break
                else:
                    p = end 
                    break 
            else:
                mid = (start + end) // 2
                order0 = self.ordersNumCompute(mid)
                order1 = self.ordersNumCompute(mid + 1)
                if order0 >= orders and order1 < orders:
                    p = mid 
                    break
                elif order0 < orders:
                    end = mid 
                else:
                    start = mid 
        
        count = 0
        ans = 0
        mod = pow(10, 9) + 7
        for color in inventory:
            if color <= p:
                continue
            a0 = p + 1
            n = color - p 
            count += n 
            ans += a0 * n + n * (n - 1) // 2
            ans %= mod 
        ans += p * (orders - count)
        ans %= mod 
        return ans 


    def ordersNumCompute(self, v):
        od = 0
        for color in self.inventory:
            if color >= v:
                od += color - v + 1
        return od 
    
    
cl = Solution()
inventory = [1000000000]
orders = 1000000000
res = cl.maxProfit(inventory, orders)