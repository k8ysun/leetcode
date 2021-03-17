#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:20:11 2021

@author: ysun
"""


class Solution:
    def minimumBoxes(self, n: int) -> int:
        # ---------- 计算可以堆放的最大层数 ----------
        level = 1
        cell = 0
        while cell + (1 + level) * level // 2 <= n:
            cell += (1 + level) * level // 2
            level += 1
        level -= 1

        # 计算当前占地面积（即最下层的盒子数量）
        area = (1 + level) * level // 2

        # ---------- 计算还需要继续放置的砖块 ----------
        now = 0
        while cell < n:
            area += 1
            cell += now + 1
            now += 1

        return area

