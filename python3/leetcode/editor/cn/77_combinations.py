#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/combinations
# source:  https://leetcode.com/problems/combinations

# [77]-combinations

# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 
# 
#  你可以按 任何顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, k = 1
# 输出：[[1]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
# 
#  Related Topics 回溯 👍 1616 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    # n =4, k =2
    # [1,2,3,4] -> [1,2][1,3][1,4],

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(pos):
            # "If there is an 'if' condition, there should be a 'return' condition."
            if len(cur) == k:
                res.append(cur.copy())
                return

            for i in range(pos, n + 1):
                cur.append(i)
                dfs(i + 1)
                cur.pop()

        dfs(1)

        return res

# leetcode submit region end(Prohibit modification and deletion)
