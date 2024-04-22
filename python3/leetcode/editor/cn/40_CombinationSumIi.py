#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/combination-sum-ii
# source:  https://leetcode.com/problems/combination-sum-ii

# [40]-combination-sum-ii

"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 

 candidates 中的每个数字在每个组合中只能使用 一次 。 

 注意：解集不能包含重复的组合。 

 

 示例 1: 

 
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
] 

 示例 2: 

 
输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
] 

 

 提示: 

 
 1 <= candidates.length <= 100 
 1 <= candidates[i] <= 50 
 1 <= target <= 30 
 

 Related Topics 数组 回溯 👍 1537 👎 0

"""
from typing import List

"""
Each number in candidates may only be used once in the combination. => i -> i+1
The solution set must not contain duplicate combinations. => pruning
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    # 如何优化????
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # pruning, which means we have to sort the list.
        candidates.sort()
        res = []
        comb = []

        def dfs(start, total):
            if total == target:
                res.append(comb.copy())
                return

            # 就这一步， cost: 160ms -> 61ms
            if total > target:
                return

            for i in range(start, len(candidates)):
                # condition, pruning, notice: the original total > target continue should not be forgotten.
                # if i > start and candidates[i] == candidates[i - 1]:
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                comb.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                comb.pop()

        dfs(0, 0)

        return res

    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     # pruning, which means we have to sort the list.
    #     candidates.sort()
    #     res = []
    #     comb = []
    #
    #     def dfs(start, total):
    #         if total == target:
    #             res.append(comb.copy())
    #             return
    #
    #         for i in range(start, len(candidates)):
    #             # condition, pruning, notice: the original total > target continue should not be forgotten.
    #             # if i > start and candidates[i] == candidates[i - 1]:
    #             if i > start and candidates[i] == candidates[i - 1] or total > target:
    #                 continue
    #
    #             comb.append(candidates[i])
    #             dfs(i + 1, total + candidates[i])
    #             comb.pop()
    #
    #     dfs(0, 0)
    #
    #     return res

# leetcode submit region end(Prohibit modification and deletion)
