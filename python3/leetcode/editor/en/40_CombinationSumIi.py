#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/combination-sum-ii
# source:  https://leetcode.com/problems/combination-sum-ii

# [40]-combination-sum-ii

"""
Given a collection of candidate numbers (candidates) and a target number (
target), find all unique combinations in candidates where the candidate numbers sum 
to target. 

 Each number in candidates may only be used once in the combination. 

 Note: The solution set must not contain duplicate combinations. 

 
 Example 1: 

 
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
 

 Example 2: 

 
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

 
 Constraints: 

 
 1 <= candidates.length <= 100 
 1 <= candidates[i] <= 50 
 1 <= target <= 30 
 

 Related Topics Array Backtracking 👍 10364 👎 292

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()

        def dfs(total, start):
            if total == target:
                ans.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(total + candidates[i], i + 1)
                path.pop()

        dfs(0, 0)

        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    # 1 1 2 5 6 7 10
    print(s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
