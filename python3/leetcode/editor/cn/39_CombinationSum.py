#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/combination-sum
# source:  https://leetcode.com/problems/combination-sum

# [39]-combination-sum

"""
无重复元素: distinct integers
The same number may be chosen from candidates an unlimited number of times

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.

Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所
有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。 

 candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

 对于给定的输入，保证和为 target 的不同组合数少于 150 个。 

 

 示例 1： 

 
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。 

 示例 2： 

 
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]] 

 示例 3： 

 
输入: candidates = [2], target = 1
输出: []
 

 

 提示： 

 
 1 <= candidates.length <= 30 
 2 <= candidates[i] <= 40 
 candidates 的所有元素 互不相同 
 1 <= target <= 40 
 

 Related Topics 数组 回溯 👍 2763 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(start, total):
            if total == target:
                res.append(comb[:])
                return

            for i in range(start, len(candidates)):
                if total > target:
                    continue

                comb.append(candidates[i])
                dfs(i, total + candidates[i])
                comb.pop()

        dfs(0, 0)

        return res
# leetcode submit region end(Prohibit modification and deletion)
