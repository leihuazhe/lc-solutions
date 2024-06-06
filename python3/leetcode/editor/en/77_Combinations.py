#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/combinations
# source:  https://leetcode.com/problems/combinations

# [77]-combinations

"""
Given two integers n and k, return all possible combinations of k numbers 
chosen from the range [1, n]. 

 You may return the answer in any order. 

 
 Example 1: 

 
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to 
be the same combination.
 

 Example 2: 

 
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

 
 Constraints: 

 
 1 <= n <= 20 
 1 <= k <= n 
 

 Related Topics Backtracking 👍 8169 👎 221

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i):
            d = k - len(path)
            if i < d:
                return
            if len(path) == k:
                # need nums count: d
                ans.append(path[:])
                return
            for j in range(i, 0, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()

        dfs(n)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
