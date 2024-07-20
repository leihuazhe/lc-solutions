#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/number-of-islands
# source:  https://leetcode.com/problems/number-of-islands

# [200]-number-of-islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
# '0's (water), return the number of islands. 
# 
#  An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] is '0' or '1'. 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 22766 👎 521


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    0 —— 海洋格子
    1 —— 陆地格子（未遍历过）
    2 —— 陆地格子（已遍历过）

    up        v - 1
    down      v + 1
    left      h - 1
    right     h + 1

    """

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid[0])  # the col length
        n = len(grid)  # the row length

        def dfs(v, h):
            # in area?
            if not self.inArea(m, n, v, h):
                return 0
            # is island?
            if grid[v][h] != "1":
                return 0
            # is traversed?
            grid[v][h] = "2"  # is traversed
            up = dfs(v - 1, h)
            down = dfs(v + 1, h)
            left = dfs(v, h - 1)
            right = dfs(v, h + 1)
            return 1 + up + down + left + right

        ans = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    x = dfs(row, col)
                    ans = max(x, ans)
        return ans

    """
    v: vertical
    h: horizon
    """

    def inArea(self, m, n, v, h):
        if (0 <= v < n) and (0 <= h < m):
            return True
        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
                                 ["0", "0", "0", "0", "0"]]))
