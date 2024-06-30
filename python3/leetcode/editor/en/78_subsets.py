#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/subsets
# source:  https://leetcode.com/problems/subsets

# [78]-subsets

# Given an integer array nums of unique elements, return all possible subsets (
# the power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in 
# any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0]
# Output: [[],[0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  All the numbers of nums are unique. 
#  
# 
#  Related Topics Array Backtracking Bit Manipulation 👍 17181 👎 281


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(i, subset):
            ans.append(subset[:])
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j + 1, subset)
                subset.pop()

        dfs(0, subset)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
