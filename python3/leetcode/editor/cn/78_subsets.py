#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/subsets
# source:  https://leetcode.com/problems/subsets

# [78]-subsets

# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  nums 中的所有元素 互不相同 
#  
# 
#  Related Topics 位运算 数组 回溯 👍 2281 👎 0


# 执行耗时:25 ms,击败了98.83% 的Python3用户
# 内存消耗:16.5 MB,击败了72.12% 的Python3用户

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # sequentially access the element of  [1,2,3]
        res = []
        subset = []

        # i stands for the current pos in the list.
        def dfs(start: int):
            res.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()

        dfs(0)

        return res

# leetcode submit region end(Prohibit modification and deletion)
