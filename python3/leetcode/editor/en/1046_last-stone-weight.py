#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from heapq import heappush, heappop
from typing import List


# source:  https://leetcode-cn.com/problems/last-stone-weight
# source:  https://leetcode.com/problems/last-stone-weight

# [1046]-last-stone-weight

# You are given an array of integers stones where stones[i] is the weight of 
# the iᵗʰ stone. 
# 
#  We are playing a game with the stones. On each turn, we choose the heaviest 
# two stones and smash them together. Suppose the heaviest two stones have weights 
# x and y with x <= y. The result of this smash is: 
# 
#  
#  If x == y, both stones are destroyed, and 
#  If x != y, the stone of weight x is destroyed, and the stone of weight y has 
# new weight y - x. 
#  
# 
#  At the end of the game, there is at most one stone left. 
# 
#  Return the weight of the last remaining stone. If there are no stones left, 
# return 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the 
# value of the last stone.
#  
# 
#  Example 2: 
# 
#  
# Input: stones = [1]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= stones.length <= 30 
#  1 <= stones[i] <= 1000 
#  
# 
#  Related Topics Array Heap (Priority Queue) 👍 5986 👎 118


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st = []
        for s in stones:
            heappush(st, -s)
        while len(st) > 1:
            x1 = -heappop(st)
            x2 = -heappop(st) if len(st) > 0 else 0
            if x1 == x2:
                continue
            heappush(st, -(x1 - x2))

        return st[0]

# leetcode submit region end(Prohibit modification and deletion)
