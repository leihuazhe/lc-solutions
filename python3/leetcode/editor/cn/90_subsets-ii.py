#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/subsets-ii
# source:  https://leetcode.com/problems/subsets-ii

# [90]-subsets-ii

# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
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
#  
# 
#  Related Topics 位运算 数组 回溯 👍 1204 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        # 对给定的数组进行排序，这样相同的元素就会排在一起。
        nums.sort()

        def dfs(start):
            # conditions
            res.append(subset.copy())
            for i in range(start, len(nums)):

                # if i > 0 and nums[i] == nums[i - 1]:
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()

        dfs(0)

        return res

# leetcode submit region end(Prohibit modification and deletion)
