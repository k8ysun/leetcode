#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 16:32:03 2021

@author: ysun
"""


class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        self.floors = set()
        self.m, self.n = len(grid), len(grid[0])
        pos_cat, pos_mouse, self.pos_food = None, None, None
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '.':
                    self.floors.add((i, j))
                elif grid[i][j] == 'C':
                    self.floors.add((i, j))
                    pos_cat = (i, j)
                elif grid[i][j] == 'M':
                    self.floors.add((i, j))
                    pos_mouse = (i, j)
                elif grid[i][j] == 'F':
                    self.pos_food = (i, j)
                    self.floors.add((i, j))
                    
        self.food_reach_cat, self.floor_reach_cat = self.get_reach(catJump)
        self.food_reach_mouse, self.floor_reach_mouse = self.get_reach(mouseJump)
        
        self.dp = {}
        self.mem = set([])
        self.debug = []

        #pos_mouse = (2, 2)
        #pos_cat = (1, 1)
        states = (pos_mouse, pos_cat, True, 1)
        return self.simulate(states)
    
    def simulate(self, states):
        #print(states, self.mem)
        pos_mouse, pos_cat, is_mouse_turn, steps = states
        if steps > 130:
            return False
        if states in self.dp:
            return self.dp[states]
        if pos_mouse == pos_cat:
            return False
        if is_mouse_turn:
            if self.food_reach_mouse[pos_mouse]:
                return True
            res = False
            for pos_next in self.floor_reach_mouse[pos_mouse]:
                states_next = (pos_next, pos_cat, False, steps + 1)
                res_next = self.simulate(states_next)
                res = max(res_next, res)
        else:
            if self.food_reach_cat[pos_cat]:
                return False
            res = True
            for pos_next in self.floor_reach_cat[pos_cat]:
                states_next = (pos_mouse, pos_next, True, steps + 1)
                res_next = self.simulate(states_next)
                res = min(res, res_next)
        self.dp[states] = res
        return self.dp[states]
                
      
                    
    def get_reach(self, jump):
        food_reach, floor_reach = {}, {}
        for i0, j0 in self.floors:
            key = (i0, j0)
            floor_reach[key] = set([])
            floor_reach[key].add((i0, j0))
            for i1 in range(i0 + 1, i0 + jump + 1):
                if i1 >= self.m:
                    break
                if (i1, j0) not in self.floors:
                    break
                if (i1, j0) == self.pos_food:
                    food_reach[key] = True
                    break
                floor_reach[key].add((i1, j0))
            for i1 in range(i0 - 1, i0 - jump - 1, -1):
                if i1 < 0:
                    break
                if (i1, j0) not in self.floors:
                    break
                if (i1, j0) == self.pos_food:
                    food_reach[key] = True
                    break
                floor_reach[key].add((i1, j0))
            for j1 in range(j0 +1, j0 + jump + 1):
                if j1 >= self.n:
                    break
                if (i0, j1) not in self.floors:
                    break
                if (i0, j1) == self.pos_food:
                    food_reach[key] = True
                    break
                floor_reach[key].add((i0, j1))
            for j1 in range(j0 - 1, j0 - jump - 1, -1):
                if j1 < 0:
                    break
                if (i0, j1) not in self.floors:
                    break
                if (i0, j1) == self.pos_food:
                    food_reach[key] = True
                floor_reach[key].add((i0, j1))

            if key not in food_reach:
                food_reach[key] = False
        return food_reach, floor_reach
                
                
    
grids = ["..#.M...","#......#","#F..#...","#..#...#","........","....##C.","..#....#","........"]
catJump = 4
mouseJump = 3
cl = Solution()
res = cl.canMouseWin(grid, catJump, mouseJump) 
                    
        
'''          
for state in cl.dp:
    if state[0] == (2, 2) and state[2] == True:
        print(state, cl.dp[state])         
'''        
        
        
        
        
        
        