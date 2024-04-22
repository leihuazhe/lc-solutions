#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/permutations-ii
# source:  https://leetcode.com/problems/permutations-ii

# [47]-permutations-ii

"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 

 

 示例 1： 

 
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 

 示例 2： 

 
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

 

 提示： 

 
 1 <= nums.length <= 8 
 -10 <= nums[i] <= 10 
 

 Related Topics 数组 回溯 👍 1562 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        n = len(nums)
        # 涉及到有重复元素，且只用一次的场景,是需要 pruning 的， pruning 意味着要先排序.
        nums.sort()
        visited = [False] * n

        def dfs():
            if len(perm) == n:
                res.append(perm[:])
                return

            for i in range(n):
                if not visited[i]:
                    if i > 0 and nums[i] == nums[i - 1] and visited[i - 1]:
                        continue

                    perm.append(nums[i])
                    visited[i] = True

                    dfs()

                    perm.pop()
                    visited[i] = False

        dfs()

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1, 1, 2]
    solution = Solution()
    res = solution.permuteUnique(nums)
    print(res)
