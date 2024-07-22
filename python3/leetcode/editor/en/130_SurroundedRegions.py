#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/surrounded-regions
# source:  https://leetcode.com/problems/surrounded-regions

# [130]-surrounded-regions

"""
You are given an m x n matrix board containing letters 'X' and 'O', capture 
regions that are surrounded: 

 
 Connect: A cell is connected to adjacent cells horizontally or vertically. 
 Region: To form a region connect every 'O' cell. 
 Surround: The region is surrounded with 'X' cells if you can connect the 
region with 'X' cells and none of the region cells are on the edge of the board. 
 

 A surrounded region is captured by replacing all 'O's with 'X's in the input 
matrix board. 

 
 Example 1: 

 
 Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O",
"X","X"]] 
 

 Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X",
"X"]] 

 Explanation: 
 
 In the above diagram, the bottom region is not captured because it is on the 
edge of the board and cannot be surrounded. 

 Example 2: 

 
 Input: board = [["X"]] 
 

 Output: [["X"]] 

 
 Constraints: 

 
 m == board.length 
 n == board[i].length 
 1 <= m, n <= 200 
 board[i][j] is 'X' or 'O'. 
 

 Related Topics Array Depth-First Search Breadth-First Search Union Find Matrix 
👍 8631 👎 1852

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)  # row len
        n = len(board[0])  # col len

        def dfs(r, c):
            # not in the area.
            if not (0 < r < m - 1 and 0 < c < n - 1):
                return
            if board[r][c] == 'X':
                return
            board[r][c] = 'A'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)

        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'A':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'




# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    s.solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]])
    s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
    print()
