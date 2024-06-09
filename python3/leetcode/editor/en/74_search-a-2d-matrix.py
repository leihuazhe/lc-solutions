#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/search-a-2d-matrix
# source:  https://leetcode.com/problems/search-a-2d-matrix

# [74]-search-a-2d-matrix

# You are given an m x n integer matrix matrix with the following two 
# properties: 
# 
#  
#  Each row is sorted in non-decreasing order. 
#  The first integer of each row is greater than the last integer of the 
# previous row. 
#  
# 
#  Given an integer target, return true if target is in matrix or false 
# otherwise. 
# 
#  You must write a solution in O(log(m * n)) time complexity. 
# 
#  
#  Example 1: 
#  
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -10⁴ <= matrix[i][j], target <= 10⁴ 
#  
# 
#  Related Topics Array Binary Search Matrix 👍 15589 👎 412


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        col_l, col_r = 0, len(matrix) - 1
        while col_l <= col_r:
            mid = col_l + (col_r - col_l) // 2
            # found
            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[mid]) - 1]:
                target_row = matrix[mid]
                row_l, row_r = 0, len(target_row) - 1
                while row_l <= row_r:
                    mid2 = row_l + (row_r - row_l) // 2
                    if mid2 == target:
                        return True
                    if mid2 < target:
                        row_l = mid2 + 1
                    else:
                        row_l = mid2 - 1
                return False


            elif matrix[mid][len(matrix[mid]) - 1] < target:
                col_l = mid + 1
            else:
                col_r = mid - 1

        return False

        # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1]], 1))
    print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
