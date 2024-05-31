#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/permutations-ii
# source:  https://leetcode.com/problems/permutations-ii

# [47]-permutations-ii

# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
# 
#  Related Topics 数组 回溯 👍 1562 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        used = set()

        def backtrack(perms: List[int]):
            if len(perms) == n:
                res.append(perms[:])
            else:
                for i in range(n):
                    if used[i]:
                        continue
                    # prune
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    perms.append(nums[i])
                    used.add(nums[i])
                    backtrack(perms)

                    perms.pop(nums[i])
                    used.remove(nums[i])

        backtrack([])

        return res

# leetcode submit region end(Prohibit modification and deletion)
