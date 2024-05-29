#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/valid-sudoku
# source:  https://leetcode.com/problems/valid-sudoku

# [36]-valid-sudoku

"""
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。 

 
 数字 1-9 在每一行只能出现一次。 
 数字 1-9 在每一列只能出现一次。 
 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图） 
 

 

 注意： 

 
 一个有效的数独（部分已被填充）不一定是可解的。 
 只需要根据以上规则，验证已经填入的数字是否有效即可。 
 空白格用 '.' 表示。 
 

 

 示例 1： 
 
 
输入：board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true
 

 示例 2： 

 
输入：board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：false
解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的
。 

 

 提示： 

 
 board.length == 9 
 board[i].length == 9 
 board[i][j] 是一位数字（1-9）或者 '.' 
 

 Related Topics 数组 哈希表 矩阵 👍 1239 👎 0

"""
from typing import List

"""
https://medium.com/spring-boot/leetcode-problem-36-valid-sudoku-medium-java-8435b5f1d244
Welcome to the 36th coding challenge of leetcode problem series. My aim to provide more than just solutions. 
In each leetcode problem, expect a comprehensive breakdown of the code, a deep dive into the techniques employed, 
and a thoughtful exploration of why we opted for a specific approach. 
Join me as I embark on this journey of problem-solving, where each challenge serves as a stepping stone to honing our coding skills and making informed algorithmic choices. 
Welcome to a series that not only solves problems but also demystifies the thought processes behind effective coding solutions.
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(9):
            for col in range(9):
                cur_value = board[row][col]
                if cur_value != ".":
                    row_key = f"row_{row}_{cur_value}"
                    col_key = f"col_{col}_{cur_value}"
                    grid_key = f"grid_{(row // 3) * 3 + col // 3}_{cur_value}"
                    if row_key in seen or col_key in seen or grid_key in seen:
                        return False
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(grid_key)
        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

    print("-----------------------------------")

    solution.isValidSudoku(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
