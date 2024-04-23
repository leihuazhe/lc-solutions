#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/combination-sum-ii
# source:  https://leetcode.com/problems/combination-sum-ii

# [40]-combination-sum-ii

# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用 一次 。 
# 
#  注意：解集不能包含重复的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ] 
# 
#  示例 2: 
# 
#  
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
# 
#  Related Topics 数组 回溯 👍 1537 👎 0

# todo 如何用英文说这题！！！

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 有两个条件是需要注意的

        res = []
        comb = []

        # we have to sort the list
        # TODO 易忘记
        candidates.sort()

        def dfs(start, total):
            if total == target:
                res.append(comb[:])
                return
            # TODO 易忘记
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                comb.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                comb.pop()

        dfs(0, 0)

        return res
# leetcode submit region end(Prohibit modification and deletion)
