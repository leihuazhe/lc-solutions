#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/combination-sum-iii
# source:  https://leetcode.com/problems/combination-sum-iii

# [216]-combination-sum-iii

"""
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件： 

 
 只使用数字1到9 
 每个数字 最多使用一次 
 

 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。 

 

 示例 1: 

 
输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。 

 示例 2: 

 
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。 

 示例 3: 

 
输入: k = 4, n = 1
输出: []
解释: 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。
 

 

 提示: 

 
 2 <= k <= 9 
 1 <= n <= 60 
 

 Related Topics 数组 回溯 👍 821 👎 0

"""
from typing import List

"""
Each number is used at most once.
The list must not contain the same combination twice, and the combinations may be returned in any order.

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(start, total):
            if len(comb) == 3 and total == n:
                res.append(comb.copy())

            for i in range(start, 10):
                if len(comb) > k or total > n:
                    continue
                comb.append(i)
                dfs(i + 1, total + i)
                comb.pop()

        dfs(1, 0)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum3(3, 7))
    print(solution.combinationSum3(3, 9))
