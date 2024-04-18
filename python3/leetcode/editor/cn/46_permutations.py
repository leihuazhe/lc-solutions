#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/permutations
# source:  https://leetcode.com/problems/permutations

# [46]-permutations

# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
# 
#  Related Topics 数组 回溯 👍 2871 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        n = len(nums)

        # 为什么全排列没有 start, 因为全排列元素可以往左边取. [1,2], [2,1] are not the same.
        def dfs(perms: List[int]):
            if len(perms) == n:
                res.append(perms.copy())
                return

            for i in range(n):
                if nums[i] not in used:
                    perms.append(nums[i])
                    used.add(nums[i])
                    dfs(perms)
                    perms.pop()
                    used.remove(nums[i])

        dfs([])
        return res

        # leetcode submit region end(Prohibit modification and deletion)
